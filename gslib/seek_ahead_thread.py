# -*- coding: utf-8 -*-
# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Threading code for estimating total work of long-running gsutil commands."""

import threading

from gslib.util import NUM_OBJECTS_PER_LIST_PAGE


class SeekAheadResult(object):
  """Result class for seek_ahead_iterator results.

  A class is used instead of a namedtuple, making it easier to document
  and use default keyword arguments.
  """

  def __init__(self, est_num_ops=1, data_bytes=0):
    """Create a SeekAheadResult.

    Args:
      est_num_ops: Number of operations the iterated result represents.
          Operation is loosely defined as a single API call for a single
          object. The total number of API calls may not be known at the time of
          iteration, so this number is approximate.
      data_bytes: Number of data bytes that will be transferred (uploaded,
          downloaded, or rewritten) for this iterated result.
    """
    self.est_num_ops = est_num_ops
    self.data_bytes = data_bytes


class SeekAheadThread(threading.Thread):
  """Thread to estimate total work to be performed by all processes and threads.

  Because the ProducerThread can only buffer a certain number of tasks on the
  global task queue, it cannot reliably provide the total count or size of
  iterated results for operations involving many iterated arguments until it
  nears the end of iteration.

  This thread consumes an iterator that should be functionally identical
  to the ProducerThread, but iterates to the end without adding tasks to the
  global task queue in an effort to estimate the amount of total work that the
  call to Apply will perform. It should be used only for large operations, and
  thus it is created by the main ProducerThread only when the number of
  iterated arguments exceeds a threshold.

  This thread may produce an inaccurate estimate if its iterator produces
  different results than the iterator used by the ProducerThread. This can
  happen due to eventual listing consistency or due to the source being
  modified as iteration occurs.

  This thread estimates operations for top-level objects only;
  sub-operations (such as a parallel composite upload) should be reported via
  the iterator as a single object including the total number of bytes affected.
  """

  def __init__(self, seek_ahead_iterator, cancel_event, status_queue):
    """Initializes the seek ahead thread.

    Args:
      seek_ahead_iterator: Iterator matching the ProducerThread's args_iterator,
          but returning only object name and/or size in the result.
      cancel_event: threading.Event for signaling the
          seek-ahead iterator to terminate.
      status_queue: Status queue for posting summary of fully iterated results.
    """
    super(SeekAheadThread, self).__init__()
    self.status_queue = status_queue
    self.seek_ahead_iterator = seek_ahead_iterator
    self.cancel_event = cancel_event
    # For unit-testing only; use cancel_event to stop the thread.
    self.terminate = False
    self.start()

  def run(self):
    num_objects = 0
    num_data_bytes = 0
    for seek_ahead_result in self.seek_ahead_iterator:
      if self.terminate:
        return
      # Periodically check to see if the ProducerThread has actually
      # completed, at which point providing an estimate is no longer useful.
      if (num_objects % NUM_OBJECTS_PER_LIST_PAGE) == 0:
        if self.cancel_event.isSet():
          return
      num_objects += seek_ahead_result.est_num_ops
      num_data_bytes += seek_ahead_result.data_bytes

    # TODO: Convert this and other status messages to proper messages,
    # including types so that we can reason about time remaining.
    estimate_message = ('Estimated work for this command: objects: %s' %
                        num_objects)
    if num_data_bytes:
      estimate_message += ', total size: %s' % num_data_bytes
    estimate_message += '\n'
    self.status_queue.put(estimate_message)

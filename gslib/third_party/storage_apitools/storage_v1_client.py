# Copyright 2014 Google Inc. All Rights Reserved.
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
"""Generated client library for storage version v1."""

import os
import platform
import sys

from apitools.base.py import base_api

import gslib
from gslib.third_party.storage_apitools import storage_v1_messages as messages


class StorageV1(base_api.BaseApiClient):
  """Generated client library for service storage version v1."""

  MESSAGES_MODULE = messages

  _PACKAGE = u'storage'
  _SCOPES = [u'https://www.googleapis.com/auth/cloud-platform', u'https://www.googleapis.com/auth/cloud-platform.read-only', u'https://www.googleapis.com/auth/devstorage.full_control', u'https://www.googleapis.com/auth/devstorage.read_only', u'https://www.googleapis.com/auth/devstorage.read_write']
  _VERSION = u'v1'
  _CLIENT_ID = 'nomatter'
  _CLIENT_SECRET = 'nomatter'
  _USER_AGENT = 'apitools gsutil/%s Python/%s (%s)' % (
      gslib.VERSION, platform.python_version(), sys.platform)
  if os.environ.get('CLOUDSDK_WRAPPER') == '1':
    _USER_AGENT += ' google-cloud-sdk'
    if os.environ.get('CLOUDSDK_VERSION'):
      _USER_AGENT += ' %s' % os.environ.get('CLOUDSDK_VERSION')
  _CLIENT_CLASS_NAME = u'StorageV1'
  _URL_VERSION = u'v1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               version=_VERSION, additional_http_headers=None):
    """Create a new storage handle."""
    url = url or u'https://www.googleapis.com/storage/v1/'
    super(StorageV1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers)
    self._version = version
    self.bucketAccessControls = self.BucketAccessControlsService(self)
    self.buckets = self.BucketsService(self)
    self.channels = self.ChannelsService(self)
    self.defaultObjectAccessControls = self.DefaultObjectAccessControlsService(self)
    self.objectAccessControls = self.ObjectAccessControlsService(self)
    self.objects = self.ObjectsService(self)


  class BucketAccessControlsService(base_api.BaseApiService):
    """Service class for the bucketAccessControls resource."""

    _NAME = u'bucketAccessControls'

    def __init__(self, client):
      super(StorageV1.BucketAccessControlsService, self).__init__(client)
      self._method_configs = {
          'Delete': base_api.ApiMethodInfo(
              http_method=u'DELETE',
              method_id=u'storage.bucketAccessControls.delete',
              ordered_params=[u'bucket', u'entity'],
              path_params=[u'bucket', u'entity'],
              query_params=[],
              relative_path=u'b/{bucket}/acl/{entity}',
              request_field='',
              request_type_name=u'StorageBucketAccessControlsDeleteRequest',
              response_type_name=u'StorageBucketAccessControlsDeleteResponse',
              supports_download=False,
          ),
          'Get': base_api.ApiMethodInfo(
              http_method=u'GET',
              method_id=u'storage.bucketAccessControls.get',
              ordered_params=[u'bucket', u'entity'],
              path_params=[u'bucket', u'entity'],
              query_params=[],
              relative_path=u'b/{bucket}/acl/{entity}',
              request_field='',
              request_type_name=u'StorageBucketAccessControlsGetRequest',
              response_type_name=u'BucketAccessControl',
              supports_download=False,
          ),
          'Insert': base_api.ApiMethodInfo(
              http_method=u'POST',
              method_id=u'storage.bucketAccessControls.insert',
              ordered_params=[u'bucket'],
              path_params=[u'bucket'],
              query_params=[],
              relative_path=u'b/{bucket}/acl',
              request_field='<request>',
              request_type_name=u'BucketAccessControl',
              response_type_name=u'BucketAccessControl',
              supports_download=False,
          ),
          'List': base_api.ApiMethodInfo(
              http_method=u'GET',
              method_id=u'storage.bucketAccessControls.list',
              ordered_params=[u'bucket'],
              path_params=[u'bucket'],
              query_params=[],
              relative_path=u'b/{bucket}/acl',
              request_field='',
              request_type_name=u'StorageBucketAccessControlsListRequest',
              response_type_name=u'BucketAccessControls',
              supports_download=False,
          ),
          'Patch': base_api.ApiMethodInfo(
              http_method=u'PATCH',
              method_id=u'storage.bucketAccessControls.patch',
              ordered_params=[u'bucket', u'entity'],
              path_params=[u'bucket', u'entity'],
              query_params=[],
              relative_path=u'b/{bucket}/acl/{entity}',
              request_field='<request>',
              request_type_name=u'BucketAccessControl',
              response_type_name=u'BucketAccessControl',
              supports_download=False,
          ),
          'Update': base_api.ApiMethodInfo(
              http_method=u'PUT',
              method_id=u'storage.bucketAccessControls.update',
              ordered_params=[u'bucket', u'entity'],
              path_params=[u'bucket', u'entity'],
              query_params=[],
              relative_path=u'b/{bucket}/acl/{entity}',
              request_field='<request>',
              request_type_name=u'BucketAccessControl',
              response_type_name=u'BucketAccessControl',
              supports_download=False,
          ),
          }

      self._upload_configs = {
          }

    def Delete(self, request, global_params=None):
      """Permanently deletes the ACL entry for the specified entity on the specified bucket.

      Args:
        request: (StorageBucketAccessControlsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (StorageBucketAccessControlsDeleteResponse) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Get(self, request, global_params=None):
      """Returns the ACL entry for the specified entity on the specified bucket.

      Args:
        request: (StorageBucketAccessControlsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (BucketAccessControl) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Insert(self, request, global_params=None):
      """Creates a new ACL entry on the specified bucket.

      Args:
        request: (BucketAccessControl) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (BucketAccessControl) The response message.
      """
      config = self.GetMethodConfig('Insert')
      return self._RunMethod(
          config, request, global_params=global_params)

    def List(self, request, global_params=None):
      """Retrieves ACL entries on the specified bucket.

      Args:
        request: (StorageBucketAccessControlsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (BucketAccessControls) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Patch(self, request, global_params=None):
      """Updates an ACL entry on the specified bucket. This method supports patch semantics.

      Args:
        request: (BucketAccessControl) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (BucketAccessControl) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Update(self, request, global_params=None):
      """Updates an ACL entry on the specified bucket.

      Args:
        request: (BucketAccessControl) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (BucketAccessControl) The response message.
      """
      config = self.GetMethodConfig('Update')
      return self._RunMethod(
          config, request, global_params=global_params)

  class BucketsService(base_api.BaseApiService):
    """Service class for the buckets resource."""

    _NAME = u'buckets'

    def __init__(self, client):
      super(StorageV1.BucketsService, self).__init__(client)
      self._method_configs = {
          'Delete': base_api.ApiMethodInfo(
              http_method=u'DELETE',
              method_id=u'storage.buckets.delete',
              ordered_params=[u'bucket'],
              path_params=[u'bucket'],
              query_params=[u'ifMetagenerationMatch', u'ifMetagenerationNotMatch'],
              relative_path=u'b/{bucket}',
              request_field='',
              request_type_name=u'StorageBucketsDeleteRequest',
              response_type_name=u'StorageBucketsDeleteResponse',
              supports_download=False,
          ),
          'Get': base_api.ApiMethodInfo(
              http_method=u'GET',
              method_id=u'storage.buckets.get',
              ordered_params=[u'bucket'],
              path_params=[u'bucket'],
              query_params=[u'ifMetagenerationMatch', u'ifMetagenerationNotMatch', u'projection'],
              relative_path=u'b/{bucket}',
              request_field='',
              request_type_name=u'StorageBucketsGetRequest',
              response_type_name=u'Bucket',
              supports_download=False,
          ),
          'Insert': base_api.ApiMethodInfo(
              http_method=u'POST',
              method_id=u'storage.buckets.insert',
              ordered_params=[u'project'],
              path_params=[],
              query_params=[u'predefinedAcl', u'predefinedDefaultObjectAcl', u'project', u'projection'],
              relative_path=u'b',
              request_field=u'bucket',
              request_type_name=u'StorageBucketsInsertRequest',
              response_type_name=u'Bucket',
              supports_download=False,
          ),
          'List': base_api.ApiMethodInfo(
              http_method=u'GET',
              method_id=u'storage.buckets.list',
              ordered_params=[u'project'],
              path_params=[],
              query_params=[u'maxResults', u'pageToken', u'prefix', u'project', u'projection'],
              relative_path=u'b',
              request_field='',
              request_type_name=u'StorageBucketsListRequest',
              response_type_name=u'Buckets',
              supports_download=False,
          ),
          'Patch': base_api.ApiMethodInfo(
              http_method=u'PATCH',
              method_id=u'storage.buckets.patch',
              ordered_params=[u'bucket'],
              path_params=[u'bucket'],
              query_params=[u'ifMetagenerationMatch', u'ifMetagenerationNotMatch', u'predefinedAcl', u'predefinedDefaultObjectAcl', u'projection'],
              relative_path=u'b/{bucket}',
              request_field=u'bucketResource',
              request_type_name=u'StorageBucketsPatchRequest',
              response_type_name=u'Bucket',
              supports_download=False,
          ),
          'Update': base_api.ApiMethodInfo(
              http_method=u'PUT',
              method_id=u'storage.buckets.update',
              ordered_params=[u'bucket'],
              path_params=[u'bucket'],
              query_params=[u'ifMetagenerationMatch', u'ifMetagenerationNotMatch', u'predefinedAcl', u'predefinedDefaultObjectAcl', u'projection'],
              relative_path=u'b/{bucket}',
              request_field=u'bucketResource',
              request_type_name=u'StorageBucketsUpdateRequest',
              response_type_name=u'Bucket',
              supports_download=False,
          ),
          }

      self._upload_configs = {
          }

    def Delete(self, request, global_params=None):
      """Permanently deletes an empty bucket.

      Args:
        request: (StorageBucketsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (StorageBucketsDeleteResponse) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Get(self, request, global_params=None):
      """Returns metadata for the specified bucket.

      Args:
        request: (StorageBucketsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Bucket) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Insert(self, request, global_params=None):
      """Creates a new bucket.

      Args:
        request: (StorageBucketsInsertRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Bucket) The response message.
      """
      config = self.GetMethodConfig('Insert')
      return self._RunMethod(
          config, request, global_params=global_params)

    def List(self, request, global_params=None):
      """Retrieves a list of buckets for a given project.

      Args:
        request: (StorageBucketsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Buckets) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Patch(self, request, global_params=None):
      """Updates a bucket. This method supports patch semantics.

      Args:
        request: (StorageBucketsPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Bucket) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Update(self, request, global_params=None):
      """Updates a bucket.

      Args:
        request: (StorageBucketsUpdateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Bucket) The response message.
      """
      config = self.GetMethodConfig('Update')
      return self._RunMethod(
          config, request, global_params=global_params)

  class ChannelsService(base_api.BaseApiService):
    """Service class for the channels resource."""

    _NAME = u'channels'

    def __init__(self, client):
      super(StorageV1.ChannelsService, self).__init__(client)
      self._method_configs = {
          'Stop': base_api.ApiMethodInfo(
              http_method=u'POST',
              method_id=u'storage.channels.stop',
              ordered_params=[],
              path_params=[],
              query_params=[],
              relative_path=u'channels/stop',
              request_field='<request>',
              request_type_name=u'Channel',
              response_type_name=u'StorageChannelsStopResponse',
              supports_download=False,
          ),
          }

      self._upload_configs = {
          }

    def Stop(self, request, global_params=None):
      """Stop watching resources through this channel.

      Args:
        request: (Channel) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (StorageChannelsStopResponse) The response message.
      """
      config = self.GetMethodConfig('Stop')
      return self._RunMethod(
          config, request, global_params=global_params)

  class DefaultObjectAccessControlsService(base_api.BaseApiService):
    """Service class for the defaultObjectAccessControls resource."""

    _NAME = u'defaultObjectAccessControls'

    def __init__(self, client):
      super(StorageV1.DefaultObjectAccessControlsService, self).__init__(client)
      self._method_configs = {
          'Delete': base_api.ApiMethodInfo(
              http_method=u'DELETE',
              method_id=u'storage.defaultObjectAccessControls.delete',
              ordered_params=[u'bucket', u'entity'],
              path_params=[u'bucket', u'entity'],
              query_params=[],
              relative_path=u'b/{bucket}/defaultObjectAcl/{entity}',
              request_field='',
              request_type_name=u'StorageDefaultObjectAccessControlsDeleteRequest',
              response_type_name=u'StorageDefaultObjectAccessControlsDeleteResponse',
              supports_download=False,
          ),
          'Get': base_api.ApiMethodInfo(
              http_method=u'GET',
              method_id=u'storage.defaultObjectAccessControls.get',
              ordered_params=[u'bucket', u'entity'],
              path_params=[u'bucket', u'entity'],
              query_params=[],
              relative_path=u'b/{bucket}/defaultObjectAcl/{entity}',
              request_field='',
              request_type_name=u'StorageDefaultObjectAccessControlsGetRequest',
              response_type_name=u'ObjectAccessControl',
              supports_download=False,
          ),
          'Insert': base_api.ApiMethodInfo(
              http_method=u'POST',
              method_id=u'storage.defaultObjectAccessControls.insert',
              ordered_params=[u'bucket'],
              path_params=[u'bucket'],
              query_params=[],
              relative_path=u'b/{bucket}/defaultObjectAcl',
              request_field='<request>',
              request_type_name=u'ObjectAccessControl',
              response_type_name=u'ObjectAccessControl',
              supports_download=False,
          ),
          'List': base_api.ApiMethodInfo(
              http_method=u'GET',
              method_id=u'storage.defaultObjectAccessControls.list',
              ordered_params=[u'bucket'],
              path_params=[u'bucket'],
              query_params=[u'ifMetagenerationMatch', u'ifMetagenerationNotMatch'],
              relative_path=u'b/{bucket}/defaultObjectAcl',
              request_field='',
              request_type_name=u'StorageDefaultObjectAccessControlsListRequest',
              response_type_name=u'ObjectAccessControls',
              supports_download=False,
          ),
          'Patch': base_api.ApiMethodInfo(
              http_method=u'PATCH',
              method_id=u'storage.defaultObjectAccessControls.patch',
              ordered_params=[u'bucket', u'entity'],
              path_params=[u'bucket', u'entity'],
              query_params=[],
              relative_path=u'b/{bucket}/defaultObjectAcl/{entity}',
              request_field='<request>',
              request_type_name=u'ObjectAccessControl',
              response_type_name=u'ObjectAccessControl',
              supports_download=False,
          ),
          'Update': base_api.ApiMethodInfo(
              http_method=u'PUT',
              method_id=u'storage.defaultObjectAccessControls.update',
              ordered_params=[u'bucket', u'entity'],
              path_params=[u'bucket', u'entity'],
              query_params=[],
              relative_path=u'b/{bucket}/defaultObjectAcl/{entity}',
              request_field='<request>',
              request_type_name=u'ObjectAccessControl',
              response_type_name=u'ObjectAccessControl',
              supports_download=False,
          ),
          }

      self._upload_configs = {
          }

    def Delete(self, request, global_params=None):
      """Permanently deletes the default object ACL entry for the specified entity on the specified bucket.

      Args:
        request: (StorageDefaultObjectAccessControlsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (StorageDefaultObjectAccessControlsDeleteResponse) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Get(self, request, global_params=None):
      """Returns the default object ACL entry for the specified entity on the specified bucket.

      Args:
        request: (StorageDefaultObjectAccessControlsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ObjectAccessControl) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Insert(self, request, global_params=None):
      """Creates a new default object ACL entry on the specified bucket.

      Args:
        request: (ObjectAccessControl) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ObjectAccessControl) The response message.
      """
      config = self.GetMethodConfig('Insert')
      return self._RunMethod(
          config, request, global_params=global_params)

    def List(self, request, global_params=None):
      """Retrieves default object ACL entries on the specified bucket.

      Args:
        request: (StorageDefaultObjectAccessControlsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ObjectAccessControls) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Patch(self, request, global_params=None):
      """Updates a default object ACL entry on the specified bucket. This method supports patch semantics.

      Args:
        request: (ObjectAccessControl) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ObjectAccessControl) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Update(self, request, global_params=None):
      """Updates a default object ACL entry on the specified bucket.

      Args:
        request: (ObjectAccessControl) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ObjectAccessControl) The response message.
      """
      config = self.GetMethodConfig('Update')
      return self._RunMethod(
          config, request, global_params=global_params)

  class ObjectAccessControlsService(base_api.BaseApiService):
    """Service class for the objectAccessControls resource."""

    _NAME = u'objectAccessControls'

    def __init__(self, client):
      super(StorageV1.ObjectAccessControlsService, self).__init__(client)
      self._method_configs = {
          'Delete': base_api.ApiMethodInfo(
              http_method=u'DELETE',
              method_id=u'storage.objectAccessControls.delete',
              ordered_params=[u'bucket', u'object', u'entity'],
              path_params=[u'bucket', u'entity', u'object'],
              query_params=[u'generation'],
              relative_path=u'b/{bucket}/o/{object}/acl/{entity}',
              request_field='',
              request_type_name=u'StorageObjectAccessControlsDeleteRequest',
              response_type_name=u'StorageObjectAccessControlsDeleteResponse',
              supports_download=False,
          ),
          'Get': base_api.ApiMethodInfo(
              http_method=u'GET',
              method_id=u'storage.objectAccessControls.get',
              ordered_params=[u'bucket', u'object', u'entity'],
              path_params=[u'bucket', u'entity', u'object'],
              query_params=[u'generation'],
              relative_path=u'b/{bucket}/o/{object}/acl/{entity}',
              request_field='',
              request_type_name=u'StorageObjectAccessControlsGetRequest',
              response_type_name=u'ObjectAccessControl',
              supports_download=False,
          ),
          'Insert': base_api.ApiMethodInfo(
              http_method=u'POST',
              method_id=u'storage.objectAccessControls.insert',
              ordered_params=[u'bucket', u'object'],
              path_params=[u'bucket', u'object'],
              query_params=[u'generation'],
              relative_path=u'b/{bucket}/o/{object}/acl',
              request_field=u'objectAccessControl',
              request_type_name=u'StorageObjectAccessControlsInsertRequest',
              response_type_name=u'ObjectAccessControl',
              supports_download=False,
          ),
          'List': base_api.ApiMethodInfo(
              http_method=u'GET',
              method_id=u'storage.objectAccessControls.list',
              ordered_params=[u'bucket', u'object'],
              path_params=[u'bucket', u'object'],
              query_params=[u'generation'],
              relative_path=u'b/{bucket}/o/{object}/acl',
              request_field='',
              request_type_name=u'StorageObjectAccessControlsListRequest',
              response_type_name=u'ObjectAccessControls',
              supports_download=False,
          ),
          'Patch': base_api.ApiMethodInfo(
              http_method=u'PATCH',
              method_id=u'storage.objectAccessControls.patch',
              ordered_params=[u'bucket', u'object', u'entity'],
              path_params=[u'bucket', u'entity', u'object'],
              query_params=[u'generation'],
              relative_path=u'b/{bucket}/o/{object}/acl/{entity}',
              request_field=u'objectAccessControl',
              request_type_name=u'StorageObjectAccessControlsPatchRequest',
              response_type_name=u'ObjectAccessControl',
              supports_download=False,
          ),
          'Update': base_api.ApiMethodInfo(
              http_method=u'PUT',
              method_id=u'storage.objectAccessControls.update',
              ordered_params=[u'bucket', u'object', u'entity'],
              path_params=[u'bucket', u'entity', u'object'],
              query_params=[u'generation'],
              relative_path=u'b/{bucket}/o/{object}/acl/{entity}',
              request_field=u'objectAccessControl',
              request_type_name=u'StorageObjectAccessControlsUpdateRequest',
              response_type_name=u'ObjectAccessControl',
              supports_download=False,
          ),
          }

      self._upload_configs = {
          }

    def Delete(self, request, global_params=None):
      """Permanently deletes the ACL entry for the specified entity on the specified object.

      Args:
        request: (StorageObjectAccessControlsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (StorageObjectAccessControlsDeleteResponse) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Get(self, request, global_params=None):
      """Returns the ACL entry for the specified entity on the specified object.

      Args:
        request: (StorageObjectAccessControlsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ObjectAccessControl) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Insert(self, request, global_params=None):
      """Creates a new ACL entry on the specified object.

      Args:
        request: (StorageObjectAccessControlsInsertRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ObjectAccessControl) The response message.
      """
      config = self.GetMethodConfig('Insert')
      return self._RunMethod(
          config, request, global_params=global_params)

    def List(self, request, global_params=None):
      """Retrieves ACL entries on the specified object.

      Args:
        request: (StorageObjectAccessControlsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ObjectAccessControls) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Patch(self, request, global_params=None):
      """Updates an ACL entry on the specified object. This method supports patch semantics.

      Args:
        request: (StorageObjectAccessControlsPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ObjectAccessControl) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Update(self, request, global_params=None):
      """Updates an ACL entry on the specified object.

      Args:
        request: (StorageObjectAccessControlsUpdateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ObjectAccessControl) The response message.
      """
      config = self.GetMethodConfig('Update')
      return self._RunMethod(
          config, request, global_params=global_params)

  class ObjectsService(base_api.BaseApiService):
    """Service class for the objects resource."""

    _NAME = u'objects'

    def __init__(self, client):
      super(StorageV1.ObjectsService, self).__init__(client)
      self._method_configs = {
          'Compose': base_api.ApiMethodInfo(
              http_method=u'POST',
              method_id=u'storage.objects.compose',
              ordered_params=[u'destinationBucket', u'destinationObject'],
              path_params=[u'destinationBucket', u'destinationObject'],
              query_params=[u'destinationPredefinedAcl', u'ifGenerationMatch', u'ifMetagenerationMatch'],
              relative_path=u'b/{destinationBucket}/o/{destinationObject}/compose',
              request_field=u'composeRequest',
              request_type_name=u'StorageObjectsComposeRequest',
              response_type_name=u'Object',
              supports_download=True,
          ),
          'Copy': base_api.ApiMethodInfo(
              http_method=u'POST',
              method_id=u'storage.objects.copy',
              ordered_params=[u'sourceBucket', u'sourceObject', u'destinationBucket', u'destinationObject'],
              path_params=[u'destinationBucket', u'destinationObject', u'sourceBucket', u'sourceObject'],
              query_params=[u'destinationPredefinedAcl', u'ifGenerationMatch', u'ifGenerationNotMatch', u'ifMetagenerationMatch', u'ifMetagenerationNotMatch', u'ifSourceGenerationMatch', u'ifSourceGenerationNotMatch', u'ifSourceMetagenerationMatch', u'ifSourceMetagenerationNotMatch', u'projection', u'sourceGeneration'],
              relative_path=u'b/{sourceBucket}/o/{sourceObject}/copyTo/b/{destinationBucket}/o/{destinationObject}',
              request_field=u'object',
              request_type_name=u'StorageObjectsCopyRequest',
              response_type_name=u'Object',
              supports_download=True,
          ),
          'Delete': base_api.ApiMethodInfo(
              http_method=u'DELETE',
              method_id=u'storage.objects.delete',
              ordered_params=[u'bucket', u'object'],
              path_params=[u'bucket', u'object'],
              query_params=[u'generation', u'ifGenerationMatch', u'ifGenerationNotMatch', u'ifMetagenerationMatch', u'ifMetagenerationNotMatch'],
              relative_path=u'b/{bucket}/o/{object}',
              request_field='',
              request_type_name=u'StorageObjectsDeleteRequest',
              response_type_name=u'StorageObjectsDeleteResponse',
              supports_download=False,
          ),
          'Get': base_api.ApiMethodInfo(
              http_method=u'GET',
              method_id=u'storage.objects.get',
              ordered_params=[u'bucket', u'object'],
              path_params=[u'bucket', u'object'],
              query_params=[u'generation', u'ifGenerationMatch', u'ifGenerationNotMatch', u'ifMetagenerationMatch', u'ifMetagenerationNotMatch', u'projection'],
              relative_path=u'b/{bucket}/o/{object}',
              request_field='',
              request_type_name=u'StorageObjectsGetRequest',
              response_type_name=u'Object',
              supports_download=True,
          ),
          'Insert': base_api.ApiMethodInfo(
              http_method=u'POST',
              method_id=u'storage.objects.insert',
              ordered_params=[u'bucket'],
              path_params=[u'bucket'],
              query_params=[u'contentEncoding', u'ifGenerationMatch', u'ifGenerationNotMatch', u'ifMetagenerationMatch', u'ifMetagenerationNotMatch', u'name', u'predefinedAcl', u'projection'],
              relative_path=u'b/{bucket}/o',
              request_field=u'object',
              request_type_name=u'StorageObjectsInsertRequest',
              response_type_name=u'Object',
              supports_download=True,
          ),
          'List': base_api.ApiMethodInfo(
              http_method=u'GET',
              method_id=u'storage.objects.list',
              ordered_params=[u'bucket'],
              path_params=[u'bucket'],
              query_params=[u'delimiter', u'maxResults', u'pageToken', u'prefix', u'projection', u'versions'],
              relative_path=u'b/{bucket}/o',
              request_field='',
              request_type_name=u'StorageObjectsListRequest',
              response_type_name=u'Objects',
              supports_download=False,
          ),
          'Patch': base_api.ApiMethodInfo(
              http_method=u'PATCH',
              method_id=u'storage.objects.patch',
              ordered_params=[u'bucket', u'object'],
              path_params=[u'bucket', u'object'],
              query_params=[u'generation', u'ifGenerationMatch', u'ifGenerationNotMatch', u'ifMetagenerationMatch', u'ifMetagenerationNotMatch', u'predefinedAcl', u'projection'],
              relative_path=u'b/{bucket}/o/{object}',
              request_field=u'objectResource',
              request_type_name=u'StorageObjectsPatchRequest',
              response_type_name=u'Object',
              supports_download=False,
          ),
          'Rewrite': base_api.ApiMethodInfo(
              http_method=u'POST',
              method_id=u'storage.objects.rewrite',
              ordered_params=[u'sourceBucket', u'sourceObject', u'destinationBucket', u'destinationObject'],
              path_params=[u'destinationBucket', u'destinationObject', u'sourceBucket', u'sourceObject'],
              query_params=[u'destinationPredefinedAcl', u'ifGenerationMatch', u'ifGenerationNotMatch', u'ifMetagenerationMatch', u'ifMetagenerationNotMatch', u'ifSourceGenerationMatch', u'ifSourceGenerationNotMatch', u'ifSourceMetagenerationMatch', u'ifSourceMetagenerationNotMatch', u'maxBytesRewrittenPerCall', u'projection', u'rewriteToken', u'sourceGeneration'],
              relative_path=u'b/{sourceBucket}/o/{sourceObject}/rewriteTo/b/{destinationBucket}/o/{destinationObject}',
              request_field=u'object',
              request_type_name=u'StorageObjectsRewriteRequest',
              response_type_name=u'RewriteResponse',
              supports_download=False,
          ),
          'Update': base_api.ApiMethodInfo(
              http_method=u'PUT',
              method_id=u'storage.objects.update',
              ordered_params=[u'bucket', u'object'],
              path_params=[u'bucket', u'object'],
              query_params=[u'generation', u'ifGenerationMatch', u'ifGenerationNotMatch', u'ifMetagenerationMatch', u'ifMetagenerationNotMatch', u'predefinedAcl', u'projection'],
              relative_path=u'b/{bucket}/o/{object}',
              request_field=u'objectResource',
              request_type_name=u'StorageObjectsUpdateRequest',
              response_type_name=u'Object',
              supports_download=True,
          ),
          'WatchAll': base_api.ApiMethodInfo(
              http_method=u'POST',
              method_id=u'storage.objects.watchAll',
              ordered_params=[u'bucket'],
              path_params=[u'bucket'],
              query_params=[u'delimiter', u'maxResults', u'pageToken', u'prefix', u'projection', u'versions'],
              relative_path=u'b/{bucket}/o/watch',
              request_field=u'channel',
              request_type_name=u'StorageObjectsWatchAllRequest',
              response_type_name=u'Channel',
              supports_download=False,
          ),
          }

      self._upload_configs = {
          'Insert': base_api.ApiUploadInfo(
              accept=['*/*'],
              max_size=None,
              resumable_multipart=True,
              resumable_path=u'/resumable/upload/storage/' + self._client._version + '/b/{bucket}/o',
              simple_multipart=True,
              simple_path=u'/upload/storage/' + self._client._version + '/b/{bucket}/o',
          ),
          }

    def Compose(self, request, global_params=None, download=None):
      """Concatenates a list of existing objects into a new object in the same bucket.

      Args:
        request: (StorageObjectsComposeRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
        download: (Download, default: None) If present, download
            data from the request via this stream.
      Returns:
        (Object) The response message.
      """
      config = self.GetMethodConfig('Compose')
      return self._RunMethod(
          config, request, global_params=global_params,
          download=download)

    def Copy(self, request, global_params=None, download=None):
      """Copies an object to a specified location. Optionally overrides metadata.

      Args:
        request: (StorageObjectsCopyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
        download: (Download, default: None) If present, download
            data from the request via this stream.
      Returns:
        (Object) The response message.
      """
      config = self.GetMethodConfig('Copy')
      return self._RunMethod(
          config, request, global_params=global_params,
          download=download)

    def Delete(self, request, global_params=None):
      """Deletes an object and its metadata. Deletions are permanent if versioning is not enabled for the bucket, or if the generation parameter is used.

      Args:
        request: (StorageObjectsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (StorageObjectsDeleteResponse) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Get(self, request, global_params=None, download=None):
      """Retrieves an object or its metadata.

      Args:
        request: (StorageObjectsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
        download: (Download, default: None) If present, download
            data from the request via this stream.
      Returns:
        (Object) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params,
          download=download)

    def Insert(self, request, global_params=None, upload=None, download=None):
      """Stores a new object and metadata.

      Args:
        request: (StorageObjectsInsertRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
        upload: (Upload, default: None) If present, upload
            this stream with the request.
        download: (Download, default: None) If present, download
            data from the request via this stream.
      Returns:
        (Object) The response message.
      """
      config = self.GetMethodConfig('Insert')
      upload_config = self.GetUploadConfig('Insert')
      return self._RunMethod(
          config, request, global_params=global_params,
          upload=upload, upload_config=upload_config,
          download=download)

    def List(self, request, global_params=None):
      """Retrieves a list of objects matching the criteria.

      Args:
        request: (StorageObjectsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Objects) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Patch(self, request, global_params=None):
      """Updates an object's metadata. This method supports patch semantics.

      Args:
        request: (StorageObjectsPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Object) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Rewrite(self, request, global_params=None):
      """Rewrites a source object to a destination object. Optionally overrides metadata.

      Args:
        request: (StorageObjectsRewriteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (RewriteResponse) The response message.
      """
      config = self.GetMethodConfig('Rewrite')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Update(self, request, global_params=None, download=None):
      """Updates an object's metadata.

      Args:
        request: (StorageObjectsUpdateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
        download: (Download, default: None) If present, download
            data from the request via this stream.
      Returns:
        (Object) The response message.
      """
      config = self.GetMethodConfig('Update')
      return self._RunMethod(
          config, request, global_params=global_params,
          download=download)

    def WatchAll(self, request, global_params=None):
      """Watch for changes on all objects in a bucket.

      Args:
        request: (StorageObjectsWatchAllRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Channel) The response message.
      """
      config = self.GetMethodConfig('WatchAll')
      return self._RunMethod(
          config, request, global_params=global_params)

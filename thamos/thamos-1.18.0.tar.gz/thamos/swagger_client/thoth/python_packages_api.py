# coding: utf-8

"""
    Thoth User API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.6.0-dev
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from thamos.swagger_client.api_client import ApiClient


class PythonPackagesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_package_metadata(self, name, version, index, **kwargs):  # noqa: E501
        """Retrieve metadata relative to a Python Package from the Knowledge Graph.   # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_package_metadata(name, version, index, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: Name of the Python Package. (required)
        :param str version: Version of the Python Package. (required)
        :param str index: Index url of the Python Package. (required)
        :return: PythonPackageMetadataResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_package_metadata_with_http_info(name, version, index, **kwargs)  # noqa: E501
        else:
            (data) = self.get_package_metadata_with_http_info(name, version, index, **kwargs)  # noqa: E501
            return data

    def get_package_metadata_with_http_info(self, name, version, index, **kwargs):  # noqa: E501
        """Retrieve metadata relative to a Python Package from the Knowledge Graph.   # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_package_metadata_with_http_info(name, version, index, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: Name of the Python Package. (required)
        :param str version: Version of the Python Package. (required)
        :param str index: Index url of the Python Package. (required)
        :return: PythonPackageMetadataResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'version', 'index']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_package_metadata" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `get_package_metadata`")  # noqa: E501
        # verify the required parameter 'version' is set
        if ('version' not in params or
                params['version'] is None):
            raise ValueError("Missing the required parameter `version` when calling `get_package_metadata`")  # noqa: E501
        # verify the required parameter 'index' is set
        if ('index' not in params or
                params['index'] is None):
            raise ValueError("Missing the required parameter `index` when calling `get_package_metadata`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in params:
            query_params.append(('name', params['name']))  # noqa: E501
        if 'version' in params:
            query_params.append(('version', params['version']))  # noqa: E501
        if 'index' in params:
            query_params.append(('index', params['index']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/python/package/metadata', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PythonPackageMetadataResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_python_package_dependencies(self, name, version, index, **kwargs):  # noqa: E501
        """Get direct dependencies of Python libraries. If environment is provided, take into account environment markers that are evaluated during dependencies installation. If environment is not provided, any environment is considered.   # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_python_package_dependencies(name, version, index, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: Name of the Python Package. (required)
        :param str version: Version of the Python Package. (required)
        :param str index: Index url of the Python Package. (required)
        :param str os_name: Name of operating system to consider as environment where package is installed in.
        :param str os_version: Version of operating system to consider as environment where package is installed in.
        :param str python_version: Version of Python interpreter used to install the given package.
        :param bool marker_evaluation_result: Consider marker evaluation result for the given environment. If set to None, marker evaluation result is not taken into account. 
        :return: PythonPackageDependencies
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_python_package_dependencies_with_http_info(name, version, index, **kwargs)  # noqa: E501
        else:
            (data) = self.get_python_package_dependencies_with_http_info(name, version, index, **kwargs)  # noqa: E501
            return data

    def get_python_package_dependencies_with_http_info(self, name, version, index, **kwargs):  # noqa: E501
        """Get direct dependencies of Python libraries. If environment is provided, take into account environment markers that are evaluated during dependencies installation. If environment is not provided, any environment is considered.   # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_python_package_dependencies_with_http_info(name, version, index, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: Name of the Python Package. (required)
        :param str version: Version of the Python Package. (required)
        :param str index: Index url of the Python Package. (required)
        :param str os_name: Name of operating system to consider as environment where package is installed in.
        :param str os_version: Version of operating system to consider as environment where package is installed in.
        :param str python_version: Version of Python interpreter used to install the given package.
        :param bool marker_evaluation_result: Consider marker evaluation result for the given environment. If set to None, marker evaluation result is not taken into account. 
        :return: PythonPackageDependencies
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'version', 'index', 'os_name', 'os_version', 'python_version', 'marker_evaluation_result']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_python_package_dependencies" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `get_python_package_dependencies`")  # noqa: E501
        # verify the required parameter 'version' is set
        if ('version' not in params or
                params['version'] is None):
            raise ValueError("Missing the required parameter `version` when calling `get_python_package_dependencies`")  # noqa: E501
        # verify the required parameter 'index' is set
        if ('index' not in params or
                params['index'] is None):
            raise ValueError("Missing the required parameter `index` when calling `get_python_package_dependencies`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in params:
            query_params.append(('name', params['name']))  # noqa: E501
        if 'version' in params:
            query_params.append(('version', params['version']))  # noqa: E501
        if 'index' in params:
            query_params.append(('index', params['index']))  # noqa: E501
        if 'os_name' in params:
            query_params.append(('os_name', params['os_name']))  # noqa: E501
        if 'os_version' in params:
            query_params.append(('os_version', params['os_version']))  # noqa: E501
        if 'python_version' in params:
            query_params.append(('python_version', params['python_version']))  # noqa: E501
        if 'marker_evaluation_result' in params:
            query_params.append(('marker_evaluation_result', params['marker_evaluation_result']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/python/package/dependencies', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PythonPackageDependencies',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_python_platform(self, **kwargs):  # noqa: E501
        """Get supported platforms for Python ecosystem.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_python_platform(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: PythonPlatforms
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_python_platform_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_python_platform_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_python_platform_with_http_info(self, **kwargs):  # noqa: E501
        """Get supported platforms for Python ecosystem.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_python_platform_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: PythonPlatforms
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_python_platform" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/python/platform', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PythonPlatforms',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_python_package_indexes(self, **kwargs):  # noqa: E501
        """List registered Python package indexes.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_python_package_indexes(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: PythonPackageIndexes
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_python_package_indexes_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_python_package_indexes_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_python_package_indexes_with_http_info(self, **kwargs):  # noqa: E501
        """List registered Python package indexes.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_python_package_indexes_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: PythonPackageIndexes
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_python_package_indexes" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/python-package-index', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PythonPackageIndexes',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_python_package_versions(self, name, **kwargs):  # noqa: E501
        """List versions of the given Python package.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_python_package_versions(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: Name of the Python Package. (required)
        :param int page: Page offset in pagination.
        :return: PythonPackageVersionsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_python_package_versions_with_http_info(name, **kwargs)  # noqa: E501
        else:
            (data) = self.list_python_package_versions_with_http_info(name, **kwargs)  # noqa: E501
            return data

    def list_python_package_versions_with_http_info(self, name, **kwargs):  # noqa: E501
        """List versions of the given Python package.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_python_package_versions_with_http_info(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: Name of the Python Package. (required)
        :param int page: Page offset in pagination.
        :return: PythonPackageVersionsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_python_package_versions" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `list_python_package_versions`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in params:
            query_params.append(('name', params['name']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/python/package/versions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PythonPackageVersionsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

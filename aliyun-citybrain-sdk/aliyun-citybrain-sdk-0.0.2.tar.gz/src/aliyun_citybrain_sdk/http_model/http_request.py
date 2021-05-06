import json
from urllib.parse import urlencode
import time
from aliyun_citybrain_sdk import sign_tool
from six import iteritems


class HttpRequest(object):
    def __init__(self,
                 app_model,
                 method='GET',
                 domain="api-citybrain.aliyun.com",
                 uri_pattern="/datafusion/dataApi/call/",
                 protocol="http",
                 header=None,
                 timeout=None,
                 body_params=None):
        """
        :param app_model: 请求接口，例如：getDrdchlInfo
        :param method: 请求方法，GET, POST
        :param domain: 域名
        :param uri_pattern: url 前缀
        :param protocol: http_model or https
        :param header: 请求头信息，选填
        :param body_params:
        """
        self._app_model = app_model
        self._uri_pattern = uri_pattern
        self._header = header or {}
        self._method = str.upper(method)
        self._protocol = protocol
        self._domain = domain
        self._timeout = timeout or 300
        self.body_params = body_params
        self._body = ''
        self._content_md5 = ''

    def get_headers(self):
        return self._header

    def set_header(self, k, v):
        self._header[k] = v

    def get_protocol(self):
        return self._protocol

    def get_domain(self):
        return self._domain

    def get_uri_pattern(self):
        return self._uri_pattern

    def get_uri(self):
        return self._uri_pattern + self._app_model

    def get_url(self):
        if self._method == 'GET':
            query = urlencode(self.get_body())

            return self._uri_pattern + self._app_model + '?' + query

        return self._uri_pattern + self._app_model

    def get_method(self):
        return self._method

    def get_timeout(self):
        return self._timeout

    def get_body(self):
        return self.body_params or {}

    def set_body_params(self, body):
        self.body_params = body

    def handle_headers(self, ak, sk):
        self.set_header('X-Ca-Key', ak)
        self.set_header('X-Ca-Timestamp', str(int(time.time() * 1000)))
        self.set_header('X-Ca-Nonce', sign_tool.get_uuid4())
        self.set_header('Accept', self._header.get('Accept', 'application/json'))

        if self._header.get('Content-Type') is None:
            content_type = "application/json" if self._method == 'GET' else "application/x-www-form-urlencoded"
            self.set_header('Content-Type', content_type)

        self.set_header('Content-Type', self._header['Content-Type'])

        if self._method == 'POST' and 'application/octet-stream' in self._header['Content-Type']:
            self.set_body_params(json.dumps(self.get_body()))
            self._header['Content-MD5'] = sign_tool.to_md5_base64(self.get_body())
            str_to_sign = self.build_sign_str(uri=self.get_uri(),
                                              method=self._method,
                                              headers=self._header,
                                              body={})
        else:
            str_to_sign = self.build_sign_str(uri=self.get_uri(),
                                              method=self._method,
                                              headers=self._header,
                                              body=self.get_body())
        self.set_header('X-Ca-Signature', sign_tool.to_hash_sha256(str_to_sign, sk))
        return self._header

    @staticmethod
    def build_sign_str(uri=None, method=None, headers=None, body=None):
        """
        :param uri:
        :param method:
        :param headers:
        :param body: get 请求参数解析成body
        :return:
        """
        lf = '\n'
        string_to_sign = []
        string_to_sign.append(method)

        string_to_sign.append(lf)
        if "Accept" in headers and headers['Accept']:
            string_to_sign.append(headers['Accept'])

        string_to_sign.append(lf)
        if 'Content-MD5' in headers and headers['Content-MD5']:
            string_to_sign.append(headers['Content-MD5'])

        string_to_sign.append(lf)
        if 'Content-Type' in headers and headers['Content-Type']:
            string_to_sign.append(headers['Content-Type'])

        string_to_sign.append(lf)
        if 'Date' in headers and headers['Date']:
            string_to_sign.append(headers['Date'])

        string_to_sign.append(lf)
        string_to_sign.append(HttpRequest.build_canonical_headers(headers=headers, header_begin="x-acs-"))
        string_to_sign.append(HttpRequest.build_query_string(uri=uri, queries=body))
        return ''.join(string_to_sign)

    @staticmethod
    def build_query_string(uri, queries):
        uri_parts = uri.split("?")
        if len(uri_parts) > 1 and uri_parts[1] is not None:
            queries[uri_parts[1]] = None
        query_builder = uri_parts[0]
        sorted_map = sorted(iteritems(queries), key=lambda queries: queries[0])
        if len(sorted_map) > 0:
            query_builder += "?"
        for (k, v) in sorted_map:
            query_builder += k
            if v is not None:
                query_builder += "="
                query_builder += str(v)
            query_builder += '&'
        if query_builder.endswith('&'):
            query_builder = query_builder[0:(len(query_builder) - 1)]
        return query_builder

    @staticmethod
    def build_canonical_headers(headers, header_begin):
        result = ""
        unsort_map = dict()
        for (key, value) in iteritems(headers):
            if key.lower().find(header_begin) >= 0:
                unsort_map[key.lower()] = value
        sort_map = sorted(iteritems(unsort_map), key=lambda d: d[0])
        for (key, value) in sort_map:
            result += key + ":" + value
            result += "\n"
        return result

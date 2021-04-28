from flask import Response
from lyrebird.mock import lb_http_status
from lyrebird.log import get_logger


logger = get_logger()
class DuplicateRequest:

    def handle(self, handler_context):
        url = ''
        if 'url' in handler_context.flow.get('request'):
            url = handler_context.flow['request']['url']

        headers = {
            'Content-Type': 'text/html; charset=utf-8'
        }
        code = lb_http_status.STATUS_CODE_INFINITE_PROXY_LOOP
        resp_data = f'Duplicate request found: {url}\n'

        handler_context.flow['response']['headers'] = headers
        handler_context.flow['response']['code'] = code
        handler_context.flow['response']['data'] = resp_data

        handler_context.response = Response(resp_data, status=code, headers=headers)
        logger.info(f'<Proxy> ERROR::INFINITE_PROXY_LOOP {url}')

# -*- coding: utf-8 -*-

from yuansfer.api_helper import APIHelper
from yuansfer.http.api_response import ApiResponse
from yuansfer.api.base_api import BaseApi
from yuansfer.exception import InvalidParamsError
from yuansfer.exception import RequireParamsError
from yuansfer import constant


class PayoutApi(BaseApi):

    """A Controller to access Endpoints in the Yuansfer API."""

    def __init__(self, config):
        super(PayoutApi, self).__init__(config)

    def pay(self,
                  body):
        """POST Request

        Args:
            body: An object containing the fields to
                POST for the request.  See the corresponding object definition
                for field details.
        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Success
        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.
        """

        # Prepare query URL
        _url_path = constant.PAYOUT_PAY
        _query_builder = self.config.get_base_uri()
        _query_url = _query_builder+_url_path

        # Parameters validation
        self.amount_validate('amount',body['amount'])

        requiredFileds = ['customerNo','accountToken','currency','invoiceId']
        self.validate_parameter(requiredFileds,body)

        # Prepare and execute request
        _request = self.config.http_client.post(_query_url, headers=None, parameters=body)
        _response = self.execute_request(_request)

        if type(_response.response) is not dict:
            _errors = _response.reason
        else:
            _errors = None
        _result = ApiResponse(_response, body=_response.response, errors=_errors)
        return _result

    def inquiry(self,
                  body):
        """POST Request

        Args:
            body: An object containing the fields to
                POST for the request.  See the corresponding object definition
                for field details.
        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Success
        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.
        """

        # Prepare query URL
        _url_path = constant.PAYOUT_INQURIES
        _query_builder = self.config.get_base_uri()
        _query_url = _query_builder+_url_path

        # Parameters validation
        requiredFileds = ['invoiceId']
        self.validate_parameter(requiredFileds,body)

        # Prepare and execute request
        _request = self.config.http_client.post(_query_url, headers=None, parameters=body)
        _response = self.execute_request(_request)

        if type(_response.response) is not dict:
            _errors = _response.reason
        else:
            _errors = None
        _result = ApiResponse(_response, body=_response.response, errors=_errors)
        return _result

    def create_account(self,
                  body):
        """POST Request

        Args:
            body: An object containing the fields to
                POST for the request.  See the corresponding object definition
                for field details.
        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Success
        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.
        """

        # Prepare query URL
        _url_path = constant.PAYOUT_CREATE_ACCOUNT
        _query_builder = self.config.get_base_uri()
        _query_url = _query_builder+_url_path

        # Parameters validation
        requiredFileds = ['accountType','email','firstName','lastName','countryCode','dateOfBirth',
                         'street','city','state','zip']
        self.validate_parameter(requiredFileds,body)

        # Prepare and execute request
        _request = self.config.http_client.post(_query_url, headers=None, parameters=body)
        _response = self.execute_request(_request)

        if type(_response.response) is not dict:
            _errors = _response.reason
        else:
            _errors = None
        _result = ApiResponse(_response, body=_response.response, errors=_errors)
        return _result

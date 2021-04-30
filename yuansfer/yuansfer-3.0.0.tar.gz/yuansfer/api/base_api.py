from yuansfer.api_helper import APIHelper
from yuansfer.exception import RequireParamsError
from yuansfer.exception import InvalidParamsError
import hashlib
import re

class BaseApi(object):

    def global_headers(self):
        return{
            'Content-Type': 'application/x-www-form-urlencoded',
            'accept': 'application/json',
        }

    def __init__(self, config):
        self._config = config

    @property
    def config(self):
        return self._config

    def date_validate(self, name, value):
        # Check if date exists
        if value is None:
            raise RequireParamsError(params=name)

        reg = r"^\\d{4}\\d{2}\\d{2}$"

        if not re.match(reg, value):
            raise InvalidParamsError("data error: " + name)

    def number_validate(self, name, value):
        # Check if number exists
        if value is None:
            raise RequireParamsError(params=name)

        reg = r"^[0-9]*[1-9][0-9]*$"

        if not re.match(reg, value):
            raise InvalidParamsError("data error: " + name)

    def amount_validate(self, name, value):
        # Check if amount exists
        if value is None:
            raise RequireParamsError(params=name)

        reg = r"(?=.*?\d)^\$?(([1-9]\d{0,2}(,\d{3})*)|\d+)?(\.\d{1,2})?$"

        if not re.match(reg, value):
            raise InvalidParamsError("data error: " + name)

    def validate_parameter(self, requiredFileds, body):
        for name in requiredFileds:
            if name not in body:
                raise RequireParamsError(params=name)
            else:
                if body[name] is None:
                    raise RequireParamsError(params=name)

    def execute_request(self, request, binary=False):
        # Invoke the API call to fetch the response.
        request.headers = self.global_headers()
        request.parameters['verifySign'] = self.verify_sign_method(request.parameters)
        func = self.config.http_client.execute
        response = func(request)

        return response

    def verify_sign_method(self, parameters):
        """Convert object to request params
        Args:
            parameters (object): The parameters to convert.
        Returns:
            str: string with appended parameters.
        """
        # Parameter validation
        if self.config is None:
            raise InvalidParamsError('Configs are missing')

        parameters['merchantNo'] = self.config.merchantNo
        parameters['storeNo'] = self.config.storeNo
        dictionaryParams = APIHelper.to_dictionary(parameters)
        stringParams = APIHelper.append_parameters(dictionaryParams)
        md5TokenStr =hashlib.md5(self.config.token.encode("utf-8")).hexdigest()
        res = hashlib.md5((stringParams + '&' + md5TokenStr).encode("utf-8")).hexdigest()

        return res

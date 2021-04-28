# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.  # noqa: E501

    OpenAPI spec version: v2.1
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class TspHealthCheckStatusDescription(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'description': 'str',
        'error': 'str',
        'hostname': 'str',
        'response_seconds': 'str',
        'status': 'str',
        'type': 'str'
    }

    attribute_map = {
        'description': 'description',
        'error': 'error',
        'hostname': 'hostname',
        'response_seconds': 'responseSeconds',
        'status': 'status',
        'type': 'type'
    }

    def __init__(self, description=None, error=None, hostname=None, response_seconds=None, status=None, type=None):  # noqa: E501
        """TspHealthCheckStatusDescription - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._error = None
        self._hostname = None
        self._response_seconds = None
        self._status = None
        self._type = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if error is not None:
            self.error = error
        if hostname is not None:
            self.hostname = hostname
        if response_seconds is not None:
            self.response_seconds = response_seconds
        if status is not None:
            self.status = status
        if type is not None:
            self.type = type

    @property
    def description(self):
        """Gets the description of this TspHealthCheckStatusDescription.  # noqa: E501

          # noqa: E501

        :return: The description of this TspHealthCheckStatusDescription.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TspHealthCheckStatusDescription.

          # noqa: E501

        :param description: The description of this TspHealthCheckStatusDescription.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def error(self):
        """Gets the error of this TspHealthCheckStatusDescription.  # noqa: E501

          # noqa: E501

        :return: The error of this TspHealthCheckStatusDescription.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this TspHealthCheckStatusDescription.

          # noqa: E501

        :param error: The error of this TspHealthCheckStatusDescription.  # noqa: E501
        :type: str
        """

        self._error = error

    @property
    def hostname(self):
        """Gets the hostname of this TspHealthCheckStatusDescription.  # noqa: E501

          # noqa: E501

        :return: The hostname of this TspHealthCheckStatusDescription.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this TspHealthCheckStatusDescription.

          # noqa: E501

        :param hostname: The hostname of this TspHealthCheckStatusDescription.  # noqa: E501
        :type: str
        """

        self._hostname = hostname

    @property
    def response_seconds(self):
        """Gets the response_seconds of this TspHealthCheckStatusDescription.  # noqa: E501

          # noqa: E501

        :return: The response_seconds of this TspHealthCheckStatusDescription.  # noqa: E501
        :rtype: str
        """
        return self._response_seconds

    @response_seconds.setter
    def response_seconds(self, response_seconds):
        """Sets the response_seconds of this TspHealthCheckStatusDescription.

          # noqa: E501

        :param response_seconds: The response_seconds of this TspHealthCheckStatusDescription.  # noqa: E501
        :type: str
        """

        self._response_seconds = response_seconds

    @property
    def status(self):
        """Gets the status of this TspHealthCheckStatusDescription.  # noqa: E501

        Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later.  # noqa: E501

        :return: The status of this TspHealthCheckStatusDescription.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TspHealthCheckStatusDescription.

        Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later.  # noqa: E501

        :param status: The status of this TspHealthCheckStatusDescription.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def type(self):
        """Gets the type of this TspHealthCheckStatusDescription.  # noqa: E501

          # noqa: E501

        :return: The type of this TspHealthCheckStatusDescription.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TspHealthCheckStatusDescription.

          # noqa: E501

        :param type: The type of this TspHealthCheckStatusDescription.  # noqa: E501
        :type: str
        """

        self._type = type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(TspHealthCheckStatusDescription, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TspHealthCheckStatusDescription):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

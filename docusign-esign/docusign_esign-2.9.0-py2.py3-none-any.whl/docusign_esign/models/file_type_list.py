# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.  # noqa: E501

    OpenAPI spec version: v2
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class FileTypeList(object):
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
        'file_types': 'list[FileType]'
    }

    attribute_map = {
        'file_types': 'fileTypes'
    }

    def __init__(self, file_types=None):  # noqa: E501
        """FileTypeList - a model defined in Swagger"""  # noqa: E501

        self._file_types = None
        self.discriminator = None

        if file_types is not None:
            self.file_types = file_types

    @property
    def file_types(self):
        """Gets the file_types of this FileTypeList.  # noqa: E501

        A collection of file types.  # noqa: E501

        :return: The file_types of this FileTypeList.  # noqa: E501
        :rtype: list[FileType]
        """
        return self._file_types

    @file_types.setter
    def file_types(self, file_types):
        """Sets the file_types of this FileTypeList.

        A collection of file types.  # noqa: E501

        :param file_types: The file_types of this FileTypeList.  # noqa: E501
        :type: list[FileType]
        """

        self._file_types = file_types

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
        if issubclass(FileTypeList, dict):
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
        if not isinstance(other, FileTypeList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

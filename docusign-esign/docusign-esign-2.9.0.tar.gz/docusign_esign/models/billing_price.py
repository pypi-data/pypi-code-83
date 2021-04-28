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


class BillingPrice(object):
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
        'begin_quantity': 'str',
        'end_quantity': 'str',
        'unit_price': 'str'
    }

    attribute_map = {
        'begin_quantity': 'beginQuantity',
        'end_quantity': 'endQuantity',
        'unit_price': 'unitPrice'
    }

    def __init__(self, begin_quantity=None, end_quantity=None, unit_price=None):  # noqa: E501
        """BillingPrice - a model defined in Swagger"""  # noqa: E501

        self._begin_quantity = None
        self._end_quantity = None
        self._unit_price = None
        self.discriminator = None

        if begin_quantity is not None:
            self.begin_quantity = begin_quantity
        if end_quantity is not None:
            self.end_quantity = end_quantity
        if unit_price is not None:
            self.unit_price = unit_price

    @property
    def begin_quantity(self):
        """Gets the begin_quantity of this BillingPrice.  # noqa: E501

        Reserved: TBD  # noqa: E501

        :return: The begin_quantity of this BillingPrice.  # noqa: E501
        :rtype: str
        """
        return self._begin_quantity

    @begin_quantity.setter
    def begin_quantity(self, begin_quantity):
        """Sets the begin_quantity of this BillingPrice.

        Reserved: TBD  # noqa: E501

        :param begin_quantity: The begin_quantity of this BillingPrice.  # noqa: E501
        :type: str
        """

        self._begin_quantity = begin_quantity

    @property
    def end_quantity(self):
        """Gets the end_quantity of this BillingPrice.  # noqa: E501

          # noqa: E501

        :return: The end_quantity of this BillingPrice.  # noqa: E501
        :rtype: str
        """
        return self._end_quantity

    @end_quantity.setter
    def end_quantity(self, end_quantity):
        """Sets the end_quantity of this BillingPrice.

          # noqa: E501

        :param end_quantity: The end_quantity of this BillingPrice.  # noqa: E501
        :type: str
        """

        self._end_quantity = end_quantity

    @property
    def unit_price(self):
        """Gets the unit_price of this BillingPrice.  # noqa: E501

        Reserved: TBD  # noqa: E501

        :return: The unit_price of this BillingPrice.  # noqa: E501
        :rtype: str
        """
        return self._unit_price

    @unit_price.setter
    def unit_price(self, unit_price):
        """Sets the unit_price of this BillingPrice.

        Reserved: TBD  # noqa: E501

        :param unit_price: The unit_price of this BillingPrice.  # noqa: E501
        :type: str
        """

        self._unit_price = unit_price

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
        if issubclass(BillingPrice, dict):
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
        if not isinstance(other, BillingPrice):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

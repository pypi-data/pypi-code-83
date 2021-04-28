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


class PrefillTabs(object):
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
        'checkbox_tabs': 'list[Checkbox]',
        'radio_group_tabs': 'list[RadioGroup]',
        'tab_groups': 'list[TabGroup]',
        'text_tabs': 'list[Text]'
    }

    attribute_map = {
        'checkbox_tabs': 'checkboxTabs',
        'radio_group_tabs': 'radioGroupTabs',
        'tab_groups': 'tabGroups',
        'text_tabs': 'textTabs'
    }

    def __init__(self, checkbox_tabs=None, radio_group_tabs=None, tab_groups=None, text_tabs=None):  # noqa: E501
        """PrefillTabs - a model defined in Swagger"""  # noqa: E501

        self._checkbox_tabs = None
        self._radio_group_tabs = None
        self._tab_groups = None
        self._text_tabs = None
        self.discriminator = None

        if checkbox_tabs is not None:
            self.checkbox_tabs = checkbox_tabs
        if radio_group_tabs is not None:
            self.radio_group_tabs = radio_group_tabs
        if tab_groups is not None:
            self.tab_groups = tab_groups
        if text_tabs is not None:
            self.text_tabs = text_tabs

    @property
    def checkbox_tabs(self):
        """Gets the checkbox_tabs of this PrefillTabs.  # noqa: E501

        Specifies a tag on the document in a location where the recipient can select an option.  # noqa: E501

        :return: The checkbox_tabs of this PrefillTabs.  # noqa: E501
        :rtype: list[Checkbox]
        """
        return self._checkbox_tabs

    @checkbox_tabs.setter
    def checkbox_tabs(self, checkbox_tabs):
        """Sets the checkbox_tabs of this PrefillTabs.

        Specifies a tag on the document in a location where the recipient can select an option.  # noqa: E501

        :param checkbox_tabs: The checkbox_tabs of this PrefillTabs.  # noqa: E501
        :type: list[Checkbox]
        """

        self._checkbox_tabs = checkbox_tabs

    @property
    def radio_group_tabs(self):
        """Gets the radio_group_tabs of this PrefillTabs.  # noqa: E501

        Specifies a tag on the document in a location where the recipient can select one option from a group of options using a radio button. The radio buttons do not have to be on the same page in a document.  # noqa: E501

        :return: The radio_group_tabs of this PrefillTabs.  # noqa: E501
        :rtype: list[RadioGroup]
        """
        return self._radio_group_tabs

    @radio_group_tabs.setter
    def radio_group_tabs(self, radio_group_tabs):
        """Sets the radio_group_tabs of this PrefillTabs.

        Specifies a tag on the document in a location where the recipient can select one option from a group of options using a radio button. The radio buttons do not have to be on the same page in a document.  # noqa: E501

        :param radio_group_tabs: The radio_group_tabs of this PrefillTabs.  # noqa: E501
        :type: list[RadioGroup]
        """

        self._radio_group_tabs = radio_group_tabs

    @property
    def tab_groups(self):
        """Gets the tab_groups of this PrefillTabs.  # noqa: E501

          # noqa: E501

        :return: The tab_groups of this PrefillTabs.  # noqa: E501
        :rtype: list[TabGroup]
        """
        return self._tab_groups

    @tab_groups.setter
    def tab_groups(self, tab_groups):
        """Sets the tab_groups of this PrefillTabs.

          # noqa: E501

        :param tab_groups: The tab_groups of this PrefillTabs.  # noqa: E501
        :type: list[TabGroup]
        """

        self._tab_groups = tab_groups

    @property
    def text_tabs(self):
        """Gets the text_tabs of this PrefillTabs.  # noqa: E501

        Specifies a that that is an adaptable field that allows the recipient to enter different text information.  When getting information that includes this tab type, the original value of the tab when the associated envelope was sent is included in the response.  # noqa: E501

        :return: The text_tabs of this PrefillTabs.  # noqa: E501
        :rtype: list[Text]
        """
        return self._text_tabs

    @text_tabs.setter
    def text_tabs(self, text_tabs):
        """Sets the text_tabs of this PrefillTabs.

        Specifies a that that is an adaptable field that allows the recipient to enter different text information.  When getting information that includes this tab type, the original value of the tab when the associated envelope was sent is included in the response.  # noqa: E501

        :param text_tabs: The text_tabs of this PrefillTabs.  # noqa: E501
        :type: list[Text]
        """

        self._text_tabs = text_tabs

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
        if issubclass(PrefillTabs, dict):
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
        if not isinstance(other, PrefillTabs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

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


class EnvelopePurgeConfiguration(object):
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
        'purge_envelopes': 'str',
        'redact_pii': 'str',
        'remove_tabs_and_envelope_attachments': 'str',
        'retention_days': 'str'
    }

    attribute_map = {
        'purge_envelopes': 'purgeEnvelopes',
        'redact_pii': 'redactPII',
        'remove_tabs_and_envelope_attachments': 'removeTabsAndEnvelopeAttachments',
        'retention_days': 'retentionDays'
    }

    def __init__(self, purge_envelopes=None, redact_pii=None, remove_tabs_and_envelope_attachments=None, retention_days=None):  # noqa: E501
        """EnvelopePurgeConfiguration - a model defined in Swagger"""  # noqa: E501

        self._purge_envelopes = None
        self._redact_pii = None
        self._remove_tabs_and_envelope_attachments = None
        self._retention_days = None
        self.discriminator = None

        if purge_envelopes is not None:
            self.purge_envelopes = purge_envelopes
        if redact_pii is not None:
            self.redact_pii = redact_pii
        if remove_tabs_and_envelope_attachments is not None:
            self.remove_tabs_and_envelope_attachments = remove_tabs_and_envelope_attachments
        if retention_days is not None:
            self.retention_days = retention_days

    @property
    def purge_envelopes(self):
        """Gets the purge_envelopes of this EnvelopePurgeConfiguration.  # noqa: E501

          # noqa: E501

        :return: The purge_envelopes of this EnvelopePurgeConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._purge_envelopes

    @purge_envelopes.setter
    def purge_envelopes(self, purge_envelopes):
        """Sets the purge_envelopes of this EnvelopePurgeConfiguration.

          # noqa: E501

        :param purge_envelopes: The purge_envelopes of this EnvelopePurgeConfiguration.  # noqa: E501
        :type: str
        """

        self._purge_envelopes = purge_envelopes

    @property
    def redact_pii(self):
        """Gets the redact_pii of this EnvelopePurgeConfiguration.  # noqa: E501

          # noqa: E501

        :return: The redact_pii of this EnvelopePurgeConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._redact_pii

    @redact_pii.setter
    def redact_pii(self, redact_pii):
        """Sets the redact_pii of this EnvelopePurgeConfiguration.

          # noqa: E501

        :param redact_pii: The redact_pii of this EnvelopePurgeConfiguration.  # noqa: E501
        :type: str
        """

        self._redact_pii = redact_pii

    @property
    def remove_tabs_and_envelope_attachments(self):
        """Gets the remove_tabs_and_envelope_attachments of this EnvelopePurgeConfiguration.  # noqa: E501

          # noqa: E501

        :return: The remove_tabs_and_envelope_attachments of this EnvelopePurgeConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._remove_tabs_and_envelope_attachments

    @remove_tabs_and_envelope_attachments.setter
    def remove_tabs_and_envelope_attachments(self, remove_tabs_and_envelope_attachments):
        """Sets the remove_tabs_and_envelope_attachments of this EnvelopePurgeConfiguration.

          # noqa: E501

        :param remove_tabs_and_envelope_attachments: The remove_tabs_and_envelope_attachments of this EnvelopePurgeConfiguration.  # noqa: E501
        :type: str
        """

        self._remove_tabs_and_envelope_attachments = remove_tabs_and_envelope_attachments

    @property
    def retention_days(self):
        """Gets the retention_days of this EnvelopePurgeConfiguration.  # noqa: E501

          # noqa: E501

        :return: The retention_days of this EnvelopePurgeConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._retention_days

    @retention_days.setter
    def retention_days(self, retention_days):
        """Sets the retention_days of this EnvelopePurgeConfiguration.

          # noqa: E501

        :param retention_days: The retention_days of this EnvelopePurgeConfiguration.  # noqa: E501
        :type: str
        """

        self._retention_days = retention_days

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
        if issubclass(EnvelopePurgeConfiguration, dict):
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
        if not isinstance(other, EnvelopePurgeConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

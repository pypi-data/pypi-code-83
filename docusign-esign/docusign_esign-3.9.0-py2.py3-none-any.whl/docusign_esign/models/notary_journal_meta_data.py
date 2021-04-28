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


class NotaryJournalMetaData(object):
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
        'comment': 'str',
        'credible_witnesses': 'list[NotaryJournalCredibleWitness]',
        'signature_image': 'str',
        'signer_id_type': 'str'
    }

    attribute_map = {
        'comment': 'comment',
        'credible_witnesses': 'credibleWitnesses',
        'signature_image': 'signatureImage',
        'signer_id_type': 'signerIdType'
    }

    def __init__(self, comment=None, credible_witnesses=None, signature_image=None, signer_id_type=None):  # noqa: E501
        """NotaryJournalMetaData - a model defined in Swagger"""  # noqa: E501

        self._comment = None
        self._credible_witnesses = None
        self._signature_image = None
        self._signer_id_type = None
        self.discriminator = None

        if comment is not None:
            self.comment = comment
        if credible_witnesses is not None:
            self.credible_witnesses = credible_witnesses
        if signature_image is not None:
            self.signature_image = signature_image
        if signer_id_type is not None:
            self.signer_id_type = signer_id_type

    @property
    def comment(self):
        """Gets the comment of this NotaryJournalMetaData.  # noqa: E501

          # noqa: E501

        :return: The comment of this NotaryJournalMetaData.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this NotaryJournalMetaData.

          # noqa: E501

        :param comment: The comment of this NotaryJournalMetaData.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def credible_witnesses(self):
        """Gets the credible_witnesses of this NotaryJournalMetaData.  # noqa: E501

          # noqa: E501

        :return: The credible_witnesses of this NotaryJournalMetaData.  # noqa: E501
        :rtype: list[NotaryJournalCredibleWitness]
        """
        return self._credible_witnesses

    @credible_witnesses.setter
    def credible_witnesses(self, credible_witnesses):
        """Sets the credible_witnesses of this NotaryJournalMetaData.

          # noqa: E501

        :param credible_witnesses: The credible_witnesses of this NotaryJournalMetaData.  # noqa: E501
        :type: list[NotaryJournalCredibleWitness]
        """

        self._credible_witnesses = credible_witnesses

    @property
    def signature_image(self):
        """Gets the signature_image of this NotaryJournalMetaData.  # noqa: E501

          # noqa: E501

        :return: The signature_image of this NotaryJournalMetaData.  # noqa: E501
        :rtype: str
        """
        return self._signature_image

    @signature_image.setter
    def signature_image(self, signature_image):
        """Sets the signature_image of this NotaryJournalMetaData.

          # noqa: E501

        :param signature_image: The signature_image of this NotaryJournalMetaData.  # noqa: E501
        :type: str
        """

        self._signature_image = signature_image

    @property
    def signer_id_type(self):
        """Gets the signer_id_type of this NotaryJournalMetaData.  # noqa: E501

          # noqa: E501

        :return: The signer_id_type of this NotaryJournalMetaData.  # noqa: E501
        :rtype: str
        """
        return self._signer_id_type

    @signer_id_type.setter
    def signer_id_type(self, signer_id_type):
        """Sets the signer_id_type of this NotaryJournalMetaData.

          # noqa: E501

        :param signer_id_type: The signer_id_type of this NotaryJournalMetaData.  # noqa: E501
        :type: str
        """

        self._signer_id_type = signer_id_type

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
        if issubclass(NotaryJournalMetaData, dict):
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
        if not isinstance(other, NotaryJournalMetaData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

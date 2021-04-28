# coding: utf-8

"""
    Thoth User API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.6.0-dev
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class AnalysisResultResponseMetadata(object):
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
        'analyzer': 'str',
        'analyzer_version': 'str',
        'arguments': 'object',
        '_datetime': 'str',
        'distribution': 'AnalysisResultResponseMetadataDistribution',
        'hostname': 'str',
        'python': 'AnalysisResultResponseMetadataPython'
    }

    attribute_map = {
        'analyzer': 'analyzer',
        'analyzer_version': 'analyzer_version',
        'arguments': 'arguments',
        '_datetime': 'datetime',
        'distribution': 'distribution',
        'hostname': 'hostname',
        'python': 'python'
    }

    def __init__(self, analyzer=None, analyzer_version=None, arguments=None, _datetime=None, distribution=None, hostname=None, python=None):  # noqa: E501
        """AnalysisResultResponseMetadata - a model defined in Swagger"""  # noqa: E501
        self._analyzer = None
        self._analyzer_version = None
        self._arguments = None
        self.__datetime = None
        self._distribution = None
        self._hostname = None
        self._python = None
        self.discriminator = None
        self.analyzer = analyzer
        self.analyzer_version = analyzer_version
        self.arguments = arguments
        self._datetime = _datetime
        self.distribution = distribution
        self.hostname = hostname
        self.python = python

    @property
    def analyzer(self):
        """Gets the analyzer of this AnalysisResultResponseMetadata.  # noqa: E501

        Analyzer name which handled analysis.  # noqa: E501

        :return: The analyzer of this AnalysisResultResponseMetadata.  # noqa: E501
        :rtype: str
        """
        return self._analyzer

    @analyzer.setter
    def analyzer(self, analyzer):
        """Sets the analyzer of this AnalysisResultResponseMetadata.

        Analyzer name which handled analysis.  # noqa: E501

        :param analyzer: The analyzer of this AnalysisResultResponseMetadata.  # noqa: E501
        :type: str
        """
        if analyzer is None:
            raise ValueError("Invalid value for `analyzer`, must not be `None`")  # noqa: E501

        self._analyzer = analyzer

    @property
    def analyzer_version(self):
        """Gets the analyzer_version of this AnalysisResultResponseMetadata.  # noqa: E501

        Version of analyzer handling analysis.  # noqa: E501

        :return: The analyzer_version of this AnalysisResultResponseMetadata.  # noqa: E501
        :rtype: str
        """
        return self._analyzer_version

    @analyzer_version.setter
    def analyzer_version(self, analyzer_version):
        """Sets the analyzer_version of this AnalysisResultResponseMetadata.

        Version of analyzer handling analysis.  # noqa: E501

        :param analyzer_version: The analyzer_version of this AnalysisResultResponseMetadata.  # noqa: E501
        :type: str
        """
        if analyzer_version is None:
            raise ValueError("Invalid value for `analyzer_version`, must not be `None`")  # noqa: E501

        self._analyzer_version = analyzer_version

    @property
    def arguments(self):
        """Gets the arguments of this AnalysisResultResponseMetadata.  # noqa: E501

        Arguments passed to analyzer.  # noqa: E501

        :return: The arguments of this AnalysisResultResponseMetadata.  # noqa: E501
        :rtype: object
        """
        return self._arguments

    @arguments.setter
    def arguments(self, arguments):
        """Sets the arguments of this AnalysisResultResponseMetadata.

        Arguments passed to analyzer.  # noqa: E501

        :param arguments: The arguments of this AnalysisResultResponseMetadata.  # noqa: E501
        :type: object
        """
        if arguments is None:
            raise ValueError("Invalid value for `arguments`, must not be `None`")  # noqa: E501

        self._arguments = arguments

    @property
    def _datetime(self):
        """Gets the _datetime of this AnalysisResultResponseMetadata.  # noqa: E501

        Date and time of analysis end in ISO format.  # noqa: E501

        :return: The _datetime of this AnalysisResultResponseMetadata.  # noqa: E501
        :rtype: str
        """
        return self.__datetime

    @_datetime.setter
    def _datetime(self, _datetime):
        """Sets the _datetime of this AnalysisResultResponseMetadata.

        Date and time of analysis end in ISO format.  # noqa: E501

        :param _datetime: The _datetime of this AnalysisResultResponseMetadata.  # noqa: E501
        :type: str
        """
        if _datetime is None:
            raise ValueError("Invalid value for `_datetime`, must not be `None`")  # noqa: E501

        self.__datetime = _datetime

    @property
    def distribution(self):
        """Gets the distribution of this AnalysisResultResponseMetadata.  # noqa: E501


        :return: The distribution of this AnalysisResultResponseMetadata.  # noqa: E501
        :rtype: AnalysisResultResponseMetadataDistribution
        """
        return self._distribution

    @distribution.setter
    def distribution(self, distribution):
        """Sets the distribution of this AnalysisResultResponseMetadata.


        :param distribution: The distribution of this AnalysisResultResponseMetadata.  # noqa: E501
        :type: AnalysisResultResponseMetadataDistribution
        """
        if distribution is None:
            raise ValueError("Invalid value for `distribution`, must not be `None`")  # noqa: E501

        self._distribution = distribution

    @property
    def hostname(self):
        """Gets the hostname of this AnalysisResultResponseMetadata.  # noqa: E501

        Pod name where the analysis was done.  # noqa: E501

        :return: The hostname of this AnalysisResultResponseMetadata.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this AnalysisResultResponseMetadata.

        Pod name where the analysis was done.  # noqa: E501

        :param hostname: The hostname of this AnalysisResultResponseMetadata.  # noqa: E501
        :type: str
        """
        if hostname is None:
            raise ValueError("Invalid value for `hostname`, must not be `None`")  # noqa: E501

        self._hostname = hostname

    @property
    def python(self):
        """Gets the python of this AnalysisResultResponseMetadata.  # noqa: E501


        :return: The python of this AnalysisResultResponseMetadata.  # noqa: E501
        :rtype: AnalysisResultResponseMetadataPython
        """
        return self._python

    @python.setter
    def python(self, python):
        """Sets the python of this AnalysisResultResponseMetadata.


        :param python: The python of this AnalysisResultResponseMetadata.  # noqa: E501
        :type: AnalysisResultResponseMetadataPython
        """
        if python is None:
            raise ValueError("Invalid value for `python`, must not be `None`")  # noqa: E501

        self._python = python

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
        if issubclass(AnalysisResultResponseMetadata, dict):
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
        if not isinstance(other, AnalysisResultResponseMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

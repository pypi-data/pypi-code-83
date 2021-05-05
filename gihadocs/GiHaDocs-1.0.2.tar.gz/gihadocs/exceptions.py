from click import ClickException


class GiHaDocsException(ClickException):
    """Base exceptions for all GiHaDocs Exceptions"""


class ConfigurationError(GiHaDocsException):
    """Error in configuration"""

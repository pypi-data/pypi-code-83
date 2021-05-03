"""Custom errors."""


class VoicesError(Exception):
    """Base Process exception for voices integration."""


class RequestError(VoicesError):
    """Error for http request error."""


class DataError(VoicesError):
    """Error on data validations."""

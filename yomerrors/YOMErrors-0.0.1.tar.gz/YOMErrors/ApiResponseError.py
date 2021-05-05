
class ApiResponseError(Exception):
    """
        Exception raised when yom api service return an error
        Attributes:
            name -- error name
            status_code -- http response error code
    """
    def __init__(self, url, status_code):
        self.url = url
        self.status_code = status_code

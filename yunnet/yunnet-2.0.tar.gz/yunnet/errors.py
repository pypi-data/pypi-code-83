class APIError(Exception):
    def __init__(self, errorDict):
        self.errorObject = errorDict["error"]

        self.errorCode = errorDict["error"]["error_code"]
        self.errorMessage = errorDict["error"]["error_message"]

        self.message = "[" + str(self.errorCode) + "] " + str(self.errorMessage)


class AuthError(Exception):
    pass

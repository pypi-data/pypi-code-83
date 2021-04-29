class BaseAuthCodeFlowError(Exception):
    pass


class AuthCodeFlowError(BaseAuthCodeFlowError):
    def __init__(self, response, *args, **kwargs):
        self.response = response
        super().__init__(*args, **kwargs)

    def __str__(self):
        return f"response={self.response}"


class ImproperlyConfigured(BaseAuthCodeFlowError):
    def __init__(self, obj, keys, *args, abstract_base=None, **kwargs):
        self.obj = obj
        self.keys = keys
        self.abstract_base = abstract_base
        super().__init__(*args, **kwargs)

    def __str__(self):
        return (
            self.obj.__class__.__name__
            + (
                ""
                if self.abstract_base is None
                else self._get_extra_str_for_abstract_base()
            )
            + " requires that the following attributes be defined: "
            + ", ".join(self.keys)
        )

    def _get_extra_str_for_abstract_base(self):
        return (
            " is a descendant of the base class " + self.abstract_base.__name__ + " and"
        )


class StateForgeryError(BaseAuthCodeFlowError):
    pass

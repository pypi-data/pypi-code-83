def reader_method(func):
    """
    Decorator method, designed to be used in all methods that read a dataset and return it as a DynamicFrame. The
    decorator will call the wrapped method, then will clear all the options dictionaries so that options from a read
    don't reappear in the next read.
    :param func: Reader function
    :return: Result of the reader function
    """
    def wrapper(self, *args, **kwargs):
        result = func(self, *args, **kwargs)
        self.connection_options_dict.clear()
        self.format_options_dict.clear()
        self.additional_options_dict.clear()
        return result

    return wrapper

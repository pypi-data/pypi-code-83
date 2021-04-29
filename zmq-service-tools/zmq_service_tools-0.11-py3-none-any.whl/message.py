

class Message(object):

    def __init__(self, *args, **kwargs):

        self.method = kwargs.get('method', None)
        self.args = kwargs.get('args', list())
        self.kwargs = kwargs.get('args', dict())

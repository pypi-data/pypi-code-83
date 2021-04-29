import uuid


class Message(object):

    def __init__(self, *args, **kwargs):

        self.id = uuid.uuid4()
        self.method = kwargs.get('method', None)
        self.args = kwargs.get('args', list())
        self.kwargs = kwargs.get('kwargs', dict())


class Reply(object):

    def __init__(self, *args, **kwargs):
        self.id = kwargs.get('id', None)
        self.data = kwargs.get('data', None)

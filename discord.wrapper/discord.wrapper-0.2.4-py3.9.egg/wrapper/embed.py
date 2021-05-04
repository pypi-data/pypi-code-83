class Embed:
    __slots__ = ('colour', 'color', 'title', 'description',)

    def __init__(self, **kwargs):
        self.color = kwargs.pop('color', None)
        self.colour = kwargs.pop('colour', None)
        self.title = kwargs.get('title')
        self.description = kwargs.pop('description', "DEFAULT")

    def __repr__(self):
        fmt = ''
        for attr in self.__slots__:
            val = getattr(self, attr, None)
            if val:
                fmt += ' {}={}'.format(attr, val)
                break
        return "<Embed{}>".format(fmt)

    def to_dict(self):
        """Turns the object into a dictionary"""
        d = {
            key: getattr(self, key)
            for key in self.__slots__
            if hasattr(self, key) and getattr(self, key)
        }       
        

class QuestionVar(object):
    def __init__(self, fget=None):
        self.fget = fget
        self._key = fget.__name__

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        if not self._key in obj._vars:
            obj._vars[self._key] = self.fget(obj)
        return obj._vars[self._key]

    def __set_name__(self, owner, name):
        owner.questionvars += [self._key]

    def __delete__(self, obj):
        raise AttributeError("can't delete attribute")

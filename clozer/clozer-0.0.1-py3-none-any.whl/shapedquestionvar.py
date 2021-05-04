from .questionvar import QuestionVar
import itertools


def getter(key, pos, name):
    def fget(obj):
        return getattr(obj, key)[pos]
    fget.__name__ = name
    return fget


def ShapedQuestionVar(shape):
    positions = itertools.product(*[range(0, s) for s in shape])

    class ShapedQuestionVar(QuestionVar):
        def __set_name__(self, owner, name):
            super().__set_name__(owner, name)
            for pos in positions:
                n = "_".join([str(p) for p in pos])
                key = "{}_{}".format(self._key, n)
                owner.questionvars += [key]
                prop = QuestionVar(getter(self._key, pos, key))
                setattr(owner, key, prop)

    return ShapedQuestionVar

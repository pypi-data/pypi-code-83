def basic_pottable(name: str):
    """Shortcut for creating a new "blank" pottable with a specific name

    Long way:
    class FooFlower(Stem):
        def __init__(self):
            super().__init__(stem_name='foo_flower')

        def setter...

        def getter...

    Do instead:
    @basic_pottable('foo_flower')
    class FooFlower(Stem):

        def setter...

        def getter...

    """

    def decorator(cls):
        def init(self):
            super(cls, self).__init__(name)

        setattr(cls, "__init__", init)
        return cls

    return decorator

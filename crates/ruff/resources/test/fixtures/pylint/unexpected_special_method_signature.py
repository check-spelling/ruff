class TestClass:
    def __bool__(self):
        ...

    def __bool__(self, x):  # too many mandatory args
        ...

    def __bool__(self, x=1):  # additional optional args OK
        ...

    def __bool__():  # ignored; should be caught by E0211/N805
        ...

    @staticmethod
    def __bool__():
        ...

    @staticmethod
    def __bool__(x):  # too many mandatory args
        ...

    @staticmethod
    def __bool__(x=1):  # additional optional args OK
        ...

    def __eq__(self, other):  # multiple args
        ...

    def __eq__(self, other=1):  # expected arg is optional
        ...

    def __eq__(self):  # too few mandatory args
        ...

    def __eq__(self, other, other_other):  # too many mandatory args
        ...

    def __round__(self):  # allow zero additional args
        ...

    def __round__(self, x):  # allow one additional args
        ...

    def __round__(self, x, y):  # disallow 2 args
        ...

    def __round__(self, x, y, z=2):  # disallow 3 args even when one is optional
        ...

    def __eq__(self, *args):  # ignore *args
        ...

    def __eq__(self, x, *args):  # extra *args is ok
        ...

    def __eq__(self, x, y, *args):  # too many args with *args
        ...

    def __round__(self, *args):  # allow zero additional args
        ...

    def __round__(self, x, *args):  # allow one additional args
        ...

    def __round__(self, x, y, *args):  # disallow 2 args
        ...

    def __eq__(self, **kwargs):  # ignore **kwargs
        ...

    def __eq__(self, /, other=42):  # ignore positional-only args
        ...

    def __eq__(self, *, other=42):  # ignore positional-only args
        ...

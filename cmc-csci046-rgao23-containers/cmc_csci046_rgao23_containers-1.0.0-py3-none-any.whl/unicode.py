import unicodedata


class NormalizedStr:
    '''
    By default, Python's str type stores any valid unicode string.
    This can result in unintuitive behavior.
    For example:

    >>> 'César' in 'César Chávez'
    True
    >>> 'César' in 'César Chávez'
    False

    The two strings to the right of the in
    keyword above are equal *semantically*,
    but not equal *representationally*.
    In particular, the first is in NFC form, and the second is in NFD form.
    The purpose of this class is to automatically normalize our strings for us,
    making foreign languages "just work" a little bit easier.
    '''

    def __init__(self, text, normal_form='NFC'):
        self.nf = normal_form
        self.text = unicodedata.normalize(self.nf, text)

    def __repr__(self):
        '''
        The string returned by the __repr__
        function should be valid python code
        that can be substituted directly into the
        python interpreter to reproduce an equivalent object.
        '''
        return 'NormalizedStr(\'' + self.text + '\', \'' + self.nf + '\')'

    def __str__(self):
        '''
        This functions converts the NormalizedStr
        into a regular string object.
        The output is similar, but not
        exactly the same, as the __repr__ function.
        '''
        return self.text

    def __len__(self):
        '''
        Returns the length of the string.
        The expression `len(a)` desugars to a.__len__().
        '''
        return len(self.__str__())

    def __contains__(self, substr):
        '''
        Returns true if the `substr` variable is contained within `self`.
        The expression `a in b` desugars to `b.__contains__(a)`.

        HINT:
        You should normalize the `substr` variable
        ensure that the comparison is
        done semantically and not syntactically.
        '''
        sub_norm = unicodedata.normalize(self.nf, substr)
        return sub_norm in self.text

    def __getitem__(self, index):
        '''
        Returns the character at position `index`.
        The expression `a[b]` desugars to `a.__getitem__(b)`.
        '''
        return self.text[index]

    def lower(self):
        '''
        Returns a copy in the same normalized form, but lower case.
        '''
        return self.text.lower()

    def upper(self):
        '''
        Returns a copy in the same normalized form, but upper case.
        '''
        return self.text.upper()

    def __add__(self, b):
        '''
        Returns a copy of `self` with `b` appended to the end.
        The expression `a + b` gets desugared into `a.__add__(b)`.

        HINT:
        The addition of two normalized strings is not
        guaranteed to stay normalized
        Therefore, you must renormalize the strings after
        adding them together.
        '''
        stringa = unicodedata.normalize(self.nf, self.__str__())
        stringb = unicodedata.normalize(self.nf, b.__str__())
        new_string = unicodedata.normalize(self.nf, stringa + stringb)
        return NormalizedStr(new_string, self.nf)

    def __iter__(self):
        '''
        HINT:
        Recall that the __iter__ method returns a class
        which is the iterator object.
        You'll need to define your own iterator class
        with the appropriate magic methods,
        and return an instance of that class here.
        '''
        return NormStrIter(self.__str__())


class NormStrIter:
    def __init__(self, text):
        self.text = text
        self.i = 0

    def __next__(self):
        '''
        Return each item for the normalized string.
        '''
        if self.i == len(self.text):
            raise StopIteration
        else:
            self.i += 1
            return self.text[self.i - 1]

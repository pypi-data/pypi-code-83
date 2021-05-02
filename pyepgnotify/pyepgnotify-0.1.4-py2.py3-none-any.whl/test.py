import unicodedata


def compare_strs(s1, s2):
    def NFD(s):
        return unicodedata.normalize("NFD", s)

    return NFD(s1) == NFD(s2)


def compare_caseless(s1, s2):
    """
    https://docs.python.org/3/howto/unicode.html
    """

    def NFD(s):
        return unicodedata.normalize("NFD", s)

    return NFD(NFD(s1).casefold()) == NFD(NFD(s2).casefold())


def norm_str(s):
    """
    https://docs.python.org/3/howto/unicode.html
    """

    def NFD(s):
        return unicodedata.normalize("NFD", s)

    return NFD(NFD(s).casefold())

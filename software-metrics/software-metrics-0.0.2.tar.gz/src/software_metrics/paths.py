import re


def split_ref(ref):
    return re.split('[/|]', ref)

#!/usr/bin/env python3


__author__ = "Stefano Gigli"
__copyright__ = "Copyright 2019, SG Software"
__credits__ = []
__license__ = "GPL"
__version__ = "0.9"
__maintainer__ = "Stefano Gigli"
__email__ = "exe.dev.exe@gmail.com"
__status__ = "Beta version"


def from_camel_case_to_underscore(s_name: str) -> str:
    l_indices = list()
    for i_index, char in enumerate(s_name):
        if char.isupper():
            l_indices.append(i_index)
    l_indices.append(len(s_name))
    l_indices = l_indices[1:]

    l_words = list()
    i_last_index = 0
    for i_current_index in l_indices:
        l_words.append(s_name[i_last_index:i_current_index])
        i_last_index = i_current_index

    s_new_name = ""
    for s_word in l_words:
        s_new_name += s_word.lower() + "_"
    s_new_name = s_new_name[:-1]

    return s_new_name


if __name__ == '__main__':
    print(from_camel_case_to_underscore("TestClassOfNames"))

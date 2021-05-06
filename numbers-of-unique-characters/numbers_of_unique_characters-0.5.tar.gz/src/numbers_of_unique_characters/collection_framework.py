import os
import argparse
from collections import Counter
from functools import lru_cache


def add_args_argument():
    """Function for working with command line arguments."""

    parser = argparse.ArgumentParser(description="find the number of unique characters in the string")
    parser.add_argument("--string", type=str, default='', help="What is the str?")
    parser.add_argument("--file", type=lambda x: is_valid_file(parser, x), help="What is the file?")
    return parser.parse_args()


def is_valid_file(parser, arg):
    """Function that returns the contents of a file"""

    if not os.path.exists(arg):
        parser.error(f"The file {arg} does not exist!!!")
    else:
        return open(arg, 'r')


@lru_cache(maxsize=256)
def get_number_of_unique_characters(source_string: str) -> int:
    """Func that takes a string and returns the number of unique characters in the string"""

    if isinstance(source_string, str):
        symbol_counter = Counter(source_string)
        result = len([symbol_counter[symbol] for symbol in symbol_counter if symbol_counter[symbol] == 1])
        return result
    else:
        raise TypeError(f"incoming parameter should be 'str' not '{type(source_string).__name__}' ")



import pytest
import argparse
import unittest
from unittest.mock import patch
from numbers_of_unique_characters.collection_framework import *



def test_typical_behavior():
    typical_cases = ["abbbccdf", " 123 ", "Aaa4Bbb", "", " 1a2b", " 1a2b "]
    typical_results = [3, 3, 3, 0, 5]
    for typical_case, typical_result in zip(typical_cases, typical_results):
        assert get_number_of_unique_characters(typical_case) == typical_result


@pytest.mark.parametrize("atypical", (TypeError, 10, 99.99, None, (14, True, 876.34,)))
def test_atypical_behavior(atypical):
    with pytest.raises(TypeError):
        get_number_of_unique_characters(atypical)


class MyTest(unittest.TestCase):
    @patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(string="Some string", file="file.txt"))
    def test_add_args_argument(self, mock_args):
        """Checking that we have added arguments to args"""
        self.assertEqual(add_args_argument(), argparse.Namespace(string='Some string', file="file.txt"))

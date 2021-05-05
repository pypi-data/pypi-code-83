from typing import Callable, List, Union, Optional

from hausse.lib import Plugin, Element
import logging
import csv
import sys


class MultiLanguage(Plugin):
    """
        Multi Language
        ==============

        Support elements in multiple languages.
    """

    KEY = "lang"

    def __init__(self, default_language: str = None, languages = None):
        self.default = default_language
        self.languages = None

    def __iter__(self):
        return iter(self.languages)

    def __call__(self, elements: List[Element], metadata: dict, settings: dict):

        for element in elements:
            if hasattr(element, self.KEY):
                language = getattr(element, self.KEY)

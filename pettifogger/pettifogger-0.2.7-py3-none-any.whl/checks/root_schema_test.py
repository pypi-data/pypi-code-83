# -*- coding: UTF-8 -*-
__author__ = 'Aki Mäkinen'

import os

from unittest import TestCase
from pettifogger.utils.yaml import yaml

from .root.schema import validate_against_schema


def load_test_data(name):
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), f"./testdata/schema/{name}.yml")) as file:
        data = yaml.load(file)
    return data


class RootSchemaTests(TestCase):
    def test_missing_jobs(self):
        test_data = load_test_data("missing_jobs")
        ok, errors = validate_against_schema(test_data)
        assert ok == False and len(errors) == 1

    def test_missing_triggers(self):
        test_data = load_test_data("missing_triggers")
        ok, errors = validate_against_schema(test_data)
        assert ok == False and len(errors) == 1
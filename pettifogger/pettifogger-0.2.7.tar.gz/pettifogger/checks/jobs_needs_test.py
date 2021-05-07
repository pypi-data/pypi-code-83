# -*- coding: UTF-8 -*-
__author__ = 'Aki Mäkinen'

import os

from unittest import TestCase
from pettifogger.utils.yaml import yaml

from .jobs.needs import no_undefined_needs, no_circular_needs


def load_test_data(name):
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), f"./testdata/jobs/{name}.yml")) as file:
        data = yaml.load(file)
    return data


class NeedsTests(TestCase):
    def test_missing_needs(self):
        test_data = load_test_data("missing_needs")
        for name, job in test_data["jobs"].items():
            ok, errors = no_undefined_needs(job, test_data["jobs"].keys())
            assert ok == False and len(errors) == 1

    def test_cyclic_needs(self):
        test_data = load_test_data("circular_needs")
        ok = no_circular_needs(test_data["jobs"])
        assert ok == False
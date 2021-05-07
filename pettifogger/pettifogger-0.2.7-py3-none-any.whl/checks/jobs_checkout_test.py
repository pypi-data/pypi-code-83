# -*- coding: UTF-8 -*-
__author__ = 'Aki Mäkinen'

import os

from unittest import TestCase
from pettifogger.utils.yaml import yaml

from .jobs.checkout import has_checkout


def load_test_data(name):
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), f"./testdata/jobs/{name}.yml")) as file:
        data = yaml.load(file)
    return data


class CheckoutTests(TestCase):
    def test_checkout_negative(self):
        test_data = load_test_data("no_checkout")
        for name, job in test_data["jobs"].items():
            assert has_checkout(job) == False

    def test_checkout_positive(self):
        test_data = load_test_data("has_checkout")
        for name, job in test_data["jobs"].items():
            assert has_checkout(job) == True



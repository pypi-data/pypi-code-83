# -*- coding: UTF-8 -*-
__author__ = 'Aki Mäkinen'

import os

from unittest import TestCase
from pettifogger.utils.yaml import yaml

from .jobs.env_variables import existence


def load_test_data(name):
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), f"./testdata/jobs/{name}.yml")) as file:
        data = yaml.load(file)
    return data


class EnvVarTests(TestCase):
    def test_export(self):
        test_data = load_test_data("export_env_var")
        for _, job in test_data["jobs"].items():
            e, _ = existence(job, {})
            assert len(e.keys()) == 0

    def test_command_env_var(self):
        test_data = load_test_data("command_env_var")
        for _, job in test_data["jobs"].items():
            e, _ = existence(job, {})
            assert len(e.keys()) == 0

    def test_missing_env_var(self):
        test_data = load_test_data("missing_env_vars")
        for _, job in test_data["jobs"].items():
            e, _ = existence(job, {})
            keys = list(e.keys())
            assert len(keys) == 1

            assert len(e[keys[0]].messages) == 2
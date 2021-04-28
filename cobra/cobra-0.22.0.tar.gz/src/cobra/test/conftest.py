# -*- coding: utf-8 -*-

from __future__ import absolute_import

import json
from os.path import join

import pytest
from pandas import DataFrame

from cobra import Metabolite, Model, Reaction
from cobra.test import create_test_model, data_dir
from cobra.util import solver as sutil


try:
    from cPickle import load as _load
except ImportError:
    from pickle import load as _load


def pytest_addoption(parser):
    try:
        parser.addoption("--run-slow", action="store_true", help="run slow tests")
        parser.addoption(
            "--run-non-deterministic",
            action="store_true",
            help="run tests that sometimes (rarely) fail",
        )
    except ValueError:
        pass


@pytest.fixture(scope="session")
def data_directory():
    return data_dir


@pytest.fixture(scope="session")
def empty_once():
    return Model()


@pytest.fixture(scope="function")
def empty_model(empty_once):
    return empty_once.copy()


@pytest.fixture(scope="session")
def small_model():
    return create_test_model("textbook")


@pytest.fixture(scope="function")
def model(small_model):
    return small_model.copy()


@pytest.fixture(scope="session")
def large_once():
    return create_test_model("ecoli")


@pytest.fixture(scope="function")
def large_model(large_once):
    return large_once.copy()


@pytest.fixture(scope="session")
def medium_model():
    return create_test_model("salmonella")


@pytest.fixture(scope="function")
def salmonella(medium_model):
    return medium_model.copy()


@pytest.fixture(scope="function")
def solved_model(data_directory):
    model = create_test_model("textbook")
    with open(join(data_directory, "textbook_solution.pickle"), "rb") as infile:
        solution = _load(infile)
    return solution, model


@pytest.fixture(scope="session")
def tiny_toy_model():
    tiny = Model("Toy Model")
    m1 = Metabolite("M1")
    d1 = Reaction("ex1")
    d1.add_metabolites({m1: -1})
    d1.upper_bound = 0
    d1.lower_bound = -1000
    tiny.add_reactions([d1])
    tiny.objective = "ex1"
    return tiny


@pytest.fixture(scope="session")
def fva_results(data_directory):
    with open(join(data_directory, "textbook_fva.json"), "r") as infile:
        df = DataFrame(json.load(infile))
    df.sort_index(inplace=True)
    return df[["minimum", "maximum"]]


@pytest.fixture(scope="session")
def pfba_fva_results(data_directory):
    with open(join(data_directory, "textbook_pfba_fva.json"), "r") as infile:
        df = DataFrame(json.load(infile))
    df.sort_index(inplace=True)
    return df[["minimum", "maximum"]]


stable_optlang = ["glpk", "cplex", "gurobi"]
all_solvers = ["optlang-" + s for s in stable_optlang if s in sutil.solvers]


@pytest.fixture(params=all_solvers, scope="session")
def opt_solver(request):
    return request.param


@pytest.fixture(scope="function")
def metabolites(model, request):
    if request.param == "exchange":
        return [
            met
            for met in model.metabolites
            if met.compartment == "e" and "EX_" + met.id not in model.reactions
        ]
    elif request.param == "demand":
        return [
            met
            for met in model.metabolites
            if met.compartment == "c" and "DM_" + met.id not in model.reactions
        ]
    elif request.param == "sink":
        return [
            met
            for met in model.metabolites
            if met.compartment == "c" and "SK_" + met.id not in model.reactions
        ]
    else:
        raise ValueError("unknown metabolites {}".format(request.param))

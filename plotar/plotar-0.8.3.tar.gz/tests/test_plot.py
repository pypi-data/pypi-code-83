import pytest

import plotar

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
from sklearn import datasets
from pathlib import Path

BASE = Path("../..")
EXAMPLES = BASE / 'examples'

def test_iris():
    iris = datasets.load_iris()
    data = plotar.plotar(iris.data, iris.target, return_data=True,push_data=False)
    with open(BASE/'iris.json') as f:
        ref = json.load(f)
    assert ref==data

from finesse.script import unparse


def test_lambda(model):
    model.lambda0 = 1550e-9
    assert unparse(model) == "lambda(1.55e-06)"

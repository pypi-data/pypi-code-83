from dssystem.method import SimpleAdditiveWeighted
import numpy as np
import pandas as pd
dataset = pd.DataFrame({"Rainfall": [25, 21, 19, 22],
                        "Drainage": [67, 78, 53, 25],
                        "Usage of land": [7, 6, 5, 2],
                        "Tophography": [20, 24, 33, 31]},
                       index=["L1", "L2", "L3", "L4"])

method = SimpleAdditiveWeighted(
    dataset, [.25, .25, .25, .25], ["Usage of land"])
print(method.getChosenOneByIndex())  # to get chosen alternative name
print(method.getDecisionMatrix())  # to get decision matrix
print(method.normalize())  # to get normalized decision matrix
print(method.createDecision())  # to get list of alternative's score

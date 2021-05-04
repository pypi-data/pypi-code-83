
import pandas as pd
import numpy as np


class SimpleAdditiveWeighted:

    def __init__(self, data, weights, non_beneficial=None):
        self.data = data
        self.alternatives = np.array(data.index.values)
        self.criteria = np.array(data.columns.values)
        self.__criteriaWeight = np.array(weights)
        if non_beneficial is not None:
            self.non_beneficial = non_beneficial
        else:
            self.non_beneficial = None

    def getDecisionMatrix(self):
        return np.array(self.data[self.criteria])

    def normalize(self):
        __normalizedMatrix = [[0]*len(self.criteria)
                              for _ in range(len(self.alternatives))]
        if self.non_beneficial is not None:
            for ix in range(len(self.alternatives)):
                for iy in range(len(self.criteria)):
                    if self.criteria[iy] in self.non_beneficial:
                        __normalizedMatrix[ix][iy] = round(min(
                            self.data[self.criteria[iy]]) / self.getDecisionMatrix()[ix][iy], 2)
                    else:
                        __normalizedMatrix[ix][iy] = round(self.getDecisionMatrix()[ix][iy] / max(
                            self.data[self.criteria[iy]]), 2)
        else:
            for ix in range(len(self.alternatives)):
                for iy in range(len(self.criteria)):
                    __normalizedMatrix[ix][iy] = round(self.getDecisionMatrix()[ix][iy] / max(
                        self.data[self.criteria[iy]]), 2)
        return np.array(__normalizedMatrix)

    def createDecision(self):
        all_decision_values = []
        for idx in range(len(self.alternatives)):
            temp_sum = 0
            for idj in range(len(self.__criteriaWeight)):
                temp_sum += round(self.normalize()
                                  [idx][idj] * self.__criteriaWeight[idj], 2)
            all_decision_values.append(temp_sum)
        return np.array(all_decision_values)

    def getChosenOneByIndex(self):
        return self.alternatives[np.where(self.createDecision() == np.max(self.createDecision()))][0]


dataset = pd.DataFrame({"Rainfall": [25, 21, 19, 22], "Drainage": [67, 78, 53, 25],
                        "Usage of land": [7, 6, 5, 2], "Topography": [20, 24, 33, 31]}, index=["L1", "L2", "L3", "L4"])
classifier = SimpleAdditiveWeighted(
    dataset, np.array([.25, .25, .25, .25]), ["Usage of land"])

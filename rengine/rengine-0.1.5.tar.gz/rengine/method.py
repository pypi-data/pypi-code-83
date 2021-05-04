
import numpy as np


class CollaborativeFiltering:

    def __init__(self):
        self.__sumxy = 0
        self.__powX = 0
        self.__powY = 0

    def cos_similarity(self, var1, var2, centered=True):
        sim_val = 0
        if len(var1) == len(var2[0]):
            if centered:
                __centeredVal1 = []
                for idx in range(len(var1)):
                    if var1[idx] == 0:
                        __centeredVal1.append(0)
                    else:
                        __centeredVal1.append(
                            round(var1[idx]-np.mean([item for item in var1 if item > 0]), 3))

                __allCentered = []
                for ix in range(len(var2)):
                    __rowCentered = []
                    for iy in range(len(var2[0])):
                        if var2[ix][iy] == 0:
                            __rowCentered.append(0)
                        else:
                            __rowCentered.append(
                                round(var2[ix][iy]-np.mean([dx for dx in var2[ix] if dx > 0]), 3))
                    __allCentered.append(__rowCentered)
                return self.__run(__centeredVal1, __allCentered)
                # return __centeredVal1, __allCentered
            else:
                return self.__run(var1, var2)

    def __run(self, target, dataToCompare):
        similarity = []

        for row in range(len(dataToCompare)):
            self.__sumxy = 0
            self.__powX = 0
            self.__powY = 0
            for col in range(len(dataToCompare[0])):
                self.__sumxy += target[col] * dataToCompare[row][col]
                self.__powX += target[col]**2
                self.__powY += dataToCompare[row][col]**2
            similarity.append(
                round(self.__sumxy/((np.sqrt(self.__powX))*(np.sqrt(self.__powY))), 3))
        return similarity

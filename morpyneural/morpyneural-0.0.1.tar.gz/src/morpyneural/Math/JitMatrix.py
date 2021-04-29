import numba
import numpy as np
import random
import math
from numba import int32, float32, deferred_type
from numba.experimental import jitclass


@jitclass([
    ('rows', int32),
    ('cols', int32),
    ('values', float32[:, :])
])
class JitMatrix(object):
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.values = np.zeros((self.rows, self.cols), dtype=np.float32)

    def set_value(self, x, y, value):
        self.values[x, y] = value

    @staticmethod
    def sigmoid(x):
        return 1 / (1 + np.exp(-x))

    @staticmethod
    def relu(x):
        return np.maximum(0, x)

    @staticmethod
    def dsigmoid(y):
        return y * (1 - y)

    @staticmethod
    def tanh(x):
        return math.tanh(x)

    @staticmethod
    def dtanh(x):
        return 1 / (math.pow(math.cos(x), 2))

    @staticmethod
    def from_array(array_values):
        """
        Set values from a 1D array values
        :param array_values:
        :return:
        """
        new_matrix = JitMatrix(array_values.size, 1)

        for i in range(array_values.size):
            new_matrix.set_value(i, 0, array_values[i])

        return new_matrix

    def randomize(self, low=-1, high=1):
        """
        Randomize values between low and high
        :param low:
        :param high:
        :return:
        """
        for i in range(self.rows):
            for j in range(self.cols):
                self.values[i, j] = random.uniform(low, high)

        return self

    def add(self, jit_matrix):
        """
        Addition operation
        :param jit_matrix:
        :return:
        """
        for i in range(self.rows):
            for j in range(self.cols):
                self.values[i, j] = self.values[i, j] + jit_matrix.values[i, j]

        return self

    def multiply(self, value):
        """
        Multiply operation
        :param value:
        :return:
        """
        self.values = np.multiply(self.values, value)
        return self

    def dot_product(self, jit_matrix):
        """
        Dot Product operation
        :param jit_matrix:
        :return:
        """
        new_matrix = JitMatrix(self.rows, jit_matrix.cols)

        for i in range(new_matrix.rows):
            for j in range(new_matrix.cols):
                for k in range(self.cols):
                    new_matrix.values[i, j] += self.values[i, k] * jit_matrix.values[k, j]

        return new_matrix

    def crossover(self, jit_matrix):
        """
        Crossover the matrix with an other to create a new one
        :param jit_matrix:
        :return:
        """
        new_matrix = JitMatrix(self.rows, self.cols)

        for i in range(self.rows):
            for j in range(self.cols):
                if random.random() <= 0.5:
                    new_matrix.values[i, j] = self.values[i, j]
                else:
                    new_matrix.values[i, j] = jit_matrix.values[i, j]

        return new_matrix

    def mutation(self, rate=0.001, low=-1, high=1):
        """
        For every values, will mutate it if the random value is smaller than the rate.
        The new value will be a random between low and high.
        :param rate:
        :param low:
        :param high:
        :return:
        """
        for i in range(self.rows):
            for j in range(self.cols):
                if random.random() <= rate:
                    self.values[i, j] = random.uniform(low, high)

        return self

    def activate(self, fn_name):
        """
        Pass every values in an Activation Function
        :param fn_name:
        :return:
        """
        for i in range(self.rows):
            for j in range(self.cols):
                if fn_name == 1:
                    self.values[i, j] = self.sigmoid(self.values[i, j])
                elif fn_name == 2:
                    self.values[i, j] = self.dsigmoid(self.values[i, j])
                elif fn_name == 3:
                    self.values[i, j] = self.tanh(self.values[i, j])
                elif fn_name == 4:
                    self.values[i, j] = self.dtanh(self.values[i, j])
                else:
                    self.values[i, j] = self.sigmoid(self.values[i, j])

        return self


"""
Define Customs Types
"""
JitMatrixType = deferred_type()
JitMatrixType.define(JitMatrix.class_type.instance_type)
JitMatrixListType = numba.types.List(JitMatrix.class_type.instance_type, reflected=True)


#@numba.jit(JitMatrixType(numba.float32[:]), nopython=True)


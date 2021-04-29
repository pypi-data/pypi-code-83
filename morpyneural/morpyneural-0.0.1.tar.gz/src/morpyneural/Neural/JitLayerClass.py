import numba
from numba import deferred_type
from numba.experimental import jitclass
from morpyneural.Math.JitMatrix import JitMatrix, JitMatrixType


@jitclass([
    ('weights', JitMatrixType),
    ('biases', JitMatrixType),
    ('activation', numba.int32)
])
class JitLayer(object):
    def __init__(self, nodes, inputs, activation):
        """
        Layer contain Weights, Biases and Activation data's of a Neural Network
        """
        # Weights JitMatrix
        self.weights = JitMatrix(nodes, inputs).randomize(-1, 1)

        # Biases JitMatrix
        self.biases = JitMatrix(nodes, 1).randomize(-1, 1)

        # Set Activation
        self.activation = activation

    def feed_forward(self, inputs):
        """
        Feed Forwarding inputs into Weights, Biases and Activation function
        :param inputs:
        :return:
        """
        output = self.weights.dot_product(inputs)
        output = output.add(self.biases)
        output = output.activate(self.activation)
        return output

    def evolve(self, parent_a, parent_b, learning_rate):
        """
        Evolving Weights and Biases matrices values
        :param parent_a:
        :param parent_b:
        :param learning_rate:
        :return:
        """
        # Evolve Weights
        self.weights = parent_a.weights.crossover(parent_b.weights).mutation(learning_rate, -1, 1)

        # Evolve Biases
        self.biases = parent_a.biases.crossover(parent_b.biases).mutation(learning_rate, -1, 1)

        return self


"""
Define Customs Types
"""
JitLayerType = deferred_type()
JitLayerType.define(JitLayer.class_type.instance_type)
JitLayerListType = numba.types.List(JitLayer.class_type.instance_type)

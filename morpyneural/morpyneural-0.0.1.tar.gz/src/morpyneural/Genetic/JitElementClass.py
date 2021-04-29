import numba
from numba import deferred_type
from numba.experimental import jitclass
from morpyneural.Neural.JitNeuralNetworkClass import JitNeuralNetwork, JitNeuralNetworkType


@jitclass([
    ('active', numba.types.boolean),
    ('neural_network', JitNeuralNetworkType)
])
class JitElement:
    def __init__(self):
        """
        Element is a part of Population, it containing the neural network and (will) handle
        the score logic
        """
        self.active = True
        self.neural_network = JitNeuralNetwork()

    def build(self, layers_configuration):
        """
        Build the neural network
        :param layers_configuration:
        :return:
        """
        for i in range(len(layers_configuration)):
            self.neural_network.add_layer(layers_configuration[i][0], layers_configuration[i][1], layers_configuration[i][2])

        return self

    def feed_forward(self, inputs):
        """
        Feed forward inputs to the neural network
        :param inputs:
        :return:
        """
        return self.neural_network.feed_forward(inputs)

    def evolve(self, parent_a, parent_b, learning_rate=0.001):
        """
        Evolve the neural network
        :param parent_a:
        :param parent_b:
        :param learning_rate:
        :return:
        """
        self.neural_network.evolve(
            parent_a.neural_network,
            parent_b.neural_network,
            learning_rate=learning_rate
        )

        return self


"""
Define Customs Types
"""
JitElementType = deferred_type()
JitElementType.define(JitElement.class_type.instance_type)
JitElementListType = numba.types.List(JitElement.class_type.instance_type)

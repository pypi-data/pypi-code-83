import numba
from numba import deferred_type
from numba.experimental import jitclass
from morpyneural.Neural.JitLayerClass import JitLayer, JitLayerListType


@jitclass([
    ('layers', JitLayerListType)
])
class JitNeuralNetwork(object):
    def __init__(self):
        self.layers = [JitLayer(1, 1, 0)]
        self.layers.pop()

    def add_layer(self, inputs, nodes, activation):
        """
        Adding a new Layer
        :param inputs:
        :param nodes:
        :param activation:
        :return JitNeuralNetwork:
        """
        self.layers.insert(len(self.layers), JitLayer(nodes, inputs, activation))
        return self

    def feed_forward(self, inputs):
        """
        Feed forward inputs into the layers and return the predictions
        :param inputs:
        :return:
        """
        for layer in self.layers:
            inputs = layer.feed_forward(inputs)

        return inputs

    def evolve(self, parent_a, parent_b, learning_rate=0.001):
        """
        Evolving all layers by crossovering the two parents and mutate the matrices
        :param parent_a:
        :param parent_b:
        :param learning_rate:
        :return JitNeuralNetwork:
        """
        for i in range(len(parent_a.layers)):
            self.layers[i].evolve(parent_a.layers[i], parent_b.layers[i], learning_rate)

        return self


"""
Define Customs Types
"""
JitNeuralNetworkType = deferred_type()
JitNeuralNetworkType.define(JitNeuralNetwork.class_type.instance_type)
JitNeuralNetworkListType = numba.types.unicode_type(JitNeuralNetwork.class_type.instance_type)

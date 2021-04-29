from morpyneural.Neural.NeuralNetworkClass import NeuralNetwork


class Element:
    def __init__(self):
        """
        Element is a part of Population, it containing the neural network and (will) handle
        the score logic
        """
        self.active = True
        self.neural_network = NeuralNetwork()

    def build(self, layers_configuration):
        """
        Build the neural network
        :param layers_configuration:
        :return:
        """
        self.neural_network.build(layers_configuration)
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

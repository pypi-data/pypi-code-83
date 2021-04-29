import numba
from numba import deferred_type
from numba.experimental import jitclass
from morpyneural.Genetic.JitElementClass import JitElement, JitElementListType


@jitclass([
    ('elements', JitElementListType)
])
class JitPopulation(object):
    def __init__(self):
        self.elements = [JitElement()]
        self.elements.pop()

    def build(self, layers_configuration, max_elements):
        """
        Building new set of Elements
        :param layers_configuration:
        :param max_elements:
        :return:
        """
        for i in range(max_elements):
            new_element = JitElement().build(layers_configuration)
            self.elements.insert(len(self.elements), new_element)

        return self

    def feed_forward(self, inputs):
        """
        Feed forwarding all Elements
        :param inputs:
        :return:
        """
        results = []
        for element in self.elements:
            results.append(element.feed_forward(inputs))

        return results

    def evolve(self, parent_a, parent_b, learning_rate=0.001):
        """
        Evolve each Element
        :param parent_a:
        :param parent_b:
        :param learning_rate:
        :return:
        """
        for element in self.elements:
            if element != parent_a and element != parent_b:
                element.evolve(parent_a, parent_b, learning_rate=learning_rate)

        return self


"""
Define Customs Types
"""
JitPopulationType = deferred_type()
JitPopulationType.define(JitPopulation.class_type.instance_type)
JitPopulationListType = numba.types.List(JitPopulation.class_type.instance_type)

import torch
import torch.nn.functional as F
from torch import nn

from .module import Module


class Activation(Module):
    def identity_corruption(self, inputs):
        return inputs


class ReLU(nn.ReLU, Activation):
    pass


class Sigmoid(nn.Sigmoid, Activation):
    pass


class Tanh(nn.Tanh, Activation):
    pass


class Softmax(nn.Softmax, Activation):
    pass

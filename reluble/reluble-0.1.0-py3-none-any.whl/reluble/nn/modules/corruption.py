import torch
from torch import nn

from .module import Module


class Corruption(Module):
    """Base class for custom modules that only perform corruptions."""

    def forward(self, inputs):
        return inputs


class PredShuffleCorruption(Corruption):
    """Shuffles the last dimension of a network when corrupted.

    Shape:
        - Input: :math:`(N, \dots, C_{out})`
        - Output: :math:`(N, \dots, C_{out})`
    """

    def shuffle_corruption(self, x):
        indexing = torch.randperm(x.shape[-1])
        return x[..., indexing]


class ImageCorruption(Corruption):
    def half_black_corruption(self, image):
        return
        raise NotImplementedError

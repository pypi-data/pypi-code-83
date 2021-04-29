import torch
from torch import nn

from .module import Module


class AvgPool2d(nn.AvgPool2d, Module):
    pass


class MaxPool2d(nn.MaxPool2d, Module):
    pass


class AdaptiveAvgPool2d(nn.AdaptiveAvgPool2d, Module):
    pass

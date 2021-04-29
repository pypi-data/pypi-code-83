import torch
from torch import nn

from .module import Module


class BatchNorm1d(nn.BatchNorm1d, Module):
    pass


class BatchNorm2d(nn.BatchNorm1d, Module):
    pass

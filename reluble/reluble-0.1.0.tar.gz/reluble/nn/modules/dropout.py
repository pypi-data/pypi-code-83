import torch
from torch import nn

from .module import Module


class Dropout(nn.Dropout, Module):
    pass

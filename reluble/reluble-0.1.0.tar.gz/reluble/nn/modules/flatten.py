import torch
import torch.nn.functional as F
from torch import nn

from .module import Module


class Flatten(nn.Flatten, Module):
    pass

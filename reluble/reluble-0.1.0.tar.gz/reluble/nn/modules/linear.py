import torch
import torch.nn.functional as F
from torch import nn

from .module import Module


class Linear(nn.Linear, Module):
    def zeroed_weights_corruption(self, inputs):
        weight = torch.zeros_like(self.weight)
        weight = weight.to(inputs.device)
        return F.linear(inputs, weight, self.bias)

import torch
import torch.nn.functional as F
from torch import nn

from .module import Module


class Conv2d(nn.Conv2d, Module):
    def zeroed_weights_corruption(self, inputs):
        weight = torch.zeros_like(self.weight)
        weight = weight.to(inputs.device)
        return F.conv2d(
            inputs,
            weight,
            bias=self.bias,
            stride=self.stride,
            padding=self.padding,
            dilation=self.dilation,
            groups=self.groups,
        )

"""

borch package to build Neural Networks,

Neural Network
========

The module `borch.nn` provides implementations of neural network modules that are used
for deep probabilistic programming. It provides an interface almost identical to the
`torch.nn` modules and in many cases it is possible to just switch

    >>> import torch.nn as nn

to


    >>> import borch.nn as nn

and a network defined in torch is now probabilistic, without any other changes in the
model specification, one also need to change the loss function to `infer.vi.vi_loss`.

Examples:
    >>> import torch
    >>> import torch.nn.functional as F
    >>> from borch import nn
    >>> class Net(nn.Module):
    ...
    ...     def __init__(self):
    ...         super(Net, self).__init__()
    ...         self.conv1 = nn.Conv2d(1, 6, 5)
    ...         self.conv2 = nn.Conv2d(6, 16, 5)
    ...         self.fc1 = nn.Linear(16 * 5 * 5, 120)
    ...         self.fc2 = nn.Linear(120, 84)
    ...         self.fc3 = nn.Linear(84, 10)
    ...
    ...     def forward(self, x):
    ...         x = F.max_pool2d(F.relu(self.conv1(x)), (2, 2))
    ...         x = F.max_pool2d(F.relu(self.conv2(x)), 2)
    ...         x = x.view(-1, self.num_flat_features(x))
    ...         x = F.relu(self.fc1(x))
    ...         x = F.relu(self.fc2(x))
    ...         x = self.fc3(x)
    ...         return x
    ...
    ...     def num_flat_features(self, x):
    ...         size = x.size()[1:]
    ...         num_features = 1
    ...         for s in size:
    ...             num_features *= s
    ...         return num_features
    >>> Net()
    Net(
      (conv1): Conv2d(1, 6, kernel_size=(5, 5), stride=(1, 1))
      (conv2): Conv2d(6, 16, kernel_size=(5, 5), stride=(1, 1))
      (fc1): Linear(in_features=400, out_features=120, bias=True)
      (fc2): Linear(in_features=120, out_features=84, bias=True)
      (fc3): Linear(in_features=84, out_features=10, bias=True)
    )

Notes:
    `borch.nn` only supports mini-batches. The entire `borch.nn`package only
    supports inputs that are a mini-batch of samples, and not a single sample.

    For example, nn.Conv2d will take in a 4D Tensor of
    nSamples x nChannels x Height x Width.

"""

from borch.nn.torch_proxies import *
from borch.nn.compose import Sequential, Concurrent, Select
from borch.nn.reshape import Expand, ExpandBatch, View, BatchView, Flatten
from borch.nn.utility_modules import Identity, Apply, Cat
from borch.nn.recall import Recall
from borch.nn.activations import Hsigmoid, Hswish
from borch.nn import utils

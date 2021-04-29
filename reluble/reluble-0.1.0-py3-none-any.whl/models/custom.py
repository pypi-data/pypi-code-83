import torch
from reluble import nn
from torchvision.models import resnet18, wide_resnet50_2, densenet121


class Net(nn.Module):
    def __init__(self, activation=torch.relu):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(3, 6, (5, 5), bias=False)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(6, 16, (5, 5), bias=False)
        self.fc1 = nn.Linear(16 * 5 * 5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)
        self.activation = activation

    def forward(self, x):
        x = self.conv1(x)
        x = self.activation(x)
        x = self.pool(x)
        x = self.conv2(x)
        x = self.activation(x)
        x = self.pool(x)
        x = x.view(-1, 16 * 5 * 5)
        x = self.fc1(x)
        x = self.activation(x)
        x = self.fc2(x)
        x = self.activation(x)
        x = self.fc3(x)
        # x = self.activation(x)
        return x


class SimpleMLP(nn.Module):
    def __init__(self):
        super().__init__()
        self.l1 = nn.Linear(3 * 32 ** 2, 512)
        self.l2 = nn.Linear(512, 32)
        self.l3 = nn.Linear(32, 10)

    def forward(self, x):
        bs, ch, r, c = x.shape
        x = x.view(bs, -1)
        x = self.l1(x)
        x = torch.relu(x)
        x = self.l2(x)
        x = torch.relu(x)
        x = self.l3(x)
        return x

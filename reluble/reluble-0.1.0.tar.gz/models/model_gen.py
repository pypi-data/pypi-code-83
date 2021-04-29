import torch
import reluble.nn as nn
import torch.nn.functional as F
import numpy as np


FLAWS = np.array(
    [(nn.Sigmoid(),), (nn.ReLU(), nn.ReLU()), (nn.Conv2d, 4)],  # bottleneck  # no-op
    dtype=object,
)


class Squeeze(nn.Module):
    def __init__(self, *args):
        super(Squeeze, self).__init__()
        self.shape = args

    def forward(self, x):
        return torch.squeeze(x)


def get_cnn(
    in_ch, n_blocks, n_layers_per_block, layer_dims, n_classes=10, flaw_prob=0.0
):
    conv1 = nn.Conv2d(
        in_ch, layer_dims[0], kernel_size=(3, 3), stride=(1, 1), padding=(1, 1)
    )
    relu1 = nn.ReLU()

    blocks = [nn.Sequential(conv1, relu1)]
    for i_block in range(n_blocks):
        block = []
        for i_layer in range(n_layers_per_block):
            block.append(
                nn.Conv2d(
                    layer_dims[i_block],
                    layer_dims[i_block],
                    kernel_size=(3, 3),
                    stride=(1, 1),
                    padding=(1, 1),
                )
            )
            block.append(nn.ReLU())
        if np.random.rand() < flaw_prob:
            flaw = np.random.choice(FLAWS)
            if flaw[0] is nn.Conv2d:
                ch_expansion = flaw[1]
                flaw0 = nn.Conv2d(
                    layer_dims[i_block],
                    ch_expansion * layer_dims[i_block],
                    kernel_size=(3, 3),
                    stride=(1, 1),
                    padding=(1, 1),
                )
                flaw1 = nn.Conv2d(
                    ch_expansion * layer_dims[i_block],
                    layer_dims[i_block],
                    kernel_size=(3, 3),
                    stride=(1, 1),
                    padding=(1, 1),
                )

                block.append(flaw0)
                block.append(flaw1)
            else:
                block.append(flaw[0])

        if i_block < len(layer_dims)-1:
            # Downsample in space and ch to match next layer
            block.append(nn.Conv2d(layer_dims[i_block], layer_dims[i_block+1], kernel_size=1, stride=2))
        blocks.append(nn.Sequential(*block))

    blocks.append(nn.AdaptiveAvgPool2d(1))
    blocks.append(torch.nn.Flatten())
    blocks.append(nn.Linear(layer_dims[-1], n_classes))

    return torch.nn.Sequential(*blocks)


def get_mlp(in_dim, layer_dims, n_classes=10, activation=nn.ReLU(), flaw_prob=0.0):
    layer1 = nn.Linear(in_dim, layer_dims[0])
    relu1 = activation

    layers = [layer1, relu1]
    for in_dim, out_dim in zip(layer_dims[:-1], layer_dims[1:]):
        layers.append(nn.Linear(in_dim, out_dim))
        layers.append(activation)
        if np.random.rand() < flaw_prob:
            flaw = np.random.choice(FLAWS)
            if nn.Conv2d not in flaw:
                layers.append(flaw[0])

    layers.append(nn.Linear(layer_dims[-1], n_classes))

    return nn.Sequential(nn.Flatten(), *layers)


# if __name__ == '__main__':
# m = get_mlp(28 ** 2, [512, 256, 256, 128], flaw_prob=0.5)
# m = get_cnn(1, n_blocks=3, n_layers_per_block=4, layer_dims=[32, 64, 128, 512], flaw_prob=0.5)
#
# print(m)

""" SimCLR Model """

# Copyright (c) 2020. Lightly AG and its affiliates.
# All Rights Reserved

import torch
import torch.nn as nn


def _get_simclr_projection_head(num_ftrs: int, out_dim: int):
    """Returns a 2-layer projection head.

    Reference (07.12.2020):
    https://github.com/google-research/simclr/blob/master/model_util.py#L141

    """
    modules = [
        nn.Linear(num_ftrs, num_ftrs),
        #nn.BatchNorm1d(num_ftrs),
        nn.ReLU(),
        nn.Linear(num_ftrs, out_dim)
    ]
    return nn.Sequential(*modules)


class SimCLRAnna(nn.Module):
    """Implementation of the SimCLR[0] architecture

    Recommended loss: :py:class:`lightly.loss.ntx_ent_loss.NTXentLoss`

    [0] SimCLR, 2020, https://arxiv.org/abs/2002.05709

    Attributes:
        backbone:
            Backbone model to extract features from images.
        num_ftrs:
            Dimension of the embedding (before the projection head).
        out_dim:
            Dimension of the output (after the projection head).

    """

    def __init__(self,
                 backbone: nn.Module,
                 num_ftrs: int = 32,
                 out_dim: int = 128,
                 n_unique_augments=2):

        super(SimCLRAnna, self).__init__()

        self.backbone = backbone
        self.projection_head = _get_simclr_projection_head(num_ftrs, out_dim)

        self.enc = _get_simclr_projection_head(num_ftrs, num_ftrs)
        self.dec = _get_simclr_projection_head(num_ftrs, num_ftrs)
        self.augmentations = torch.nn.Embedding(n_unique_augments, num_ftrs)

    def forward(self,
                x0: torch.Tensor,
                x1: torch.Tensor,
                labels0,
                labels1):
        """Embeds and projects the input images.

        Extracts features with the backbone and applies the projection
        head to the output space. If both x0 and x1 are not None, both will be
        passed through the backbone and projection head. If x1 is None, only
        x0 will be forwarded.

        Args:
            x0:
                Tensor of shape bsz x channels x W x H.
            x1:
                Tensor of shape bsz x channels x W x H.
            return_features:
                Whether or not to return the intermediate features backbone(x).

        Returns:
            The output projection of x0 and (if x1 is not None) the output
            projection of x1. If return_features is True, the output for each x
            is a tuple (out, f) where f are the features before the projection
            head.

        Examples:
            >>> # single input, single output
            >>> out = model(x) 
            >>> 
            >>> # single input with return_features=True
            >>> out, f = model(x, return_features=True)
            >>>
            >>> # two inputs, two outputs
            >>> out0, out1 = model(x0, x1)
            >>>
            >>> # two inputs, two outputs with return_features=True
            >>> (out0, f0), (out1, f1) = model(x0, x1, return_features=True)

        """
        
        # forward pass of first input x0
        # f_back_0 = self.backbone(x0).squeeze()
        # f_latent0 = self.enc(f_back_0)
        
        # labels_ohe0 = torch.Tensor([[1, 0]] * x0.shape[0]).cuda()
        # f_augment0 = labels_ohe0 @ self.augmentations.weight

        # f_0 = self.dec(f_latent0 + f_augment0)

        # out0 = self.projection_head(f_back_0)
        #out0 = f_latent0

        f0 = self.backbone(x0).squeeze()
        # labels_ohe0 = torch.Tensor([[1, 0]]*x0.shape[0]).cuda()
        # f_augment0 = labels_ohe0 @ self.augmentations.weight
        # f0 = f_latent0 + f_augment0
        out0 = self.projection_head(f0)


        # forward pass of second input x1
        f1 = self.backbone(x1).squeeze()
        # labels_ohe1 = torch.Tensor([[0, 1]]*x1.shape[0]).cuda()
        # f_augment1 = labels_ohe1 @ self.augmentations.weight
        # f1 = f_latent1 + f_augment1
        out1 = self.projection_head(f1)
        
        #out1 = f_latent1

        # # append features if requested
        # if return_features:
        #     out1 = (out1, f1)

        # return both outputs
        return out0, out1, f0, f1

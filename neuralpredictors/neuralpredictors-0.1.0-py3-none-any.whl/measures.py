from torch import nn
import torch
import numpy as np
import warnings


def corr(y1, y2, axis=-1, eps=1e-8, **kwargs):
    """
    Compute the correlation between two NumPy arrays along the specified dimension(s).

    Args:
        y1:      first NumPy array
        y2:      second NumPy array
        axis:    dimension(s) along which the correlation is computed. Any valid NumPy axis spec works here
        eps:     offset to the standard deviation to avoid exploding the correlation due to small division (default 1e-8)
        **kwargs: passed to final numpy.mean operatoin over standardized y1 * y2

    Returns: correlation array
    """
    y1 = (y1 - y1.mean(axis=axis, keepdims=True)) / (y1.std(axis=axis, keepdims=True, ddof=0) + eps)
    y2 = (y2 - y2.mean(axis=axis, keepdims=True)) / (y2.std(axis=axis, keepdims=True, ddof=0) + eps)
    return (y1 * y2).mean(axis=axis, **kwargs)


def ptcorr(y1, y2, dim=-1, eps=1e-8, **kwargs):
    """
    Compute the correlation between two PyTorch tensors along the specified dimension(s).

    Args:
        y1:      first PyTorch tensor
        y2:      second PyTorch tensor
        dim:     dimension(s) along which the correlation is computed. Any valid PyTorch dim spec works here
        eps:     offset to the standard deviation to avoid exploding the correlation due to small division (default 1e-8)
        **kwargs: passed to final numpy.mean operatoin over standardized y1 * y2

    Returns: correlation tensor
    """
    y1 = (y1 - y1.mean(dim=dim, keepdim=True)) / (y1.std(dim=dim, keepdim=True) + eps)
    y2 = (y2 - y2.mean(dim=dim, keepdim=True)) / (y2.std(dim=dim, keepdim=True) + eps)
    return (y1 * y2).mean(dim=dim, **kwargs)


class Corr(nn.Module):
    def __init__(self, eps=1e-12, detach_target=True):
        """
        Compute correlation between the output and the target

        Args:
            eps (float, optional): Used to offset the computed variance to provide numerical stability.
                Defaults to 1e-12.
            detach_target (bool, optional): If True, `target` tensor is detached prior to computation. Appropriate when
                using this as a loss to train on. Defaults to True.
        """
        self.eps = eps
        self.detach_target = detach_target
        super().__init__()

    def forward(self, output, target):
        if self.detach_target:
            target = target.detach()
        delta_out = output - output.mean(0, keepdim=True)
        delta_target = target - target.mean(0, keepdim=True)

        var_out = delta_out.pow(2).mean(0, keepdim=True)
        var_target = delta_target.pow(2).mean(0, keepdim=True)

        corrs = (delta_out * delta_target).mean(0, keepdim=True) / (
            (var_out + self.eps) * (var_target + self.eps)
        ).sqrt()
        return corrs


class AvgCorr(nn.Module):
    def __init__(self, eps=1e-12):
        self.eps = eps
        super().__init__()

    def forward(self, output, target):
        # Add target detach here

        delta_out = output - output.mean(0, keepdim=True)
        delta_target = target - target.mean(0, keepdim=True)

        var_out = delta_out.pow(2).mean(0, keepdim=True)
        var_target = delta_target.pow(2).mean(0, keepdim=True)

        corrs = (delta_out * delta_target).mean(0, keepdim=True) / (
            (var_out + self.eps) * (var_target + self.eps)
        ).sqrt()
        # TODO: address the sign flip applied here
        return -corrs.mean()


class PoissonLoss(nn.Module):
    def __init__(self, bias=1e-12, per_neuron=False, avg=True):
        """
        Computes Poisson loss between the output and target. Loss is evaluated by computing log likelihood
        (up to a constant offset dependent on the target) that
        output prescribes the mean of the Poisson distribution and target is a sample from the distribution.

        Args:
            bias (float, optional): Value used to numerically stabilize evalution of the log-likelihood. This value is effecitvely added to the output during evaluation. Defaults to 1e-12.
            per_neuron (bool, optional): If set to True, the average/total Poisson loss is returned for each entry of the last dimension (assumed to be enumeration neurons) separately. Defaults to False.
            avg (bool, optional): If set to True, return mean loss. Otherwise returns the sum of loss. Defaults to True.
        """
        super().__init__()
        self.bias = bias
        self.per_neuron = per_neuron
        self.avg = avg
        if self.avg:
            warnings.warn("Poissonloss is averaged per batch. It's recommended to use `sum` instead")

    def forward(self, output, target):
        target = target.detach()
        loss = output - target * torch.log(output + self.bias)
        if not self.per_neuron:
            return loss.mean() if self.avg else loss.sum()
        else:
            loss = loss.view(-1, loss.shape[-1])
            return loss.mean(dim=0) if self.avg else loss.sum(dim=0)


class PoissonLoss3d(PoissonLoss):
    """
    Same as PoissonLoss, except that this automatically adjusts the length of the
    target along the 1st dimension (expected to correspond to the temporal dimension), such that
    when lag = target.size(1) - outout.size(1) > 0,
    PoissonLoss(output, target[:, lag:])
    is evaluted instead (thus equivalent to skipping the first `lag` frames).

    The constructor takes in the same arguments as in PoissonLoss
    """

    def forward(self, output, target):
        lag = target.size(1) - output.size(1)
        return super().forward(output, target[:, lag:])


class GammaLoss(nn.Module):
    def __init__(self, bias=1e-12, per_neuron=False):
        super().__init__()
        self.bias = bias
        self.per_neuron = per_neuron

    def forward(self, output, target):
        target = (target + self.bias).detach()
        # use output + 1/2 as shape parameter
        shape = output + 0.5

        # assert np.all(shape.detach().cpu().numpy() > 0), 'Shape parameter is smaller than zero'
        loss = torch.lgamma(shape) - (shape - 1) * torch.log(target) + target

        if not self.per_neuron:
            return loss.mean()
        else:
            return loss.view(-1, loss.shape[-1]).mean(dim=0)


class ExponentialLoss(nn.Module):
    def __init__(self, bias=1e-12, target_bias=1e-6, per_neuron=False):
        super().__init__()
        self.bias = bias
        self.target_bias = target_bias
        self.per_neuron = per_neuron

    def forward(self, output, target):
        output = output + self.bias

        target = (target + self.target_bias).detach()

        loss = target / output + torch.log(output)

        if not self.per_neuron:
            return loss.mean()
        else:
            return loss.view(-1, loss.shape[-1]).mean(dim=0)


class AnscombeMSE(nn.Module):
    def __init__(self, per_neuron=False):
        super().__init__()
        self.per_neuron = per_neuron

    @staticmethod
    def A(x):
        return 2 * torch.sqrt(x + 3 / 8)

    def forward(self, output, target):
        target = self.A(target).detach()
        output = self.A(output) - 1 / (4 * output.sqrt())

        loss = (target - output).pow(2)

        if not self.per_neuron:
            return loss.mean()
        else:
            return loss.view(-1, loss.shape[-1]).mean(dim=0)

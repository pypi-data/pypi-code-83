from typing import Callable, Dict, Any, Optional

import torch
from torch import Tensor
import torch.nn.functional as F

import numpy as np
from scipy.stats import t
from .warn import warn
import logging

from .exceptions import LearningError

logger = logging.getLogger(__name__)


class Checker:
    """A Checker used to halt execution based on corruption statistics.

    Args:
        loss_function: the Torch loss function.
        threshold: the threshold that the base model should outperform the corrupted model by.
        check_prob: The probability on a given batch that a check is performed.
        patience: Number of failed checks in a row required to halt execution.
        initial_patience: Number of checks to wait at the beginning of each epoch before failing.
        warn (bool): If False, raise an error to halt execution immediately, rather than confirming
            with the user.

    Attributes:
        infractions (Dict[str, int]): the number of times in a row that a corruption's belief has
            been violated.
    """

    infractions: Dict[str, int]

    def __init__(
        self,
        loss_function: Callable[[Tensor, Tensor], Tensor],
        threshold=0,
        check_prob: float = 0.05,
        patience: int = 1,
        initial_patience: int = 0,
        warn: bool = True,
    ):
        self.loss_function = loss_function
        self.threshold = threshold
        self.check_prob = check_prob
        self.patience = patience
        self.initial_patience = initial_patience
        self.warn = warn

        # Various corruption statistics
        self.corruption_values = {}
        self.infractions = {}

        # Internal variables
        self._num_checks = 0

    def __call__(
        self,
        network,
        device,
        data,
        target,
        optimizer,
        base_loss: Optional[float] = None,
    ) -> None:
        if np.random.uniform() > self.check_prob:
            return

        self._num_checks += 1
        logger.debug("check {}".format(self._num_checks))

        network = network.to(device)

        if base_loss is None:
            # Get the base loss to compare against.
            # optimizer.zero_grad()
            data = data.to(device)
            output = network(data)
            base_loss = self.loss_function(output, target.to(device))
            # base_loss.backward()

        for corruption in network.corruptions():
            output = network(data)
            loss = self.loss_function(output, target.to(device))

            # If the corruption made the module worse, then this value should be positive.
            corruption_difference = float(loss - base_loss)

            print(
                "Check {}: {}: base loss: {:.05f}, corrupted loss: {:.05f}, "
                "difference: {:.05f}".format(
                    self._num_checks, corruption, base_loss, loss, corruption_difference
                )
            )

            # Defines the "belief" that all corruption values should be less than 0.
            self.infractions.setdefault(corruption, 0)
            if corruption_difference <= self.threshold or np.isnan(
                corruption_difference
            ):
                self.infractions[corruption] += 1
            else:
                # Reset the number of infractions.
                self.infractions[corruption] = 0

            if self._num_checks < self.initial_patience:
                continue

            if self.infractions[corruption] >= self.patience:
                if not self.warn:
                    raise LearningError(corruption)
                warn(corruption, message="")

    def step(self):
        """Step the checker at the end of the epoch.

        This allows for statistics to be reset.
        """
        self._num_checks = 0
        for c in self.corruption_values:
            self.corruption_values[c] = None


class Stats(object):
    def __init__(self):
        self.clean_grads = []
        self.noise_grads = []
        self.p = []


class GradientChecker(object):
    def __init__(self, significance=0.05, alpha=0.25, beta=0.5):
        self.significance = significance
        self.alpha = alpha
        self.beta = beta
        self.stats_logs = []

        self.stats = Stats()

    def __call__(
        self, network, data, current_iter, loss_function=F.cross_entropy, loss_val=None
    ):
        network.zero_grad()
        images, targets = data
        outputs = network(images)
        loss = loss_function(outputs, targets)
        loss.backward()

        clean_avg, clean_std, clean_raw = self._inspect_gradients(network)
        network.zero_grad()

        idx = torch.randperm(len(targets))
        outputs = network(images)
        loss = loss_function(outputs, targets[idx])
        loss.backward()

        noise_avg, noise_std, noise_raw = self._inspect_gradients(network)
        network.zero_grad()  # Just a precaution
        tstat, df, cv, p = self._ttest(
            clean_avg, noise_avg, clean_std, noise_std, len(targets)
        )
        self.stats.clean_grads.append(clean_avg)
        self.stats.noise_grads.append(noise_avg)
        self.stats.p.append(p)

        self._check_pvals(current_iter, loss_val)

    def _inspect_gradients(self, network):
        ave_grads = []
        std_grads = []
        raw_grads = []
        layers = []
        for n, p in network.named_parameters():
            if p.requires_grad and "bias" not in n:
                layers.append(n)
                grad = p.grad
                ave_grads.append(grad.mean())
                std_grads.append(grad.std())
                raw_grads.append(grad.flatten())
        return (
            torch.tensor(ave_grads).squeeze(),
            torch.tensor(std_grads).squeeze(),
            raw_grads,
        )

    def _ttest(self, mu1, mu2, sigma1, sigma2, n):
        std_err1 = sigma1 / np.sqrt(n)
        std_err2 = sigma2 / np.sqrt(n)

        std_err = np.sqrt(std_err1 ** 2.0 + std_err2 ** 2.0)
        t_statistic = (mu1 - mu2) / std_err
        deg_freedom = 2 * n - 2
        critical_value = t.ppf(1.0 - self.significance, deg_freedom)
        p_value = (1.0 - t.cdf(abs(t_statistic), deg_freedom)) * 2.0

        return t_statistic, deg_freedom, critical_value, p_value

    def _check_pvals(self, current_iter, loss_val):
        pvals = np.vstack(self.stats.p)
        layer_rejection_rate = (pvals > self.significance).astype(int).mean(0)
        total_rejection_rate = (layer_rejection_rate > self.alpha).mean()
        if total_rejection_rate > self.beta:
            logger.debug(
                f"Null hypothesis is not rejected in {total_rejection_rate:.3f}% layers"
            )
            self.stats_logs.append(f"{current_iter},{total_rejection_rate},{loss_val}")

    def write_logs(self, log_file, iteration, acc=None, loss=None):
        if acc is not None:
            self.stats_logs.append(f"{iteration},,{loss},{acc}")
        with open(log_file, "w") as f:
            f.write("\n".join(self.stats_logs))

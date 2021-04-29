import torch
from typing import Tuple
import numpy as np
from scipy.stats import t


def inspect_gradients(named_parameters):
    ave_grads = []
    std_grads = []
    raw_grads = []
    layers = []
    for n, p in named_parameters:
        if p.requires_grad and "bias" not in n:
            layers.append(n)
            grad = p.grad  # .abs()
            ave_grads.append(grad.mean())
            std_grads.append(grad.std())
            raw_grads.append(grad.flatten())
    return torch.tensor(ave_grads).squeeze(), torch.tensor(std_grads).squeeze(), raw_grads


def ttest(mu1, mu2, sigma1, sigma2, n, alpha=0.05):
    std_err1 = sigma1 / np.sqrt(n)
    std_err2 = sigma2 / np.sqrt(n)

    std_err = np.sqrt(std_err1 ** 2.0 + std_err2 ** 2.0)
    t_statistic = (mu1 - mu2) / std_err
    deg_freedom = 2 * n - 2
    critical_value = t.ppf(1.0 - alpha, deg_freedom)
    p_value = (1.0 - t.cdf(abs(t_statistic), deg_freedom)) * 2.0

    return t_statistic, deg_freedom, critical_value, p_value


class RunningMeanStd(object):
    def __init__(self, epsilon: float = 1e-4, shape: Tuple[int, ...] = ()):
        """
        Calulates the running mean and std of a data stream
        https://en.wikipedia.org/wiki/Algorithms_for_calculating_variance#Parallel_algorithm
        :param epsilon: helps with arithmetic issues
        :param shape: the shape of the data stream's output
        """
        self.mean = torch.zeros(shape, dtype=torch.float)
        self.var = torch.ones(shape, dtype=torch.float)
        self.epsilon = epsilon
        self.count = 0

    def update(self, arr: torch.tensor) -> None:
        batch_mean = torch.mean(arr, dim=0)
        batch_var = torch.var(arr, dim=0)
        batch_count = arr.shape[0]
        self.update_from_moments(batch_mean, batch_var, batch_count)

    def update_from_moments(self, batch_mean: torch.tensor, batch_var: torch.tensor, batch_count: int) -> None:
        delta = batch_mean - self.mean
        tot_count = self.count + batch_count

        new_mean = self.mean + delta * batch_count / tot_count
        m_a = self.var * self.count
        m_b = batch_var * batch_count
        m_2 = m_a + m_b + torch.square(delta) * self.count * batch_count / (self.count + batch_count)
        new_var = m_2 / (self.count + batch_count)

        new_count = batch_count + self.count

        self.mean = new_mean
        self.var = new_var
        self.count = new_count

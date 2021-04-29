import torch
import abc
from collections import defaultdict


class Predicate(object):
    @abc.abstractmethod
    def check(self, x):
        """ Returns True/False according to the predicate evaluation """
        pass


class Bounds(Predicate):
    """ Checks whether a given tensor (e.g. grad/activation) is within a set of bounds """
    def __init__(self, lower=None, upper=None):
        self.lower = lower
        self.upper = upper

    def check(self, x):
        lower_check = torch.ones_like(x).bool()
        if self.lower is not None:
            lower_check = (x > self.lower).bool()

        upper_check = torch.ones_like(x).bool()
        if self.upper is not None:
            upper_check = (x < self.upper).bool()

        return torch.all(lower_check & upper_check)


class GradientDelta(Predicate):
    """
    Checks whether a given gradient is changing at too fast of a rate.
    Allows for considering vanishing/exploding gradients
    """
    def __init__(self, thresh=1e3):
        self.mean = None
        self.var = None
        self.count = 0
        self.thresh = thresh

    def _update(self, x):
        """
        Calulates the running mean and std of a data stream
        https://en.wikipedia.org/wiki/Algorithms_for_calculating_variance#Parallel_algorithm
        """
        bs, *dims = x.shape
        batch_mean = x.view(bs, -1).mean(-1).mean()
        batch_var = x.view(bs, -1).var(-1).mean()

        if self.mean is None:
            self.mean = batch_mean
        if self.var is None:
            self.var = batch_var

        delta = batch_mean - self.mean
        tot_count = self.count + bs

        new_mean = self.mean + delta * bs / tot_count
        m_a = self.var * self.count
        m_b = batch_var * bs
        m_2 = m_a + m_b + torch.square(delta) * self.count * bs / (self.count + bs)
        new_var = m_2 / (self.count + bs)

        self.mean = new_mean
        self.var = new_var
        self.count += bs

    def check(self, x):
        bs, *dims = x.shape
        batch_mean = x.view(bs, -1).mean(-1).mean()
        batch_var = x.view(bs, -1).var(-1).mean()

        delta = batch_mean.abs() - self.mean.abs()
        var_ratio = batch_var / self.var

        self._update(x)

        # If gradients are trending up/down too quickly, return False
        if delta.abs() > self.thresh:
            return False

        return True


class PredicateChecker(object):
    def __init__(self, predicate, burn_in=30, batch_freq=10):
        self.predicate = predicate
        self.burn_in = burn_in  # Number of batches required before statistics can be trusted
        self.batch_freq = batch_freq

        self.layers = None
        self.predicate_results = defaultdict(list)
        self.eval_bias = defaultdict(list)
        self.sample_mean = dict()
        self.sample_std = dict()

    def check_predicates(self, named_params):
        """
        This is computed per evaluation of the loss function (e.g., per batch)
        """
        layers = []
        for n, p in named_params:
            if p.requires_grad and "bias" not in n:
                layers.append(n)
                grad = p.grad
                self.predicate_results[n].append(self.predicate(grad))

        if self.layers is None:
            self.layers = layers

    def _compute_evaluation_bias(self):
        """
        This is computed *per batch* as the fraction of true evaluations of the predicate over the total evaluations
        of the predicate.
        """
        for name, result in self.predicate_results.items():
            result = torch.tensor(result).int()
            n_total = result.sum()
            n_true = (result > 0).sum()
            eval_bias = float(n_true) / n_total
            self.eval_bias[name].append(eval_bias)

    def compute_test_statistics(self):
        """
        This is the sample mean/variance of the predicate evaluation biases (over n batches)
        """
        Y = {}
        for layer, bias in self.eval_bias.items():
            self.sample_mean[layer] = torch.tensor(bias).mean()
            self.sample_std[layer] = torch.tensor(bias).std()

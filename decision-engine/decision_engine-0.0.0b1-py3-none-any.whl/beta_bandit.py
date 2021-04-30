import logging

import numpy as np
from numpy.core import argmax
from scipy.stats import beta


logger = logging.getLogger(__name__)


# In case of multiple bandit classes, define base class.
# class BanditBase:
#     pass

# In case of Upper Confidence bound:
# * check out https://www.analyticsvidhya.com/blog/2018/09/reinforcement-multi-armed-bandit-scratch-python/
# * Though bailed on that because it is deterministic on the next lever to pull
#   to balance exploitation/exploration, so fails with the Batch interface.

# A good resource:
# https://github.com/WhatIThinkAbout/BabyRobot/blob/master/Multi_Armed_Bandits/Part%205%20-%20Thompson%20Sampling.ipynb
# See that page for some good graphs and overlapping code, and a gaussian
# version of this BetaBandit


class BetaBandit:
    """
    Init patterns:
    * BetaBandit() -> gives bare model with default prior
    * BetaMandit(prior_a=
    ...

    Designed to be either
    * loaded from scratch just given proper counts, as you would do in
      production loading data from a db.
    * iteratively built as you could do when testing on simulated data.

    I had intended to make a root class that is one lever and another class
    that is a set of levers.  Not yet sure if I want to get back to that
    abstraction.  We'll see when it's time to have multiple selections
    implemented.

    # TODO: bring back a notion of learning rate
    """

    # TODO: make the default use case expect numpy array for prios and observs
    def __init__(self, n_levers, observations=None, priors=None):
        """
        Defaults to giving you a beta bandit with (1,1) as the priors.  You can
        also override the priors and/or pass in historical performance data.

        n_levers
            assert int
            is the "k" of this "k-armed bandit"
        observations
            list shaped thing holding the n pos and n neg for all levers:
            [(n_pos_l0, n_neg_l0), (n_pos_l1, ...
            default is None, which is equivalant to all zeros
        priors
            list shaped thing holding the alphas and betas for all priors:
            [(alpha_l0, beta_l0), (alpha_l1, ...
            default is None, which is equivalent to ((1, 1), (1, 1), ...)

        TODO: format above properly for type-hinting and doc generation.
        """
        # TODO: Does alpha tolerate floats?  Could be a nice alternative
        #  interface to give the prior as a ratio and an N instead.

        assert type(n_levers) == int, "n_levers must be an int"
        assert n_levers > 0, "n_levers must be greater than 0"
        self.n_levers = n_levers

        self.alphas = np.zeros(n_levers)
        self.betas = np.zeros(n_levers)

        if priors is None:
            priors = [(1, 1) for i in range(n_levers)]
        self.update(priors)
        self.update(observations)

    def update(self, observations):
        # This is convertible to a np.array conversion, slicing alphas from
        # betas (or n_pos from n_neg), and vector addition.
        if observations is not None:
            for i, this_obs in enumerate(observations):   # TODO: TEST: that both np.array and list-of-lists work here.
                n_pos, n_neg = this_obs
                self.alphas[i] += n_pos
                self.betas[i] += n_neg

    # TODO: these two should certainly collapse into doing numpy-native matrix math rather than manually looping
    def sample_one(self):
        xs = []
        for a, b in zip(self.alphas, self.betas):
            xs.append(beta.rvs(a, b, size=1)[0])
        this_choice = argmax(xs)
        logger.debug("a,b,[x_0,x_1,...], this_choice:", a, b, xs, this_choice)
        return this_choice

    def sample(self, n):  # TODO: reconsider naming here.  "choose action"?
        # Certainly theoretically faster to pull all `beta.rvs`s of the proper
        # size and solve for the winner as vector math, but code wise this is
        # easier at the moment
        choices = []
        for i in range(n):
            choices.append(self.sample_one())
        return choices

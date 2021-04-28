import pickle
from collections import OrderedDict

from .searcher import BaseSearcher
from ..utils import try_import_mxnet

__all__ = ['RLSearcher']


class RLSearcher(BaseSearcher):
    """Reinforcement Learning Searcher for ConfigSpace

    Parameters
    ----------
    kwspaces : keyword search spaces
        The keyword spaces automatically generated by :func:`autogluon.args`

    Examples
    --------
    >>> import autogluon.core as ag
    >>> @ag.args(
    ...     lr=ag.space.Real(1e-3, 1e-2, log=True),
    ...     wd=ag.space.Real(1e-3, 1e-2))
    >>> def train_fn(args, reporter):
    ...     pass
    >>> searcher = RLSearcher(train_fn.kwspaces)
    >>> searcher.get_config()
    """
    def __init__(self, kwspaces, ctx=None, controller_type='lstm',
                 **kwargs):
        try_import_mxnet()
        import mxnet as mx
        # We assume that if MXNet is installed, we also have autogluon.mxnet
        from autogluon.mxnet.scheduler.rl_scheduler import LSTMController, \
            AlphaController, AttenController

        super().__init__(
            configspace=None, reward_attribute=kwargs.get('reward_attribute'))
        if ctx is None:
            ctx = mx.cpu()
        self._best_state_path = None
        if controller_type == 'lstm':
            self.controller = LSTMController(kwspaces, ctx=ctx, **kwargs)
        elif controller_type == 'alpha':
            self.controller = AlphaController(kwspaces, ctx=ctx, **kwargs)
        elif controller_type == 'atten':
            self.controller = AttenController(kwspaces, ctx=ctx, **kwargs)
        else:
            raise NotImplementedError
        self.controller.initialize(ctx=ctx)
        for _ in range(self.controller._nprefetch):
            self.controller._prefetch()

    def __repr__(self):
        reprstr = self.__class__.__name__ + '(' +  \
            'Number of Trials: {}.'.format(len(self._results)) + \
            'Best Config: {}'.format(self.get_best_config()) + \
            'Best Reward: {}'.format(self.get_best_reward()) + \
            ')'
        return reprstr

    def get_config(self, **kwargs):
        return self.controller.sample()[0]

    def state_dict(self, destination=None):
        if destination is None:
            destination = OrderedDict()
            destination._metadata = OrderedDict()
        destination['results'] = pickle.dumps(self._results)
        destination['controller_params'] = pickle.dumps(self.controller.collect_params())
        return destination

    def load_state_dict(self, state_dict):
        try_import_mxnet()
        from autogluon.mxnet.utils import update_params
        self._results=pickle.loads(state_dict['results'])
        update_params(self.controller, pickle.loads(state_dict['controller_params']))

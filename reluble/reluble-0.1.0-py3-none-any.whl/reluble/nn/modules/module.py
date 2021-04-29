"""Module with checkers."""

from __future__ import annotations

from typing import Union, Tuple, Any, Callable, List, Iterator, Optional

import logging
import torch
from torch import nn
import torch.nn.functional as F

from ...warn import warn
from ...utils.printing import summarize
import numpy as np


logger = logging.getLogger(__name__)


class Module(nn.Module):
    """A corruptible version of the PyTorch module.

    Sub-classes should add corruptions by creating methods that end with `corruption`, e.g.
    `identity_corruption` on activation layers.

    When a module is corrupted, it uses one of these methods instead of `forward()`, either at
    random or by passing the name of the method to :func:`~reluble.nn.Module.corrupt`. Children of a
    module can be corrupted by name as well (see :func:`~reluble.nn.Module.corrupt`).

    """

    corruption: Optional[str]

    def __init__(self):
        super(Module, self).__init__()
        self.corruption = None
        self._forward = self.forward
        self._corruptions = set(
            attr
            for attr in dir(self)
            if attr != "corruption"
            and not attr.startswith("_")
            and attr.endswith("corruption")
            and callable(getattr(self, attr, None))
        )

    @property
    def corrupted(self) -> bool:
        return self.corruption is not None

    def corruptions(self) -> Iterator[Module]:
        """Corrupt the module so that it produces worse output (in theory).

        This function iterates over self._corruptions then over `module._corruptions`
        for each module in `self.children()`.

        Yields:
            str: the name of the corruption. For children, this is prefixed by the child
                module's name and `.`.

        """
        for corruption in self._corruptions:
            self.corrupt(corruption)
            yield corruption
            self.restore()

        for name, module in self.named_modules():
            if module is self:
                continue

            for corruption in module.corruptions():
                yield f"{name}.{corruption}"

    def corruption_names(self) -> List[str]:
        corruptions = []
        for name, module in self.named_modules():
            corruptions += module._corruptions

        return corruptions

    def corrupt(self, corruption: Optional[str] = None) -> None:
        """Corrupt the module so that it produces worse output.

        """
        if corruption is None:
            corruption = np.random.choice(self._corruptions)

        if "." in corruption:
            module_name, module_corruption = corruption.split(".", 1)
            getattr(self, module_name).corrupt(module_corruption)
        else:
            assert corruption in self._corruptions, f"invalid corruptions: {corruption}"
            self.forward = getattr(self, corruption)
            logger.debug(f"corrupted {self} with {corruption}")

        self.corruption = corruption

    def restore(self) -> None:
        """Restore the module to normal execution."""
        self.forward = self._forward
        self.corruption = None
        logger.debug(f"restored {self} from {self.corruption}")

        for module in self.children():
            module.restore()

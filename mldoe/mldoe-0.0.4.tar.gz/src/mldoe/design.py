# Packages
from math import log2
from src.mldoe.matrix import bmat
from itertools import chain
import oapackage as oa
from typing import List
import numpy as np


class Design:
    """
    Private meta-class for two-level design (TLD) and mixed-level design (MLD) class.

    :param n_runs: Number of experimental runs
    :type n_runs: int
    :param cols: Column numbers of the two-level columns of the design. Must also include the basic factors.
    :type cols: List[int]
    :raises TypeError: n_runs must be an integer
    :raises ValueError: n_runs must be a positive power of 2
    :raises TypeError: cols must be a list of integers
    :raises ValueError: cols can only contain integers between 0 and N (non-included)
    """

    def __init__(self, n_runs: int, cols: List[int]):
        """Constructor method"""
        # Check value for number of runs
        if not isinstance(n_runs, int):
            raise TypeError('Number of runs must be an integer')
        elif n_runs <= 0 or (n_runs & n_runs - 1) != 0:
            raise ValueError('Number of runs must be a positive power of two')
        else:
            self.n_runs = n_runs

        # Check values for column numbers
        if any([not isinstance(i, int) for i in cols]):
            raise TypeError('All column number should integer')
        elif any([(i < 1 or i >= self.n_runs) for i in cols]):
            raise ValueError(
                'All column numbers should be positive integers between 0 and N (non-included)')
        else:
            self.cols = cols

        # Compute additional values
        self.k = len(self.cols)
        """Total number of two-level factors"""
        self.n = int(log2(self.n_runs))
        """Number of basic (independent) factors"""
        self.p = self.k - self.n_runs
        """Number of added factors (created from generators)"""


class TLD(Design):
    __doc__ = Design.__doc__  # + """Class for a regular two-level design. Inherits from the meta-class `Design`."""

    def __init__(self, n_runs: int, cols: List[int]):
        """Constructor method"""
        # Inherit the characteristics from the parent Design class
        super().__init__(n_runs, cols)

    @property
    def array(self):
        """
        Design matrix in (0,1) coding.
        """
        b_mat = bmat(self.n)
        return b_mat[:, [i - 1 for i in self.cols]]

    @property
    def wlp(self):
        """
        Word-length pattern. It is a :math:`1` by :math:`k+1` vector :math:`\mathbf{W}`, where :math:`W_i` is the number
        of words of length :math:`i` among the :math:`2^{p}-1` words of the design.
        """
        return oa.array_link(self.array).GWLP()

    @property
    def resolution(self):
        """
        Minimum length of words in the design. Also defined as the smallest value of :math:`i` for which
        :math:`W_i > 0`.
        """
        for i in self.wlp[1:]:
            if i != 0:
                return i

    def __repr__(self):
        """Representation method"""
        return f'TLD({self.n_runs},{self.cols})'

    def __str__(self):
        """Formatted string print method"""
        return f'Two-level design in {self.n_runs} runs, with {self.k} factors'


class MLD(Design):
    __doc__ = Design.__doc__ + """
    Class for regular mixed-level designs. Inherits from the meta-class `Design`. Mixed-level designs only
    contains four-level factors and two-level factors. Four-level factors are built using three pseudo-factors,
    according to the grouping scheme of Wu [1989]_.

    :param pf_lst: List of the pseudo-factor triplets used for the four-level factors. All triplets should be list of integers of the form a,b,ab.
    :type pf_lst: List[List[int]]
    :raises TypeError: pf_list must contain lists of integers
    :raises ValueError: all pseudo-factors must be between 0 and N
    :raises ValueError: all pseudo-factors must be of the form a, b, ab
    :raises ValueError: pseudo-factors cannot be used as two-level columns
    """

    def __init__(self, n_runs: int, pf_lst: List[List[int]], cols: List[int]):
        """Constructor method"""
        # Inherit the characteristics from the parent Design class
        super().__init__(n_runs, cols)
        # Additional definition for the pseudo-factors
        for pf_set in pf_lst:
            if any([(not isinstance(i, int)) for i in pf_set]):
                raise TypeError('All pseudo-factors must be integers')
            elif pf_set[0] ^ pf_set[1] != pf_set[2]:
                raise ValueError('All pseudo-factor triplets must be of the form a, b, ab')
            elif any([(i in cols) for i in pf_set]):
                raise ValueError('Pseudo-factors cannot be used as two-level columns')
            elif any([(i <= 0 or i >= n_runs) for i in pf_set]):
                raise ValueError('Pseudo-factors must be positive integers between 0 and N (non-included)')
            else:
                self.pf_lst = pf_lst

        # Compute additional variables concerning the four-level factor(s)
        self.m = len(self.pf_lst)
        """Number of four-level factors"""
        self.pf = list(chain(*self.pf_lst))
        """All two-level factors used as pseudo-factors for the four-level factors"""

    @property
    def array(self):
        """
        Design matrix in (0,1) coding with the four-level factor in (0,1,2,3) coding.
        The four-level factors are created according to the grouping scheme of Wu [1989]_:
        """
        # TODO: add the grouping scheme to the documentation

        b_mat = bmat(self.n)
        two_lvl_part = b_mat[:, [i - 1 for i in self.cols]]
        four_lvl_part = np.zeros((self.n_runs, self.m))
        for i, pf_set in enumerate(self.pf_lst):
            four_lvl_part[:, i] = b_mat[:, pf_set[0] - 1] * \
                                  2 + b_mat[:, pf_set[1] - 1]
        return np.concatenate((four_lvl_part, two_lvl_part), axis=1).astype(int)

    @property
    def wlp(self):
        """
        Word-length pattern. It is a :math:`1` by :math:`k+1` vector :math:`\mathbf{W}`, where :math:`W_i` is the number
        of words of length :math:`i` among the :math:`2^{p}-1` words of the design.
        """
        # TODO: add a type-specific word-length pattern definition
        return oa.array_link(self.array.astype(int)).GWLP()

    @property
    def resolution(self):
        """
        Minimum length of words in the design. Also defined as the smallest value of :math:`i` for which
        :math:`W_i > 0`.
        """
        # TODO: implement type-specific resolution for the type-specific wlp
        return next((i for i, x in enumerate(self.wlp[1:]) if x), self.k) + 1

    def generators(self, resolution: int = 3) -> List[int]:
        """
        List the generators of the design that have a minimal resolution of r.

        :param resolution: minimal resolution needed for the generators
        :type resolution: int
        :return: list of suitable generators
        :rtype: List[int]
        """
        generators = []
        for i in range(1, self.n_runs):
            if (i & i - 1) == 0:
                continue
            elif i in self.cols or i in self.pf:
                continue
            elif gen_len(i, self.pf_lst) < resolution - 1:
                continue
            else:
                generators.append(i)
        return generators

    def dop(self):
        """
        Generate the delete-one-factor projections (DOP) (only on two-level designs) of the design.

        :return: generator with all the DOP
        """
        for i in range(self.k):
            new_cols = self.cols.copy()
            new_cols.pop(i)
            yield MLD(self.n_runs, self.pf_lst, new_cols)


# Additional functions
def pow2(x: int) -> List[int]:
    """
    Decompose a number into powers of 2
    :param x: number to decompose
    :type x: int
    :return: list of powers of 2 that compose the number
    :rtype: List[int]
    """
    powers = []
    i = 1
    while i <= x:
        if i & x:
            powers.append(i)
        i <<= 1
    return powers


def gen_len(gen: int, pf_lst: List[List[int]]) -> int:
    """
    Determine the length of a generator, according to the pseudo-factors used in the mixed-level design.

    :param gen: generator as a column number
    :type gen: int
    :param pf_lst: list of the pseudo-factor triplets
    :type pf_lst: List[List[int]]
    :return: adapted length of the generator
    """
    gen_bf = pow2(gen)
    gen_len_temp = len(gen_bf)
    for pf in pf_lst:
        pf_bf = np.unique(list(chain(*[pow2(i) for i in pf])))
        in_gen = False
        for i in pf_bf:
            if i in gen_bf:
                gen_len_temp -= 1
                in_gen = True
        if in_gen:
            gen_len_temp += 1
    return gen_len_temp


def gen_char(x: int) -> str:
    """
    Character representation of a generator.
    The generator is represented as a word containing the basic factors used (starting at a).

    :param x: generator number.
    :type x: int
    :rtype: str
    :return: generator string representation
    """
    pow_lst = pow2(x)
    return ''.join([chr(97 + int(log2(i))) for i in pow_lst])

"""
Simulations of Physically Unclonable Functions (PUFs).
"""
from typing import Optional, List
from typing import Union, Callable

from numpy import prod, sign, sqrt, append, empty, ceil, \
    ones, zeros, reshape, einsum, int8, \
    concatenate, ndarray, transpose, broadcast_to, array
from numpy.random import default_rng


class Simulation:
    """
    A PUF simulation that can be evaluated on challenges.
    """

    @property
    def challenge_length(self) -> int:
        """ The expected challenge length of this simulation, ``int``. """
        raise NotImplementedError()

    @property
    def response_length(self) -> int:
        """ The length of responses generated by this simulation, ``int``. """
        raise NotImplementedError()

    def eval(self, challenges: ndarray) -> ndarray:
        """
        Evaluate the PUF on a list of given challenges.

        :param challenges: List of challenges to evaluate on. Challenges must be given as ``ndarray`` of shape
            (:math:`N`, ``challenge_length``), where :math:`N` is the number of challenges to be evaluated.
            Evaluating many challenges at once may have performance benefits, to evaluate a single challenge, provide
            an ``ndarray`` with shape (1, ``challenge_length``). In cases where ``challenge_length`` = 0, an
            empty array with shape (:math:`N`, 0) needs to be provided to determine the number of responses requested.
        :return: ``ndarray``, shape (:math:`N`, ``response_length``), listing the simulated responses to the
            challenges in order they were given.
        """
        raise NotImplementedError()

    def r_eval(self, r: int, challenges: ndarray) -> ndarray:
        """
        Evaluates the Simulation ``r`` times on the list of :math:`N` ``challenges`` given and returns an array
        of shape (``r``, :math:`N`, ``self.response_length``) of all responses.

        >>> from pypuf.simulation import XORArbiterPUF
        >>> from pypuf.io import random_inputs
        >>> puf = XORArbiterPUF(n=64, k=4, noisiness=.02, seed=1)
        >>> responses = puf.r_eval(5, random_inputs(N=2, n=64, seed=2))
        >>> responses[0, :, :]  # unstable example
        array([[ 1.,  1., -1.,  1.,  1.]])
        >>> responses[1, :, :]  # stable example
        array([[-1., -1., -1., -1., -1.]])

        .. note::
            To approximate the expected respones value, use average along the last axis:

            >>> from numpy import average
            >>> average(responses, axis=-1)
            array([[ 0.6],
                   [-1. ]])
        """
        N = challenges.shape[0]
        responses = empty(shape=(N, self.response_length, r))
        for i in range(r):
            responses[:, :, i] = self.eval(challenges).reshape(N, self.response_length)
        return responses

    @staticmethod
    def seed(description: str) -> int:
        """
        Helper function that turns a string into an integer that can be consumed as seed by a pseudo-random number
        generator (PRNG). Usage scenario: create a descriptive seed and use it to initialize the PRNG.

        >>> from numpy.random import default_rng
        >>> from pypuf.simulation import Simulation
        >>> seed = 'parameter seed for my PUF instance'
        >>> prng = default_rng(seed=Simulation.seed(seed))
        >>> parameters = prng.normal(size=(3, 4))
        >>> parameters
        array([[ 1.64917478, -1.28702893,  0.17287684, -1.69475886],
               [-1.74432269,  1.59592227,  1.12435243, -0.23488442],
               [-0.74190059,  0.95516568, -2.25170753, -0.22208081]])

        """
        return int.from_bytes(description.encode(), byteorder='big')


class LTFArray(Simulation):
    r"""
    Highly optimized, numpy-based implementation that can batch-evaluate functions as found in the
    Additive Delay Model of Arbiter PUFs, i.e. functions :math:`f` of the form

    .. math::
        f: \{-1,1\}^n \to \{-1,1\}, f(c) &= \text{sgn } \hat{f}(c), \\
        \hat{f}: \{-1,1\}^n \to \mathbb{R}, \hat{f}(x) &= \prod_{l=1}^k (b_l + \sum_{i=1}^n W_{l,i} \cdot x_i ),

    where :math:`n, k` are natural numbers (positive ``int``) specifying the size of the `LTFArray`,
    :math:`W \in \mathbb{R}^{k \times n}` are the `weights` of the linear threshold functions, and
    :math:`b_i, i \in [k]` are the biases of the LTFs.

    For performance reasons, the evaluation interface of ``LTFArray`` is specialized for evaluating a list of challenges
    with each call, returning a list of responses of same length; this length will often be referred to as :math:`N`.

    .. todo:: Detail on weight distribution.

    Two generalizations of :math:`f` are supported. First, modifying the challenge input has been extensively
    studied in the literature [Lightweight Secure PUF, Permutation PUF]. In ``LTFArray``, this is implemented as `input
    transformation`. Second, using a function different from XOR to combine the individual results into a final result,
    which is less studied and is known to ``LTFArray`` as `combiner function` (in reference to LFSRs). We detail on
    both below.

    **Input Transformations.**
    An input transformation can be understood as a list of functions :math:`\lambda_1,...,\lambda_k`, where
    :math:`\lambda_i:\{-1,1\}^n \to \{-1,1\}^n` generates the input for the :math:`i`-th LTF in the ``LTFArray``.
    In order to use input transformations with ``LTFArray``, implement a Python function that maps a list of challenges
    ``challenges`` given as ``ndarray`` of shape :math:`(N, n)` and the number of LTFs given as a positive ``int`` ``k``
    to a
    list of list of sub-challenges to the individual LTFs (``sub_challenges``), returned as ``ndarray`` of shape
    :math:`(N, k, n)`, where for all :math:`i \in [N]` and :math:`l \in [k]`

    .. math::
        \mathtt{sub\_challenges}_{i, l} = \lambda_l(\mathtt{challenges}_i).

    Given such a function, ``LTFArray`` will evaluate

    .. math::
        f: \{-1,1\}^n \to \{-1,1\}, f(c) &= \text{sgn } \hat{f}(c), \\
        \hat{f}: \{-1,1\}^n \to \mathbb{R}, \hat{f}(x) &= \prod_{l=1}^k (b_l + \langle W_l, \lambda_l(x) \rangle ).

    .. warning::
        In above definition, the :math:`\lambda_i` are different from preprocessing functions implemented in hardware.
        This is due to the nature of the Arbiter PUF Additive Delay Model: in order to accurately model the behavior of
        an Arbiter PUF without additional challenge processing on a given hardware input :math:`c \in \{-1,1\}^n`, the
        Arbiter PUF needs ot be modeled as function

        .. math:: f(c) = \text{sgn } \prod_{l=1}^k b_l + \sum_{i=1}^n W_{l,i} \cdot c_i c_{i+1} \cdots c_n,

        i.e. :math:`\lambda_1 = \cdots = \lambda_k` with :math:`\lambda_1(c)_i = c_i c_{i+1} \cdots c_n`. This
        function is implemented in ``LTFArray`` as ``att``; its inverse is ``att_inverse``.

    **Combiner Function.**
    The combiner function replaces the product of linear thresholds in the definition of :math:`\hat f`. Setting
    the `combiner` parameter to a `Callable` `my_combiner` taking a shape :math:`(N, k)` array of `sub-responses` and
    returning an array of shape :math:`(N,)`, will compute the function

    .. math:: f(c) = \text{sgn } \mathtt{my\_combiner}
        \left( b_l + \sum_{i=1}^n W_{l,i} \cdot c_i c_{i+1} \cdots c_n \right).

    To instanciate an ``LTFArray``, provide the following parameters:

    :param weight_array: `weights` of the LTFs in this array, `ndarray` of floats with shape :math:`(k, n)`
    :param transform: `input transformation` as described above, given as callable function or string `s` identifying
        a member function of this class with name `s` or `f'transform_{s}'`.
    :param combiner: optional `combiner function` as described above, given as callable function or string `s` identifying
        a member function of this class with name `s` or `f'combiner_{s}'`, defaults to `xor`, i.e. the partity
        function.
    :param bias: optional `ndarray` of floats with shape :math:`(k,)`, specifying the bias values :math:`b_l` for
        :math:`l \in [k]`, defaults to zero bias.

    To create an ``LTFArray`` containing just one function, the majority vote function of four inputs, use

    >>> from pypuf.simulation import LTFArray
    >>> from numpy import array, ones
    >>> my_puf = LTFArray(ones(shape=(1, 4)), transform='id')
    >>> my_puf.eval(array([[1, 1, -1, 1]]))
    array([1])
    >>> my_puf.eval(array([[1, -1, -1, -1]]))
    array([-1])
    """

    _BIT_TYPE = int8

    @classmethod
    def combiner_xor(cls, responses: ndarray) -> ndarray:
        return prod(responses, axis=1)

    @classmethod
    def transform_id(cls, challenges: ndarray, k: int) -> ndarray:
        """
        Broadcast original challenge input to all LTFs without modification.
        This does not allocate additional memory for challenges.
        """
        (N, n) = challenges.shape
        return transpose(broadcast_to(challenges, (k, N, n)), axes=(1, 0, 2))

    @classmethod
    def generate_stacked_transform(cls, transform_1: Callable, k1: int, transform_2: Callable) -> Callable:
        """
        Combines input transformations ``transform_1`` and ``transform_2`` into a `stacked` input transformation,
        where the first ``k1`` sub-challenges are obtained by using ``transform_1`` on the challenge, and the remaining
        ``k - k1`` are sub-challenges are generated using ``transform_2``.
        """

        def transform(challenges: ndarray, k: int) -> ndarray:
            """Generates sub-challenges by applying by applying different input transformations depending on the index
            of the sub-challenge."""
            (N, n) = challenges.shape
            transformed_1 = transform_1(challenges, k1)
            transformed_2 = transform_2(challenges, k - k1)
            assert transformed_1.shape == (N, k1, n)
            assert transformed_2.shape == (N, k - k1, n)
            return concatenate(
                (
                    transformed_1,
                    transformed_2,
                ),
                axis=1
            )

        transform.__name__ = f'transform_stack_{k1}_{transform_1.__name__.replace("transform_", "")}_' \
                             f'{transform_2.__name__.replace("transform_", "")}'

        return transform

    @classmethod
    def generate_concatenated_transform(cls, transform_1: Callable, n1: int, transform_2: Callable) -> Callable:
        """
        Combines input transformations ``transform_1`` and ``transform_2`` into a `concatenated` input transformation,
        where the first ``n1`` bit of each sub-challenges are obtained by using ``transform_1`` on the first ``n1`` bit
        of the challenge, and the remaining ``n - n1`` bit of each sub-challenge are generated using ``transform_2``
        on the remaining ``n - n1`` bit of each given challenge.
        """

        def transform(challenges: ndarray, k: int) -> ndarray:
            """Generates sub-challenges by applying by applying different input transformations depending on the index
            of the sub-challenge bit."""
            (N, n) = challenges.shape
            challenges1 = challenges[:, :n1]
            challenges2 = challenges[:, n1:]
            transformed_1 = transform_1(challenges1, k)
            transformed_2 = transform_2(challenges2, k)
            assert transformed_1.shape == (N, k, n1)
            assert transformed_2.shape == (N, k, n - n1)
            return concatenate(
                (
                    transformed_1,
                    transformed_2
                ),
                axis=2
            )

        transform.__name__ = f'transform_concat_{n1}_{transform_1.__name__.replace("transform_", "")}_' \
                             f'{transform_2.__name__.replace("transform_", "")}'

        return transform

    @classmethod
    def att(cls, sub_challenges: ndarray) -> None:
        r"""
        Performs the "Arbiter Threshold Transform" (``att``) on an array of sub-challenges of shape
        :math:`(N, k, n)`.
        ``att`` is defined to modify any given sub-challenge :math:`c` as follows:
        Let :math:`c \in \{-1,1\}^n`, then the :math:`i`-th output bit of :math:`\mathtt{att}(c)` equals
        :math:`\prod_{j=i}^n c_j`, i.e. the :math:`i`-th output bit is the product of the :math:`i`-th input bit
        and all following input bits.

        This operation is performed in place, i.e. the input will be overwritten.
        This method returns None.
        """
        (_, _, n) = sub_challenges.shape
        for i in range(n - 2, -1, -1):
            sub_challenges[:, :, i] *= sub_challenges[:, :, i + 1]

    @classmethod
    def att_inverse(cls, sub_challenges: ndarray) -> None:
        r"""
        Performs the **inverse** "Arbiter Threshold Transform" (``inverse_att``) on an array of sub-challenges of shape
        :math:`(N, k, n)`.
        The inverse ATT is defined to modify any given sub-challenge :math:`x` as follows:
        Let :math:`x \in \{-1,1\}^n`, then the :math:`i`-th output bit of :math:`\mathtt{att\_inverse}(x)` equals
        :math:`x_i / x_{i+1}`, where :math:`x_{n+1}` is treated as 1. I.e. the :math:`i`-th output bit is the division
        of the :math:`i`-th input bit and the following input bit.

        This operation is performed in place, i.e. the input will be overwritten.
        This method returns None.
        """
        (_, _, n) = sub_challenges.shape
        for i in range(n - 1):
            sub_challenges[:, :, i] *= sub_challenges[:, :, i + 1]

    @classmethod
    def normal_weights(cls, n: int, k: int, seed: int, mu: float = 0, sigma: float = 1) -> ndarray:
        """
        Returns weights for an array of k LTFs of size n each.
        The weights are drawn from a normal distribution with given
        mean and std. deviation, if parameters are omitted, the
        standard normal distribution is used.
        """
        return default_rng(seed).normal(loc=mu, scale=sigma, size=(k, n))

    def __init__(self, weight_array: ndarray, transform: Union[str, Callable], combiner: Union[str, Callable] = 'xor',
                 bias: ndarray = None) -> None:

        self.weight_array = weight_array

        if isinstance(transform, str):
            if not transform.startswith('transform_'):
                transform = 'transform_' + transform
            self.transform = getattr(self, transform)
        else:
            self.transform = transform

        if isinstance(combiner, str):
            if not combiner.startswith('combiner_'):
                combiner = 'combiner_' + combiner
            self.combiner = getattr(self, combiner)
        else:
            self.combiner = combiner

        # If necessary, convert bias definition
        if bias is None:
            self.bias = zeros(shape=(self.k, 1))
        elif isinstance(bias, float):
            self.bias = bias * ones(shape=(self.k, 1))
        elif isinstance(bias, ndarray) or isinstance(bias, list) and array(bias).shape == (self.k, ):
            self.bias = reshape(array(bias), (self.k, 1))
        else:
            self.bias = bias if isinstance(bias, ndarray) else array(bias)

        # Append bias values to weight array
        assert self.bias.shape == (self.k, 1),\
            'Expected bias to either have shape ({}, 1) or be a float, ' \
            'but got an array with shape {} and value {}.'.format(self.k, self.bias.shape, self.bias)
        self.weight_array = append(self.weight_array, self.bias, axis=1)

    @property
    def challenge_length(self) -> int:
        return self.weight_array.shape[1] - 1

    @property
    def response_length(self) -> int:
        return 1

    @property
    def ltf_count(self) -> int:
        """Number of LTFs in this ``LTFArray``."""
        return self.weight_array.shape[0]

    n = challenge_length
    k = ltf_count

    @property
    def biased(self) -> bool:
        """Indicates whether any LTF in this LTFArray is biased."""
        return (self.weight_array[:, -1] != 0).any()

    def eval(self, challenges: ndarray, block_size: Optional[int] = 10**6) -> ndarray:
        N = challenges.shape[0]
        block_size = block_size or N
        responses = empty(shape=(N,), dtype=challenges.dtype)
        for idx in range(int(ceil(N / block_size))):
            block = slice(idx * block_size, (idx + 1) * block_size)
            responses[block] = self.eval_block(challenges[block])
        return responses

    def eval_block(self, challenges: ndarray) -> ndarray:
        return sign(self.val(challenges))

    def val(self, challenges: ndarray) -> ndarray:
        """
        Evaluates a given array of (master) challenges and returns the precise value of the combined LTFs responses.
        That is, the master challenges are first transformed into sub-challenges, using this LTFArray's transformation
        method. The challenges are then evaluated using ltf_eval. The responses are then combined using this LTFArray's
        combiner.
        :param challenges: array of shape(N,n)
                       Array of challenges which should be evaluated by the simulation.
        :return: array of float or int depending on the combiner of shape (N,)
                 Array of responses for the N different challenges.
        """
        return self.combiner(self.ltf_eval(self.transform(challenges, self.weight_array.shape[0])))

    @classmethod
    def efba_bit(cls, sub_challenges: ndarray) -> ndarray:
        """
        Given an array of sub-challenges of shape :math:`(N, k, n)`, returns an array of sub-challenges `extended
        for bias awareness (efba)` of shape :math:`(N, k, n+1)`, where the last bit of each challenge is :math:`+1`.
        This is useful for seamless evaluation of LTF values when the bias value is at the :math:`(n+1)`-th position
        in the weights (as is the case for `LTFArray.weight_array`).

        .. warning::
            The current implementation of this function creates a copy of the challenge array in order to concatenate
            the :math:`+1` bits, which doubles memory consumption.

        :param sub_challenges: array of sub-challenges of shape :math:`(N,k,n)`
        :return: array of efba sub-challenges, shape :math:`(N,k,n+1)`
        """
        return append(sub_challenges, array(1, dtype=cls._BIT_TYPE))  # note this creates a copy :-(

    def ltf_eval(self, sub_challenges: ndarray) -> ndarray:
        r"""
        Given an array of :math:`N` groups of :math:`k` sub-challenges of bit length :math:`n` each, this function
        computes for the :math:`j`-th group of :math:`k`
        sub-challenges the values of the individual LTF evaluation, that is, the :math:`k` real numbers

        .. math::
            \langle W_1&, \mathtt{sub\_challenges}_{j,1} \rangle, \\
            \langle W_2&, \mathtt{sub\_challenges}_{j,2} \rangle, \\
            &\vdots \\
            \langle W_k&, \mathtt{sub\_challenges}_{j,k} \rangle, \\

        :param sub_challenges: array of sub-challenges of shape :math:`(N,k,n)`
        :return: array of individual LTF values as floats, shape :math:`(N,k)`
        """
        k, n = self.weight_array.shape
        n -= 1

        assert sub_challenges.shape[1:] == (k, n),\
            f'Sub-challenges given to ltf_eval had shape {sub_challenges.shape}, but shape (N, k, n) = ' \
            f'(N, {k}, {n}) was expected.'

        unbiased = einsum('ji,...ji->...j', self.weight_array[:, :-1], sub_challenges, optimize=True)
        bias = self.weight_array[:, -1]
        return unbiased + bias


class NoisyLTFArray(LTFArray):
    """
    Class that simulates k LTFs with n bits and a constant term each
    with noise effect and constant bias added.
    """

    @staticmethod
    def sigma_noise_from_random_weights(n: int, sigma_weight: float, noisiness: float = 0.1) -> float:
        """
        returns sd of noise (sigma_noise) out of n stages with
        sd of weight differences (sigma_weight) and noisiness factor
        """
        return sqrt(n) * sigma_weight * noisiness

    def __init__(self, weight_array: ndarray, transform: Union[Callable, str], combiner: Union[Callable, str],
                 sigma_noise: float, seed: int, bias: ndarray = None) -> None:
        """
        Initializes LTF array like in LTFArray and uses the provided
        PRNG instance for drawing noise values. If no PRNG provided, a
        fresh instance is used.
        :param bias: None, float or a two dimensional array of float with shape (k, 1)
                     This bias value or array of bias values will be appended to the weight_array.
                     Use a single value if you want the same bias for all weight_vectors.
        """
        super().__init__(weight_array, transform, combiner, bias)
        self.sigma_noise = sigma_noise
        self.random = default_rng(seed)

    def ltf_eval(self, sub_challenges: ndarray) -> ndarray:
        """
        Calculates weight_array with given set of challenges including noise.
        The noise effect is a normal distributed random variable with mu=0,
        sigma=sigma_noise.
        Random numbers are drawn from the PRNG instance generated when
        initializing the NoisyLTFArray.
        """
        evaled_inputs = super().ltf_eval(sub_challenges)
        noise = self.random.normal(loc=0, scale=self.sigma_noise, size=(len(evaled_inputs), self.k))
        return evaled_inputs + noise


class XORPUF(Simulation):
    """Simulates the XOR of a number of given simulations."""

    def __init__(self, simulations: List[Simulation]) -> None:
        super().__init__()
        self.simulations = simulations

    @property
    def challenge_length(self) -> int:
        return self.simulations[0].challenge_length

    @property
    def response_length(self) -> int:
        return self.simulations[0].response_length

    def val(self, challenges: ndarray) -> ndarray:
        return prod([s.val(challenges) for s in self.simulations], axis=0)

    def eval(self, challenges: ndarray) -> ndarray:
        return prod([s.eval(challenges) for s in self.simulations], axis=0)

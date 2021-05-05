from fractions import Fraction
from math import sqrt, prod, log2, ceil, floor, log
from typing import Tuple, Optional, Iterable, List
from collections import Counter
from rfb_mc.component.eamp.primes import get_pj, get_closest_prime
from rfb_mc.component.eamp.eamp_rfm import EampRfm, EampParams, EampTransformMethod
from rfb_mc.component.eamp.types import EampEdgeInterval
from rfb_mc.component.eamp.utility import multi_majority_vote_iteration_count_to_ensure_beta, \
    majority_vote_error_probability, probability_of_correctness
from rfb_mc.scheduler import SchedulerBase
from rfb_mc.store import StoreBase
from rfb_mc.types import RfBmcTask, RfBmcResult, BmcTask, BmcResult


class EampSEdgeScheduler(SchedulerBase[EampEdgeInterval, EampEdgeInterval, EampRfm]):
    def __init__(
        self,
        store: StoreBase,
        confidence: Fraction,
        a: int,
        q: int,
        min_model_count: Optional[int] = None,
        max_model_count: Optional[int] = None,
    ):
        super().__init__(store, EampRfm)

        assert a >= 1, "a >= 1"
        assert q >= 1, "q >= 1"
        assert 0 <= confidence < 1, "Confidence is < 1 and >= 0"

        self.confidence: Fraction = confidence
        self.a: int = a
        self.q: int = q
        self.max_model_count: int = max_model_count if max_model_count is not None else prod([
            2 ** (bit_width * count) for bit_width, count in self.store.data.params.bit_width_counter.items()
        ])
        self.min_model_count: int = min_model_count if min_model_count is not None else 0

    def _run_algorithm_once(self):
        if self.max_model_count == 0:
            return EampEdgeInterval(interval=(0, 0), confidence=Fraction(1))

        g, lg = self.get_g_and_lg(self.a)

        cn = max(int(floor(log2(log2(self.max_model_count ** self.q / lg) + 1) + 1)), 1)

        beta = 1 - self.confidence

        # maximum amount of values that need to be iterated for c[0]
        max_c0 = 5

        # maximum amount of expected majority vote counting procedures
        max_majority_vote_countings = cn - 1 + max_c0

        # probability that an estimate call returns the less likely result
        alpha = Fraction(1, 4)

        r = multi_majority_vote_iteration_count_to_ensure_beta(
            alpha,
            beta,
            max_majority_vote_countings,
        )

        def make_eamp_params(t: Tuple[Tuple[int, ...], Tuple[int, ...]]):
            return EampParams(
                c=t[1],
                p=t[0],
                transform_method=EampTransformMethod.SORTED_ROLLING_WINDOW,
            )

        def make_rf_bmc_task(eamp_params: EampParams):
            return RfBmcTask(
                rfm_guid=self.rf_module.get_guid(),
                rfm_formula_params=eamp_params,
                a=self.a,
                q=self.q,
            )

        def range_size(t: Tuple[Tuple[int, ...], Tuple[int, ...]]):
            return self.rf_module.get_restrictive_formula_properties(
                self.store.data.params, make_eamp_params(t),
            ).range_size

        def pre_estimate(t: Tuple[Tuple[int, ...], Tuple[int, ...]]) -> Optional[bool]:
            if self.max_model_count ** self.q < range_size(t) * lg:
                return False
            elif self.min_model_count ** self.q > range_size(t) * g:
                return True
            elif t_neg is not None and range_size(t_neg) <= range_size(t):
                return False
            elif t_pos is not None and range_size(t) <= range_size(t_pos):
                return True
            else:
                return None

        t_pos: Optional[Tuple[Tuple[int, ...], Tuple[int, ...]]] = None
        t_neg: Optional[Tuple[Tuple[int, ...], Tuple[int, ...]]] = None

        # error probability of the independent probabilistic execution that have occurred
        error_probabilities: List[Fraction] = []

        min_model_count = self.min_model_count
        max_model_count = self.max_model_count

        def get_edge_interval():
            if t_pos is not None:
                lower_bound = int(floor(max(float(min_model_count), (range_size(t_pos) * g) ** (1 / self.q))))
            else:
                lower_bound = min_model_count

            if t_neg is not None:
                upper_bound = int(ceil(min(float(max_model_count), (range_size(t_neg) * lg) ** (1 / self.q))))
            else:
                upper_bound = max_model_count

            return EampEdgeInterval(
                interval=(lower_bound, upper_bound),
                confidence=probability_of_correctness(error_probabilities),
            )

        def majority_vote_estimate(t: Tuple[Tuple[int, ...], Tuple[int, ...]]):
            while True:
                rf_bmc_task = make_rf_bmc_task(make_eamp_params(t))

                # copies the required results data in order for it not to be modified while using them
                rf_bmc_results: Counter[RfBmcResult] = \
                    self.store.data.rf_bmc_results_map.get(rf_bmc_task, Counter()).copy()

                positive_voters = sum([
                    count
                    for result, count in rf_bmc_results.items()
                    if result.bmc is None
                ])

                negative_voters = sum([
                    count
                    for result, count in rf_bmc_results.items()
                    if result.bmc is not None
                ])

                remaining = max(0, r - (positive_voters + negative_voters))

                if positive_voters >= negative_voters and positive_voters >= negative_voters + remaining:
                    return True, majority_vote_error_probability(alpha, r)

                if negative_voters > positive_voters and negative_voters > positive_voters + remaining:
                    return False, majority_vote_error_probability(alpha, r)

                yield EampSEdgeScheduler.AlgorithmYield(
                    required_tasks=Counter(remaining * [rf_bmc_task]),
                    predicted_required_tasks=Counter(),
                    intermediate_result=get_edge_interval(),
                )

        j = cn - 1
        c: Tuple[int, ...] = tuple([0 for _ in range(cn - 1)]) + (1,)

        def make_t() -> Tuple[Tuple[int, ...], Tuple[int, ...]]:
            if all([c[i] == 0 for i in range(cn) if i != 0]):
                return (2,), (c[0],)

            return (get_closest_prime(prod([
                2**(2**i) for i in range(cn) if c[i] == 1 and i != 0
            ])), 2), (1, c[0])

        while True:
            while pre_estimate(make_t()) is False and j != 0:
                c = c[0:j-1] + (1, 0) + c[j+1:]
                j -= 1

            if pre_estimate(make_t()) is False and j == 0:
                break

            mv_estimate, mv_error_prob = yield from majority_vote_estimate(make_t())
            error_probabilities.append(mv_error_prob)

            if mv_estimate:
                t_pos = make_t()

                if j == 0:
                    c = c[:-1] + (c[0] + 1,)
                else:
                    c = c[0:j] + (1,) + c[j+1:]
                    j -= 1
            else:
                t_neg = make_t()

                if j == 0:
                    break
                else:
                    c = c[0:j-1] + (1, 0) + c[j+1:]
                    j -= 1

        if t_pos is None:
            s = int(ceil(g ** (1 / self.q)))

            bmc_task_result: Optional[Tuple[BmcTask, BmcResult]] = self.store.data.bmc_task_result

            while bmc_task_result is None or bmc_task_result[0].a < s:
                yield EampSEdgeScheduler.AlgorithmYield(
                    required_tasks=Counter([BmcTask(a=s)]),
                    predicted_required_tasks=Counter(),
                    intermediate_result=get_edge_interval(),
                )

                bmc_task_result = self.store.data.bmc_task_result

            if bmc_task_result[1].bmc is not None and bmc_task_result[1].bmc < s:
                return EampEdgeInterval(
                    interval=(bmc_task_result[1].bmc, bmc_task_result[1].bmc),
                    confidence=Fraction(1),
                )
            else:
                min_model_count = max(min_model_count, s)

        return get_edge_interval()

    def _run_algorithm(self):
        yield from self._run_algorithm_once()
        # second iteration ensures updated results are used
        return (yield from self._run_algorithm_once())

    @staticmethod
    def get_g_and_lg(a: int) -> Tuple[float, float]:
        """
        Returns the internal parameters g and G for the given a.
        """

        return (sqrt(a + 1) - 1) ** 2, (sqrt(a + 1) + 1) ** 2

    @staticmethod
    def get_q_for_fixed_a_that_ensures_upper_bound_for_multiplicative_gap_of_result(
        a: int,
        epsilon: float,
    ) -> int:
        """
        Returns the minimal parameter q that ensures that for the given a we have,
        get_upper_bound_for_multiplicative_gap_of_result(a, q) <= (1 + epsilon) ** 2.
        That condition is equivalent to the statement that the geometric mean of the final edge interval
        is a multiplicative approximation with error epsilon i.e.
        model_count / (1 + epsilon) <= geometric_mean <= model_count * (1 + epsilon).
        """

        g, lg = EampSEdgeScheduler.get_g_and_lg(a)
        return int(ceil(0.5 * log(2 * lg / g, 1 + epsilon)))

    @staticmethod
    def get_a_for_fixed_q_that_ensures_upper_bound_for_multiplicative_gap_of_result(
        q: int,
        epsilon: float,
    ) -> int:
        """
        Returns the minimal parameter a that ensures that for the given q we have,
        get_upper_bound_for_multiplicative_gap_of_result(a, q) <= (1 + epsilon) ** 2.
        That condition is equivalent to the statement that the geometric mean of the final edge interval
        is a multiplicative approximation with error epsilon i.e.
        model_count / (1 + epsilon) <= geometric_mean <= model_count * (1 + epsilon).
        """

        if 2 ** (1 / q) >= (1 + epsilon) ** 2:
            raise ValueError(f"For epsilon={epsilon} and q={q} "
                             f"i.e. (1 + epsilon) ** 2 = {(1 + epsilon) ** 2}, higher a "
                             f"values will only be able to converge to {2 ** (1 / q)} thus epsilon "
                             f"{sqrt(2 ** (1 / q)) - 1}")

        # TODO: replace by proper formula
        a = 1
        while EampSEdgeScheduler.get_upper_bound_for_multiplicative_gap_of_result(a, q) > (1 + epsilon) ** 2:
            a += 1

        return a

    @staticmethod
    def get_upper_bound_for_multiplicative_gap_of_result(a: int, q: int) -> float:
        """
        Returns an upper bound on the multiplicative gap of the final edge interval returned
        by the eamp edge scheduler.
        """

        g, lg = EampSEdgeScheduler.get_g_and_lg(a)
        return (2 * lg / g) ** (1 / q)

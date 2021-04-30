import numpy as np

from ortools.linear_solver import pywraplp

from hipar import check

class HiPaRRuleSelector :
    '''
    Parent class for rule selectors
    '''
    def select(self, df_rules):
        pass

## Select all rules
class TrivialHiPaRRuleSelector(HiPaRRuleSelector) :
    def select(self, df_rules) :
        return list(df_rules.index)

class DefaultHiPaRRuleSelector(HiPaRRuleSelector) :

    def __init__(self, overlap_bias=1.0, support_bias=1.0,
                 metric_weights=None, timeout=300000, min_k=1) :
        self.overlap_bias = check._check_overlap_bias(overlap_bias)
        self.support_bias = check._check_support_bias(support_bias)
        self.metric_weights = metric_weights
        self.timeout = timeout
        self.min_k = check._check_min_k(min_k)

    def select(self, df_rules, min_rules=1) :
        return self.ilp_selection(df_rules)

    def _normalize(self, v, order=1) :
        N = np.linalg.norm(v, ord=order)
        return v / N if N > 0 else v

    def _aggregate_scores(self, scores_dict) :
        if self.metric_weights is not None :
            weights = []
            scores = []
            for k, v in scores_dict.items() :
                scores.append(v)
                weights.append(self.metric_weights[k])
            return np.average(scores, weights=weights)
        else :
            return np.average(list(scores_dict.values()))

    def _compute_error_scores(self, rules_df) :
        return rules_df['scores'].apply(self._aggregate_scores).to_numpy()

    def _compute_jaccard_matrix(self, rules_df):
        jaccard_matrix = np.full((len(rules_df.index), len(rules_df.index)), fill_value=-1, dtype=float)

        for i1 in range(len(rules_df.index)):
            for i2 in range(len(rules_df.index)):
                if i1 != i2:
                    intersect_size = np.intersect1d(rules_df['tids'].iloc[i1], rules_df['tids'].iloc[i2]).size
                    j = intersect_size / (len(rules_df['tids'].iloc[i1]) + len(rules_df['tids'].iloc[i2]) - intersect_size)
                    jaccard_matrix[i1][i2], jaccard_matrix[i2][i1] = j, j

        return jaccard_matrix

    def ilp_selection(self, rules_df):
        num_rules = len(rules_df)
        MINERROR = 0.0000001

        if num_rules == 0:
            raise ValueError("No rules were provided for selection")

        if num_rules == 1:
            return list(rules_df.index)

        errors = np.clip(self._compute_error_scores(rules_df), a_min=MINERROR, a_max=1.0)
        supports = self._normalize(rules_df['support'].to_numpy())

        solver = pywraplp.Solver('DiversityMIP', pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)
        x = [solver.IntVar(0, 1, "x[%i]" % i) for i in range(num_rules)]

        jaccard_matrix = self._compute_jaccard_matrix(rules_df)
        xrs = {}
        for i in range(num_rules):
            for j in range(i + 1, num_rules):
                xrs[i, j] = solver.NumVar(0, 1, "x[%i,%i]" % (i, j))

        for i in range(num_rules):
            for j in range(i + 1, num_rules):
                jaccard_constraint = solver.Constraint(0, 1)
                jaccard_constraint.SetCoefficient(x[i], 1)
                jaccard_constraint.SetCoefficient(x[j], 1)
                jaccard_constraint.SetCoefficient(xrs[i, j], -2)

        mink = solver.Constraint(self.min_k, solver.infinity())
        for i in range(num_rules):
            mink.SetCoefficient(x[i], 1)

        o = solver.Objective()
        coefsList = []
        for i in range(num_rules):
            tmpe = errors[i]
            tmps = pow(supports[i], self.support_bias)
            coef = -tmps / tmpe
            coefsList.append(abs(coef))
            o.SetCoefficient(x[i], coef)

        for i in range(num_rules):
            for j in range(i + 1, num_rules):
                coefij = (jaccard_matrix[i, j] * self.overlap_bias) * (coefsList[i] + coefsList[j])
                o.SetCoefficient(xrs[i, j], coefij)

        o.SetMinimization()
        solver.SetTimeLimit(self.timeout)
        solver.Solve()

        chosen = [i for i in range(len(x)) if x[i].solution_value() == 1]
        ## Make sure the default model is always there
        if (num_rules - 1) not in chosen :
            chosen.append(num_rules - 1)
        return chosen

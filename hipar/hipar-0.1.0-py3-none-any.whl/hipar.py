# Authors: Luis Galárraga <luis.galarraga@inria.fr>
#
# License: BSD 3 clause

import pandas as pd
import numpy as np
import sys
import time
import threading
import multiprocessing
import math

from collections import deque
from joblib import Parallel, delayed
from sortedcontainers import SortedDict, SortedSet
from sklearn.linear_model import LinearRegression
from sklearn.feature_extraction import DictVectorizer
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import KFold
from typing import Callable, List, Tuple, Dict

from hipar import check
from hipar import patterns
from hipar.data import df_to_patterns
from hipar.utils import categorical_attributes, numerical_attributes, project_on_numerical_attributes, project_on_categorical_attributes, project_on_attributes
from hipar.metrics import better_performance, interclass_variance
from hipar.discretize import HIPARDiscretizer
from hipar.rule_selection import HiPaRRuleSelector, DefaultHiPaRRuleSelector
from hipar.output import output_ids_list, simplify_pattern_for_output
from hipar.types import ScikitModel, Condition, Pattern


class HiPaR :
    """ Implementation of the HiPaR (Hierarchical Pattern-aided Regression algorithm [1].
    It mines hybrid rules of the form : variety='Merlor Noir' -> incidence = 3.4 + 0.5 * mean-temp
    where the left-hand side is the characterization of a region, i.e., a pattern or condition, and the right-hand side is
    a regression model applicable only to the corresponding condition.

     Parameters
        ----------
        min_support: int or float, default=0.1
            The minimum support for patterns to be rendered in the output
            Either an int representing the absolute support, or a float for relative support
            Default to 0.1 (10%)
        enable_pruning_interclass_variance: bool, default=True
            If true, HiPaR will use the interclass variance as pruning heuristic for rules
        use_cross_validation: bool, default=False
            If true, HiPaR selects the best linear model in cross-validation for rules (using the .
        cross_validation_rounds: int, default=5
            If use_cross_validation=True, it defines the number of rounds of cross-validation used to select
            the best linear function for a rule. It has to be at least 2.
        interclass_variance_percentile_threshold: int, default=85 (little nu in the paper)
            When a pattern 'p' is refined, HiPaR computes the interclass variance of all the conditions
            that can be used to refine 'p'. Then, HiPaR sets the value at this percentile as threshold
            on interclass variance for new refinements.
        force_discretization: bool, default=False
            If true, it forces the discretization of numerical variables even if there is no optimal
            split according to the discretization algorithm (MDLP).
        regression_class: class in sklearn.linear_regression, default=sklearn.linear_regression.LinearRegression
            The class of the models in the right-hand side of rules.
        n_jobs : int, default=1
            The number of jobs to use for the computation. Each single item is attributed a job
            to discover potential itemsets, considering this item as a root in the search space.
            **Processes are preferred** over threads.
        metrics : list
            It consists of a list of error functions that will be used by HiPaR to guide the enumeration
            phase. A child rule must be better than its parent in all the metrics to be accepted as a candidate.
            Default to the mean_squared_error. If multiple metrics are given, the first metric in the list
            is used as the main metric to calculate the error-to-support trade-off as well as to guide the learning
            if cross-validation is enabled during training.
        rule_selector : rule_selection.RuleSelector
            An object of the class rule_selection.RuleSelector that tells HiPaR how to choose a subset of
            rules from the output of the enumeration phase. By default HiPaR uses an instance of the class
            rule_selection.DefaultRuleSelector.
        debug : bool, default=False
            It enables verbose logging during execution.
        References
        ----------
        .. [1]
            Luis Galárraga, Olivier Pelgrin, Alexandre Termier
            "Hierarchical Pattern-aided Regression", 2020

    """
    def __init__(self, min_support=0.1, enable_pruning_interclass_variance=True, interclass_variance_percentile_threshold=85,
                 regression_class = LinearRegression, use_cross_validation=False, cross_validation_rounds=5,
                 symbolic_attributes_in_default_model=False,
                 force_discretization=False, n_jobs=1, metrics=[mean_squared_error],
                 rule_selector=DefaultHiPaRRuleSelector(), debug=False,
                 parallel_closure_exec=False) :
        self.min_support = check._check_min_support(min_support)
        self.interclass_variance_percentile_threshold = check._check_iv_percentile(interclass_variance_percentile_threshold)
        self.enable_pruning_interclass_variance=enable_pruning_interclass_variance
        self.item_to_tids_ = SortedDict()
        self._regression_class = regression_class
        self.use_cross_validation = use_cross_validation
        self.cross_validation_rounds = check._check_cross_validation_rounds(cross_validation_rounds)
        self.symbolic_attributes_in_default_model = symbolic_attributes_in_default_model
        self.all_rules = None
        self.selected_rules = None
        self.default_model = None
        self.default_model_vectorizer = None
        self.force_discretization = force_discretization
        self.abs_min_support = None
        self.n_jobs = n_jobs
        self._train_X = None
        self._train_y = None
        self._metrics = metrics
        self.rule_selector = rule_selector
        self.debug = debug
        self._enumeration_time = 0
        self._selection_time = 0
        self._parallel_closure_exec = parallel_closure_exec
        self._numerical_attributes = None
        self._mean_y = None


    def _hipar_init_discretize(self, X : pd.DataFrame, y : pd.Series, excluded_attributes_in_conditions=set()) :
        discretizer = HIPARDiscretizer(self.force_discretization, min_support=self.abs_min_support)
        X_discr = discretizer.fit_transform(X, y, excluded_attributes_in_conditions=excluded_attributes_in_conditions)
        return X_discr
    
    def _hipar_init_get_size_one_patterns(self, X : pd.DataFrame, excluded_attributes_in_conditions=set()) :
        item_to_tids = []
        cat_attrs = [x for x in categorical_attributes(X) if x not in excluded_attributes_in_conditions]
        for attr in cat_attrs :
            col = X[attr]
            values = col.unique()
            for value in values :
                tids = col[col == value].index
                if len(tids) >= self.abs_min_support :
                    item_to_tids.append(((attr, value), list(tids)))

        return item_to_tids
        

    def _calculate_interclass_variance_threshold(self, items):
        ivs = []
        for item in items :
            tids = item[1]
            ivs.append(interclass_variance(tids, self._train_y, self._mean_y))

        if len(ivs) == 0 :
            return 0.0
        else :
            threshold = np.percentile(np.array(ivs), self.interclass_variance_percentile_threshold)
            return threshold


    def _set_intersection(self, chunk: list, output : set):
        output.update(chunk[0].intersection(*chunk))

    def _pattern_closure_parallel(self, X : pd.DataFrame, base_pattern : Pattern):
        n_threads = multiprocessing.cpu_count()
        n_transactions = len(X.index)
        if n_transactions >= 100 and n_threads > 1:
            n_threads = int(min(math.ceil(n_transactions / 100), n_threads))
            jobs = []
            partial_sets = []
            transaction_per_thread = int(math.ceil(n_transactions / n_threads))
            if self.debug:
                print('Parallelizing the closure computation using', n_threads, 'threads', file=sys.stderr)
            for i in range(0, n_threads):
                partial_set = set()
                k = i * transaction_per_thread
                kp1 = min((i + 1) * transaction_per_thread, n_transactions)
                thread = threading.Thread(target=self._pattern_closure_1, args=(X.iloc[k:kp1], base_pattern, partial_set))
                jobs.append(thread)
                partial_sets.append(partial_set)

            # Start the threads (i.e. calculate the random number lists)
            for j in jobs:
                j.start()
            # Ensure all of the threads have finished
            for j in jobs:
                j.join()

            return partial_sets[0].intersection(*partial_sets)
        else :
            ## Standard closure calculation
            return self._pattern_closure(X, base_pattern)

    def _pattern_closure_1(self, X : pd.DataFrame, base_pattern : Pattern, output : set) :
        closure = self._pattern_closure(X, base_pattern)
        output.update(closure)

    def _pattern_closure(self, X : pd.DataFrame, base_pattern : Pattern) :
        df = project_on_categorical_attributes(X)
        closure = None
        parent_pattern_set = SortedSet(base_pattern)
        for idx, row in df.iterrows():
            transaction = SortedSet()
            for col in df.columns:
                item = (col, df.loc[idx].at[col])
                transaction.add(item)

            if closure is None :
                transaction = transaction - parent_pattern_set
                closure = transaction
            elif len(closure) == 0 :
                break
            else :
                closure = closure & transaction

        return parent_pattern_set | closure

    def _is_left_most_parent(self, p: set, p_closed : set, condition : Condition, conditions : List[Condition]) :
        ## Check if new additions are before our condition
        diff = p_closed.difference(p)
        diff.remove(condition)
        idx_condition = conditions.index(condition)
        for item in diff:
            if conditions.index(item) < idx_condition :
                return False

        return True

    def _enumerate_candidates_for_condition(self, tids : List[int], conditions_and_tids : List[Tuple[Condition, List[int]]],
                                             idx : int, reference_metrics_dict : Dict[Callable, float], X : pd.DataFrame,
                                            y : pd.Series, excluded_attributes_in_conditions=set()) :
        it = self._hipar_enumerate((), tids, conditions_and_tids[idx], conditions_and_tids, reference_metrics_dict, X, y,
                                   excluded_attributes_in_conditions)
        df = pd.DataFrame(data=it, columns=["condition", "model", "tids", "scores"])
        return df

    def _get_predicates_from_pattern(self, pattern, types) :
        predicates  = []
        num_attrs = set(self._train_X.select_dtypes(include=types))
        for p in pattern :
            pred = patterns.extract_predicate_from_single_pattern(p)
            if pred in num_attrs :
                predicates.append(pred)

        return predicates

    def _get_redundant_discretizations(self, original_items, new_items_to_tids_dict) :
        redundant_original_items = set()

        discr_predicates = set()
        ## Let us first process the dictionary
        for pattern in new_items_to_tids_dict :
            if patterns.is_discretized(pattern) :
                pred = patterns.extract_predicate_from_single_pattern(pattern)
                discr_predicates.add(pred)

        ## Now iterate over the original items
        for pattern, tids in original_items :
            if patterns.is_discretized(pattern) :
                pred = patterns.extract_predicate_from_single_pattern(pattern)
                if pred in discr_predicates :
                    redundant_original_items.add(pattern)

        return redundant_original_items, discr_predicates

    def _remove_column_labels(self, X, column_labels) :
        new_X = X.copy()
        for label in column_labels :
            del new_X[label]

        return new_X

    def _rule_better_than_parent(self, f : ScikitModel, X : pd.DataFrame, y : pd.Series, reference_metrics_dict: dict) :
        add_rule = True
        new_reference_metrics_dict = {}
        for metric in self._metrics:
            value = self._compute_metric(f, metric, X, y)
            new_reference_metrics_dict[metric] = value
            if not better_performance(metric, value, reference_metrics_dict[metric]):
                add_rule = False
                break

        return add_rule, new_reference_metrics_dict

    def _hipar_enumerate(self, p : Pattern, tids : List[int],
                         new_condition_and_tids : Tuple[Condition, List[int]],
                         conditions_and_tids : List[Tuple[Condition, List[int]]],
                         reference_metrics_dict, X : pd.DataFrame, y : pd.Series,
                         excluded_attributes_in_conditions : set):
        ## Calculate the interclass variance threshold
        iv_threshold = self._calculate_interclass_variance_threshold(conditions_and_tids) if self.enable_pruning_interclass_variance else 0.0
        only_conditions = [x[0] for x in conditions_and_tids]
        new_condition = new_condition_and_tids[0]
        other_tids = new_condition_and_tids[1]

        if patterns.share_predicate(p, new_condition) :
            return

        p_prime = patterns._and_(p, new_condition)
        new_tids = list(set(tids) & set(other_tids))
        if len(new_tids) >= self.abs_min_support :
            ## Time to materialize the dataset
            iv = interclass_variance(new_tids, self._train_y, self._mean_y)
            if not self.enable_pruning_interclass_variance or iv >= iv_threshold :
                y_reduced = y.loc[new_tids]
                X_reduced = X.loc[new_tids]
                ## Compute the closure
                p_prime_closed_set = self._pattern_closure_parallel(X_reduced, p_prime) if self._parallel_closure_exec \
                    else self._pattern_closure(X_reduced, p_prime)
                p_prime_closed = tuple(p_prime_closed_set)
                ## Check if we are visiting this path a second time
                if not self._is_left_most_parent(set(p), p_prime_closed_set, new_condition, only_conditions) :
                    return

                ## Remove all the other items that may have been added because of
                ## the closure calculation. They are not anymore needed for the recursive step
                #redundant_items = p_prime_closed_set - set(p_prime)
                #remaining_items = deque([(pattern, tids) for pattern, tids in conditions_and_tids
                #                         if pattern not in redundant_items])

                f_p = self._learn_regression_model(X_reduced, y_reduced)
                ## Check if we win for all metrics
                add_rule, new_reference_metrics_dict = self._rule_better_than_parent(f_p, X_reduced, y_reduced,
                                                                                     reference_metrics_dict)

                ## If so, add the rule
                if add_rule :
                    ## Produce the rule: pattern, linear model, covered points, scores
                    scores = {k.__name__ : v for k, v in new_reference_metrics_dict.items()}
                    if self.debug :
                        print('Selecting candidate', p_prime_closed, '(refined from', p, 'and', str(new_condition) + ')',
                              str(len(new_tids)) + '/' + str(len(self._train_X)),
                              output_ids_list(new_tids, n=10), scores, file=sys.stderr)
                    yield simplify_pattern_for_output(p_prime_closed), f_p, new_tids, scores

                    ## Discretize the remaining numerical variables
                    numerical_attributes_in_pattern = set(self._get_predicates_from_pattern(p_prime_closed,
                                                                             types=['int64', 'float64']))

                    attrs_to_discr = set(self._numerical_attributes) - numerical_attributes_in_pattern
                    if len(attrs_to_discr) > 0 :
                        X_rediscr = self._hipar_init_discretize(X_reduced[attrs_to_discr], y_reduced,
                                                                excluded_attributes_in_conditions=excluded_attributes_in_conditions)
                        new_discr_items_to_tids = SortedDict(self._hipar_init_get_size_one_patterns(X_rediscr))
                        ## Here we have to make sure to remove redundant discretizations
                        redundant_discr_conds, redundant_num_attrs = self._get_redundant_discretizations(conditions_and_tids,
                                                                                                    new_discr_items_to_tids)
                        new_other_items = [x for x in conditions_and_tids if x[0] not in redundant_discr_conds]
                        new_other_items.extend(new_discr_items_to_tids.items())
                        #new_other_items = sorted(
                        #    new_other_items, key=lambda e: len(e[1]), reverse=True
                        #)

                        columns_to_remove = redundant_num_attrs | set([x[0] for x in redundant_discr_conds])
                        X_adjusted = self._remove_column_labels(X_reduced, columns_to_remove)
                        X_adjusted = pd.concat([X_adjusted, X_rediscr], axis=1)
                        X_adjusted = X_adjusted.loc[:, ~X_adjusted.columns.duplicated()]
                    else :
                        new_other_items = conditions_and_tids
                        X_adjusted = X_reduced

                    ## Fix the recursive step to consider all items
                    for idx, item in enumerate(new_other_items) :
                        yield from self._hipar_enumerate(p_prime_closed, new_tids, item, new_other_items,
                                                         new_reference_metrics_dict, X_adjusted, y_reduced,
                                                         excluded_attributes_in_conditions)

    def _compute_metric(self, f : ScikitModel, metric : Callable, X : pd.DataFrame, y : pd.Series) -> np.array :
        y_predicted = self.predict_with_model(X, f)
        return metric(y_predicted, y)

    def _prepare_for_default_model(self, X : pd.DataFrame, vectorizer : DictVectorizer = None)  :
        if isinstance(X, pd.DataFrame) :
            records = X.to_dict('records')
        else :
            records = X[0].to_dict()

        if vectorizer is None :
            vectorizer = DictVectorizer()
            X_vec = vectorizer.fit_transform(records)
        else :
            X_vec = vectorizer.transform(records)

        return X_vec, vectorizer

    def _train(self, X : pd.DataFrame, y : pd.Series) :
        if len(self._metrics) > 0 :
            error_metric = self._metrics[0]
        else :
            error_metric = mean_squared_error

        size_threshold = 10 * self.cross_validation_rounds
        if self.use_cross_validation and len(X) >= size_threshold :
            kf = KFold(n_splits=self.cross_validation_rounds)
            best_model = None
            best_error = None
            for train_index, test_index in kf.split(X, y):
                model = self._regression_class()
                X_train, X_test = X.iloc[train_index], X.iloc[test_index]
                y_train, y_test = y.iloc[train_index], y.iloc[test_index]
                model.fit(X_train, y_train)
                error = error_metric(model.predict(X_test), y_test)

                if best_model is None or better_performance(error_metric, error, best_error) :
                    best_model = model
                    best_error = error
        else :
            best_model = self._regression_class()
            best_model.fit(X, y)

        return best_model

    
    def _learn_default_model(self, X : pd.DataFrame, y : pd.Series)  :
        if self.symbolic_attributes_in_default_model :
            ## We have to vectorize the categorical attributes
            X_b, default_model_vectorizer = self._prepare_for_default_model(X)
        else :
            ## We get rid of the categorical attributes
            X_b = project_on_attributes(X, self._numerical_attributes)
            default_model_vectorizer = None

        ## We now fit the default model to the labels
        default_model = self._train(X_b, y)
        return default_model, default_model_vectorizer

    def _learn_regression_model(self, X : pd.DataFrame, y : pd.Series) -> ScikitModel :
        X_num = project_on_attributes(X, self._numerical_attributes)
        return self._train(X_num, y)

    ## This implementation has been inspired on LCM's scikit-mine implementation
    ## https://github.com/scikit-mine/scikit-mine/blob/master/skmine/itemsets/lcm.py
    def fit(self, X : pd.DataFrame, y : pd.Series, excluded_attributes_in_conditions=[]) :
        """
        It learns hybrid rules that predict 'y' from the input data 'X'.
        The learned rules are stored in the object attribute rules.

        :param X: pandas.DataFrame
        :param y: pandas.Series (using the same indexing as X)
        :param excluded_attributes_in_conditions : Iterable, default=set()
            A list of attributes that are not allowed in conditions (left-hand side of rules). They can be
            either categorical or numerical (in the latter case they are ignored for discretization)
        :return: self
        """
        self._enumeration_time = time.time()
        self.abs_min_support = self.min_support if isinstance(self.min_support, int) else int(self.min_support * len(X.index))
        self._numerical_attributes = numerical_attributes(X)
        ## Learn the default model (Line 1 in the algorithm description)
        self.default_model, self.default_model_vectorizer = self._learn_default_model(X, y)
        
        ## Bootstrap the search: get patterns of size 1 with their support and 
        ## discretize numerical variables
        excluded_attrs_set = set(excluded_attributes_in_conditions)
        X_discretized = self._hipar_init_discretize(X, y, excluded_attributes_in_conditions=excluded_attrs_set)
        self.item_to_tids_ = SortedDict(self._hipar_init_get_size_one_patterns(X_discretized,
                                                                               excluded_attributes_in_conditions=excluded_attrs_set))
        self._train_X = X_discretized
        self._train_y = y
        self._mean_y = np.mean(self._train_y)

        # reverse order of support
        supp_sorted_conditions = sorted(
            self.item_to_tids_.items(), key=lambda e: len(e[1]), reverse=True
        )
        if self.debug :
            print('Search space consists of', len(supp_sorted_conditions), ' first-level conditions',  file=sys.stderr)

        metrics_dict = {}
        y_hat = self.predict_with_default_model(X)
        for metric in self._metrics :
            metrics_dict[metric] = metric(y_hat, self._train_y)

        all_tids = list(self._train_X.index)

        rule_batches = Parallel(n_jobs=self.n_jobs, prefer="processes")(
            delayed(self._enumerate_candidates_for_condition)(all_tids, supp_sorted_conditions, idx,
                                                              metrics_dict,
                                                              self._train_X, self._train_y, excluded_attrs_set)
            for idx in range(len(supp_sorted_conditions))
        )


        df_model = pd.DataFrame(
            {'condition' : [()], 'model' : [self.default_model], 'tids' : [list(self._train_X.index)],
             'scores' : [{metric.__name__ : metric(self.predict_with_default_model(self._train_X), self._train_y)
                          for metric in self._metrics}]}
        )

        rule_batches.append(df_model)  # make sure we have something to concat
        self.all_rules = pd.concat(rule_batches, axis=0, ignore_index=True)
        self.all_rules.loc[:, "support"] = self.all_rules["tids"].map(len).astype(np.uint32)
        self._enumeration_time = time.time() - self._enumeration_time

        if self.debug :
            print("Enumeration time:", self._enumeration_time, 'seconds', file=sys.stderr)

        self._selection_time = time.time()
        if self.rule_selector is not None :
            self.selected_rules = self.rule_selector.select(self.all_rules)
        else :
            self.selected_rules = self.all_rules.index
        self._selection_time = time.time() - self._selection_time

        if self.debug :
            print('Selection time:', self._selection_time, 'seconds', file=sys.stderr)
            print('Selecting rules with indexes', list(self.selected_rules), file=sys.stderr)

        return self

    def predict_with_model(self, X : pd.DataFrame, model : ScikitModel) -> np.array :
        if isinstance(X, pd.DataFrame) :
            return model.predict(project_on_attributes(X, self._numerical_attributes))
        else :
            return model.predict([project_on_attributes(X, self._numerical_attributes)])

    def predict_with_default_model(self, X : pd.DataFrame) -> np.array :
        if self.symbolic_attributes_in_default_model :
            if isinstance(X, pd.DataFrame) :
                X_b, vectorizer = self._prepare_for_default_model(X, self.default_model_vectorizer)
            else :
                X_b, vectorizer = self._prepare_for_default_model([X], self.default_model_vectorizer)

            return self.default_model.predict(X_b)
        else :
            if isinstance(X, pd.DataFrame) :
                return self.default_model.predict(project_on_attributes(X, self._numerical_attributes))
            else :
                return self.default_model.predict([project_on_attributes(X, self._numerical_attributes)])

    def get_selected_rules(self) -> pd.DataFrame :
        return self.all_rules.loc[self.selected_rules]

    def _retrieve_reciprocal_errors(self, all_non_trivial_rule_ids, matched_rules_idx, error_fn : Callable) -> List[float] :
        errors = []
        error_fn_name = error_fn.__name__
        matched_errors = []

        for idx in matched_rules_idx :
            matched_errors.append(self.all_rules.loc[idx]['scores'][error_fn_name])
        matched_errors = np.array(matched_errors)

        ## If all relevant errors are zero, then return an array full of zeros
        if len(matched_errors[matched_errors > 0.0]) == 0 :
            raise ValueError('Error relevant error values are all equals 0')
        else :
            ## Calculate the minimum non-zero value
            all_errors = np.array([self.all_rules.loc[idx]['scores'][error_fn_name] for idx in all_non_trivial_rule_ids])
            all_inv_errors = 1. / all_errors[all_errors > 0.0]
            if len(all_inv_errors) > 0 :
                min_inv_error = np.min(all_inv_errors)
                for idx in all_non_trivial_rule_ids :
                    if idx in matched_rules_idx :
                        error_value = self.all_rules.loc[idx]['scores'][error_fn_name]
                        if not np.isclose(error_value, 0.0, rtol=1e-05, atol=1e-08, equal_nan=False) :
                            errors.append(1./ error_value)
                        else :
                            ## Assign the smallest non-zero value
                            errors.append(min_inv_error)
                    else :
                        errors.append(0.0)
            else :
                raise ValueError('All error values are equals 0')

        return errors

    def _retrieve_supports(self, all_non_trivial_rule_ids, matched_rules_idx) :
        supports = []
        for idx in all_non_trivial_rule_ids :
            if idx in matched_rules_idx :
                supports.append(self.all_rules.loc[idx]['support'])
            else :
                supports.append(0)

        return supports


    def predict(self, X: pd.DataFrame, rule_selector : HiPaRRuleSelector = None,
                debug : bool = False) -> np.array :
        """
        It uses the rules learned by HiPaR to make predictions based on the input data.
        :param X: pandas.DataFrame
        :param debug: boolean
        :return: numpy.array containing the predictions for each row of the input data frame.
        """
        X_p = []
        # Define the error metric for weighting
        if len(self._metrics) > 0 :
            error_metric = self._metrics[0]
        else :
            error_metric = mean_squared_error

        default_idx = len(self.all_rules) - 1
        if rule_selector is None :
            selected_rules = self.get_selected_rules()
        else :
            selected_rules_ids = rule_selector.select(self.all_rules)
            selected_rules = self.all_rules.loc[selected_rules_ids]

        non_trivial_rule_ids = [x for x in selected_rules.index if x != default_idx]

        for i, x_i in X.iterrows() :
            tmp_dict = {}
            tmp_dict_mask = {}
            for idx in non_trivial_rule_ids :
                tmp_dict[idx] = None
                tmp_dict_mask[idx] = None
                if patterns.matches(selected_rules.loc[idx]['condition'], x_i) :
                    tmp_dict[idx] = self.predict_with_model(x_i, selected_rules.loc[idx]['model']).item()
                    tmp_dict_mask[idx] = True
                else :
                    tmp_dict[idx] = 0.0
                    tmp_dict_mask[idx] = False

            if (np.any([x for x in tmp_dict_mask.values()])) :
                ## Normalize the values according to the error
                values = np.array([x for x in tmp_dict.values()], dtype=float)
                matched_rule_ids = [x for x in tmp_dict_mask.keys() if tmp_dict_mask[x]]
                try :
                    errors = self._retrieve_reciprocal_errors(non_trivial_rule_ids, matched_rule_ids, error_metric)
                    values = values * (errors / np.linalg.norm(errors, ord=1))
                    if debug :
                        print('Obs=', i, ': using rules with ids', list(matched_rule_ids), 'and weights (error)',
                              (errors / np.linalg.norm(errors, ord=1)), ' with predictions: ', values, file=sys.stderr)
                except ValueError :
                    supports = self._retrieve_supports(non_trivial_rule_ids, matched_rule_ids)
                    values = values * (supports / np.linalg.norm(supports, ord=1))
                    if debug :
                        print('Obs=', i, ': using rules with ids', list(matched_rule_ids),
                              'and weights (support)', (supports / np.linalg.norm(supports, ord=1)),
                              ' with predictions: ', values, file=sys.stderr)
                finally :
                    X_p.append(sum(values))
            else :
                if debug :
                    print('Obs=', i, ': using the default model', file=sys.stderr)
                X_p.append(self.predict_with_default_model(x_i).item())

        return np.array(X_p)

HIPAR = HiPaR
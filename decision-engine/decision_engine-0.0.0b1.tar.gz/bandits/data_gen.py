from scipy.stats import bernoulli


def generate_bernoulli_responses(actual_positive_rates, treatment_selections):
    """
    Generate list of responses biased by the given rates and treatment
    selections.

    Integers within the list passed into `treatment_selection` must all be
    valid indices of `actual_positive_rates`, which itself must be a list of rates.
    """

    # define counter structure:
    observations = [[0, 0] for _ in range(len(actual_positive_rates))]

    for this_treatment in treatment_selections:
        this_open_rate = actual_positive_rates[this_treatment]

        # {0, 1}, biased towards 1 according to given rate:
        raw_observation = bernoulli.rvs(this_open_rate, size=1)[0]

        # observation gives 1 or 0 for pos or neg
        # index 0 is our pos and index 1 is our neg
        obs_as_index = 1-raw_observation

        # convert to n_positives and n_negatives
        observations[this_treatment][obs_as_index] += 1

    return observations
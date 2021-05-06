"""This module contains the classes EventData, ContData."""
import pickle
import os.path
import numpy as np


def get_stim_intervals_from_starts_stops(stim_starts, stim_stops):
    # checks and rounding down
    assert len(stim_starts) == len(stim_stops)
    stim_starts = np.floor(stim_starts[0, :] * 1000) / 1000
    stim_stops = np.floor(stim_stops[0, :] * 1000) / 1000
    # option 0: 2D array
    stim_intervals = np.array((2, len(stim_starts)))
    stim_intervals[0, :] = stim_starts
    stim_intervals[1, :] = stim_stops
    # option 1: list of tuples
    stim_intervals = [(stim_starts[idx], stim_stops[idx]) for idx in range(stim_starts)]
    # option 2: list of lists
    stim_intervals = [[stim_starts[idx], stim_stops[idx]] for idx in range(stim_starts)]
    return stim_intervals


def update_saving_paths(obj, results_path, figures_path):
    """Updates the paths where any results anf figures should be saved into.

    Parameters
    ----------
    results_path: str
        path to folder where results should be saved into
    figures_path: str
        path to folder where figures should be saved into
    """
    assert type(results_path) == str
    assert type(figures_path) == str
    obj.results_path = results_path
    obj.figures_path = figures_path


class EventData:
    """
    Class to transform spike_indices (i) and spike_times (t) into a ntm-usable format.

    Creating an 'Import' object does by default not load any data, you need to call .create() or .load_from_file()
    instead.
    To re-format files, you need to call .read()

    """

    def __init__(self):
        """
        Instantiates the class instance and standard variables.
        """
        print('Creating EventData instance')
        self.results_path = './'
        self.figures_path = './'

    def add_events(self, indices, times):
        """
        Loads spike_indices (i) and spike_times (t) into class instance.

        Parameters
        ----------
        indices: array or array_like, 1d
            indices of neurons (length needs to be the same as times); needs to be sorted by times
        times: array or array_like, 1d, [s]!
            times of spikes (length needs to be the same as indices); needs to be sorted by time
        """
        print('adding events')
        # necessary parameters
        assert len(indices) == len(times)
        assert len(indices) > 0
        self.indices = indices
        self.times = times
        # get neuron ids
        inds, counts = np.unique(self.indices, return_counts=True)
        self.neurons_good = inds
        self.number_neurons = len(inds)
        self.exp_length = self.times[-1] - self.times[0]


class Experiment:

    def __init__(self):
        pass

    def add_experiment_structure(self, stim_starts, stim_stops, stim_id, exp_name=''):
        """Loads experimental information into class instance.

        Intervals given should all be of the same length.
        Stim_id is a 2D matrix to allow multiple stimuli to happen at the same time.

        Parameters
        ----------
        stim_intervals: list of tuples
            for each stimulus presentation, the tuple contains the start and end time,
            needs to be same length as stim_id.
        stim_id: array or array_like, 2d shape (n_stimuli_types, n_trials), optional
            identity (number) of which stimulus was present (needs to be same length as stim_intervals)
        exp_name: string, optional
            name of experiment used for titles of plots
        """
        assert len(stim_starts) == len(stim_stops) == stim_id.shape[1]
        assert len(stim_id.shape) == 2

        self.stim_starts = stim_starts  # np.floor(stim_starts * 1000) / 1000
        self.stim_stops = stim_stops  # np.floor(stim_stops * 1000) / 1000
        self.stim_id = stim_id
        self.exp_name = exp_name

        # calculate other experimental parameters
        self.exp_length = self.stim_stops[-1][1] - self.stim_starts[0][0]
        self.avg_trial_length = np.round(np.mean(self.stim_stops - self.stim_starts), 3)
        self.number_trials = len(self.stim_stops)


class NeuroPixel(EventData, Experiment):

    def __init__(self):
        super().__init__()






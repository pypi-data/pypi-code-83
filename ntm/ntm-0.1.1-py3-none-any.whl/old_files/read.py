import numpy as np
import pickle
import os.path


class Read:
    """
    Class to format raw data for word creation

    Creating a 'Read' object does by default not load any data, you need to call .create() or .load_from_file()
    instead. Opt
    To re-format files, you need to call .read()

    """

    def __init__(self, flag_return_only_matrix=False):
        """please see help(Read) for documentation on this class"""

        print('initialisation of Read ')
        # general flags
        # *******************************************************************************************************
        self.flag_return_only_matrix = flag_return_only_matrix

        # initialise all variables in Read objects as None
        # *******************************************************************************************************

        self.indices = None
        self.times = None
        self.stim_starts = None
        self.stim_stops = None
        self.stim_id = None
        self.exp_name = None
        self.neurons_good = None
        self.neurons_good_depth = None
        self.depth_min = None
        self.depth_max = None

        self.firing_rate_threshold = None

    def create(self, indices, times, stim_starts=None, stim_stops=None, stim_id=None, exp_name='',
               results_path='./', figures_path='./'):
        """
        Loads variables into class instance

        If stimulus information is provided, more experimental variables are calculated from the variables given.

        Parameters
        ----------
        indices: array or array_like, 1d
            indices of neurons (length needs to be the same as times), needs to be sorted by times
        times: array or array_like, 1d, [s]!
            times of spikes (length needs to be the same as indices); needs to be sorted by time
        stim_starts: array or array_like, 1d, optional
            times when each stimulus starts (needs to be same length as stim_stops and stim_id)
        stim_stops: array or array_like, 1d, optional
            times when each stimulus stops (needs to be same length as stim_starts and stim_id)
        stim_id: array or array_like, 2d shape (n_stimuli_types, n_trials), optional
            identity (number) of what stimulus was present (needs to be same length as stim_starts and stim_stops)
        exp_name: string, optional
            name of experiment used for titles of plots

        """
        # necessary parameters
        assert len(indices) == len(times)
        assert len(indices) > 0
        self.indices = indices
        self.times = times

        # get neuron ids
        inds, counts = np.unique(self.indices, return_counts=True)
        self.neurons_good = inds
        self.number_neurons = len(inds)

        # non-essential parameters
        if isinstance(stim_starts, np.ndarray) and isinstance(stim_stops, np.ndarray) and isinstance(stim_id, np.ndarray):
            # this is only relevant for exp 3, but not for others so will disable this assert
            # assert len(stim_id.shape) == 2
            assert len(stim_starts) == len(stim_stops) == stim_id.shape[1]

            self.stim_starts = np.floor(stim_starts * 1000) / 1000
            self.stim_stops = np.floor(stim_stops * 1000) / 1000
            self.stim_id = stim_id

            # calculate other experimental parameters
            self.exp_length = self.stim_stops[-1] - self.stim_starts[0] # + 0.001  # add one ms to include last spike
            self.exp_structure = True
            self.avg_trial_length = np.round(np.mean(self.stim_stops - self.stim_starts), 3)
            self.number_trials = len(self.stim_starts)

        else:
            self.exp_length = self.times[-1] - self.times[0] # + 0.001  # add one ms to include last spike
            self.exp_structure = False

        self.exp_name = exp_name
        self.results_path = results_path
        self.figures_path = figures_path



    def load_from_file(self, path_to_data, filename, only_params=False):
        """
        Loads a previously saved instance of Read

        Replaces the current instance with the loaded one.

        Parameters
        ----------
        path_to_data: string
            path to folder in which data is located, needs a '/' in the end
        filename: string
            name of file, needs to include '.pickle' at the end
        """

        # Make sure that file can be loaded
        # *******************************************************************************************************
        if path_to_data[-1] != '/':
            print(f'path does not end in "/", so I am adding it to hopefully prevent errors ')
            path_to_data = path_to_data + '/'

        if filename[-7:] != '.pickle':
            print('filename does not end with ".pickle", cannot proceed safely, please check file name and format.')

        # check that file exists and if yes, load that file into the current instance. if no print error message
        if os.path.exists(path_to_data + filename):
            data = pickle.load(open(f'{path_to_data}{filename}', 'rb'))
            self.__dict__ = data.__dict__
        else:
            print(f'Error. Could not find the following file: \n {path_to_data}{filename} '
                  f'\n Have you included the extension .pickle?')

        if only_params == False:
            # when saving large matrix was deleted to save disk space - need to recreate now.
            self.full_2d_matrix = self.process_2d()



    def filter(self, by_spiking_behaviour=False, firing_rate_threshold=0.05, by_location=False,
               depth_min=-1, depth_max=1000000, neurons_good_depth=None):
        """
        Filters neurons

        Filters out neurons either by minumum firing rate (no max firing rate implemented so far)
        or by location on electrode (only words for depth so far, so mostly applicable to Neuropixel electrodes)

        Parameters
        ----------
        by_spiking_behaviour: bool
            whether to filter by minimum firing rate
        firing_rate_threshold: float
            minumum firing rate for neurons
        by_location: bool
            whether to filter by depth, can specify minimum and maximum depth
        depth_min: float or int
            lower bound on electrode (smaller depth value)
        depth_max: float or int
            higher bound on electrode (larger depth value)
        neurons_good_depth: array or array_like
            needs to be the same length as neurons_good and needs to be sorted by neurons_good id numbers low to high!!
        """


        print(f'before filtering: number spikes total: {len(self.indices)}')

        neurons_eligible = np.ones(len(self.neurons_good), dtype=bool)
        print(f'before filtering: number eligible neurons = {sum(neurons_eligible)}')

        # filter by firing rate threshold
        if by_spiking_behaviour:
            self.firing_rate_threshold = firing_rate_threshold
            neurons_eligible = self.filter_by_spiking_behaviour(neurons_eligible)
            print(f'after filtering by spiking behaviour: number eligible neurons = {sum(neurons_eligible)}')

        # filter by locaiton on electrode (neuropixel only etm)
        if by_location:
            self.depth_min = depth_min
            self.depth_max = depth_max
            self.neurons_good_depth = neurons_good_depth
            neurons_eligible = self.filter_by_location(neurons_eligible)
            print(f'after filtering by location: number eligible neurons = {sum(neurons_eligible)}')

        # apply exclusion criteria
        self.neurons_good = self.neurons_good[neurons_eligible]

        if by_location:
            self.neurons_good_depth = self.neurons_good_depth[neurons_eligible]

        # filter indices and times accordingly
        self.filter_spikes()
        print(f'after filtering: number spikes total: {len(self.indices)}')

        # sort neurons by depth (shallow first)
        if by_location:
            sort_array = self.neurons_good_depth.argsort()
            sort_array = np.flipud(sort_array)
            self.neurons_good_depth = self.neurons_good_depth[sort_array]
            self.neurons_good = self.neurons_good[sort_array]

        self.number_neurons = len(self.neurons_good)


    def filter_by_spiking_behaviour(self, neurons_eligible):

        # get firing rates
        inds, counts = np.unique(self.indices, return_counts=True)
        count_threshold = self.firing_rate_threshold * self.exp_length

        # check whether neurons_good has changed
        assert np.sum(inds != self.neurons_good) == 0

        # exclude all neurons with too low spike count
        neurons_eligible[np.where(counts <= count_threshold)[0]] = False

        return neurons_eligible


    def filter_by_location(self, neurons_eligible):
        """
        this only works for 1d Neuropixel electrodes, not for Utah arrays (at the moment)
        """

        # check that depth_min is actually the smaller number, if not, switch them
        if self.depth_min < self.depth_max:
            self.depth_min = self.depth_min
            self.depth_max = self.depth_max
        else:
            print('Note: were depth_min and depth_max switched?')
            self.depth_min = self.depth_max
            self.depth_max = self.depth_min

        # check which neurons fulfil requirements
        neurons_eligible[np.where(self.neurons_good_depth >= self.depth_max)[0]] = False
        neurons_eligible[np.where(self.neurons_good_depth <= self.depth_min)[0]] = False

        return neurons_eligible


    def filter_spikes(self):
        # keep only entries in indices and times of neurons in relevant regions and whose firing rates are high enough
        keep_flag = np.zeros(len(self.indices), dtype=bool)
        for neuron in self.neurons_good:
            keep_flag[np.where(self.indices == neuron)[0]] = True

        self.indices = self.indices[keep_flag]
        self.times = self.times[keep_flag]



    def read(self, res=0.001, keep_only_relevant=True):
        """
        Converts indices and times into sparse binary matrix

        Resulting sparse matrix is of dimensions (number_neurons, experiment_length_in_res + 100ms).

        Parameter
        ---------
        res: float or int
            resolution of matrix, depends on resolution of variable 'times'. If 'times' is [s] and you want matrix
            to be in [ms], then res needs to be 0.001
        """

        self.res = res

        # create a binary matrix, shape: n_neurons, n_time_windows

        self.full_2d_matrix = self.process_2d()


        if self.exp_structure:

            if keep_only_relevant:

                # create array where shape is (n_different_trialtypes, n_trials)
                self.stim_id_appearance = np.zeros(self.stim_id.shape, dtype=int)

                # from stim_id get info of when squares appeared
                # only keep 1 or -1 for the start of the stimulus - this only works when a white square never goes to black immediately
                # without being grey in the middle!
                self.stim_id_appearance = np.zeros(self.stim_id.shape, dtype=int)
                self.stim_id_appearance[:, 0] = self.stim_id[:, 0]
                # keep the 1 or -1 if the change went from 0 to 1/-1 not other way round (when square turned off)
                self.stim_id_appearance[:, 1:] = abs(self.stim_id[:, 1:]) * (self.stim_id[:, 1:] - self.stim_id[:, :-1])
                if np.any(abs(self.stim_id_appearance) > 1):
                    print('Oh oh! Looks like a stimulus is going from -1 (black) to +1 (white) or the other way round '
                          'without being 0 (grey) in between! '
                          'I have not programmed this case yet, so you cannot run this...')

                # check which trials actually have a new square appearing or disappearing
                self.stim_id_relevant = np.where(np.sum(abs(self.stim_id_appearance), axis=0) != 0)[0]

                # self.full_matrix = self.full_matrix[:, self.stim_id_relevant, :]
                self.stim_id = self.stim_id[:, self.stim_id_relevant]
                self.stim_id_appearance = self.stim_id_appearance[:, self.stim_id_relevant]
                self.stim_starts = self.stim_starts[self.stim_id_relevant]
                self.stim_stops = self.stim_stops[self.stim_id_relevant]
                self.number_trials = len(self.stim_id_relevant)

            else:
                self.stim_id_appearance = self.stim_id
                self.stim_id_relevant = np.arange(self.stim_id.shape[1])
                self.number_trials = len(self.stim_id_relevant)


            self.trials = np.arange(0, self.stim_id_appearance.shape[0], 1)
            self.trial_counts = np.sum((self.stim_id_appearance != 0), axis=1)
            self.trial_counts_b = np.sum((self.stim_id_appearance == -1), axis=1)
            self.trial_counts_w = np.sum((self.stim_id_appearance == 1), axis=1)




    def process_2d(self):

        buffer_1s = 1000
        if self.exp_structure:
            start = self.stim_starts[0]
            # added buffer to stop to make sure that any response delay can also be calculated
            stop = self.stim_stops[-1] + self.res + buffer_1s*self.res  # add 1 res unit to make sure last spike is counted
            # need to save the start_time (?)

        else:
            # this is when there are no trial starts and stops etc to rely on.
            # So the first spike is the start and the last spike the end
            start = self.times[0]
            stop = self.times[-1]

        # check if there are spikes after the end of the experiment
        last_spike = min(self.times[-1], stop + int(buffer_1s/self.res))
        # cut times at start and stop (stop already has buffer included)
        if self.times[-1] < stop + buffer_1s*self.res:
            self.indices = self.indices[np.where(self.times >= start)[0][0]:]
            self.times = self.times[np.where(self.times >= start)[0][0]:]
        else:
            self.indices = self.indices[np.where(self.times >= start)[0][0]:
                                    np.where(self.times >= stop)[0][0] - 1]
            self.times = self.times[np.where(self.times >= start)[0][0]:
                                    np.where(self.times >= stop)[0][0] - 1]
        assert len(self.times) == len(self.indices)
        # transform times and stim_starts and stops into relative time to start of experiment
        self.times -= start
        if self.exp_structure:
            self.stim_starts -= start
            self.stim_stops -= start


        # initialise full_2d_matrix
        full_2d_matrix = np.zeros((self.number_neurons, int(np.round((stop - start) / self.res)) + buffer_1s), dtype=int)

        # for each neuron translate spike times into position in matrix
        for neuron_idx, neuron in enumerate(self.neurons_good):
            # get indices of all spikes from that neuron; times has already been cut properly
            spikes_temp = self.times[self.indices == neuron]
            # convert spikes into indices for full 2d matrix

            # !!! this gets rid of some spikes happening in the same millisecond
            # the round() then astype converts the whole array into int without wrongly rounding down.
            # when spikes happen at 0.5, there are rounding errors - sometimes the numbers are rounded up,sometimes down
            spikes_inds = np.round(spikes_temp / self.res, 0).astype(int)
            # if max(spikes_inds) >= 481280:
            #     print(f'neuron_idx {neuron_idx}')
            #     print(f'spike_inds {spikes_inds}')
            full_2d_matrix[neuron_idx, spikes_inds] = 1

        print(f'2D matrix: Number of spikes happening within 1 ms of each other (discarded): '
              f'{len(self.indices) - np.sum(full_2d_matrix)}')
        self.sparsity = 100 * (full_2d_matrix > 0).sum() / full_2d_matrix.size
        print(f'2D matrix: Sparsity = {self.sparsity} %')
        return full_2d_matrix


    def process_3d(self):

        # calculate number of windows
        self.number_windows = int(round((self.avg_trial_length + 2 * self.buffer) / self.res))

        full_matrix = np.zeros((self.number_neurons, self.number_trials, self.number_windows), dtype=int)

        min_idx = 0

        for trial_idx, trial_start in enumerate(self.stim_starts):

            if trial_idx % 5000 == 0:
                print(f'passing trial number {trial_idx}')

            # find indices referring to times where this trial happens in arrays indices and times
            time_dyn_start = np.searchsorted(self.times[min_idx:], trial_start - self.buffer)
            time_dyn_stop = np.searchsorted(self.times[min_idx:], self.stim_stops[trial_idx] + self.buffer)

            ind_temp = self.indices[min_idx + time_dyn_start:min_idx + time_dyn_stop]
            tim_temp = self.times[min_idx + time_dyn_start:min_idx + time_dyn_stop]

            ind_temp_set = list(set(ind_temp))
            inds_temp_position_in_matrix = [np.where(self.neurons_good == i)[0][0] for i in ind_temp_set]

            min_idx += time_dyn_start

            for neuron_idx, neuron in enumerate(ind_temp_set):
                spikes_temp = tim_temp[ind_temp == neuron] - trial_start + self.buffer
                # need to get an int array, but is really tricky, .astype(int) sometimes gave the rounded down number...
                spikes_in_windows = np.round(spikes_temp * (1 / self.res), 0).astype(int)
                spikes_in_windows = spikes_in_windows[spikes_in_windows < self.number_windows]

                full_matrix[inds_temp_position_in_matrix[neuron_idx], trial_idx, spikes_in_windows] += 1
        return full_matrix


    def save(self, path_to_data, filename):
        """
        Saves the current instance of Read object using pickle.

        Overrides any existing files with the same name without asking

        Parameters
        ----------
        path_to_data: string
            path to folder in which data should be located, needs a '/' in the end
        filename: string
            name of file, needs to include '.pickle' at the end

        """
        # do not save large matrix - cannot be handled by pickle, so save matrix, delete, save, add matrix again
        full_matrix_temp = np.copy(self.full_2d_matrix)
        self.full_2d_matrix = None

        if path_to_data[-1] != '/':
            print(f'path does not end in "/", so I am adding it to hopefully prevent errors ')
            path_to_data = path_to_data + '/'

        if filename[-7:] != '.pickle':
            print('filename does not end with ".pickle", cannot proceed safely, please check file name and format.')

        with open(path_to_data + filename, 'wb') as output:  # Overwrites any existing file.
            pickle.dump(self, output, pickle.HIGHEST_PROTOCOL)

        self.full_2d_matrix = full_matrix_temp



def make_regular_documents(trial_length=0.16, overlap=0, time_start=0, time_stop=1000, meaningless_stim_id=True):
        # make time windows [s]
        stim_starts = np.arange(np.round(time_start, 3),
                                np.round(time_stop - trial_length, 3),
                                (1 - overlap) * trial_length)
        print(f' with {overlap} overlap there are {len(stim_starts)} documents')
        stim_stops = stim_starts + trial_length

        if meaningless_stim_id:
            # create a placeholder for stim_ids
            stim_id = np.zeros((2, len(stim_starts)), dtype=int)
            stim_id[0, 1:] = 1
            # to avoid dividing by zero later when normalising: (but won't need this anymore once i finished
            # the proper assignment of trials)
            stim_id[1, 0] = 1

            return stim_starts, stim_stops, stim_id
        else:
            return stim_starts, stim_stops




def make_nonexperiment_documents(trial_length=0.16, overlap=0,
                                 stim_starts=np.array([0]), stim_stops=np.array([1000]),
                                 stim_id=np.array([0]), blank_cond=-1):

    time_start = stim_starts[0]
    time_stop = stim_stops[-1]

    # make new time windows [s]
    stim_starts_new, stim_stops_new = make_regular_documents(trial_length=trial_length, overlap=overlap,
                                                     time_start=time_start, time_stop=time_stop,
                                                     meaningless_stim_id=False)

    # actually make new stim_id based on overlap with original stim_id
    # have to take into account that there could be a stimulus present or not (blank condition is always last?)
    # clank condition and time between stimulus both go into the same conditon

    stim_id_new = np.zeros((stim_id.shape[0], len(stim_starts_new)))
    # I know that each trial is 0.16s long - that is fixed
    # so go through each stimulus and add ones
    for real_stim_id_idx in range(stim_id.shape[1]):
        # what stimulus was presented
        current_stim_condition = np.where(stim_id[:, real_stim_id_idx] > 0)[0]
        # search for which trials start during this presentation and end < 0.5*trial_length before stim ends
        inds_to_assign = np.where((stim_starts_new >= stim_starts[real_stim_id_idx] - 0.25*trial_length) * \
                                  (stim_stops_new <= stim_stops[real_stim_id_idx] + 0.25*trial_length))[0]

        if len(inds_to_assign) > 0:
            stim_id_new[current_stim_condition, inds_to_assign] = 1
        else:
            print(f'did not find stim starts in this time window - did something go wrong? index {real_stim_id_idx}')

    # at end fill all runs which were not assigned to at least one stimulus to blank condition.
    stim_id_new[blank_cond, np.where(np.sum(stim_id_new, axis=0) == 0)[0]] = 1
    # check that every trial has a stimulus associated with it
    if np.all(stim_id_new.sum(axis=0) >= 1):
        print(f'each trial has **at least** one stimulus associated with it')
    elif np.all(stim_id_new.sum(axis=0) == 1):
        print(f'each trial has **only** one stimulus associated with it')

    # assert np.all(stim_id_new.sum(axis=0) == 1)

    return stim_starts_new, stim_stops_new, stim_id_new


def put_data_on_diet(data):
    """
    Replaces large class variables with None

    Used to pass parameters of data creating to result of LDA (so that data can be re-created), but not larger variables
    to save space.

    Parameters
    ----------
    data: Read object

    Returns
    -------
    data: Read object
        Larger variables have been set to None
    """

    data.full_matrix = None
    data.full_2d_matrix = None
    data.indices = None
    data.times = None

    data.stim_id = None
    data.stim_id_appearance = None
    data.stim_id_relevant = None
    data.stim_starts = None
    data.stim_stops = None
    data.trial_counts = None
    data.trial_counts_b = None
    data.trial_counts_w = None
    data.trials = None

    return data


class Read_old(Read):

    def __init__(self, exp_no=3, dataset='/dualPhase3_posterior', brain_regions_to_include=[0], exclude_low_fr=False,
                 res=0.001, buffer=0, firing_rate_threshold=0.05,
                 flag_return_only_matrix=False, flag_force_create=True, flag_cluster=False):
        print(f'I am initialising the class Reader')

        # data set
        # *******************************************************************************************************
        self.exp_no = exp_no  # 3  # 1, 2, 3, 4
        self.dataset = dataset  # '/dualPhase3_posterior'
        self.direc_data = './data' + self.dataset + '/'
        self.direc_results = './results' + self.dataset + '/'
        if flag_cluster:
            self.direc_data = '/rds/general/user/ph416/home/lda/data' + self.dataset + '/'
            self.direc_results = '/rds/general/user/ph416/home/lda/results' + self.dataset + '/'
    
        # preprocessing parameters
        # *******************************************************************************************************
        self.brain_regions_to_include = brain_regions_to_include # 0 = only cortex at the moment
        self.exclude_low_fr = exclude_low_fr  # not yet used
        # self.only_onset = False  # for Sparse noise experiment - only look at start of trial or whole trial?
        self.res = res  # [s]
        self.buffer = buffer
        self.firing_rate_threshold = firing_rate_threshold

       
        # general flags
        # *******************************************************************************************************
        self.flag_return_only_matrix = flag_return_only_matrix
        self.flag_force_create = flag_force_create

    
    def read(self):
        """
        This is the main function of Reader. If called this function will
        - check for existing files
            if no file was found or flag_force_create is True, the following methods are called
                - load()
                - get_stimuli_info()
                - select_neurons()
                - filter_spikes()
                - make_spike_matrix()
            if file exists
                - load existing file()
        
        
        """
        # this is the first part of analysis where indices and times are turned into a binary spike matrix
        # this is also the part where neuron characteristics are saved
        print(f'read() should be in a generator, but it has to wait until it actually works :)')
        
        # check if data already exists
        flag_file_exists = False
        print(f'start checking_existence()')
        flag_file_exists, filename = self.check_existence(flag_file_exists)
        print(flag_file_exists)
        print(filename)
        
        
        if flag_file_exists == False or self.flag_force_create:
            
            # call function to load data dictionary
            print(f'start load()')
            self.load()
            
            # call function to get stimuli information
            print(f'start get_stimuli_info()')
            stim_starts, stim_stops = self.get_stimuli_info()
            
            # call function to get correct neurons
            print(f'start select_neurons()')
            self.neurons_good, self.neurons_good_depth, self.number_neurons = self.select_neurons()
            
            # call function to filter indices and times according to which neurons are selected
            print(f'start filter_spikes()')
            indices, times = self.filter_spikes()
            
             # call function to make full 2D matrix (no division of time into trials yet)
            print(f'start make_spike_2d_matrix()')
            self.make_2d_spike_matrix(indices, times)

            # call function to make full matrix
            print(f'start make_spike_matrix()')
            self.make_spike_matrix(indices, times, stim_starts, stim_stops)
                
            if self.flag_return_only_matrix:
                print('returning only matrix')
                return self.full_matrix

            
        else:
            print(f'file already exists, so existing file will be loaded and returned. \n'
                  f'If this is not the desired behaviour, set flag_force_create to True')
            data = self.load_existing(filename)
            
            if self.flag_return_only_matrix:
                print('returning only matrix')
                return data.full_matrix
            else:
                self.__dict__ = data


    def check_existence(self, flag_file_exists):
        reg = ''
        regions = [reg + '-' + str(i) for i in self.brain_regions_to_include]
        
        filename = f'{self.direc_data}exp{self.exp_no}_fullmatrix_region{regions[0]}_buf{self.buffer}_' \
                   f'thr{self.firing_rate_threshold}_res{self.res}.pickle'
                
        if os.path.exists(filename):
            flag_file_exists = True
        
        return flag_file_exists, filename
    
        
    def load(self):
        """
        loads the dictionary with the data into the instance
        does not need an argument except self
        does not return anything
        """
        self.d = pickle.load(open(f'{self.direc_data}data_exp{self.exp_no}.pickle', 'rb'))
        
        
    def load_existing(self, filename):
        """
        loads the existing data
        """
        reg = ''
        regions = [reg + '-' + str(i) for i in self.brain_regions_to_include]
        filename = f'{self.direc_data}exp{self.exp_no}_fullmatrix_region{regions[0]}_buf{self.buffer}_' \
                   f'thr{self.firing_rate_threshold}_res{self.res}.pickle'
        data = pickle.load(open(filename, 'rb'))
        return data.__dict__
        
        
    def get_stimuli_info(self):
        """
        documentation for get_stimuli_info
        :return:
        """
        self.exp_name = self.d['exp_name']
        self.exp_length = self.d['exp_length']
        # exp_start = self.d['exp_start']
        # exp_stop = self.d['exp_stop']
        
        stim_starts = self.d['stim_starts']
        stim_starts = np.floor(stim_starts * 1000) / 1000
        stim_stops = self.d['stim_stops']
        self.number_trials = len(stim_starts)
        self.avg_trial_length = np.round(np.mean(stim_stops - stim_starts), 3)
        
        # information about where and when squares were appearing
        self.stim_id = self.d['stim_id']
        self.stim_id = self.stim_id.reshape(self.stim_id.shape[0] * self.stim_id.shape[1], self.stim_id.shape[2])
        
        # from stim_id get info of when squares appeared
        # grid of 9 x 34 locations per trial - only keep 1 or -1 for the start of the stimulus
        self.stim_id_appearance = np.zeros(self.stim_id.shape)
        self.stim_id_appearance[:, 0] = self.stim_id[:, 0]
        # keep the 1 or -1 if the change went from 0 to 1/-1 not other way round (when square turned off)
        self.stim_id_appearance[:, 1:] = abs(self.stim_id[:, 1:]) * (self.stim_id[:, 1:] - self.stim_id[:, :-1])
    
        # check which trials actually have a new square appearing or disappearing
        self.stim_id_relevant = np.where(np.sum(abs(self.stim_id_appearance), axis=0) != 0)[0]
    
        self.trials = np.arange(0, self.stim_id_appearance.shape[0], 1)
        self.trial_counts = np.sum((self.stim_id_appearance != 0), axis=1)
        self.trial_counts_b = np.sum((self.stim_id_appearance == -1), axis=1)
        self.trial_counts_w = np.sum((self.stim_id_appearance == 1), axis=1)
        
        return stim_starts, stim_stops
        
        
    
    def select_neurons(self):
        """
        docstring
        look at overall firing rate and exclude neurons below certain count
        exclude either by
            - firing rate too low 0.1 Hz
            - total spike count is too low < trial types
        """
        # dictionary entries to keep in class
        neurons_good = self.d['neurons_good']
        number_neurons = len(neurons_good)
        neurons_good_depth = self.d['neurons_good_depth']
        brain_region_borders = self.d['brain_region_borders']
        # buffer_recording = self.d['buffer_recording']
        # max_buffer_around_trial_no_overlap = self.d['max_buffer_around_trial_no_overlap']
        
        indices = self.d['i']
        # quick check overall firing rate of neurons present in recording
        inds, counts = np.unique(indices, return_counts=True)
        assert sum(inds != neurons_good) == 0
        neurons_eligible = np.ones(number_neurons, dtype=bool)
    
        # ##### by location
        # only works if you want to include regions from cortex down, have not specified the rest yet
        region = max(self.brain_regions_to_include)
        # exclude all neurons outside region of interest
        neurons_eligible[np.where(neurons_good_depth <= brain_region_borders[region])[0]] = False
    
        # ##### by firing rate
        number_of_condition_types = min(self.trial_counts)
        if self.exp_name[0:6] == 'Sparse':
            count_threshold = self.firing_rate_threshold * self.exp_length
        else:
            count_threshold = max(self.firing_rate_threshold * self.exp_length, number_of_condition_types)
        # exclude all neurons with too low spike count
        neurons_eligible[np.where(counts <= count_threshold)[0]] = False
    
        # ##### apply exclusion criteria
        neurons_good = neurons_good[neurons_eligible]
        neurons_good_depth = neurons_good_depth[neurons_eligible]
        self.neurons_fr_overall = counts[neurons_eligible]
        # sort neurons according to depth (shallow first)
        sort_array = neurons_good_depth.argsort()
        sort_array = np.flipud(sort_array)
        neurons_good_depth = neurons_good_depth[sort_array]
        neurons_good = neurons_good[sort_array]
        self.neurons_fr_overall = self.neurons_fr_overall[sort_array]
        
        return neurons_good, neurons_good_depth, len(neurons_good)
        
        
        
    def filter_spikes(self):
        
        indices = self.d['i']
        times = self.d['t']
        
        # keep only neurons in relevant regions and whose firing rates are high enough
        # only keep entries in indices and times of those neurons
        keep_flag = np.zeros(len(indices), dtype=bool)
        for neuron in self.neurons_good:
            keep_flag[np.where(indices == neuron)[0]] = True
        indices = indices[keep_flag]
        times = times[keep_flag]
        # original_neurons, original_spike_counts = np.unique(indices, return_counts=True)
    
        return indices, times



    def make_spike_matrix(self, indices, times, stim_starts, stim_stops):
    
        stim_starts = self.d['stim_starts']
        stim_starts = np.floor(stim_starts * 1000) / 1000
        stim_stops = self.d['stim_stops']
        
        # calculate number of windows
        self.number_windows = int(round((self.avg_trial_length + 2 * self.buffer) / self.res))

        self.full_matrix = np.zeros((self.number_neurons, self.number_trials, self.number_windows), dtype=int)
    
        min_idx = 0
    
        for trial_idx, trial_start in enumerate(stim_starts):
    
            # find indices referring to times where this trial happens in arrays indices and times
            time_dyn_start = np.searchsorted(times[min_idx:], trial_start - self.buffer)
            time_dyn_stop = np.searchsorted(times[min_idx:], stim_stops[trial_idx] + self.buffer)
    
            ind_temp = indices[min_idx + time_dyn_start:min_idx + time_dyn_stop]
            tim_temp = times[min_idx + time_dyn_start:min_idx + time_dyn_stop]
    
            ind_temp_set = list(set(ind_temp))
            inds_temp_position_in_matrix = [np.where(self.neurons_good == i)[0][0] for i in ind_temp_set]
    
    
            min_idx += time_dyn_start
    
            for neuron_idx, neuron in enumerate(ind_temp_set):
                spikes_temp = tim_temp[ind_temp == neuron] - trial_start + self.buffer
                spikes_in_windows = (spikes_temp / self.res).astype(int)  # need to be aware, rounds down like floor()
                spikes_in_windows = spikes_in_windows[spikes_in_windows < self.number_windows]
    
                self.full_matrix[inds_temp_position_in_matrix[neuron_idx], trial_idx, spikes_in_windows] += 1
            # assert len(spikes_in_windows) == (len(set(spikes_in_windows)))
            
        print(f'Number of spikes happening within 1 ms of each other (discarded): '
              f'{len(indices) - np.sum(self.full_2d_matrix)}')
        self.sparsity = 100*(self.full_matrix > 0).sum()/self.full_matrix.size
        print(f'Sparsity = {self.sparsity} %')



    def make_2d_spike_matrix(self, indices, times):
        
        start = self.d['stim_starts'][0]
        stop = self.d['stim_stops'][-1]
        self.full_2d_matrix = np.zeros((self.number_neurons, int(np.round((stop-start)/self.res))), dtype=int)
        times_temp = times - start
        
        # for each neuron translate spike times into position in matrix
        for neuron_idx, neuron in enumerate(self.neurons_good):
            # get indices of all spikes from that neuron; times has already been cut properly
            spikes_temp = times_temp[indices == neuron]
            # convert spikes into indices for full matrix
            # need to be aware, rounds down like floor(), so we are also getting rid of spikes that happen
            # in the same millisecond: 85 spikes in this case
            spikes_inds = (spikes_temp / self.res).astype(int)
            self.full_2d_matrix[neuron_idx, spikes_inds] += 1
        
        print(f'Number of spikes happening within 1 ms of each other (discarded): '
              f'{len(indices) - np.sum(self.full_2d_matrix)}')
        self.sparsity = 100*(self.full_2d_matrix > 0).sum()/self.full_2d_matrix.size
        print(f'Sparsity = {self.sparsity} %')
        
        
        
    def save(self, filename):
        # this is where I use the parameters from self to save into the correct directory with the correct file name

        with open(filename, 'wb') as output:  # Overwrites any existing file.
            _pickle.dump(self, output, pickle.HIGHEST_PROTOCOL)


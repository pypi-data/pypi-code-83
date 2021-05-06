import numpy as np
import scipy.ndimage.filters as fi
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.signal import find_peaks

word_str_order = ['s+', 's-', 'c+', 'c-', 'i+', 'i-', 'on', 'of', 'sa']

class Translate:
    
    def __init__(self, data, response_delay=0, response_duration=0, visualise_overview=False):
        print('in Translate')
        self.data = data
        self.response_delay = response_delay
        self.response_duration = response_duration
        self.visualise_overview_flag = visualise_overview


    def translate(self, visualise_words=False):
        print(f'start make_doc_word_matrix()')
        self.make_doc_word_matrix()
        print(f'start create_vocabulary()')
        self.create_vocabulary()
        print(f'start create_corpus()')
        self.create_corpus()
        print(f'start create_neuron_word_matrix()')
        self.create_neuron_word_matrix()
        if visualise_words:
            print(f'start visualising neuron receptive fields & word receptive fields')
            self.visualise()
        if self.visualise_overview_flag:
            print('start making overview figure for this word')
            self.visualise_overview()
        
        
    def make_doc_word_matrix(self):
        print('Something went wrong. there is not proper way yet \n'
              'to create this word, please check in subclass')
        
    
    def get_relevant_matrix(self):
        # check that buffer on right hand side is big enough
        assert int(self.data.buffer / self.data.res) + self.response_delay + self.response_duration <= \
               self.data.full_matrix.shape[2]

        # calculate which columns from full_matrix i want to sum up for spike counts
        idx_left = int(self.data.buffer / self.data.res) + self.response_delay
        idx_right = idx_left + self.response_duration
        assert idx_right - idx_left == self.response_duration

        self.relevant_matrix = self.data.full_matrix[:, self.data.stim_id_relevant, :]
        self.relevant_spike_counts_per_trial = np.sum(self.relevant_matrix[:, :, idx_left:idx_right], axis=2)
        

    def create_corpus(self):
        # make corpus
        # *******************************************************************************************************
        # initialise list of lists of tuples
        self.corpus = []
        # make vectors of documents and for each document a tuple of the word index and the count
        for doc_idx in range(self.word_trial_binary_matrix.shape[1]):
            # get the non-zero elements of document
            idxes_of_words_in_doc = np.where(self.word_trial_binary_matrix[:, doc_idx] > 0)[0]
            tups = list(zip(idxes_of_words_in_doc, self.word_trial_binary_matrix[idxes_of_words_in_doc, doc_idx]))
            self.corpus.append(tups)
    
        self.vocab_dictionary = {}
        for word_idx in range(len(self.vocab)):
            self.vocab_dictionary[word_idx] = self.vocab[word_idx]
    
    
        # stats about corpus
        # *******************************************************************************************************
        # calculate average number of words per trial per trialtype
        self.sum_number_words_per_trialtype = np.empty((self.number_words, len(self.data.trials)))
        # of all trials keep the relevant ones (when new stim was shown) to extract which stim was shown when
        for trial_type in self.data.trials:
            # which trials had this stimulus?
            relev_trials = np.where(self.data.stim_id_appearance[trial_type, :] != 0)[0]
            # how many words appeared each time
            self.sum_number_words_per_trialtype[:, trial_type] = np.sum(self.word_trial_binary_matrix[:, relev_trials], axis=1)
    
        self.avg_number_words_per_trialtype = np.sum(self.sum_number_words_per_trialtype, axis=0) / self.data.trial_counts
        self.idx_docs_with_no_words = np.where(np.sum(self.word_trial_binary_matrix, axis=0) == 0)[0]

        # calculate how often each word appears in total
        self.word_occurances = np.sum(self.word_trial_binary_matrix, axis=1)
        
        
    def create_vocabulary(self):
        # create actual words with letters for LDA
        # *******************************************************************************************************
        self.vocab = []
        self.word_depths = np.empty(len(self.idx_to_use))
        for idx, word_idx in enumerate(self.idx_to_use):
            self.vocab.append(str(self.data.neurons_good[word_idx]) + self.word_str)
            # self.vocab.append(str(word_idx) + self.word_str)
            self.word_depths[idx] = self.data.neurons_good_depth[word_idx]

            
    def create_neuron_word_matrix(self):
        # this only works for single neuron words, ont if multiple neurons combine to make up a word
        self.neuron_word_matrix = np.zeros((self.data.number_neurons, len(self.idx_to_use)), dtype=int)
        self.neuron_word_matrix[self.idx_to_use, range(len(self.idx_to_use))] = 1


    def assign_trials_to_peaks(self, peaky_function, peak_thresh_diff):

        # ### the assignment works on the basis of finding the overlap between the peak (when it's above threshold)
        # ### and the trial time windows that completely enclose the peak

        # search again for peaks above threshold and with a minimum distance of 9
        peaks_above_thresh, _ = find_peaks(x=peaky_function, height=peak_thresh_diff, distance=9)
        peaks_above_thresh = np.array(peaks_above_thresh)

        signs = np.sign(peaky_function - peak_thresh_diff)
        # in the cases where the peaky function is exactly threshold, I replace the sign with a 1, because I only want to have one start time per peak
        signs[np.where(signs == 0)[0]] = 1
        sign_change = np.diff(signs)
        # get all places where a sign changes from -1 to 1 (diff > 0)
        all_peak_starts = np.where(sign_change > 0)[0]
        all_peak_ends = np.where(sign_change < 0)[0]

        # now go through each peak, find start and end time of each and assign trials accordingly
        inds_trials_above_thresh = []
        min_peak_halfwidth = 0.25 * int(self.data.avg_trial_length / self.data.res)
        last_trial_idx = 0

        for peak_idx, peak in enumerate(peaks_above_thresh):
            # peak_idx is the peak number; peak is the position of the peak in the peaky_function array (is also an index)

            # 0) find out where this peak started and ended
            peak_start = all_peak_starts[np.searchsorted(all_peak_starts, peak) - 1]
            peak_end = all_peak_ends[np.searchsorted(all_peak_ends, peak)]
            # could track where to start searching, but i am not in the mood

            # 1) check if there are multiple peaks - if yes, use the earlier/next minima as peak_start and peak_end
            if peak_idx > 0 and peaks_above_thresh[peak_idx - 1] > peak_start:
                # if there is another peak before this one
                temp_function = peaky_function[peaks_above_thresh[peak_idx - 1]:peak]
                # calculate where this function part is at a minimum;
                # relative index! starting from peaks_above_thresh[peak_idx - 1]
                peak_start_temp = np.where(temp_function == np.min(temp_function))[0]
                # check that there are not mutliple or no solutions
                if len(peak_start_temp) > 1:
                    # if there are more solutions, take the last one
                    peak_start = peaks_above_thresh[peak_idx - 1] + peak_start_temp[-1]
                elif len(peak_start_temp) == 0:
                    print(
                        'did not find minimum between peaks, this should not happen; peak {peak, peak+idx {peak_idx}}')
                    peak_start = peak - min_peak_halfwidth

            elif peak_idx < len(peaks_above_thresh) - 1 and peaks_above_thresh[peak_idx + 1] < peak_end:
                # if there is another peak after this one
                temp_function = peaky_function[peak:peaks_above_thresh[peak_idx + 1]]
                peak_end_temp = np.where(temp_function == np.min(temp_function))[0]
                # check that there are not mutliple or no solutions
                if len(peak_end_temp) > 1:
                    peak_end = peak + peak_end_temp[0]
                elif len(peak_end_temp) == 0:
                    print(
                        'did not find minimum between peaks, this should not happen; peak {peak, peak+idx {peak_idx}}')
                    peak_end = peak + min_peak_halfwidth

            # 2) check peak duration relative to response duration
            if peak_end - peak_start > self.response_duration:
                # peak duration is longer than response_duration
                # check which tail is longer and cut
                if peak - peak_start > 2 * min_peak_halfwidth and peak_end - peak < 2 * min_peak_halfwidth:
                    # if both of them are longer than half the avg_trial_length, cut both of them, but more at start
                    peak_start = peak - min_peak_halfwidth
                    peak_end = peak + 2 * min_peak_halfwidth
                elif peak - peak_start > 2 * min_peak_halfwidth:
                    # if left tail is the longer one, cut it to half
                    peak_start = peak - 2 * min_peak_halfwidth
                elif peak_end - peak > 2 * min_peak_halfwidth:
                    # if right tail is the longer one, cut it to half
                    peak_end = peak + 2 * min_peak_halfwidth
            else:
                # peak duration is smaller than response duration, need to check if it's too narrow and adjust accordingly
                if peak - peak_start < min_peak_halfwidth:
                    peak_start = peak - min_peak_halfwidth
                if peak_end - peak < min_peak_halfwidth:
                    peak_end = peak + min_peak_halfwidth

            # 3) calculate overlap of peak (peak_end - peak_start) with trials
            # find trials happening in the time window peak_end - response_duration - delay to peak_start
            start_search = self.data.res * (peak_end - self.response_delay - self.response_duration)
            end_search = self.data.res * peak_start
            min_trial_idx = last_trial_idx + np.searchsorted(self.data.stim_starts[last_trial_idx:], start_search)
            max_trial_idx = last_trial_idx + np.searchsorted(self.data.stim_starts[last_trial_idx:], end_search)

            # make sure that there are trials in this time period, if not, soften up search
            if min_trial_idx == last_trial_idx:
                # no new trial starts were found
                if peak - peak_start >= peak_end - peak:
                    # there is a longer tail before the peak: soften up end_search
                    peak_start = peak - min_peak_halfwidth
                    end_search = self.data.res * peak_start
                    max_trial_idx = last_trial_idx + np.searchsorted(self.data.stim_starts[last_trial_idx:], end_search)
                elif peak - peak_start <= peak_end - peak:
                    # there is a longer tail after the peak: soften up start_search
                    peak_end = peak + min_peak_halfwidth
                    start_search = self.data.res * (peak_end - self.response_delay - self.response_duration)
                    min_trial_idx = last_trial_idx + np.searchsorted(self.data.stim_starts[last_trial_idx:],
                                                                     start_search)
            elif max_trial_idx - min_trial_idx > 10:
                print('finding more than 10 start times, should not be possible...')

            # 4) Collect all trials which could have been responsible for this peak
            for trial_idx in range(min_trial_idx, max_trial_idx):
                inds_trials_above_thresh.append(trial_idx)

            # reset the last_trial_idx to the earliest trial found for this peak
            last_trial_idx = min_trial_idx

        return inds_trials_above_thresh



    def visualise(self):
        # for each neuron, visualise
        # - for b, w, a squares: number of spikes on average for a square shown at a particular location
        # - for b, w, a squares: how often a word came up when the square was at this location

        # need to get a stim_id (location) vector in the same size as 2d_full_matrix.
        stim_2d = np.zeros((self.data.stim_id.shape[0], self.data.full_2d_matrix.shape[1]))
        start_inds = (self.data.stim_starts/self.data.res).astype(int)

        for trial_idx, start_ind in enumerate(start_inds):
            # find which squares appear and add ones for the next 160 time steps (at 0.001s resolution)
            locs = np.where(self.data.stim_id_appearance[:, trial_idx] != 0)[0]
            colours = self.data.stim_id_appearance[locs, trial_idx]

            if len(locs) > 0:
                for loc_idx, loc in enumerate(locs):
                    stim_2d[loc, start_ind:start_ind + (self.data.avg_trial_length/self.data.res).astype(int)] += \
                        colours[loc_idx]

        # we have a response delay of 20 ms or whatever the input is. Add in this delay
        stim_2d_del = np.zeros((self.data.stim_id.shape[0], self.data.full_2d_matrix.shape[1]))
        if self.response_delay > 0:
            stim_2d_del[:, self.response_delay:] = stim_2d[:, 0:-self.response_delay]
        else:
            stim_2d_del = stim_2d

        # plt.figure();
        # sns.heatmap(stim_2d_del[:, 20].reshape(9, 34), vmin=-1, vmax=1, cmap='Greys_r')
        # plt.show()

        # how often was a square shown at a particular location
        present_bnw = abs(np.sum(abs(stim_2d), axis=1)/(self.data.avg_trial_length/self.data.res))
        present_b = abs(np.sum(stim_2d*(stim_2d < 0), axis=1)/(self.data.avg_trial_length/self.data.res))
        present_w = abs(np.sum(stim_2d*(stim_2d > 0), axis=1)/(self.data.avg_trial_length/self.data.res))
        assert np.sum(present_w + present_b - present_bnw) == 0

        # fastest way I can think of to sum up the spikes happening in each time window is a dot product
        # between the binned spike train and the times when a specific square was present.
        spikes_per_loc_w = np.dot(abs(stim_2d_del) * (stim_2d_del > 0),
                                  self.data.full_2d_matrix.transpose()).transpose()
        spikes_per_loc_b = np.dot(abs(stim_2d_del) * (stim_2d_del < 0),
                                  self.data.full_2d_matrix.transpose()).transpose()
        spikes_per_loc_bnw = np.dot(abs(stim_2d_del), self.data.full_2d_matrix.transpose()).transpose()

        # for word occurrances
        assert self.data.stim_id_appearance.shape[1] == self.word_trial_binary_matrix.shape[1]

        word_occs_per_loc_w = np.dot(self.word_trial_binary_matrix,
                                     abs(self.data.stim_id_appearance*(self.data.stim_id_appearance > 0)).transpose())
        word_occs_per_loc_b = np.dot(self.word_trial_binary_matrix,
                                     abs(self.data.stim_id_appearance*(self.data.stim_id_appearance < 0)).transpose())
        word_occs_per_loc_bnw = np.dot(self.word_trial_binary_matrix,
                                       abs(self.data.stim_id_appearance).transpose())

        # go through neurons with word only
        for idx, neuron_idx in enumerate(self.idx_to_use):

            # plot spikes of each neuron
            vmax = np.max(np.array([np.max(spikes_per_loc_w[neuron_idx, :]/present_w),
                                    np.max(spikes_per_loc_b[neuron_idx, :]/present_b),
                                    np.max(spikes_per_loc_bnw[neuron_idx, :]/present_bnw)]))
            vmin = np.min(np.array([np.min(spikes_per_loc_w[neuron_idx, :]/present_w),
                                    np.min(spikes_per_loc_b[neuron_idx, :]/present_b),
                                    np.min(spikes_per_loc_bnw[neuron_idx, :]/present_bnw)]))

            n_subplots_x = 3
            n_subplots_y = self.n_neurons_contributing_to_word

            def plot_one_row(n_subplots_y, n_subplots_x, neuron_idx, vmax, subplot_idx, str_neuronword, str_label,
                             spikes_per_loc_w, spikes_per_loc_b, spikes_per_loc_bnw):

                plt.subplot(n_subplots_y, n_subplots_x, subplot_idx + 1)
                plt.title(f'{str_neuronword} - white square')
                axw = sns.heatmap((spikes_per_loc_w[neuron_idx, :] / present_w).reshape(9, 34), vmin=0, vmax=vmax,
                                  cmap='viridis', cbar_kws={'label': str_label})
                axw.invert_yaxis()

                plt.subplot(n_subplots_y, n_subplots_x, subplot_idx + 2)
                plt.title(f'{str_neuronword} - black square')
                axb = sns.heatmap((spikes_per_loc_b[neuron_idx, :] / present_b).reshape(9, 34), vmin=0, vmax=vmax,
                                  cmap='viridis', cbar_kws={'label': str_label})
                axb.invert_yaxis()

                plt.subplot(n_subplots_y, n_subplots_x, subplot_idx + 3)
                plt.title(f'{str_neuronword} - either colour')
                axbnw = sns.heatmap((spikes_per_loc_bnw[neuron_idx, :] / present_bnw).reshape(9, 34), vmin=0, vmax=vmax,
                                    cmap='viridis', cbar_kws={'label': str_label})
                axbnw.invert_yaxis()


            plt.figure(figsize=(12, 5))

            plt.suptitle(f'neuron {neuron_idx} -> word {str(self.data.neurons_good[neuron_idx]) + self.word_str}')

            subplot_idx = 0
            for row_idx in range(n_subplots_y):

                if row_idx < n_subplots_y - 1:
                    # top rows --- only neurons

                    # TODO NEED TO FIX NUERON IDX!! IS FROM IDX TO USE, NOT FROM INDS_1 ETC!!
                    str_neuronword='neuron'
                    str_label = 'avg nr spikes'
                    plot_one_row(n_subplots_y=n_subplots_y, n_subplots_x=n_subplots_x, neuron_idx=neuron_idx,
                                 vmax=vmax, subplot_idx=subplot_idx, str_neuronword=str_neuronword, str_label=str_label,
                                 spikes_per_loc_w=spikes_per_loc_w,
                                 spikes_per_loc_b=spikes_per_loc_b,
                                 spikes_per_loc_bnw=spikes_per_loc_bnw)
                    subplot_idx += n_subplots_x
                else:
                    # last row --- word receptive field
                    str_neuronword='word'
                    str_label = 'prob of word'
                    plot_one_row(n_subplots_y=n_subplots_y, n_subplots_x=n_subplots_x, neuron_idx=idx,
                                 vmax=1, subplot_idx=subplot_idx, str_neuronword=str_neuronword, str_label=str_label,
                                 spikes_per_loc_w=word_occs_per_loc_w,
                                 spikes_per_loc_b=word_occs_per_loc_b,
                                 spikes_per_loc_bnw=word_occs_per_loc_bnw)
                    subplot_idx += n_subplots_x


            plt.tight_layout()
            plt.subplots_adjust(top=0.8)

            plt.savefig(f'{self.data.figures_path}'
                        f'word{str(neuron_idx)+self.word_str}_'
                        f'{self.word_name}'
                        f'spikes_and_words_per_loc_'
                        f'del{self.response_delay}_dur{self.response_duration}.png')
            plt.close()




    def visualise_overview(self):
        # provide overview figure showing for all words:
        # - number of spikes of the underlying neuron
        # - number of words per underlying neuron
        # - number of words per location (b, w, all) in heatmap and

        word_occs_per_loc_w = np.dot(self.word_trial_binary_matrix,
                                     abs(self.data.stim_id_appearance * (self.data.stim_id_appearance > 0)).transpose())
        word_occs_per_loc_b = np.dot(self.word_trial_binary_matrix,
                                     abs(self.data.stim_id_appearance * (self.data.stim_id_appearance < 0)).transpose())
        word_occs_per_loc_bnw = np.dot(self.word_trial_binary_matrix, abs(self.data.stim_id_appearance).transpose())

        sns.set_style("white")

        plt.figure(figsize=(8, 7.5))
        plt.suptitle(f'Overview word: {self.word_name} \n'
                     f'delay = {self.response_delay}, duration = {self.response_duration}')

        ax0 = plt.subplot(3, 1, 1)
        ax0.plot(range(self.data.number_neurons), np.sum(self.data.full_2d_matrix, axis=1), '.-', color='C1')
        ax0.set_xlabel('neuron id')
        ax0.set_ylabel('# spikes', color='C1')
        ax1 = ax0.twinx()
        if len(self.idx_to_use) == self.data.number_neurons:
            ax1.plot(np.sum(self.word_trial_binary_matrix, axis=1), '.', color='C0')
        else:
            ax1.plot(self.idx_to_use, np.sum(self.word_trial_binary_matrix, axis=1), '.', color='C0')
        ax1.set_ylabel('# words', color='C0')

        plt.subplot(3, 2, 3)
        plt.title(f'both colours')
        ax2 = sns.heatmap(np.sum(word_occs_per_loc_bnw, axis=0).reshape(9, 34), cmap='viridis')
        ax2.invert_yaxis()

        plt.subplot(3, 2, 4)
        plt.title(f'white square')
        ax3 = sns.heatmap(np.sum(word_occs_per_loc_w, axis=0).reshape(9, 34), cmap='viridis')
        ax3.invert_yaxis()

        plt.subplot(3, 2, 6)
        plt.title(f'black square')
        ax4 = sns.heatmap(np.sum(word_occs_per_loc_b, axis=0).reshape(9, 34), cmap='viridis')
        ax4.invert_yaxis()

        plt.subplot(3, 2, 5)
        ax5 = sns.boxplot(x=['both', 'white', 'black'], y=[np.sum(word_occs_per_loc_bnw, axis=0),
                                                           np.sum(word_occs_per_loc_w, axis=0),
                                                           np.sum(word_occs_per_loc_b, axis=0)],
                          palette='viridis')
        ax5.set_ylabel('number of words')

        plt.tight_layout()
        plt.subplots_adjust(top=0.9)

        plt.savefig(f'{self.data.figures_path}'
                    f'{self.word_name}_overview_'
                    f'perc{self.percentile_threshold}'
                    f'del{self.response_delay}_dur{self.response_duration}.pdf')
        plt.close()


        
class TranslateFRchange(Translate):
    
    def __init__(self, data, response_delay=0, response_duration=0, percentile_threshold=20, visualise_overview=False):
        
        super().__init__(data, response_delay, response_duration, visualise_overview)
        print('in TranslateFRincrease')
        self.percentile_threshold = percentile_threshold
        if self.percentile_threshold < 50:
            self.word_str = 's-'
            self.word_name = f'FRDs_p{self.percentile_threshold}'
        else:
            self.word_str = 's+'
            self.word_name = f'FRIs_p{self.percentile_threshold}'
        self.n_neurons_contributing_to_word = 1

        
    def make_doc_word_matrix(self):
        # only select the trials in which a new square was shown
        # need to make selection now because otherwise the trials with no new square come into the calculation
        # of the percentiles, which I do not want
        # only select the trials in which a new square was shown

        # to count spikes per trial, need to define which part of the trial we should look at
        # need to take into account buffer, response_delay, response_duration
        # this is then flexible for example to deal with onset
        
        relevant_spike_counts_per_trial = self.get_spike_counts_per_trial()

        self.threshold_of_counts_to_consider = np.empty(self.data.number_neurons)
        for neuron_idx in range(self.data.number_neurons):
            self.threshold_of_counts_to_consider[neuron_idx] = np.percentile(
                relevant_spike_counts_per_trial[neuron_idx, :], self.percentile_threshold)
            
        change_fr_words = np.zeros(relevant_spike_counts_per_trial.shape, dtype=int)

        for neuron_idx in range(self.data.number_neurons):
            if self.percentile_threshold < 50:
                change_fr_idx = np.where(relevant_spike_counts_per_trial[neuron_idx, :] <
                                         self.threshold_of_counts_to_consider[neuron_idx])[0]
            else:
                change_fr_idx = np.where(relevant_spike_counts_per_trial[neuron_idx, :] >
                                         self.threshold_of_counts_to_consider[neuron_idx])[0]
            change_fr_words[neuron_idx, change_fr_idx] = 1

        print(f'n words appearing = {sum(np.sum(change_fr_words, axis=1) != 0)}')
        print(f'n words not appearing = {sum(np.sum(change_fr_words, axis=1) == 0)}')

        self.number_words = change_fr_words.shape[0] - sum(np.sum(change_fr_words, axis=1) == 0)

        # create words-documents binary matrix
        # *******************************************************************************************************
        # see for which indices a word appears more than 0 times
        self.idx_to_use = np.where(np.sum(change_fr_words, axis=1) != 0)[0]
        self.word_trial_binary_matrix = change_fr_words[self.idx_to_use, :]
    
    
    def get_spike_counts_per_trial(self):
        
        # initialise the number of spikes per neuron per trial
        relevant_spike_counts_per_trial = np.zeros((self.data.number_neurons, self.data.number_trials), dtype=int)
        
        # loop through start times of trials (already relative to first trial start and beginning of matrix)
        for trial_idx, t_stimstart in enumerate(self.data.stim_starts):
            
            # check which spikes happened during that time period.
            # t_stimstart is in [s], so I need to convert this into ms because response_delay is in ms
            ind_t_start = int(t_stimstart/self.data.res) + self.response_delay
            ind_t_stop = ind_t_start + self.response_duration
            
            # take sum and put into matrix
            relevant_spike_counts_per_trial[:, trial_idx] = np.sum(self.data.full_2d_matrix[:, ind_t_start:ind_t_stop], axis=1)
        
        
        return relevant_spike_counts_per_trial


class TranslateFRincrConv(Translate):

    def __init__(self, data, w_small=40, w_large=160, response_delay=10, response_duration=160, percentile_threshold=65,
                 visualise_overview=False):

        super().__init__(data, response_delay, response_duration, visualise_overview)

        print('in TranslateFRincrConv')
        self.percentile_threshold = percentile_threshold
        self.w_small = w_small
        self.w_large = w_large
        self.response_duration = response_duration
        self.response_delay = response_delay
        self.word_str = f'c+'
        self.word_name = f'FRIc_w{self.w_small}_{self.w_large}'
        self.n_neurons_contributing_to_word = 1

    def make_doc_word_matrix(self):

        # define word_trial binary matrix - will fill one at a time
        # self.word_trial_binary_matrix = np.zeros((self.data.number_neurons, len(self.data.stim_id_relevant)), dtype=int)
        word_trial_temp = np.zeros((self.data.number_neurons, len(self.data.stim_id_relevant)), dtype=int)
        n_peaks_orig = np.zeros(self.data.number_neurons)
        n_peaks_final = np.zeros(self.data.number_neurons)

        for neuron_idx in range(self.data.number_neurons):

            # convolve spike trains
            conv_wsmall = fi.gaussian_filter(self.data.full_2d_matrix[neuron_idx, :].astype(float), sigma=self.w_small)
            conv_wlarge = fi.gaussian_filter(self.data.full_2d_matrix[neuron_idx, :].astype(float), sigma=self.w_large)

            # take difference (and flip depending on whether I want decrease or increase)
            if self.percentile_threshold > 50:
                diff_convs = conv_wsmall - conv_wlarge
            else:
                diff_convs = - (conv_wsmall - conv_wlarge)
            word_str = f'diff{self.w_small}_{self.w_large}'

            # get indices of where difference of convolved spike trains has local maxima
            # local_max_diff_inds = self.get_local_max(a=diff_convs)
            local_max_diff_inds, _ = find_peaks(x=diff_convs)
            local_max_diff_inds = np.array(local_max_diff_inds)
            local_max_diff = local_max_diff_inds*self.data.res

            # determine threshold
            # need to now filter which maxima are significant or not
            peak_thresh_diff = np.percentile(diff_convs[local_max_diff_inds], self.percentile_threshold)

            # go through found peaks and assign trials
            # enumerate over the indices for a (local_max_diff_inds) where local maxima where the height of a (diff) is above threshold
            peaks_above_thresh = local_max_diff_inds[diff_convs[local_max_diff_inds] > peak_thresh_diff]


            inds_trials_above_thresh = self.assign_trials_to_peaks(peaky_function=diff_convs, 
                                                                   peak_thresh_diff=peak_thresh_diff)

            # print(f' neuron {neuron_idx}: '
            #       f'n_peaks={len(local_max_diff_inds)}, '
            #       f'n_peaks after perc={len(peaks_above_thresh)}, '
            #       f'n_trials associated={len(inds_trials_above_thresh)}'
            #       f'    ----    factor={len(inds_trials_above_thresh)/len(peaks_above_thresh)}')

            plt.figure()
            plt.hist(diff_convs, bins=100)
            plt.title(f'neuron {neuron_idx}')
            plt.close()


            # fill word_trial_binary_matrix
            word_trial_temp[neuron_idx, inds_trials_above_thresh] = 1

            n_peaks_orig[neuron_idx] = len(local_max_diff_inds)
            n_peaks_final[neuron_idx] = len(peaks_above_thresh)


        # idx_to_use - which neurons to include in vocabulary
        self.idx_to_use = np.where(np.sum(word_trial_temp, axis=1) != 0)[0]
        self.number_words = len(self.idx_to_use)
        self.word_trial_binary_matrix = word_trial_temp[self.idx_to_use, :]

        self.n_peaks_orig = n_peaks_orig
        self.n_peaks_final = n_peaks_final


class TranslateFRdecrConv(Translate):

    def __init__(self, data, w=20, nonzero_threshold=50, factor=0.8, factor_ml=10, response_delay=10, response_duration=160, percentile_threshold=65,
                 visualise_overview=False):

        super().__init__(data, response_delay, response_duration, visualise_overview)

        print('in TranslateFRchangeConv')
        self.percentile_threshold = percentile_threshold
        self.w = w
        self.response_duration = response_duration
        self.response_delay = response_delay
        if nonzero_threshold < 50:
            print('nonzero threshold is set lower than 50%, this is unusual, please be sure that you meant this.')
        self.nonzero_threshold = nonzero_threshold/100
        self.factor = factor
        self.factor_ml = factor_ml

        self.word_str = f'c-'
        self.word_name = f'FRDc_w{self.w}'
        self.n_neurons_contributing_to_word = 1

    def make_doc_word_matrix(self):

        # define word_trial binary matrix - will fill one at a time
        # self.word_trial_binary_matrix = np.zeros((self.data.number_neurons, len(self.data.stim_id_relevant)), dtype=int)
        word_trial_temp = np.zeros((self.data.number_neurons, len(self.data.stim_id_relevant)), dtype=int)
        n_peaks_orig = np.zeros(self.data.number_neurons)
        n_peaks_final = np.zeros(self.data.number_neurons)

        for neuron_idx in range(self.data.number_neurons):

            # convolve spike train
            conv = fi.gaussian_filter(self.data.full_2d_matrix[neuron_idx, :].astype(float), sigma=self.w)

            # ### check whether the array is non-zeros for more than 50% (or threshold given) of time
            perc_nonzero_conv = (len(conv) - np.sum(conv == 0)) / len(conv)

            plt.figure()
            plt.hist(conv, bins=100)
            plt.title(f'neuron {neuron_idx}')
            plt.close()

            if perc_nonzero_conv < self.nonzero_threshold:
                # leave zeros as they are - no FRdecreased words for this neuron

                pass
            else:

                # ### 1) calculate how long the zero intervals are and get their starts and ends
                ranges = self.zero_runs(conv)
                zerotimes_lengths = self.data.res * (ranges[:, 1] - ranges[:, 0])
                # check that all intervals are positive and larger than 0
                assert np.all(zerotimes_lengths > 0)

                # ### exclude zero intervals that are
                # ### a. very short or
                # ### b. lower than a certain threshold


                # ### 2) filter out some intervals
                keep_array = np.ones(len(zerotimes_lengths), dtype=bool)
                # print(f'neuron {neuron_idx}')
                # print(sum(keep_array))

                # a. exclude intervals that are too short (shorter than one trial duration*factor)
                # if factor = 0, then all intervals stay selected
                keep_array[np.where(zerotimes_lengths < self.data.res*self.response_duration*self.factor)[0]] = False
                # print(f'{sum(keep_array)} after excluding intervals shorter than {self.factor}*response_duration')

                # exclude intervals that are longer than x s
                keep_array[np.where(zerotimes_lengths > self.data.res*self.response_duration*self.factor_ml)[0]] = False
                # print(f'{sum(keep_array)} after excluding intervals longer than {self.factor_ml}*response_duration')

                # b. calculate where the cutoff should be according to percentile and keep only longer zero intervals
                perc = np.percentile(zerotimes_lengths, self.percentile_threshold)
                keep_array[np.where(zerotimes_lengths < self.data.res*perc)[0]] = False
                # print(f'{sum(keep_array)} after excluding intervals shorter than {perc} (percentile)')

                # filter
                ranges = ranges[keep_array, :]

                # ### get trials assigned to zero intervals
                inds_trials_above_thresh = self.assign_trials_zero_intervals(ranges=ranges)


                # print(f' neuron {neuron_idx}: '
                #       f'n_peaks={len(zerotimes_lengths)}, '
                #       f'n_peaks after perc={len(ranges)}, '
                #       f'n_trials associated={len(inds_trials_above_thresh)}'
                #       f'    ----    factor={len(inds_trials_above_thresh)/len(ranges)}')


                # spikes = np.where(self.data.full_2d_matrix[neuron_idx, :] > 0)[0] * self.data.res
                #
                # plt.figure()
                # plt.suptitle(f'neuron {neuron_idx}')
                #
                # ax1 = plt.subplot(3, 1, 1)
                # ax1.plot(spikes, np.ones(len(spikes)), '.', color='k', label='spikes')
                # for trial_idx, start in enumerate(self.data.stim_starts[inds_trials_above_thresh]):
                #     ax1.axvline(x=start, linestyle='--', color='blue', linewidth=0.75)
                #
                # ax2 = plt.subplot(3, 1, 2, sharex=ax1)
                # ax2.plot(np.arange(0, len(conv) * self.data.res, self.data.res), conv, color='C0', label='w20')
                # ax2.set_xlim([200, 205])
                #
                # ax3 = plt.subplot(3, 1, 3)
                # ax3.hist(zerotimes_lengths, bins=100)
                # ax3.axvline(x=perc, color='k', linestyle='--')
                # ax3.axvline(x=min(zerotimes_lengths[keep_array]), color='gold', linestyle='--')
                # ax3.axvline(x=max(zerotimes_lengths[keep_array]), color='gold', linestyle='--')
                # plt.show()



                # fill word_trial_binary_matrix
                word_trial_temp[neuron_idx, inds_trials_above_thresh] = 1

                n_peaks_orig[neuron_idx] = len(zerotimes_lengths)
                n_peaks_final[neuron_idx] = len(ranges)

        # idx_to_use - which neurons to include in vocabulary
        self.idx_to_use = np.where(np.sum(word_trial_temp, axis=1) != 0)[0]
        self.number_words = len(self.idx_to_use)
        self.word_trial_binary_matrix = word_trial_temp[self.idx_to_use, :]

        self.n_peaks_orig = n_peaks_orig
        self.n_peaks_final = n_peaks_final


    def zero_runs(self, a):
        # Create an array that is 1 where a is 0, and pad each end with an extra 0.
        iszero = np.concatenate(([0], np.isclose(a, 0, atol=0.0001).view(np.int8), [0]))
        absdiff = np.abs(np.diff(iszero))
        # Runs start and end where absdiff is 1.
        ranges = np.where(absdiff == 1)[0].reshape(-1, 2)
        return ranges


    def assign_trials_zero_intervals(self, ranges):

        # instantiate list of indices to pass back
        inds_trials_above_thresh = []
        last_trial_idx = 0

        # ### for each interval (from ranges), check what trials overlap

        for intv_idx in range(len(ranges)):

            # get start and end of interval
            peak_start = ranges[intv_idx, 0]
            peak_end = ranges[intv_idx, 1]

            # find idx of first trial that happened after peak_start - response_delay
            start_search = self.data.res * (peak_start - self.response_delay)
            # add correction for convolution pushing start time of zero interval to the right
            start_search -= self.data.res * self.w * 2

            # find idx of last trial that happened before peak_end - response_delay - factor*response_duration
            end_search = self.data.res * (peak_end - self.response_delay - self.factor*self.response_duration)
            # add correction for convolution pushing start time of spike to the left
            end_search += self.data.res * self.w * 2

            # append all these indices to list
            min_trial_idx = last_trial_idx + np.searchsorted(self.data.stim_starts[last_trial_idx:], start_search)
            max_trial_idx = last_trial_idx + np.searchsorted(self.data.stim_starts[last_trial_idx:], end_search)

            for trial_idx in range(min_trial_idx, max_trial_idx):
                inds_trials_above_thresh.append(trial_idx)

            # reset the last_trial_idx to the earliest trial found for this peak
            last_trial_idx = min_trial_idx

        return inds_trials_above_thresh







class TranslateSimulAct(Translate):

    def __init__(self, data, response_delay=10, response_duration=160, percentile_threshold=65, t_c=2, furthest_overlap=2,
                 min_n_peaks_thresh=25, conv_w=20, visualise_overview=False):

        super().__init__(data, response_delay, response_duration, visualise_overview)

        print('in TranslateSimulAct')
        self.percentile_threshold = percentile_threshold
        self.response_duration = response_duration
        self.response_delay = response_delay
        self.t_c = t_c
        self.furthest_overlap = furthest_overlap
        self.min_n_peaks_thresh = min_n_peaks_thresh
        self.conv_w = conv_w

        self.word_str = f'sa'
        self.word_name = f'SA'
        self.n_neurons_contributing_to_word = 2


    def make_doc_word_matrix(self):

        # 1) filter spike trains with exponential function (small t_c) (all spike trains in full_2d_matrix)

        kernel_len = self.t_c * 20
        x = np.arange(0, kernel_len, 1)
        exponential = np.exp(-x / self.t_c)

        conv_full2dmatrix = np.zeros((self.data.full_2d_matrix.shape[0],
                                      self.data.full_2d_matrix.shape[1] + kernel_len - 1))
        for neuron_idx in range(self.data.number_neurons):
            conv_full2dmatrix[neuron_idx, :] = np.convolve(self.data.full_2d_matrix[neuron_idx, :], exponential)

        # 1.5) filter beforehand pairs for which it makes sense to calculate correlation?
        print('calculating dot product (may take a while)')
        overlap_dotprod, n_pairs_to_check_peaks = self.get_candidates()

        # 2) calculate crosscorrelation (multiply the two) - done in double loop

        # instantiate variables
        inds_1 = np.zeros(n_pairs_to_check_peaks, dtype=int)
        inds_2 = np.zeros(n_pairs_to_check_peaks, dtype=int)

        word_trial_binary_matrix = np.zeros((n_pairs_to_check_peaks, len(self.data.stim_id_relevant)),dtype=int)

        n_words_per_word = np.zeros(n_pairs_to_check_peaks, dtype=int)
        n_simspikes_per_word = np.zeros(n_pairs_to_check_peaks, dtype=int)

        word_idx = 0

        for i in range(self.data.number_neurons):
            
            if i % 20 == 0:
                print(f'starting neuron {i}')

            for j in range(i + 1, self.data.number_neurons):

                if overlap_dotprod[i, j] > self.overlap_thresh:

                    inds_1[word_idx] = i
                    inds_2[word_idx] = j
                    word_str = f'simil{i}_{j}'
                    # word_idx += 1

                    # multiply the two spike traces with each other
                    crosscorr = conv_full2dmatrix[i, :] * conv_full2dmatrix[j, :]

                    # 3) smooth out curve
                    conv_crosscorr = fi.gaussian_filter(crosscorr, sigma=20)

                    # 4) find peaks

                    # get indices of where curve has local maxima
                    # local_max_diff_inds = self.get_local_max(a=conv_crosscorr)
                    local_max_diff_inds, _ = find_peaks(x=conv_crosscorr)
                    local_max_diff_inds = np.array(local_max_diff_inds)
                    
                    # determine threshold
                    # need to now filter which maxima are significant or not
                    peak_thresh_diff = np.percentile(conv_crosscorr[local_max_diff_inds],
                                                     self.percentile_threshold)
                    
                    # # make sure that peak_thresh_diff is at least higher than 0.15* highest peak
                    # if peak_thresh_diff < 0.15*max(conv_crosscorr[local_max_diff_inds]):
                    #     print(f'need to raise thresh n1 = {i} n2 = {j} '
                    #           f'from {np.round(peak_thresh_diff, 4)} '
                    #           f'to {np.round(0.15*max(conv_crosscorr[local_max_diff_inds]), 4)} '
                    #           f'by {np.round(0.15*max(conv_crosscorr[local_max_diff_inds]) - peak_thresh_diff, 4)}')
                    # peak_thresh_diff = max(0.15*max(conv_crosscorr[local_max_diff_inds]), peak_thresh_diff)

                    # go through found peaks and assign trials
                    # enumerate over the indices for a (local_max_diff_inds) where local maxima where the height of a (diff) is above threshold
                    peaks_above_thresh = local_max_diff_inds[
                        conv_crosscorr[local_max_diff_inds] > peak_thresh_diff]

                    # only continue if there are enough peaks above threshold!!

                    if len(peaks_above_thresh) > self.min_n_peaks_thresh:

                        inds_trials_above_thresh = self.assign_trials_to_peaks(peaky_function=conv_crosscorr,
                                                                               peak_thresh_diff=peak_thresh_diff)
                        
                        # plt.figure(figsize=(12, 6))
                        # plt.title(f'n {i} & n {j}, n_peaks={len(local_max_diff_inds)}, '
                        #           f'npeaksabovethresh = {len(peaks_above_thresh)}, '
                        #           f'n_words={len(inds_trials_above_thresh)}')
                        # plt.hist(conv_crosscorr[local_max_diff_inds], bins=50)
                        # plt.axvline(x=peak_thresh_diff)
                        # plt.show()
                        
                        

                        # fill word_trial_binary_matrix
                        word_trial_binary_matrix[word_idx, inds_trials_above_thresh] = 1

                        # optional plot for each word
                        visualise_each_word = False
                        if visualise_each_word:
                            plt.figure(figsize=(10, 7))
                            ax1 = plt.subplot(2, 1, 1)
                            plt.title(f'neuron {i} & neuron {j}, t_c={self.t_c}')
                            plt.plot(np.where(self.data.full_2d_matrix[i, :] > 0)[0],
                                     -0.15 + np.zeros(len(np.where(self.data.full_2d_matrix[i, :] > 0)[0])), '.', color='C0')
                            plt.plot(np.where(self.data.full_2d_matrix[j, :] > 0)[0],
                                     -0.3 + np.zeros(len(np.where(self.data.full_2d_matrix[j, :] > 0)[0])), '.', color='C1')
                            plt.plot(conv_full2dmatrix[i, :], 'C0', label='neuron 1')
                            plt.plot(conv_full2dmatrix[j, :], 'C1', label='neuron 2')
                            plt.legend()
                            ax2 = plt.subplot(2, 1, 2, sharex=ax1)
                            plt.plot(crosscorr, color='C2', label='neur1*neur2')
                            plt.plot(10 * conv_crosscorr, color='C3', label=f'10*conv(neur1*neur2), w=20')
                            plt.axhline(y=10 * peak_thresh_diff, color='C3', linestyle='--')
                            plt.legend()
                            t_low = 410000
                            t_high = 420000
                            plt.xlim([t_low, t_high])
                            plt.tight_layout()
                            # plt.savefig(
                            #     f'{self.data.figures_path}Corr_neurons_{i}_{j}_tc{self.t_c}_{t_low}_{t_high}.png')
                            # plt.close()
                            plt.show()
                            
                    else:
                        inds_trials_above_thresh = []

                    n_simspikes_per_word[word_idx] = len(inds_trials_above_thresh)
                    n_words_per_word = len(inds_trials_above_thresh)
                    word_idx += 1

        # idx_to_use - which neurons to include in vocabulary
        self.idx_to_use = np.where(np.sum(word_trial_binary_matrix, axis=1) > self.min_n_peaks_thresh)[0]
        self.word_trial_binary_matrix = word_trial_binary_matrix[self.idx_to_use, :]
        self.number_words = len(self.idx_to_use)

        # for later access - but there might be no point in keeping these
        self.inds_1 = inds_1[self.idx_to_use]
        self.inds_2 = inds_2[self.idx_to_use]


    def get_candidates(self):
        overlapping_matrix = np.copy(self.data.full_2d_matrix)
        for t in range(1, self.furthest_overlap + 1):
            # add spikes on the left and right so that [0, 0, 1, 0, 0] -> [0, 1, 1, 1, 0]
            overlapping_matrix[:, :-t] += self.data.full_2d_matrix[:, t:]
            overlapping_matrix[:, t:] += self.data.full_2d_matrix[:, :-t]

        # calculate dot product and make diagonal 0
        overlap_dotprod = np.dot(overlapping_matrix, overlapping_matrix.transpose())
        overlap_dotprod[np.arange(len(overlapping_matrix)), np.arange(len(overlapping_matrix))] = 0

        # impose threshold of how many spikes have to overlap at least a bit
        self.overlap_thresh = 25 * (self.furthest_overlap * 2 + 1)
        print(f'sum spikes overlap > thresh={self.overlap_thresh} : {np.sum(overlap_dotprod > self.overlap_thresh)/2}')
        overlap_dotprod *= (overlap_dotprod > self.overlap_thresh)
        n_pairs_to_check_peaks = int(np.sum(overlap_dotprod > self.overlap_thresh) / 2)
        
        return overlap_dotprod, n_pairs_to_check_peaks

        

    def create_vocabulary(self):
        # create actual words with letters for LDA
        # *******************************************************************************************************
        self.vocab = []
        for word_idx in range(self.number_words):
            # self.vocab.append(str(self.data.neurons_good[word_idx]) + self.word_str)
            self.vocab.append(str(self.inds_1[word_idx]) + '_' + str(self.inds_2[word_idx]) + self.word_str)


    def create_neuron_word_matrix(self):
        self.neuron_word_matrix = np.zeros((self.data.number_neurons, self.number_words), dtype=int)

        # need to change this because now for each word two neurons get a 1
        self.neuron_word_matrix[self.inds_1, range(self.number_words)] = 1
        self.neuron_word_matrix[self.inds_2, range(self.number_words)] = 1


class TranslateOnset(Translate):

    def __init__(self, data, response_delay=10, response_duration=160, onset_duration=50, visualise_overview=False):

        super().__init__(data, response_delay, response_duration, visualise_overview)
        print('in TranslateOnset')
        self.onset_duration = onset_duration
        self.word_str = f'Onset{onset_duration}'
        self.word_name = f'Onset{onset_duration}'
        self.n_neurons_contributing_to_word = 1

    def make_doc_word_matrix(self):
        # onset takes the relevant matrix and gives a word if
        # - there is one or more spikes in the first X ms of the start of the stimulus (excl delay)
        # - there are less spikes in the following duration-X ms of the stimulus being present
        # - there are less spikes in the preceding Y ms
        
        # get number of spikes in preceding time window
        pre_onset_time = 50
        if int(self.data.buffer/self.data.res) + self.response_delay < pre_onset_time:
            print(f'OOPS: buffer is not long enough to calculate the number of spikes \n'
                  f'in the 50ms preceding the stimulus onset. Please choose a longer buffer. Thanks')
            return
        # time before stimulus
        start_idx = int(self.data.buffer/self.data.res) + self.response_delay - pre_onset_time
        stop_idx = int(self.data.buffer/self.data.res) + self.response_delay
        pre = np.sum(self.data.full_matrix[:, :, start_idx:stop_idx], axis=2)
        # onset of stimulus
        start_idx = int(self.data.buffer/self.data.res) + self.response_delay
        stop_idx = int(self.data.buffer/self.data.res) + self.response_delay + self.onset_duration
        ons = np.sum(self.data.full_matrix[:, :, start_idx:stop_idx], axis=2)
        # after onset time window
        start_idx = int(self.data.buffer/self.data.res) + self.response_delay + self.onset_duration
        stop_idx = int(self.data.buffer/self.data.res) + self.response_delay + self.response_duration
        post = np.sum(self.data.full_matrix[:, :, start_idx:stop_idx], axis=2)

        # where were all three conditions fulfilled?
        onset_matrix = (ons > 0) * (pre == 0) * (ons > post)

        print(f'n words appearing = {sum(np.sum(onset_matrix, axis=1) != 0)}')
        print(f'n words not appearing = {sum(np.sum(onset_matrix, axis=1) == 0)}')

        self.number_words = onset_matrix.shape[0] - sum(np.sum(onset_matrix, axis=1) == 0)

        # create words-documents binary matrix
        # *******************************************************************************************************
        # see for which indices a word appears more than 0 times
        self.idx_to_use = np.where(np.sum(onset_matrix, axis=1) != 0)[0]
        self.word_trial_binary_matrix = onset_matrix[self.idx_to_use, :]




class TranslateISIdistr(Translate):

    def __init__(self, data, response_delay=20, response_duration=160, percentile_threshold=20, visualise_overview=False):

        super().__init__(data, response_delay, response_duration, visualise_overview)
        print('in TranslateISIdistr')
        self.percentile_threshold = percentile_threshold
        if self.percentile_threshold < 50:
            self.word_str = f'minISI'
            self.word_name = f'minISI{self.percentile_threshold}'
        else:
            self.word_str = f'ISIlong'
            self.word_name = f'ISIlong{self.percentile_threshold}'
        self.n_neurons_contributing_to_word = 1

    def make_doc_word_matrix(self):
        # get all ISI's in full matrix
        # compare to ISI distribution of 2d matrix

        threshold_isi = np.zeros(self.data.number_neurons)

        # np.where() will sort the times according to neuron (0 to n_neurons)
        i, t = np.where(self.data.full_2d_matrix != 0)
        # calculate isi per neuron, but there are still the borders where indices change from one neuron to the next
        isi_all = t[1:] - t[0:-1]
        #  check that this happens for all neurons and get rid of the negative isi's
        assert np.sum(isi_all < 0) == self.data.number_neurons - 1
        # isi_all = isi_all[isi_all > 0]
        # print(f'min { min(isi_all)}, max {max(isi_all)}')

        # # plot isi's regardless of neuron
        # plt.figure()
        # plt.hist(isi_all, bins=80, range=np.array([0, 160]))
        
        # for full_matrix, calculate ISI for each trial
        # max_possible_isi = int(self.data.avg_trial_length/data.res)
        # isi matrix is the binned matrix (2nd dim = all possible isis), this is more like a count
        isi_matrix = np.zeros((self.data.number_neurons, self.data.full_matrix.shape[1], self.response_duration), dtype=int)
        start_idx = int(self.data.buffer / self.data.res) + self.response_delay
        stop_idx = start_idx + self.response_duration

        min_isi_matrix = np.zeros((self.data.number_neurons, self.data.full_matrix.shape[1]))

        # loop through trials to register isis
        for trial_idx in range(self.data.full_matrix.shape[1]):
            # find neurons where more than 1 spike happened
            neurons_with_isi = np.where(np.sum(self.data.full_matrix[:, trial_idx, start_idx:stop_idx], axis=1) > 1)[0]

            for neuron_idx in neurons_with_isi:
                # get times when spikes happened (in ms)
                tim = np.where(self.data.full_matrix[neuron_idx, trial_idx, start_idx:stop_idx] == 1)[0]
                isi = tim[1:] - tim[0:-1]
                isi_matrix[neuron_idx, trial_idx, isi] = 1

                min_isi_matrix[neuron_idx, trial_idx] = min(isi)

        self.min_isi_matrix = min_isi_matrix
        self.isi_matrix = isi_matrix

        isi_word_matrix = np.zeros((self.data.number_neurons, len(self.data.stim_id_relevant)), dtype=int)

        self.threshold_min_isi = np.zeros(self.data.number_neurons)

        for neuron_idx in range(self.data.number_neurons):
            # calculate threshold for this neuron
            # need to calculate this on the whole time, not just on the relevant trials
            # isi [ms]
            isi = t[i == neuron_idx][1:] - t[i == neuron_idx][0:-1]
            threshold_isi[neuron_idx] = np.percentile(isi, self.percentile_threshold)
            # print(f'number of isis smaller than threshold: {np.sum(isi < threshold_isi[neuron_idx])} = '
            #       f'{np.round(100*np.sum(isi < threshold_isi[neuron_idx])/len(isi), 2)}%')


            self.threshold_min_isi[neuron_idx] = np.percentile(
                self.min_isi_matrix[neuron_idx, np.where(self.min_isi_matrix[neuron_idx, :] > 0)[0]],
                self.percentile_threshold)

            # can be re-introduced
            visualise_word = False
            if visualise_word:
                plt.figure()
                plt.suptitle(f'neuron {neuron_idx}; word={self.word_name}, percentile threshold={self.percentile_threshold}')
                plt.subplot(2, 1, 1)
                plt.title('all ISIs')
                plt.hist(isi, bins=100)
                plt.axvline(x=threshold_isi[neuron_idx], color='C1', label='all isi')
                plt.axvline(x=self.threshold_min_isi[neuron_idx], color='C2', label='only min isi')
                plt.xlim([0, max(isi)])
                plt.legend()

                plt.subplot(2, 1, 2)
                plt.title('only trial length')
                plt.hist(isi, bins=80, range=(0, self.data.avg_trial_length / self.data.res))
                plt.axvline(x=threshold_isi[neuron_idx], color='C1', label='all isi')
                plt.axvline(x=self.threshold_min_isi[neuron_idx], color='C2', label='only min isi')
                plt.xlim([0, self.data.avg_trial_length / self.data.res])

                plt.tight_layout()
                plt.subplots_adjust(top=0.85)

                # plt.savefig(
                #     f'{self.data.figures_path}neuron{neuron_idx}_{word_name}{self.percentile_threshold}_'
                #     f'del{response_delay}_dur{response_duration}.pdf')
                plt.savefig(f'{self.data.figures_path}neuron{neuron_idx}_{self.word_name}'
                            f'{self.percentile_threshold}_del{self.response_delay}_dur{self.response_duration}.pdf')
                plt.close()

            # apply threshold

            # get 2d matrix of this neuron (n_trials x possible isi's)
            isi_matrix_temp = isi_matrix[neuron_idx, :, :]

            # check in which trials there is an isi smaller than threshold
            if self.threshold_min_isi[neuron_idx] >= 1:
                # threshold needs to be larger than 2 actually because there is no ISI of 0
                c, m = np.divmod(self.threshold_min_isi[neuron_idx], 1)

                # if want to find low ISIs
                if m != 0:  # so if the threshold is a decimal
                    # round threshold up in either case!
                    temp_thresh = int(np.ceil(self.threshold_min_isi[neuron_idx]))
                elif self.percentile_threshold < 50 and np.isclose(m, 0):
                    # use the next smaller possible isi, so that percentile is guaranteed to stay under threshold
                    temp_thresh = int(self.threshold_min_isi[neuron_idx])
                elif self.percentile_threshold >= 50 and np.isclose(m, 0):
                    temp_thresh = int(self.threshold_min_isi[neuron_idx] + 1)
                else:
                    print(f'threshold for neuron {neuron_idx} cannot be properly determined. Please check!')

                # find trials (actually, indices of trials) where small ISI happens
                if self.percentile_threshold < 50 and temp_thresh < int(self.data.avg_trial_length / self.data.res):
                    # only trials where ISI was below threshold
                    inds_temp = np.where(np.sum(isi_matrix_temp[:, 0:temp_thresh], axis=1) > 0)[0]
                elif self.percentile_threshold < 50 and temp_thresh >= int(self.data.avg_trial_length / self.data.res):
                    # all trials where an ISI happens should become a word
                    inds_temp = np.where(np.sum(isi_matrix_temp, axis=1) > 0)[0]
                elif self.percentile_threshold >= 50 and temp_thresh < int(self.data.avg_trial_length / self.data.res):
                    inds_temp = np.where(np.sum(isi_matrix_temp[:, temp_thresh:], axis=1) > 0)[0]
                else:
                    inds_temp = np.array([])

                # for now, even if there are more than one spikes, I still give only 1 word
                if len(inds_temp) > 0:
                    isi_word_matrix[neuron_idx, inds_temp] = 1

        self.threshold_isi = threshold_isi

        print(f'number of spikes (total):         {sum(sum(self.data.full_2d_matrix))}')
        print(f'number of isis in matrix (total): {sum(sum(sum(isi_matrix)))}')
        print(f'number of words:                  {isi_word_matrix.sum()} ------- '
              f'avg per neuron {np.round(isi_word_matrix.sum()/self.data.number_neurons, 2)}')
        print(f'number neuron  -> word (appearing)     = {sum(np.sum(isi_word_matrix, axis=1) != 0)}')
        print(f'number neuron !-> word (not appearing) = {sum(np.sum(isi_word_matrix, axis=1) == 0)}')

        self.number_words = isi_word_matrix.shape[0] - sum(np.sum(isi_word_matrix, axis=1) == 0)

        # create words-documents binary matrix
        # *******************************************************************************************************
        # see for which indices a word appears more than 0 times
        self.idx_to_use = np.where(np.sum(isi_word_matrix, axis=1) != 0)[0]
        self.word_trial_binary_matrix = isi_word_matrix[self.idx_to_use, :]



class TranslateNumberSpikes(Translate):
    
    def __init__(self, data):
        
        super().__init__(data)
        print('in TranslateNumberSpike')
        
        self.word_string = '_abs'
        self.word_name = 'abs number of spikes'
        self.n_neurons_contributing_to_word = 1

        
    def make_doc_word_matrix(self):
        
        self.word_trial_binary_matrix = np.sum(self.data.full_matrix, axis=2)
        
        self.idx_to_use = np.where(np.sum(self.word_trial_binary_matrix, axis=1) != 0)[0]
        self.number_words = len(self.idx_to_use)
        



class TranslateIfSpikepike(Translate):
    
    def __init__(self, data):
        
        super().__init__(data)
        print('in TranslateIfSpike')
        
        self.word_str = '_spiked'
        self.word_name = 'spike y/n'
        self.n_neurons_contributing_to_word = 1

        
        
    def make_doc_word_matrix(self):
        
        self.word_trial_binary_matrix = np.sum(self.data.full_matrix, axis=2)
        self.word_trial_binary_matrix = np.ones(self.word_trial_binary_matrix.shape)*(self.word_trial_binary_matrix > 0)
        
        self.idx_to_use = np.where(np.sum(self.word_trial_binary_matrix, axis=1) != 0)[0]
        self.number_words = len(self.idx_to_use)
        
        


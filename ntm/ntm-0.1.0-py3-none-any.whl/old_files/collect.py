import numpy as np




def combine_vocabularies(word_list):

    # collect number of words first to do rest more efficiently
    # also collect word names
    n_words_in_vocabs = np.zeros(len(word_list), dtype=int)
    words_present = []
    for vocab_idx, vocab in enumerate(word_list):
        n_words_in_vocabs[vocab_idx] = vocab.word_trial_binary_matrix.shape[0]
        words_present.append(vocab.word_str)
    n_words_total = np.sum(n_words_in_vocabs)

    # initialise
    final_word_trial_binary_matrix = np.zeros((int(n_words_total),
                                                    word_list[0].word_trial_binary_matrix.shape[1]), dtype=int)

    n_neurons = word_list[0].data.number_neurons
    neuron_word_matrix = np.zeros((n_neurons, n_words_total))
    word_depths_all = np.empty(n_words_total)

    # combine words: vocabs, word-doc-matrices, word depths
    running_idx = int(0)
    vocab_all = []
    for vocab_idx, vocab in enumerate(word_list):
        # fill binary matrix for lda input
        final_word_trial_binary_matrix[running_idx:running_idx + n_words_in_vocabs[vocab_idx], :] = \
            vocab.word_trial_binary_matrix
        vocab_all.extend(vocab.vocab)
        word_depths_all[running_idx:running_idx + n_words_in_vocabs[vocab_idx]] = vocab.word_depths

        # check that number fo neurons is the same for each word (same input data)
        assert vocab.data.number_neurons == n_neurons
        # fill neuron_word_matrix with the information of what neuron is the basis of each word
        neuron_word_matrix[:, running_idx:running_idx + n_words_in_vocabs[vocab_idx]] = vocab.neuron_word_matrix

        running_idx += n_words_in_vocabs[vocab_idx]
    final_word_trial_binary_matrix = final_word_trial_binary_matrix.transpose()

    return final_word_trial_binary_matrix, vocab_all, neuron_word_matrix, word_depths_all, words_present
    
    




class Collect:
    
    def __init__(self, word_list):
        
        self.word_list = word_list
        self.n_vocabs = len(self.word_list)
        
    
    def collect(self):

        self.final_word_trial_binary_matrix = self.combine_vocabularies(self)
        
        
    
    def combine_vocabularies(self):
        
        # collect stats first to do rest more efficiently
        n_words_in_vocabs = np.zeros(self.n_vocabs, dtype=int)
        for vocab_idx, vocab in enumerate(self.word_list):
            n_words_in_vocabs[vocab_idx] = vocab.word_trial_binary_matrix.shape[0]
        self.n_words_total = np.sum(n_words_in_vocabs)
            
        self.final_word_trial_binary_matrix = np.zeros((int(np.sum(n_words_in_vocabs)),
                                                        self.word_list[0].word_trial_binary_matrix.shape[1]), dtype=int)
        
        n_neurons = self.word_list[0].data.number_neurons
        self.neuron_word_matrix = np.zeros((n_neurons, self.n_words_total))
        
        running_idx = int(0)
        self.vocab_all = []
        for vocab_idx, vocab in enumerate(self.word_list):
            # fill binary matrix for lda input
            self.final_word_trial_binary_matrix[running_idx:running_idx + n_words_in_vocabs[vocab_idx], :] = \
                vocab.word_trial_binary_matrix
            self.vocab_all.extend(vocab.vocab)

            # check that number fo neurons is the same for each word (same input data)
            assert vocab.data.number_neurons == n_neurons
            # fill neuron_word_matrix with the information of what neuron is the basis of each word
            self.neuron_word_matrix[:, running_idx:running_idx + n_words_in_vocabs[vocab_idx]] = vocab.neuron_word_matrix
            
            running_idx += n_words_in_vocabs[vocab_idx]
        self.final_word_trial_binary_matrix = self.final_word_trial_binary_matrix.transpose()
            
        return self.final_word_trial_binary_matrix


        
        
class CheckVocab:
    
    def __init__(self, word_list, check_correlations=True):
        
        self.word_list = word_list
        self.check_correlations = check_correlations
        
        
    def check(self):
        
        if self.check_correlations == True:
            print(f'start checking correlations')
            self.check_corrs()
        
        
        
    def check_corrs(self):
        
        pass
    
    
    
    
    
    
class CreateWordSpace:
    
    def __init__(self, data, collection):
        
        pass
    
    
    def create_wordspace(self):
        
        pass
    
    
    def get_neuron_characteristics(self):
        
        # depth, location, AP shape?
        
        # firing rate, preferred receptive field (max of rec field?), bursting
        # offset/onset?
        
        pass
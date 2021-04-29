import re
from transformers import BertTokenizerFast, AutoModelForSequenceClassification
import torch
import sys
import pandas as pd
from numpy.random import multinomial
from numpy import log, exp
from numpy import argmax
import spacy
import tkinter as _TK

path_models = 'utils/models/'
path_sentiment = path_models + 'sentiment'
path_tokenizer = path_models + 'tokenizer'

ERR_SYS = "\nSystem error: "
bertnlp_model = AutoModelForSequenceClassification.from_pretrained(path_sentiment)
bert_tokenizer = BertTokenizerFast.from_pretrained(path_tokenizer)
spacy.prefer_gpu()
nlp_model = spacy.load('es_core_news_md', disable=['ner', 'parser'])


class CleanText():
    
    def __init__(self, input_txt, verbose=False):
        """
        This functions validates if the input of the class is a string.
        
        Parameters
        ----------
        input_txt: 
            type: str 
            String to clean.
        mentions: 
            verbose: bool 
            If True prints when the input is not a string.
        """
        METHOD_NAME="init"
        if type(input_txt) == str:
            self.input_txt = input_txt
        else:
            print(f'WARNING: Input {input_txt} is not a string. Default set to "".')
            print(f'Class: {self.__str__()}\nMethod: {METHOD_NAME}')
            self.input_txt = ''

    def process_text(self, rts=False, mentions=False, hashtags=False, links=False, spec_chars=False):
        """
        This functions cleans the input text.

        Parameters
        ----------
        rts: 
            type: bool 
            If True the patterns associated with retweets are removed
            from the text, default=False.
        mentions: 
            type: bool 
            If True the mentions are removed from the text, default=False.
        hashtags: 
            type: bool 
            If True the hashtags are removed from the text, default=False.
        links: 
            type: bool 
            If True the patterns associated with links (urls) are removed
            from the text, default=False.
        spec_chars:
            type: bool 
            If True all special characters (except accents, # and @) are removed
            from the text, default=False.
            
        Returns
        -------
        str
        """
        
        input_txt = self.input_txt
        if rts:
            rt_pattern = re.compile(r'^(?:RT|rt) \@[a-zA-Z0-9\-\_]+\b')
            input_txt = re.sub(rt_pattern, '', input_txt)
        if mentions:
            mention_pattern = re.compile(r'\@[a-zA-Z0-9\-\_]+\b')
            input_txt = re.sub(mention_pattern, '', input_txt)
        else:
            input_txt = input_txt.replace('@', 'xxatsignxx') #procect '@' signs of being removed in spec_chars
        if hashtags:
            hashtag_pattern = re.compile(r'\#[a-zA-Z0-9\-\_]+\b')
            input_txt = re.sub(hashtag_pattern, '', input_txt)
        else:
            input_txt = input_txt.replace('#', 'xxhashtagsignxx') #procect '#' signs to being removed in spec_chars
        if links:
            link_pattern = re.compile(r'\bhttps:.+\b')
            input_txt = re.sub(link_pattern, '', input_txt)
            link_pattern = re.compile(r'\bhttp:.+\b')
            input_txt = re.sub(link_pattern, '', input_txt)
        if spec_chars:
            input_txt = re.sub(r'[^a-zA-Z\u00C0-\u00FF ]', ' ',input_txt)
        input_txt = input_txt.split()
        output_txt = ' '.join(input_txt)
        output_txt = output_txt.replace('xxatsignxx', '@')
        output_txt = output_txt.replace('xxhashtagsignxx', '#')
        return output_txt


class Features():
    
    def __init__(self):
        """
        This functions loads the spacy model for spanish.

        """
        #self.nlp_model = Language().from_disk(path_models + 'pipeline')

        self.bad_words = ['de', 'que', 'la', 'los', 'el', 'las']
        ##def remove_names(self, rem_names=False, names_list=[]): 
        #if(rem_names ==True):
        #    self.bad_words = self.bad_words + names_list

    def pos_tags(self, input_txt):
        """
        This functions get the features of the words in the input_txt parameter.

        Parameters
        ----------
        input_txt: 
            type: str 
            String to get the features from.

        Returns
        -------
        dict: keys -> tokens, lemmas and part of speech tags.
        i
        """
        METHOD_NAME="pos_tags"
        self.input_txt = input_txt
        if type(input_txt) != str:
            print('ERROR: Input is not a string.')
            print(f'Class: {self.__str__()}\nMethod: {METHOD_NAME}')
            self.input_txt = ''
        bad_words = self.bad_words
        
        try:
            doc = nlp_model(self.input_txt.lower())
            features = [(token.text.replace('xxhashtagsignxx', '#').replace('xxatsignxx', '@'), \
                         token.lemma_.replace('xxhashtagsignxx', '#').replace('xxatsignxx', '@'), \
                         token.pos_) for token in doc if token.text not in bad_words and len(token.text) > 1]

            words = []
            lemmas = []
            pos_tags = []
            for feat in features:
                if feat[2] in {'PROPN', 'NOUN', 'VERB', 'ADJ'}:
                    words.append(feat[0])
                    lemmas.append(feat[1])
                    pos_tags.append(feat[2])

            out_dict = {
                'words': words,
                'lemmas': lemmas,
                'pos_tags': pos_tags
            }
        except Exception as e:
            print(e)
            error_1 = sys.exc_info()[0]
            print(ERR_SYS + str(error_1))
            print(f'Class: {self.__str__()}\nMethod: {METHOD_NAME}')
            out_dict = {
                'words': [],
                'lemmas': [],
                'pos_tags': []
            }
            
        return out_dict


class Polarity(object):
    def __init__(self):
        self.polscore = [-1.0, -0.5, 0, 0.5, 1.0]
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        print(f'Loading model to {self.device}')
        self.model = bertnlp_model
        self.model.to(self.device)
        print('Done.\n')

        self.tokenizer = bert_tokenizer
        self.softmax = torch.nn.Softmax(dim=1)

    def tokenize_texts(self, text_list, max_length=128):


        encoded_dict = tokenizer.batch_encode_plus(text_list,
                        add_special_tokens = True,     # Add '[CLS]' and '[SEP]'
                        truncation=True,
                        max_length = max_length,              # THIS SHOULD BE CHANGED IS JUST EXAMPLE!!!!            
                        pad_to_max_length = True,      # Pad & truncate all sentences to max_length
                        return_attention_mask = True,  # Construct attn. masks.
                        return_tensors = 'pt',         # Return pytorch tensors.
                   )

        # Convert the input_ids lists into tensors (expand in first dim as we suppose is the batch size).
        input_ids_b = encoded_dict['input_ids']
        attention_masks_b = encoded_dict['attention_mask']

        return (input_ids_b, attention_masks_b)

    def forward_model(self, data):

        (input_ids_b, attention_masks_b) = data 
        (out,) = model(input_ids_b.to(self.device), 
                           token_type_ids=None, 
                           attention_mask=attention_masks_b.to(self.device),
                           labels=None)
        
        sentiment = list( out.argmax(1).numpy() )

        return sentiment

    def batch_forward(self, text_list, batch_size, max_length):

        num_texts = len(df_text)
        batch_idx = slice(0,num_texts, batch_size)

        polarity = []
        for i in range(num_texts//batch_size):
            batch_idx = slice( batch_size*i, batch_size*(i+1), 1)
            (input_ids_b, attention_masks_b) = self.tokenize_texts( text_list[batch_idx], max_length=max_length)
            sentiment_list = forward_model((input_ids_b, attention_masks_b))

            polarity.extend( sentiment_list )

        if num_texts%batch_size: 
            batch_idx = slice(batch_size*(num_texts//batch_size),num_texts,1)
            (input_ids_b, attention_masks_b) = self.tokenize_texts( text_list[batch_idx], max_length=max_length)
            sentiment_list = self.forward_model((input_ids_b, attention_masks_b))

            polarity.extend( sentiment_list )

        return polarity

    def batch_polarity(self, df_text, text_column_name ='processed_text', batch_size=2, max_length=128):
        """
        This function returns the polarity of an input texts procesed by batches.

        Parameters
        ----------
        df_text: 
            type: str, list of strings, pandas DataFrame with a text column. 
            clean text for which the polarity is obtained

        text_column_name (optional):
            type: str, name of the text column in the pandas DataFrame.

        batch_size (optional):
            type: int, number of text to process at the same time by doing a forward in the model.
            default: 20

        Returns
        -------
        pandas DataFrame with a 'polarity' column with the polarity values. (warning, this method returns -100 if input is not a list of strings or pandas DataFrame.)

        """

        METHOD_NAME = "batch_polarity"

        if isinstance(df_text, list) and all(isinstance(text, str) for text in df_text):    
            df_text = pd.DataFrame(columns=['processed_text'], data=df_text)

        if isinstance(df_text, pd.DataFrame):
            try:
                df_text['polarity'] = self.batch_forward( list(df_text[text_column_name]), batch_size=batch_size, max_length=max_length) 
                dict_polscore = {idx: score for idx, score in enumerate(self.polscore) }
                df_text['polarity'] = df_text['polarity'].map( dict_polscore )

            except Exception as e:
                print(e)
                error_1 = sys.exc_info()[0]
                print(ERR_SYS + str(error_1))
                print(f'Class: {self.__str__()}\nMethod: {METHOD_NAME}')
                df_text['polarity'] = ""
            return df_text

        elif isinstance(df_text, str):    
            print(f'Class: {self.__str__()}\nMethod: {METHOD_NAME}')
            print(f'Must recieve a list of string of pandas DataFrame with strings. returning -100 ...')
            return -100

        else:
            print(f'Class: {self.__str__()}\nMethod: {METHOD_NAME}')
            print('Calling polarity method for a non-string variable. returning -100 ...')
            polarity=-100 
            return polarity
        
    def polarity(self, df_text, text_column_name ='processed_text'):

        """
        This function returns the polarity of an input text(s).

        Parameters
        ----------
        df_text: 
            type: str, list of strings, pandas DataFrame with a text column. 
            clean text for which the polarity is obtained
        
        text_column_name (optional):
            type: str, name of the text column in the pandas DataFrame.
            
        Returns
        -------
        polarity value or pandas DataFrame with a 'polarity' column with the polarity values. (warning, this method returns -100 if input is not a string or if input text is too long.)
        
        """
        METHOD_NAME = 'polarity'
        
        if isinstance(df_text, list) and all(isinstance(text, str) for text in df_text):    
            df_text=pd.DataFrame(columns=['message'], data=df_text)
            df_text['processed_text'] = df_text['message'].apply(lambda msg: CleanText(msg).process_text(mentions=True, hashtags=True, links=True, spec_chars=True))
            df_text = df_text.dropna(subset=['processed_text'])
            df_text = df_text.drop(df_text[df_text['processed_text']==""].index)
        
        if isinstance(df_text, pd.DataFrame):
        
            try:
                df_text['tokenized_data']=df_text[text_column_name].apply(lambda msg: self.tokenizer.encode(msg))
                df_text['len_tokenized_data']=df_text.tokenized_data.apply(lambda l: len(l))
                df_text=df_text[df_text.tokenized_data.str.len()<511]
                df_text['tokenized_data']=df_text.tokenized_data.apply(lambda l: torch.tensor([l]))
                df_text['polarity']=df_text.tokenized_data.apply(lambda tkd: self.polscore[self.softmax(self.model(tkd.to(self.device) )[0]).argmax()])
            except Exception as e:
                print(e)
                error_1 = sys.exc_info()[0]
                print(ERR_SYS + str(error_1))
                print(f'Class: {self.__str__()}\nMethod: {METHOD_NAME}')
                df_text['polarity']=""
            return df_text
        
        elif isinstance(df_text, str):    
            try:
                text_tokens = self.tokenizer.encode(df_text,return_tensors="pt")
                
                #if the text is too long the model does not work
                if(len(text_tokens[0])>512):
                    print(f'Class: {self.__str__()}\nMethod: {METHOD_NAME}')
                    print('text too long for polarity model. returning -100 ...')
                    polarity = -100
                    return polarity
                else:
                    output      = self.softmax(self.model(text_tokens)[0])
                    polarity    = self.polscore[output.argmax()]
    
            except Exception as e:
                print(e)
                error_1 = sys.exc_info()[0]
                print(ERR_SYS + str(error_1))
                print(f'Class: {self.__str__()}\nMethod: {METHOD_NAME}')
                polarity=-100 
            return polarity
                
        else:
            print(f'Class: {self.__str__()}\nMethod: {METHOD_NAME}')
            print('Calling polarity method for a non-string variable. returning -100 ...')
            polarity=-100 
            return polarity


class STTM(object):

    def __init__(self, df_data, text_column_name ='tokenized_text'):
        """
        This function stores the input DataFrame. 

        Parameters
        ----------
        df_data: 
            type: DataFrame 
            This Pandas DataFrame must have the column 'tokenized text'.

        """

        self.df_data = df_data
        self.text_column_name = text_column_name

    def sttm_model(self, K=20, alpha=0.1, beta=0.2, n_iters=100):
        """
        This function classifies the tokenized texts into groups of similar texts. It creates the 'sttm_group' column with the number of the group that the text was classified into. 

        Parameters
        ----------
        K: 
            type: int 
            Number of initial groups that the texts are classified into.
        alpha: 
            type: float 
            Parameter of the sttm model .
        beta: 
            type: float 
            Parameter of the sttm model.
        n_iters: 
            type: int
            Number of iterations of the sttm model.
        
        Returns
        ----------
        df_data:
            DataFrame with the 'sttm_group' column

        """
        METHOD_NAME='sttm_model'
        try:
            
            # Input format for the STTM model : list of strings (list of tokens)
            docs = self.df_data[self.text_column_name].tolist() #tokenized_data.tokens.tolist()
            vocab = set(x for doc in docs for x in doc)
            n_terms = len(vocab)
            n_docs = len(docs)
            #print("numero de documentos", n_docs)
            
            # Train a new model 
            # Init of the Gibbs Sampling Dirichlet Mixture Model algorithm
            mgp = MovieGroupProcess(K, alpha, beta, n_iters)
    
            # Fit the model on the data given the chosen seeds
            y = mgp.fit(docs, n_terms)
            
            labels = []
            for doc in self.df_data[self.text_column_name]:
                labels.append(mgp.choose_best_label(doc)[0])
            self.df_data['sttm_group'] = labels
        
        except Exception as e:
            print(e)
            error_1 = sys.exc_info()[0]
            print(ERR_SYS + str(error_1))
            print(f'Class: {self.__str__()}\nMethod: {METHOD_NAME}')
            self.df_data['sttm_group'] = "" 
        

        return self.df_data
    

class MovieGroupProcess:
    def __init__(self, K=8, alpha=0.1, beta=0.1, n_iters=30):
        '''
        A MovieGroupProcess is a conceptual model introduced by Yin and Wang 2014 to
        describe their Gibbs sampling algorithm for a Dirichlet Mixture Model for the
        clustering short text documents.
        Reference: http://dbgroup.cs.tsinghua.edu.cn/wangjy/papers/KDD14-GSDMM.pdf

        Imagine a professor is leading a film class. At the start of the class, the students
        are randomly assigned to K tables. Before class begins, the students make lists of
        their favorite films. The teacher reads the role n_iters times. When
        a student is called, the student must select a new table satisfying either:
            1) The new table has more students than the current table.
        OR
            2) The new table has students with similar lists of favorite movies.

        :param K: int
            Upper bound on the number of possible clusters. Typically many fewer
        :param alpha: float between 0 and 1
            Alpha controls the probability that a student will join a table that is currently empty
            When alpha is 0, no one will join an empty table.
        :param beta: float between 0 and 1
            Beta controls the student's affinity for other students with similar interests. A low beta means
            that students desire to sit with students of similar interests. A high beta means they are less
            concerned with affinity and are more influenced by the popularity of a table
        :param n_iters:
        '''
        self.K = K
        self.alpha = alpha
        self.beta = beta
        self.n_iters = n_iters

        # slots for computed variables
        self.number_docs = None
        self.vocab_size = None
        self.cluster_doc_count = [0 for _ in range(K)]
        self.cluster_word_count = [0 for _ in range(K)]
        self.cluster_word_distribution = [{} for i in range(K)]

    @staticmethod
    def from_data(K, alpha, beta, D, vocab_size, cluster_doc_count, cluster_word_count, cluster_word_distribution):
        '''
        Reconstitute a MovieGroupProcess from previously fit data
        :param K:
        :param alpha:
        :param beta:
        :param D:
        :param vocab_size:
        :param cluster_doc_count:
        :param cluster_word_count:
        :param cluster_word_distribution:
        :return:
        '''
        mgp = MovieGroupProcess(K, alpha, beta, n_iters=30)
        mgp.number_docs = D
        mgp.vocab_size = vocab_size
        mgp.cluster_doc_count = cluster_doc_count
        mgp.cluster_word_count = cluster_word_count
        mgp.cluster_word_distribution = cluster_word_distribution
        return mgp

    @staticmethod
    def _sample(p):
        '''
        Sample with probability vector p from a multinomial distribution
        :param p: list
            List of probabilities representing probability vector for the multinomial distribution
        :return: int
            index of randomly selected output
        '''
        return [i for i, entry in enumerate(multinomial(1, p)) if entry != 0][0]

    def fit(self, docs, vocab_size):
        '''
        Cluster the input documents
        :param docs: list of list
            list of lists containing the unique token set of each document
        :param V: total vocabulary size for each document
        :return: list of length len(doc)
            cluster label for each document
        '''
        alpha, beta, K, n_iters, V = self.alpha, self.beta, self.K, self.n_iters, vocab_size

        D = len(docs)
        self.number_docs = D
        self.vocab_size = vocab_size

        # unpack to easy var names
        m_z, n_z, n_z_w = self.cluster_doc_count, self.cluster_word_count, self.cluster_word_distribution
        cluster_count = K
        d_z = [None for i in range(len(docs))]

        # initialize the clusters
        for i, doc in enumerate(docs):

            # choose a random  initial cluster for the doc
            z = self._sample([1.0 / K for _ in range(K)])
            d_z[i] = z
            m_z[z] += 1
            n_z[z] += len(doc)

            for word in doc:
                if word not in n_z_w[z]:
                    n_z_w[z][word] = 0
                n_z_w[z][word] += 1

        for _iter in range(n_iters):
            total_transfers = 0

            for i, doc in enumerate(docs):

                # remove the doc from it's current cluster
                z_old = d_z[i]

                m_z[z_old] -= 1
                n_z[z_old] -= len(doc)

                for word in doc:
                    n_z_w[z_old][word] -= 1

                    # compact dictionary to save space
                    if n_z_w[z_old][word] == 0:
                        del n_z_w[z_old][word]

                # draw sample from distribution to find new cluster
                p = self.score(doc)
                z_new = self._sample(p)

                # transfer doc to the new cluster
                if z_new != z_old:
                    total_transfers += 1

                d_z[i] = z_new
                m_z[z_new] += 1
                n_z[z_new] += len(doc)

                for word in doc:
                    if word not in n_z_w[z_new]:
                        n_z_w[z_new][word] = 0
                    n_z_w[z_new][word] += 1

            cluster_count_new = sum([1 for v in m_z if v > 0])
            print("In stage %d: transferred %d clusters with %d clusters populated" % (
            _iter, total_transfers, cluster_count_new))
            if total_transfers == 0 and cluster_count_new == cluster_count and _iter>25:
                print("Converged.  Breaking out.")
                break
            cluster_count = cluster_count_new
        self.cluster_word_distribution = n_z_w
        return d_z

    def score(self, doc):
        '''
        Score a document

        Implements formula (3) of Yin and Wang 2014.
        http://dbgroup.cs.tsinghua.edu.cn/wangjy/papers/KDD14-GSDMM.pdf

        :param doc: list[str]: The doc token stream
        :return: list[float]: A length K probability vector where each component represents
                              the probability of the document appearing in a particular cluster
        '''
        alpha, beta, K, V, D = self.alpha, self.beta, self.K, self.vocab_size, self.number_docs
        m_z, n_z, n_z_w = self.cluster_doc_count, self.cluster_word_count, self.cluster_word_distribution

        p = [0 for _ in range(K)]

        #  We break the formula into the following pieces
        #  p = N1*N2/(D1*D2) = exp(lN1 - lD1 + lN2 - lD2)
        #  lN1 = log(m_z[z] + alpha)
        #  lN2 = log(D - 1 + K*alpha)
        #  lN2 = log(product(n_z_w[w] + beta)) = sum(log(n_z_w[w] + beta))
        #  lD2 = log(product(n_z[d] + V*beta + i -1)) = sum(log(n_z[d] + V*beta + i -1))

        lD1 = log(D - 1 + K * alpha)
        doc_size = len(doc)
        for label in range(K):
            lN1 = log(m_z[label] + alpha)
            lN2 = 0
            lD2 = 0
            for word in doc:
                lN2 += log(n_z_w[label].get(word, 0) + beta)
            for j in range(1, doc_size +1):
                lD2 += log(n_z[label] + V * beta + j - 1)
            p[label] = exp(lN1 - lD1 + lN2 - lD2)

        # normalize the probability vector
        pnorm = sum(p)
        pnorm = pnorm if pnorm>0 else 1
        return [pp/pnorm for pp in p]

    def choose_best_label(self, doc):
        '''
        Choose the highest probability label for the input document
        :param doc: list[str]: The doc token stream
        :return:
        '''
        p = self.score(doc)
        return argmax(p),max(p)


import pickle
import math
import re
from itertools import groupby
from src.preprocessing.hashtag_processing_utils import HashtagProcessingUtils

class TextProcessingUtils:
    emoji_dict = open("src/resources/emoji_dictionary.txt").read()

    @staticmethod
    def remove_twitter_jargon(text: str) -> str:
        text = re.sub("@[a-z\.]+ |@\w+|rt ", " ", text)
        return text

    @staticmethod
    def remove_urls(text: str) -> str:
        text = re.sub(
            r"https?:\S+|http?:\S|www\..+\.com|www\..+\.net|\.com", " ", text)
        return text

    @staticmethod
    def remove_emails(text: str) -> str: 
        emailpattern = "[a-zA-Z0-9]+[\._]?[a-zA-Z0-9]+[@]\w+[.]\w{2,3}"
        return re.sub(emailpattern, " ", text)

    @staticmethod
    def remove_emojis(text: str) -> str:
        text = re.sub("\u200d", "", text)
        return re.sub(TextProcessingUtils.emoji_dict, " ", text)

    @staticmethod
    def remove_special_chars(text: str) -> str:
        text = re.sub("[!?]", ".", text)
        text = re.sub("&amp", "", text)
        text = re.sub("&gt;", "", text)
        text = re.sub('[\[\\-\'"*_\/()\]\:+<>@=-]', "", text)
        text = text.replace(r"\r", " ")
        text = text.replace(r"\n", " ")
        text = text.replace(r"\t", " ")
        return text

    @staticmethod
    def remove_excess_whitespaces(text: str) -> str:
        text = re.sub(" +", " ", text)
        return text

    @staticmethod
    def remove_spaces_before_punctuations(text: str) -> str:
        text = re.sub(" +\.", ".", text)
        text = re.sub(" +\;", ";", text)
        text = re.sub(" +\!", "!", text)
        text = re.sub(" +\?", "?", text)
        text = re.sub(" +\:", ":", text)
        text = re.sub(" +\,", ",", text)
        return text

    @staticmethod
    def remove_similar_consecutive_words(text: str) -> str:
        text = " ".join(
            [grouped_words[0].strip() for grouped_words in groupby(text.split())]
        )
        return text

    @staticmethod
    def get_sentence_perplexity(sentence: str) -> float:
        words = sentence.split()
        n_words = len(words)
        perplexity = 1
        for word in words:
            perplexity *= 1 / HashtagProcessingUtils.get_word_probability(word)
        perplexity = pow(perplexity, 1/float(n_words))
        return perplexity


class GibberishDetector:
    gibberish_model = pickle.load(open('src/resources/gib_model.pki', 'rb'))
    letters_probability_matrix = gibberish_model['mat']
    threshold = gibberish_model['thresh']
    accepted_chars = 'abcdefghijklmnopqrstuvwxyz '
    pos = dict([(char, idx) for idx, char in enumerate(accepted_chars)])

    @staticmethod
    def normalize(sentence: str) -> list:
        return [char.lower() for char in sentence if char.lower() in GibberishDetector.accepted_chars]
    
    @staticmethod
    def ngram(n: int, sentence: str) -> str:
        filtered = GibberishDetector.normalize(sentence)
        for start in range(0, len(filtered) - n + 1):
            yield ''.join(filtered[start:start + n])

    @staticmethod
    def get_gibberish_prob(sentence: str) -> float:
        log_prob = 0.0
        transition_ct = 0
        for a, b in GibberishDetector.ngram(2, sentence):
            log_prob += GibberishDetector.letters_probability_matrix[GibberishDetector.pos[a]][GibberishDetector.pos[b]]
            transition_ct += 1
        if transition_ct == 0:
            return 'Empty String'
        return math.exp(log_prob / (transition_ct or 1))

    @staticmethod
    def detect_gibberish(sentence: str) -> bool:
        prob_non_gibberish = GibberishDetector.get_gibberish_prob(sentence)
        if prob_non_gibberish == 'Empty String':
            return 0, True
        return prob_non_gibberish, prob_non_gibberish < GibberishDetector.threshold



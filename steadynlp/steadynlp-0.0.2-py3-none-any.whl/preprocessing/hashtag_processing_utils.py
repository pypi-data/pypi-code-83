import re

class HashtagProcessingUtils:
    word_dictionary = eval(open("src/resources/word_dict.json").read())
    dictionary_size = float(sum(word_dictionary.values()))
    max_word_length = max(map(len, word_dictionary))

    @staticmethod
    def get_word_probability(word: str) -> float:
        return max(HashtagProcessingUtils.word_dictionary.get(
            word, 0) / HashtagProcessingUtils.dictionary_size, 0.01)

    @staticmethod
    def segment_combined_text(text: str) -> list:
        probability_of_word_at_index, last_index_of_predicted_word = [1.0], [0]
        for index_of_end_word in range(1, len(text) + 1):
            word_index_probability_pair = []
            for index_of_start_word in range(
                max(0, index_of_end_word - HashtagProcessingUtils.max_word_length), 
                index_of_end_word
            ):
                word_probability = HashtagProcessingUtils.get_word_probability(
                    text[index_of_start_word:index_of_end_word])
                word_probability = word_probability * probability_of_word_at_index[index_of_start_word]
                word_index_probability_pair.append(
                    (word_probability, index_of_start_word))
            most_probable_word_probability, most_probable_word_index = max(word_index_probability_pair)
            probability_of_word_at_index.append(most_probable_word_probability)
            last_index_of_predicted_word.append(most_probable_word_index)
        words = []
        index = len(text)
        while 0 < index:
            words.append(text[last_index_of_predicted_word[index]:index])
            index = last_index_of_predicted_word[index]
        words.reverse()
        return words

    @staticmethod
    def segment_hashtags(text: str) -> str:
        text = re.sub("#", " #", text)
        text = [" ".join(HashtagProcessingUtils.segment_combined_text(word[1:]))
                if word.startswith("#") else word for word in text.split()]
        return " ".join(text)
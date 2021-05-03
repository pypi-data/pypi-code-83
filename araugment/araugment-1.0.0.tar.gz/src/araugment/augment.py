# coding:utf-8
# author Abdulshaheed Alqunber
# version : 1.0.0
from google_trans_new import google_translator  
import markovify as mk

def back_translate(text, language_src="ar", language_dst="zh"):
    """Translate text to a foreign language then translate back to original language to augment data
    Parameters:
    text (string): non-empty string
    original: language of input text, must match the format in this link
    https://github.com/lushan88a/google_trans_new/blob/main/constant.py
    language: language in which the text is going to be translated to

    Returns:
    string: the back translated text.  
    """
    
    try:
        t = google_translator()
        # translate to target language
        translated_text = t.translate(text.strip(), language_dst)
        # translate to orignal language
        translated_back = t.translate(translated_text, language_src)
        return translated_back
    
    # failed to translate, return original
    except: 
        return text

def markov(document, n):
    """This method uses Markov chains to string together n new sequences of words based on previous sequences.
    
    Parameters:
    document (list): list of sentences

    Returns:
    list: list of new generated sentences
    """

    text_model = mk.Text(document)
    return [text_model.make_sentence() for i in range(n)]

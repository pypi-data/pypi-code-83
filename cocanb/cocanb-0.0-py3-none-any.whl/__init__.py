from .sentences import *
from .quotes import *
from .english_to_cocanb import toc
from .cocanb_to_english import toe

def english_to_cocanb(initial):
    q_initial = split_quotes(initial)
    sentences = split_sentences(q_initial["outside"])
    for sentence in sentences:
        sentence.string = toc(sentence.string)
    for quote in q_initial["inside"]: 
        q_sentences = split_sentences(quote)
        for sentence in q_sentences:
            sentence.string = toc(sentence.string)
        q_initial["inside"][q_initial["inside"].index(quote)] = join_sentences(q_sentences)
    joined = join_sentences(sentences)
    final = join_quotes({
        "outside": joined,
        "inside": q_initial["inside"]
    })
    return final

def cocanb_to_english(initial):
    q_initial = split_quotes(initial)
    sentences = split_sentences(q_initial["outside"])
    for sentence in sentences:
        sentence.string = toe(sentence.string)
    for quote in q_initial["inside"]: 
        q_sentences = split_sentences(quote)
        for sentence in q_sentences:
            sentence.string = toe(sentence.string)
        q_initial["inside"][q_initial["inside"].index(quote)] = join_sentences(q_sentences)
    joined = join_sentences(sentences)
    final = join_quotes({
        "outside": joined,
        "inside": q_initial["inside"]
    })
    return final
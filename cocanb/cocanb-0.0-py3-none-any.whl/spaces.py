from numpy.random import choice
from re import findall, sub
from unidecode import unidecode

def add_spaces(initial):
    special = findall("<.*>", initial)
    replaced = sub("<.*>", "|", initial)
    replaced = list(replaced)
    for i in replaced:
        replaced[replaced.index(i)] = i + choice(["", " "], p=[0.7, 0.3]) #change
    replaced = "".join(replaced)
    for i in special:
        replaced = replaced.replace("|", i)
    final = sub(" +", " ", replaced)
    return final
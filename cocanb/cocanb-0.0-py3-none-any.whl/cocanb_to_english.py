from unidecode import unidecode

#I wrote this in the meanwhile
def toe(sentence):
    sentence = sentence.replace(" ", "").replace("æ", "ae").replace("œ", "oe")
    initial = sentence[:sentence.index("non")]
    additional = sentence[sentence.index("non")+3:]
    final = []
    letters_gone = 0
    for i in range(int(len(additional)/2)):
        final.append(initial[letters_gone:letters_gone + ord(additional[2*i+1])-97]+additional[2*i])
        letters_gone += ord(additional[2*i+1])-97
    return " ".join(final)
from re import sub, findall
from numpy.random import choice

a = ["a","à","á","â","ä"]
a_p = [8/15, 2/15, 2/15, 2/15, 1/15]
e = ["e","è","é","ê"]
e_p = [8/14, 2/14, 2/14, 2/14]
i = ["i","î","í","ì"]
i_p = [8/14, 2/14, 2/14, 2/14]
o = ["o","ô","ó","ò","ö"]
o_p = [8/15, 2/15, 2/15, 2/15, 1/15]
u = ["u","ü","ù","ú","û"]
u_p = [8/15, 2/15, 2/15, 2/15, 1/15]
y = ["y","ý"]
c = ["c","č","ć"]
r = ["r","ř"]
s = ["s","š","ś"]
n = ["n","ň","ń"]
d = ["d","đ"]
l = ["l","ł"]
g = ["g","ğ"]
z = ["z","ž","ź"]

# I just picked some keys from my keyboard. This translator should remove everything here before getting to this point
cocanb_char = "|"
cocan_char = "&"
non_char = "¦"
no_char = "¬"
special_char = "¤"

def add_diacritics(initial):
    initial = sub("[nňń][oóòôö]$", no_char, sub("[nňń][oóòôö][nňń]", non_char, sub("[cćč][oóòôö][cćč][aáàâä]$", cocan_char, sub("[cćč][oóòôö][cćč][aáàâä][nňń]", cocanb_char, initial))))
    special = findall("<.*>", initial)
    initial = sub("<.*>", special_char, initial)
    final = []
    for letter in initial:
        if letter == "a":
            final.append(choice(a, p=a_p))
        elif letter == "e":
            final.append(choice(e, p=e_p))
        elif letter == "i":
            final.append(choice(i, p=i_p))
        elif letter == "o":
            final.append(choice(o, p=o_p))
        elif letter == "u":
            final.append(choice(u, p=u_p))
        elif letter == "y":
            final.append(choice(y))
        elif letter == "c":
            final.append(choice(c))
        elif letter == "r":
            final.append(choice(r))
        elif letter == "s":
            final.append(choice(s))
        elif letter == "n":
            final.append(choice(n))
        elif letter == "d":
            final.append(choice(d))
        elif letter == "l":
            final.append(choice(l))
        elif letter == "g":
            final.append(choice(g))
        elif letter == "z":
            final.append(choice(z))
        else:
            final.append(letter)
    output = "".join(final)
    output = output.replace(cocanb_char, "Cocán").replace(cocan_char, "Cocá").replace(non_char, choice(["nön", "nôn", "nón", "nòn"])).replace(no_char, choice(["nö", "nô", "nó", "nò"]))
    for sp in special:
        output = output.replace(special_char, sp)
    return output
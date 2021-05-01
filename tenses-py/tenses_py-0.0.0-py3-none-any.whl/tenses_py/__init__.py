class Continuous:
    def __init__(self, cont):
        self.cont = cont
        self.string = "ing"
        
        vowels = "aeiou"
        # Get vowels
        res = set([each for each in cont if each in vowels])
        #Convert to string
        res = ''.join(res) 
        #The exceptions in English
        if cont[-1] == "t" and cont[-2] == res:
            print(cont + cont[-1] + self.string)
        elif cont[-2:] == "ie":
            print(cont.replace(cont[-2:], "y") + self.string)
        elif cont[-1] == "c":
            print(cont + "k" + self.string)
        elif cont[-1] and cont[-2] == "e":
            print(cont + self.string)
        elif cont[-1] == "e":
            print(cont.replace(cont[-1], '') + self.string)
        elif cont[-1] == "m":
            print(cont + cont[-1] + self.string)
        else:
            print(cont + self.string)

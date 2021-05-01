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


        
    
class Past:
    def __init__(self, past):
        
        self.past = past
        
        def f(v):
            T,x,m='aeiou',"ed",v[-1];return[[[v+x,v+m+x][v[-2]in T and m and v[-3]not in T],[v+x,v[:-1]+"ied"][v[-2]not in T]][m=='y'],v+"d"][m=='e']
        if past == "go":
            print("went")
        elif past == "get":
            print("got")
        elif past == "eat":
            print("ate")
        else:
            print(f(past))
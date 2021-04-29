class Past:
    def __init__(self, past):
        """
        self.past = past
        past.hello = str(input("Enter a word:"))
        """
        self.past = past

        def f(v):
            T,x,m='aeiou',"ed",v[-1];return[[[v+x,v+m+x][v[-2]in T and m and v[-3]not in T],[v+x,v[:-1]+"ied"][v[-2]not in T]][m=='y'],v+"d"][m=='e']
        if past == "go":
            print("went")
        elif past == "get":
            print("got")
        elif past == "eat":
            print("ate")
        elif past == "put" or "cut":
            print(past)
        else:
            print(f(past))



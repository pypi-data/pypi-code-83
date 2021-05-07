import time
# Important note
# ==============
# This prorgam does not use threads for a reason : all tests have also access to the same resources.
# ##
class test():
    """
    A wonderful class to test things
    """
    def __init__(self, nb = 1, gen = None, genParams = None, verif = None, displayRound = 5) -> None:
        self.functions = {}
        self.time = {}
        self.nb = nb
        self.generator = gen
        self.genParams = genParams
        self.verif = verif
        self.displayRound = displayRound
    def params(self, nb = None, gen = None, genParams = None, verif = None, displayRound = None):
        """
        Allows us to set all parameters
        """
        if nb : self.nb = int(round(nb))
        if gen : self.generator = gen
        if genParams : self.genParams = genParams
        if verif : self.verif = verif
        if displayRound : self.displayRound = displayRound
    def add(self, name, fonction):
        """
        to add a function to the test queue
        """
        self.functions[name] = (fonction)
    def run(self, report = True):
        """
        Run the tests
        """
        self.generated = []
        for i in range(self.nb):
            self.generated.append(self.generator(self.genParams))
        for name, fonction in self.functions.items():
            self.time[name] = []
            for n in self.generated:
                self.timeOne = time.time()
                self.result = fonction(n)
                self.timeTwo = time.time()
                self.time[name].append((self.timeTwo - self.timeOne, self.verif(self.result, n)))
        if report :
            self.report(self.time)
        return self.time
    def report(self, data):
        """
        Make a human readable report
        """
        print(". . . generating stats . . .")
        self.stats = {}
        for name, results in data.items():
            self.stats[name] = {'time':{}, 'success':0}
            self.stats[name]['time']['average'] = round((sum(i[0] for i in results)/len(results)), self.displayRound)
            self.stats[name]['time']['minimum'] = round(min(i[0] for i in results), self.displayRound)
            self.stats[name]['time']['maximum'] = round(max(i[0] for i in results), self.displayRound)
            self.stats[name]['success'] = round(len(i for i in results if i[1]) / len(results) * 100, 2)
        print("#"*42)
        print("RESULTS FOR " + str(self.stats) + " TEST(S)")
        print("#######\n")
        print("*** time stats ***")
        self.rank = 1
        for name, stat in sorted(self.stats.items(), key=lambda t: t['time']['average']):
            print(" -> " + str(name))
            print("    rank : #" + str(self.rank))
            print("    average = " + str(stat['time']['average']))
            print("    minimum = " + str(stat['time']['minimum']))
            print("    maximum = " + str(stat['time']['maximum']))
            print("")
            self.rank += 1
        print("\n*** success stats ***")
        self.rank = 1
        for name, stat in reversed(sorted(self.stats.items(), key=lambda t: t['success'])):
            print(" -> " + str(name))
            print("    rank : #" + str(self.rank))
            print("    success = " + str(stat['success']) + " %")
            print("")
            self.rank += 1
        print("#"*42)
        return self.stats
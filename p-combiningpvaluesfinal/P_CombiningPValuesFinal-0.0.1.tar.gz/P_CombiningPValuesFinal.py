#Purpose: Combining P-values methodology
#Author: Breya McGlown
#Math Master's Thesis
"""
    Functions within this module allow for multiple p values
    to be defined within each method below
    Method options include: Fisher, Pearson, Ed, Stouffer, George, Tippett
"""
__version__ = "0.0.1"

import pandas as pd
import numpy as np
import copy
import statistics as st
import scipy
from scipy.stats import norm
import math as mt
from scipy.stats import chisquare
from scipy.stats import t

class CountPs:
    """
    Functions within this class allow for multiple p values
    to be defined within each method below
    Method options include: Fisher, Pearson, Ed, Stouffer, George, Tippett
    """

    def __init__(self, method):
        self.method = method

    def InfinitePs(self, *args):
        """
        Select n number of p-values to use with desired method
        enter p values into args parameter
        """
        if self.method == self.method:
            pass
        return list(args)

    def FisherMethod(self,output):
        """
        Fishers method
        """
        if self.method == 'Fisher':
            self.output = output
            List = output
            temp = []
            for x in List:
                temp.append(mt.log(x))
            temp1 = sum(temp)
            output = -2 * temp1 #-2SF is distributed chisquare 2 ddof

        return output

    def PearsonMethod(self,output):
        """
        Pearsons Method
        """
        if self.method == 'Pearson':
                self.output = output
                List = output
                temp = []
                for x in List:
                    temp.append(-mt.log(1 - x))
                temp1 = sum(temp)
                output = -2 * temp1 #-2SP is distributed chisquare 2 ddof

        return output

    def GeorgeMethod(self,output):
        """
        Georges Method
        """
        if self.method == 'George':
                self.output = output
                List = output
                temp = []
                for x in List:
                    temp.append(mt.log(x/(1 - x)))
                temp1 = sum(temp)
                output = temp1 #SG is distributed Gamma or Gaussian distribution #TODO ask Dr George if Gamma distirbution or gaussian

        return output

    def EdMethod (self,output):
        """
        Edgington's Method
        """

        if self.method == 'Ed':
            self.output = output
            List = output
            temp = []
            for x in List:
                temp.append(x)
            temp1 = sum(temp)
            output = temp1 #SE is Gaussian Distribution

        return output

    def StoufferMethod(self,output):
        """
        StoufferMethod
        """

        if self.method == 'Stouffer':
            self.output = output
            List = output
            temp = []
            for x in List:
                temp.append(norm.ppf(x)) #inverse CDF
            temp1 = sum(temp)
            output = temp1 #SS is N(0,n)

        return output

    def TippettMethod(self,output):
        """
        Tippett Method
        """
        if self.method == 'Tippett':
            self.output = output
            List = output
            output = min(List) #ST is Beta(1,n)

        return output


if __name__ == "__main__":
 
    A = CountPs('Stouffer') #Fisher, Pearson, Ed, Stouffer, George, Tippett
    Output = A.InfinitePs(0.1,.3,.7)
    Final = A.StoufferMethod(Output)
    SignOrNot = A.DetermineSig(Final)
    print(Final)

    #Test
    #random generator 10,12,15,18,20 N(mu,sigma^2) various values of mu and sigma^2
    mu = np.random.random_integers(low = 1,high = 10, size = 1)
    sigma = np.random.random_integers(low = 0,high = 10, size = 1)
    List = [10,12,15,18,20] #sample size
    PvalsFromPaper = [0.585,0.76,0.365,0.905,0.08,0.265,0.405,0.76,0.1,0.25,0.185,0.115,0.525,0.035,0.65,0.035,0.075,0.01,0.205,0.43,0.52,0.435,0.12]
    for x in List:
        Various = np.random.normal(mu, sigma, x)
        Pvalues = norm.cdf(Various)
        Output = A.InfinitePs(Pvalues)
        #Get P values and combine
        Final = A.StoufferMethod(Output[0])
        #print(Final)
        SignOrNot = A.DetermineSig(Final)

    #Get P values and Combine

    #random generator 10,12,15,18,20 t-statistic N(0,sigma^2)
    #Based on t-statistic each sample to test mu = 0. get P values and combine
    #mu = 0
    #sigma = np.random.random_integers(low = 1,high = 10, size = 1)
    List = [10,12,15,18,20] #sample size
    for x in List:
        Various = t.rvs(x-1, size = x)
        Pvalues = t.cdf(Various,x-1)
        Output = A.InfinitePs(Pvalues)
        #Get P values and combine
        Final = A.StoufferMethod(Output[0])
        print(Final)
        SignOrNot = A.DetermineSig(Final)

    #Testing functionality based on P values provided by Cheng and Sheng paper
    
    Test = A.InfinitePs(PvalsFromPaper)
    print(Test)
    #Stouffer's test
    A = CountPs('Stouffer')
    StouffersOut = A.StoufferMethod(copy.deepcopy(Test[0]))
    print(StouffersOut)
    #Tippet's test
    A = CountPs('Fisher')
    FishersOut = A.FisherMethod(PvalsFromPaper)
    print(FishersOut)

    

    



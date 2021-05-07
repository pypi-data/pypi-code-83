# Reference
__all__ = ["statisticalTest"]

class statisticalTest:
    def __init__(self):
        # Initialize Statistical Test Flowchart
        print("Choose a proper Statistical Test for your requirements.")
        print("Reference: https://www.scribbr.com/statistics/statistical-tests/")
    
    def questionnaire(self):
        """
        Call function questionnaire() directly.
        """

        self._predictor()

    def _checkUserInput(self, userInput, maxChoice):
        #return type(userInput)
        assert type(userInput) == str, 'Input must be a integer'
        if int(userInput) in range(1, maxChoice+1):
            return int(userInput)
        else:
            raise Exception(f'Input must be one of {list(range(1, maxChoice+1))}')

    def _predictor(self):
        predictorType = input(
            '''
            Type of Predictor Variables:
            1. Categorical
            2. Quantitative
            ''')
        predictorCount = input(
            '''
            Number of Predictor Variables:
            1. One
            2. Two or More
            ''')
        predictorType = self._checkUserInput(predictorType, 2)
        predictorCount = self._checkUserInput(predictorCount, 2)
        predictorVars = [predictorType, predictorCount]
        
        if predictorType == 1:
            if predictorCount == 1:
                pass
            else:
                pass
        else:
            if predictorCount == 1:
                pass
            else:
                pass
        
        self._outcome(predictorVars)
                
    def _outcome(self, predictorVars):
        outcomeType = input(
            '''
            Type of Outcome Variables:
            1. Categorical
            2. Quantitative
            ''')
        outcomeCount = input(
            '''
            Number of Outcome Variables:
            1. One
            2. Two or More
            ''')
        outcomeType = self._checkUserInput(outcomeType, 2)
        outcomeCount = self._checkUserInput(outcomeCount, 2)
        outcomeVars = [outcomeType, outcomeCount]
 
        if (predictorVars == [1, 1]) & (outcomeVars == [1, 1]):
            self._chisqure()
        elif (predictorVars == [1, 1]) & (outcomeVars == [2, 1]):
            self._ttest()
        elif (predictorVars == [1, 2]) & (outcomeVars == [2, 1]):
            self._anova()
        elif (predictorVars == [1, 2]) & (outcomeVars == [2, 2]):
            self._manova()
        elif (predictorVars == [2, 1]) & (outcomeVars == [2, 1]):
            self._linearRegression('simple')
        elif (predictorVars == [2, 2]) & (outcomeVars == [1, 1]):
            self._logisticRegression()
        elif (predictorVars == [2, 2]) & (outcomeVars == [2, 1]):
            self._linearRegression('multiple')

        
    def _chisqure(self):
        print('Chi-Square test')
        print("Pearson's chi-squared test is used to determine whether there is a statistically significant difference between the expected frequencies and the observed frequencies in one or more categories of a contingency table.")

    def _ttest(self):
        popType = input(
            '''
            Groups from the same population?
            1. Yes
            2. No
            ''')
        popType = self._checkUserInput(popType, 2)
        if popType == 1:
            print('Paired t-test')
            print('Example: What is the effect of two different test prep programs on the average exam scores for students from the same class?')
        else:
            print('Independent t-test')
            print('Example: What is the difference in average exam scores for students from two different schools?')

    def _anova(self):
        print('ANOVA test')
        print('Example: What is the difference in average pain levels among post-surgical patients given three different painkillers?')
        
    def _manova(self):
        print('MANOVA test')
        print('Example: What is the effect of flower species on petal length, petal width, and stem length?')
        
    def _linearRegression(self, t):
        if t == 'simple':
            print('Simple Linear Regression')
            print('Example: What is the effect of income on longevity?')
        else:
            print('Multiple Linear Regression')
            print('Example: What is the effect of income and minutes of exercise per day on longevity?')
            
    def _logisticRegression(self):
        print('Logistic Regression')
        print('Example: What is the effect of drug dosage on the survival of a test subject?')
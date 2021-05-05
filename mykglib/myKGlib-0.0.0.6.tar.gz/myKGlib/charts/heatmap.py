from .chart import Chart
import seaborn as sns

class HeatMap(Chart):
    def __init__(self, dataframe):
        """
        Constructs all the necessary attributes for the HeatMap object

        Parameters:
            dataframe (pandas.Dataframe): The dataframe
        """
        Chart.__init__(self, dataframe)

    def plot(self):
        """
        Generate HeatMap visualization
        """

        if self._is_integer_column_exist(3):
            #plot HeatMap
            sns.heatmap(self.dataframe.corr(), annot = True)
            pass
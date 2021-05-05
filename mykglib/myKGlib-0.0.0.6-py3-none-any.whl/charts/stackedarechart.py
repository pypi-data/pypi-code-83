from .chart import Chart
import matplotlib.pyplot as plt
import plotly.express as px

class StackedAreaChart(Chart):
    def __init__(self, dataframe):
        """
        Constructs all the necessary attributes for the StackedAreaChart object

        Parameters:
            dataframe (pandas.Dataframe): The dataframe
        """
        Chart.__init__(self, dataframe)

    def _check_requirements(self):
        """
        Check the requirements for generating StackedAreaChart visualization

        Returns:
            (string) date_label: date label  for axis-x
            (list) integer_columns: integer/float list
        """
        date_label = None
        integer_column = None

        if self._is_date_column_exist(1):
            date_label = self._date_column[0]
            if self._is_integer_column_exist(1):
                integer_column = self._integer_column
        
        return date_label, integer_column          
  

    def plot(self):
        """
        Generate StackedAreaChart visualization
        """
        date_label, integer_column  = self._check_requirements()

        if date_label is not None and integer_column is not None:
            #set index by date label
            dataframe = self.dataframe.copy()
            dataframe = dataframe.set_index(date_label)
            #plot
            ax = dataframe.plot.area(stacked=True)
            plt.show(block=True)


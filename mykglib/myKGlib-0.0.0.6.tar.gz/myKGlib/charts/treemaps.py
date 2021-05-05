from .chart import Chart
import plotly.express as px

class TreeMap(Chart):
    def __init__(self, dataframe):
        """
        Constructs all the necessary attributes for the TreeMap object

        Parameters:
            dataframe (pandas.Dataframe): The dataframe
        """
        Chart.__init__(self, dataframe)

    def _check_requirements(self):
        """
        Check the requirements for generating TreeMap visualization

        Returns:
            (list) label_column: label name
            (list) integer_column: list of integer column
        """
        label_column = None
        integer_column = None
        
        if self._is_object_column_exist(1):
            label_column = self._object_column
            if self._is_integer_column_exist(1):
                integer_column = self._integer_column

        
        return label_column, integer_column    

    def plot(self):
        """
        Generate TreeMap visualization
        """
        label_column, integer_column  = self._check_requirements()

        if label_column is not None and integer_column is not None:
            values_label,hover_label = self._check_integer_columns()
            if hover_label is not None:
                #plot
                fig = px.treemap(self.dataframe, values=values_label, path=label_column, hover_data=[hover_label], labels={hover_label:hover_label})
                fig.show()
            else:
                fig = px.treemap(self.dataframe, values=values_label, path=label_column)
                fig.show()                



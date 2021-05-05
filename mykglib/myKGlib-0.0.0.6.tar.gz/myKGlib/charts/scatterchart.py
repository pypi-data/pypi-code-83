from .chart import Chart
import plotly.express as px

class ScatterChart(Chart):
    def __init__(self, dataframe):
        """
        Constructs all the necessary attributes for the ScatterChart object

        Parameters:
            dataframe (pandas.Dataframe): The dataframe
        """
        Chart.__init__(self, dataframe)

    def _check_requirements(self):
        """
        Check the requirements for generating ScatterChart visualization

        Returns:
            (list) integer_columns: list of integer/float column
            (string) label_name: label name
        """
        integer_columns = None
        label_name = None

        if self._is_integer_column_exist(2):
            integer_columns = self._integer_column
            if len(self._object_column) > 0:
                label_name = self._object_column[0]
        
        return integer_columns, label_name    

    def plot(self):
        """
        Generate ScatterChart visualization
        """
        integer_columns, label_name = self._check_requirements()

        if integer_columns is not None:
            x_label = integer_columns[0]
            y_label = integer_columns[1]
            if label_name is not None:
                fig = px.scatter(self.dataframe, x=x_label, y=y_label, color=label_name)
                fig.show()
            else:
                fig = px.scatter(self.dataframe, x=x_label, y=y_label)
                fig.show()                
from .chart import Chart
import plotly.express as px

class DonutChart(Chart):
    def __init__(self, dataframe):
        """
        Constructs all the necessary attributes for the DonutChart object

        Parameters:
            dataframe (pandas.Dataframe): The dataframe
        """
        Chart.__init__(self, dataframe)

    def _check_requirements(self):
        """
        Check the requirements for generating DonutChart visualization

        Returns:
            (string) label_name: label name
            (list) integer_column: list of integer column
        """
        label_name = None
        integer_column = None
        
        if self._is_integer_column_exist(1):
            integer_column = self._integer_column
            if self._is_object_column_exist(1):
                if len(self._object_column) > 1:
                    axis_label, group_label = self._check_labels()
                    if group_label is not None:
                        label_name = group_label
                    else:
                        label_name = axis_label
                else:    
                    label_name = self._object_column[0]

        
        return label_name, integer_column    

    def plot(self):
        """
        Generate DonutChart visualization
        """
        label_name, integer_column  = self._check_requirements()

        if label_name is not None and integer_column is not None:
            values_label,hover_label = self._check_integer_columns()
            if hover_label is not None:
                #plot
                fig = px.pie(self.dataframe, values=values_label, names=label_name, hole=0.3,
                                hover_data=[hover_label])
                fig.show()
            else:
                fig = px.pie(self.dataframe, values=values_label, names=label_name, hole=0.3)
                fig.show()                




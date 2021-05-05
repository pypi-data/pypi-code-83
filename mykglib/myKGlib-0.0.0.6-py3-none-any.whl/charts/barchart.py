from .chart import Chart
import seaborn as sns
import plotly.express as px

class BarChart(Chart):
    def __init__(self, dataframe):
        """
        Constructs all the necessary attributes for the BarChart object

        Parameters:
            dataframe (pandas.Dataframe): The dataframe
        """
        Chart.__init__(self, dataframe)

    def _check_requirements(self):
        """
        Check the requirements for generating BarChart visualization

        Returns:
            (string) int_label: integer/float label 
            (list) label_column: label column
        """
        int_label = None
        label_column = None

        if self._is_integer_column_exist(1):
            int_label = self._integer_column[0]
            if self._is_object_column_exist(1):
                label_column = self._object_column
        
        return int_label, label_column    

    def plot(self):
        """
        Generate BarChart visualization
        """
        integer_label, label_column  = self._check_requirements()

        if label_column is not None and integer_label is not None:
            axis_label,group_label,make_axis_label = None,None, None
            if len(label_column) >= 3:
                axis_label,group_label,make_axis_label = self._check_labels()
            else:
                axis_label,group_label = self._check_labels()
                
            orientation = self._check_orientation(axis_label,group_label)

            if make_axis_label is not None:
                axis_label = make_axis_label
            else:
                pass

            if group_label is not None:
                if orientation is not None:
                    fig = px.bar(self.dataframe, x=integer_label, y=axis_label, color=group_label)
                    fig.show()
                else:
                    fig = px.bar(self.dataframe, x=axis_label, y=integer_label, color=group_label)
                    fig.show()
            else:
                if orientation is not None:
                    fig = px.bar(self.dataframe, x=integer_label, y=axis_label)
                    fig.show()
                else:
                    fig = px.bar(self.dataframe, x=axis_label, y=integer_label)
                    fig.show() 

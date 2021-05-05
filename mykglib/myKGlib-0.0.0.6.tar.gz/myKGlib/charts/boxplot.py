from .chart import Chart
import plotly.express as px

class BoxPlot(Chart):
    def __init__(self, dataframe):
        """
        Constructs all the necessary attributes for the BoxPlot object

        Parameters:
            dataframe (pandas.Dataframe): The dataframe
        """
        Chart.__init__(self, dataframe)

    def _check_requirements(self):
        """
        Check the requirements for generating BoxPlot visualization

        Returns:
            (string) integer_label: label of integer/float column
            (list) label_column: label column
        """
        integer_label = None
        label_column = None

        if self._is_integer_column_exist(1):
            integer_label = self._integer_column[0]
            if self._is_object_column_exist(1):
                label_column=self._object_column
                
        return integer_label, label_column      

    def plot(self):
        """
        Generate BoxPlot visualization
        """
        integer_label, label_column  = self._check_requirements()

        if integer_label is not None and label_column is not None:
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
                    fig = px.box(self.dataframe, x=integer_label, y=axis_label, color=group_label)
                    fig.show()
                else:
                    fig = px.box(self.dataframe, x=axis_label, y=integer_label, color=group_label)
                    fig.show()
            else:
                if orientation is not None:
                    fig = px.box(self.dataframe, x=integer_label, y=axis_label)
                    fig.show()
                else:
                    fig = px.box(self.dataframe, x=axis_label, y=integer_label)
                    fig.show()                     
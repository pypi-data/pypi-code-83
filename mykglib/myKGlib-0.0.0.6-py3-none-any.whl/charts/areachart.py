from .chart import Chart
import plotly.express as px

class AreaChart(Chart):
    def __init__(self, dataframe):
        """
        Constructs all the necessary attributes for the AreaChart object

        Parameters:
            dataframe (pandas.Dataframe): The dataframe
        """
        Chart.__init__(self, dataframe)

    def _check_requirements(self):
        """
        Check the requirements for generating AreaChart visualization

        Returns:
            (string) date_label: date label  for axis-x
            (string) int_label: integer/float label for axis-y
            (string) label_name: label name
        """
        date_label = None
        int_label = None
        label_name = None

        if self._is_date_column_exist(1):
            date_label = self._date_column[0]
            if self._is_integer_column_exist(1):
                int_label = self._integer_column[0]
                if self._is_object_column_exist(1):
                    label_name = self._object_column[0]
        
        return date_label, int_label, label_name          

    def plot(self):
        """
        Generate AreaChart visualization
        """
        date_label, integer_label, label_name  = self._check_requirements()

        if date_label is not None and integer_label is not None and label_name is not None:
            #plot
            fig = px.area(self.dataframe, x=date_label, y=integer_label, color=label_name, line_group=label_name)
            fig.show()


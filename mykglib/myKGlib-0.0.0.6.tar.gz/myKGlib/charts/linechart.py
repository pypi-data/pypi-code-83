from .chart import Chart
import plotly.express as px
import seaborn as sns

class LineChart(Chart):
    def __init__(self, dataframe):
        """
        Constructs all the necessary attributes for the LineChart object

        Parameters:
            dataframe (pandas.Dataframe): The dataframe
        """
        Chart.__init__(self, dataframe)

    def _check_requirements(self):
        """
        Check the requirements for generating LineChart visualization

        Returns:
            (string) date_label: date label  for axis-x
            (string) int_label: integer/float label for axis-y
            (string) label_name: label for hue
        """
        date_label = None
        int_label = None
        label_name = None

        if self._is_date_column_exist(1):
            date_label = self._date_column[0]
            if self._is_integer_column_exist(1):
                int_label = self._integer_column[0]
                if len(self._object_column) > 0:
                    label_name = self._object_column[0]
        
        return date_label, int_label, label_name      

    def plot(self):
        """
        Generate LineChart visualization
        """
        date_label, integer_label, label_name  = self._check_requirements()

        if date_label is not None and integer_label is not None:
            if label_name is not None:
                sns.lineplot(data=self.dataframe, x=date_label, y=integer_label, hue=label_name)
                pass
            else:
                fig = px.line(data_frame=self.dataframe, x=date_label, y=integer_label)
                fig.show()


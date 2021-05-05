from .chart import Chart
import seaborn as sns

class DensityPlot(Chart):
    def __init__(self, dataframe):
        """
        Constructs all the necessary attributes for the DensityPlot object

        Parameters:
            dataframe (pandas.Dataframe): The dataframe
        """
        Chart.__init__(self, dataframe)

    def _check_requirements(self):
        """
        Check the requirements for generating DensityPlot visualization

        Returns:
            (string) integer_label: label of integer/float column
            (string) label_name: label name
        """
        integer_label = None
        label_name = None

        if self._is_integer_column_exist(1):
            integer_label = self._integer_column[0]
            if len(self._object_column) > 0:
                unique_list = [len(self.dataframe[name].unique()) for name in self._object_column]
                min_unique = min(unique_list)
                idx_min_unique = unique_list.index(min(unique_list))
                if min_unique <= 5 and min_unique < len(self.dataframe):
                    label_name=self._object_column[idx_min_unique]

        return integer_label, label_name   

    def plot(self):
        """
        Generate DensityPlot visualization
        """
        integer_label, label_name  = self._check_requirements()

        if integer_label is not None:
            if label_name is not None:
                sns.displot(data=self.dataframe, x=integer_label, hue=label_name, kind="kde")
                pass
            else:
                sns.displot(data=self.dataframe, x=integer_label, kind="kde")
                pass               



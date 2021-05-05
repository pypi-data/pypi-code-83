import pandas as pd
import matplotlib.pyplot as plt

from .processing import set_dataframe, set_mode
from .charts import Chart
from .charts import Table, ImageGrid
from .charts import Tree, Graph
from .charts import HeatMap, Dimensions
from .charts import WordCloud, Map
from .charts import BubbleChart, ScatterChart
from .charts import DensityPlot, Histogram
from .charts import BoxPlot, ViolinPlot, BarChart
from .charts import DonutChart, PieChart
from .charts import SunBurstChart, TreeMap
from .charts import LineChart, Timeline
from .charts import AreaChart,StackedAreaChart

class vizKG:
  """
  Instantiate vizKG object.
  
  Attributes:
      sparql_query (string): The SPARQL query to retrieve.
      sparql_service_url (string): The SPARQL endpoint URL.
      mode (string): Type of visualization
                     Default = 'Table'
                     Options = {'Table', 'ImageGrid', 'Timeline' 'Graph' 
                                'Map', 'Tree','WordCloud', 'Dimensions',
                                'LineChart', 'BarChart', 'Histogram',
                                'DensityPlot', 'TreeMap' ,'SunBurstChart', 
                                'HeatMap' ,'PieChart', 'DonutChart',
                                'BoxPlot' ,'ViolinPlot', 'AreaChart',
                                'StackedAreaChart', 'ScatterChart', 'BubbleChart'}.
      dataframe (pandas.Dataframe): The data table                 
  """

  def __init__(self, sparql_query, sparql_service_url, mode='Table'):
      """
      Constructs all the necessary attributes for the vizKG object

      Parameters:
          sparql_query (string): The SPARQL query to retrieve.
          sparql_service_url (string): The SPARQL endpoint URL.
          mode (string): Type of visualization
          dataframe (pandas.Dataframe): The data table
      """

      self.sparql_query = sparql_query
      self.sparql_service_url = sparql_service_url
      self.mode = set_mode(mode)
      self.dataframe = set_dataframe(sparql_query, sparql_service_url)

  def plot(self):
      """
      Plot visualization with suitable corresponding mode

      """
      mode_list = ['ImageGrid', 'Timeline', 'Graph', 'Dimensions', 'Map', 'Tree',
                    'WordCloud', 'LineChart', 'BarChart', 'Histogram' ,'DensityPlot',
                     'TreeMap' ,'SunBurstChart', 'HeatMap' ,'PieChart', 'DonutChart',
                     'BoxPlot' ,'ViolinPlot', 'AreaChart', 'StackedAreaChart',
                      'ScatterChart', 'BubbleChart', 'Table']
      mode_list = [name.lower() for name in mode_list]
      chart = Chart(self.dataframe)
      candidate_visualization = chart.candidate_form()
      figure = None

      if len(self.dataframe) != 0:
        if self.mode not in mode_list:
          print("no matching mode found instead use one of the available mode:", *candidate_visualization, sep = " ")
        else:
          try:
            if self.mode == 'imagegrid':
              figure = ImageGrid(self.dataframe)
            elif self.mode == 'timeline':
              figure = Timeline(self.dataframe)
            elif self.mode == 'graph':
              figure = Graph(self.dataframe)
            elif self.mode == 'dimensions':
              figure = Dimensions(self.dataframe)          
            elif self.mode == 'map':
              figure = Map(self.dataframe)
            elif self.mode == 'tree':
              figure = Tree(self.dataframe)
            elif self.mode == 'wordcloud':
              figure = WordCloud(self.dataframe)      
            elif self.mode == 'linechart':
              figure = LineChart(self.dataframe)
            elif self.mode == 'barchart':
              figure = BarChart(self.dataframe)
            elif self.mode == 'histogram':
              figure = Histogram(self.dataframe)
            elif self.mode == 'densityplot':
              figure = DensityPlot(self.dataframe)
            elif self.mode == 'treemap':
              figure = TreeMap(self.dataframe)
            elif self.mode == 'sunburstchart':
              figure = SunBurstChart(self.dataframe)
            elif self.mode == 'heatmap':
              figure = HeatMap(self.dataframe)
            elif self.mode == 'piechart':
              figure = PieChart(self.dataframe)
            elif self.mode == 'donutchart':
              figure = DonutChart(self.dataframe)
            elif self.mode == 'boxplot':
              figure = BoxPlot(self.dataframe)
            elif self.mode == 'violinplot':
              figure = ViolinPlot(self.dataframe)
            elif self.mode == 'areachart':
              figure = AreaChart(self.dataframe)
            elif self.mode == 'stackedareachart':
              figure = StackedAreaChart(self.dataframe)
            elif self.mode == 'scatterchart':
              figure = ScatterChart(self.dataframe)
            elif self.mode == 'bubblechart':
              figure = BubbleChart(self.dataframe)
            else:
              figure = Table(self.dataframe)
          finally:
            figure.plot()
      else:
        print("No matching records found")
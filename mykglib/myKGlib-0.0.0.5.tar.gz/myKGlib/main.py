import re
import time
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
import seaborn as sns
import networkx as nx
import folium

from pandas import json_normalize
from SPARQLWrapper import SPARQLWrapper
from anytree import Node, RenderTree
from wordcloud import WordCloud
from IPython.display import display
from imageio import imread


from .bubbleChart import BubbleChart

class vizKG:
  """
  Instantiate vizKG object.
  
  Attributes:
      sparql_query (string): The SPARQL query to retrieve.
      sparql_service_url (string): The SPARQL endpoint URL.
      mode (string): Type of visualization
                     Default = 'Table'
                     Options = {'Table', 'ImageGrid', 'Timeline',
                                'ImageGrid', 'Timeline', 'Graph', 
                                'Dimensions', 'Map', 'Tree','WordCloud', 
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
      self.mode = mode
      self.dataframe = self.query_result()
      

  def query_result(self, is_value='True'):
      """
      Query the endpoint with the given query string.

      Parameters:
          is_value (bool): The boolean to filter (dot)value column.

      Returns:
          (pandas.Dataframe) table: The Query Result      
      """

      sparql = SPARQLWrapper(self.sparql_service_url, agent="Sparql Wrapper on Jupyter example")  
      
      sparql.setQuery(self.sparql_query)
      sparql.setReturnFormat('json')

      # ask for the result
      result = sparql.query().convert()
      table  = json_normalize(result["results"]["bindings"])

      #extract value
      if is_value:
        df = table.filter(regex='.value')
        table = df.rename(columns = lambda col: col.replace(".value", ""))
      
      #rename column
      table = self.__rename_column(table)

      return table


  def __rename_column(self, dataframe):
      """
      Rename column of dataframe based on regex validity check

          :param (pandas.Dataframe) dataframe: The table of query result.

      Returns:
          (pandas.Dataframe) table: The result of renaming table column             
      """

      #Regex pattern
      pattern_url = r"^(?:http(s)?:\/\/)[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&'\(\)\*\+,;=.]+$(?<!.[jpg|gif|png|JPG|PNG])" #regex url
      pattern_img = r"^http(s)?://(?:[a-z0-9\-]+\.)+[a-z]{2,6}(?:/[^/#?]+)+\.(?:jpg|jpeg|gif|png|JPG|JPEG|Jpeg)$"        #regex img
      pattern_coordinate = r"^Point"
      pattern_label = r"Label$"

      for i in range (len(dataframe.columns)):
        check = dataframe[dataframe.columns[i]].iloc[0]
        if re.match(pattern_url, check):
          if 'uri' in dataframe.columns:
            if 'uri2' in dataframe.columns:
              dataframe = dataframe.rename(columns={dataframe.columns[i]: "uri_"+str(dataframe.columns[i])}, errors="raise")
            else:          
              dataframe = dataframe.rename(columns={dataframe.columns[i]: "uri2"}, errors="raise")
          else:
            dataframe = dataframe.rename(columns={dataframe.columns[i]: "uri"}, errors="raise")
        elif re.match(pattern_img, check): 
          dataframe =  dataframe.rename(columns={dataframe.columns[i]: "pic"}, errors="raise")
        elif re.match(pattern_coordinate, check):
          dataframe =  dataframe.rename(columns={dataframe.columns[i]: "coordinate"}, errors="raise")
        elif i == len(dataframe.columns)-1 and (re.match(pattern_label, check)):
          dataframe = dataframe.rename(columns={dataframe.columns[i]: dataframe.columns[i]}, errors="raise")

      #change data types in each column
      dataframe = self.__change_dtypes(dataframe)  
      
      return dataframe


  def __change_dtypes(self, dataframe):
      """
      Change data type column of dataframe

          :param dataframe (pandas.Dataframe): The result of renaming table column .

      Returns:
          (pandas.Dataframe) table: The result of changing data type table column             
      """

      for column in dataframe:
        try:
          dataframe[column] = dataframe[column].astype('datetime64')
        except ValueError:
          pass
      for column in dataframe:
        try:
          dataframe[column] = dataframe[column].astype('float64')
        except (ValueError, TypeError):
          pass

      return dataframe

  def candidate_form(self, dataframe):
      """
      Find candidate form for visualization

      Parameter:
          dataframe (pandas.Dataframe): The data table

      Returns:
          candidate_visualization (list): List of candidate visualization
      """

      candidate_visualization = []

      #reserved name column
      reserved_name = ['uri', 'pic', 'coordinate']

      #Get column based on particular value
      date_column = [name for name in self.dataframe.columns if self.dataframe[name].dtypes == 'datetime64[ns]']
      integer_column = [name for name in self.dataframe.columns if self.dataframe[name].dtypes == 'float64']
      object_column = [name for name in self.dataframe.columns if not name.startswith(tuple(reserved_name)) and self.dataframe[name].dtypes == 'object']
      dimension_column = [name for name in self.dataframe.columns if not name.startswith(tuple(['pic', 'coordinate']))]
      uri_column = [name for name in self.dataframe.columns if name.startswith('uri')]

      num_date_column = len(date_column)
      num_integer_column = len(integer_column)
      num_object_column = len(object_column)
      num_dimension_column = len(dimension_column)
      num_uri_column = len(uri_column) 
      
      #Add to candidate visualization
      if 'pic' in self.dataframe.columns:
        candidate_visualization.append('ImageGrid')
      if 'coordinate' in self.dataframe.columns:
        candidate_visualization.append('Map')
      if num_date_column == 2:
        candidate_visualization.append('Timeline')
      if num_object_column == 2 and num_uri_column == 2:
        candidate_visualization.append('Graph')
        candidate_visualization.append('Tree')
      if num_dimension_column >= 2 :
        candidate_visualization.append('Dimensions')
      if num_object_column >= 1:
        candidate_visualization.append('WordCloud')
      if num_object_column == 1 and num_date_column == 1 and num_integer_column == 1:
        candidate_visualization.append('AreaChart')
      if num_date_column == 1 and num_integer_column >= 1:
        candidate_visualization.append('StackedAreaChart')
      if num_object_column == 1 and num_integer_column == 2:
        candidate_visualization.append('ScatterChart')
      if num_date_column == 1 and num_integer_column == 1:
        candidate_visualization.append('LineChart')
      if num_object_column <= 2 and num_integer_column == 1:
        candidate_visualization.append('BarChart')
      if num_object_column >= 2 and num_integer_column == 1:
        candidate_visualization.append('TreeMap')
        candidate_visualization.append('SunBurstChart')
      if num_integer_column == 1:
        candidate_visualization.append('Histogram')
        candidate_visualization.append('DensityPlot')
      if num_object_column == 1 and num_integer_column == 1:
        candidate_visualization.append('PieChart')
        candidate_visualization.append('DonutChart')
        candidate_visualization.append('BoxPlot')
        candidate_visualization.append('ViolinPlot')
        candidate_visualization.append('BubbleChart')
        candidate_visualization.append('TreeMap')
        candidate_visualization.append('SunBurstChart')
      if num_integer_column >= 3:
        candidate_visualization.append('HeatMap')
      else:
        candidate_visualization.append('Table')

      return candidate_visualization

  def plot(self):
      """
      Plot visualization with suitable corresponding mode

      """
      mode_list = ['ImageGrid', 'Timeline', 'Graph', 'Dimensions', 'Map', 'Tree',
                    'WordCloud', 'LineChart', 'BarChart', 'Histogram' ,'DensityPlot',
                     'TreeMap' ,'SunBurstChart', 'HeatMap' ,'PieChart', 'DonutChart',
                     'BoxPlot' ,'ViolinPlot', 'AreaChart', 'StackedAreaChart',
                      'ScatterChart', 'BubbleChart', 'Table']
      candidate_visualization = self.candidate_form(self.dataframe)
      mode = self.mode

      if len(self.dataframe) != 0:
        if self.mode not in mode_list:
          print("no matching mode found instead use one of the available mode ", *candidate_visualization, sep = ", ")
        else:
          if self.mode == 'ImageGrid':
            self.ImageGrid(self.dataframe)
          elif self.mode == 'Timeline':
            self.Timeline(self.dataframe)
          elif self.mode == 'Graph':
            self.Graph(self.dataframe)
          elif self.mode == 'Dimensions':
            self.Dimensions(self.dataframe)
          elif self.mode == 'Map':
            self.Map(self.dataframe)
          elif self.mode == 'Tree':
            self.Tree(self.dataframe)
          elif self.mode == 'WordCloud':
            self.WordCloud(self.dataframe)         
          elif self.mode == 'LineChart':
            self.LineChart(self.dataframe)
          elif self.mode == 'BarChart':
            self.BarChart(self.dataframe)
          elif self.mode == 'Histogram':
            self.Histogram(self.dataframe)
          elif self.mode == 'DensityPlot':
            self.DensityPlot(self.dataframe)
          elif self.mode == 'TreeMap':
            self.TreeMap(self.dataframe) 
          elif self.mode == 'SunBurstChart':
            self.SunBurstChart(self.dataframe)
          elif self.mode == 'HeatMap':
            self.HeatMap(self.dataframe)
          elif self.mode == 'PieChart':
            self.PieChart(self.dataframe)
          elif self.mode == 'DonutChart':
            self.DonutChart(self.dataframe)
          elif self.mode == 'BoxPlot':
            self.BoxPlot(self.dataframe)
          elif self.mode == 'ViolinPlot':
            self.ViolinPlot(self.dataframe)
          elif self.mode == 'AreaChart':
            self.AreaChart(self.dataframe)
          elif self.mode == 'StackedAreaChart':
            self.StackedAreaChart(self.dataframe)
          elif self.mode == 'ScatterChart':
            self.ScatterChart(self.dataframe)
          elif self.mode == 'BubbleChart':
            self.BubbleCharts(self.dataframe)
          else:
            self.SimpleTable(self.dataframe)
      else:
        print("No matching records found")
    
  @staticmethod
  def ScatterChart(dataframe):
    """
    Generate ScatterChart visualization

    :param dataframe (pandas.Dataframe): data for visualization
    """
    #Get column name based on data type
    integer_columns = [name for name in dataframe.columns if dataframe[name].dtypes == 'float64']
    x_label = integer_columns[0]
    y_label = integer_columns[1]
    if len(integer_columns) >= 2:
      object_label = [name for name in dataframe.columns if name != x_label and name != y_label][0]
      object_label = [name for name in dataframe.columns if not name.startswith(tuple(['uri', 'coordinate', 'pic'])) and dataframe[name].dtypes == 'object'][0]
      if object_label != '':
        #plot
        fig = px.scatter(dataframe, x=x_label, y=y_label, color=object_label)
        fig.show()
      else:
        print("'ScatterChart' needs atleast 3 attributes of dataframe and one of them as label")
    else:
      print("'ScatterChart' needs 2 attributes with 'float' data type")


  @staticmethod
  def StackedAreaChart(dataframe):
    """
    Generate StackedAreaChart visualization

    :param dataframe (pandas.Dataframe): data for visualization
    """
    #Get column name based on data type
    integer_columns = [name for name in dataframe.columns if dataframe[name].dtypes == 'float64']
    if len(integer_columns) >= 1:
      date_label = [name for name in dataframe.columns if dataframe[name].dtypes == 'datetime64[ns]'][0]
      if date_label != '':
        #set index by date label
        dataframe = dataframe.set_index(date_label)
        #plot
        ax = dataframe.plot.area(stacked=True)
        plt.show(block=True)
      else:
        print("'StackedAreaChart' needs 1 attributes with 'date' data type as axis-x")
    else:
      print("'StackedAreaChart' needs atleast 1 attributes with 'float' data type")

  @staticmethod
  def AreaChart(dataframe):
    """
    Generate AreaChart visualization

    :param dataframe (pandas.Dataframe): data for visualization
    """
    #Get column name based on data type
    object_label = [name for name in dataframe.columns if not name.startswith(tuple(['uri', 'coordinate', 'pic'])) and dataframe[name].dtypes == 'object'][0]
    integer_label = [name for name in dataframe.columns if dataframe[name].dtypes == 'float64'][0]
    date_label = [name for name in dataframe.columns if dataframe[name].dtypes == 'datetime64[ns]'][0]
    if integer_label != 0:
      if date_label != 0:
        if object_label != 0:
          #plot
          fig = px.area(dataframe, x=date_label, y=integer_label, color=object_label, line_group=object_label)
          fig.show()
        else:
          print("'AreaChart' needs atleast 3 attributes of dataframe and one of them as label")
      else:
        print("'AreaChart' needs 1 attributes with 'date' data type as axis-x")
    else:
      print("'AreaChart' needs 1 attributes with 'float' data type as axis-y")    


  @staticmethod
  def BubbleCharts(dataframe):
    """
    Generate BubbleChart visualization

    :param dataframe (pandas.Dataframe): data for visualization
    """
    #Get column name based on data type
    integer_label = [name for name in dataframe.columns if dataframe[name].dtypes == 'float64'][0]
    if integer_label != '':
      object_label = [name for name in dataframe.columns if not name.startswith(tuple(['uri', 'coordinate', 'pic'])) and dataframe[name].dtypes == 'object'][0]
      if object_label != '':
        #Plot
        bubble_chart = BubbleChart(area=dataframe[integer_label],
                              bubble_spacing=0.1)

        bubble_chart.collapse()

        fig, ax = plt.subplots(subplot_kw=dict(aspect="equal"))
        bubble_chart.plot(
            ax, dataframe[object_label])
        ax.axis("off")
        ax.relim()
        ax.autoscale_view()
        ax.set_title('Plot')

        plt.show()
      else:
        print("'BubbleChart' needs atleast 2 attributes of dataframe and one of them as label")
    else:
      print("'BubbleChart' needs 1 attribute with 'float' data type")

  @staticmethod
  def ViolinPlot(dataframe):
    """
    Generate ViolinPlot visualization

    :param dataframe (pandas.Dataframe): data for visualization
    """
    #Get column name based on data type
    integer_label = [name for name in dataframe.columns if dataframe[name].dtypes == 'float64'][0]
    if integer_label != '':
      object_label = [name for name in dataframe.columns if not name.startswith(tuple(['uri', 'coordinate', 'pic'])) and dataframe[name].dtypes == 'object'][0]
      if object_label != '':
        #Plot
        fig = px.violin(dataframe, x=object_label, y=integer_label)
        fig.show()
      else:
        print("'ViolinPlot' needs atleast 2 attributes of dataframe and one of them as label")
    else:
      print("'ViolinPlot' needs 1 attribute with 'float' data type")

  @staticmethod
  def BoxPlot(dataframe):
    """
    Generate BoxPlot visualization

    :param dataframe (pandas.Dataframe): data for visualization
    """
    #Get column name based on data type
    integer_label = [name for name in dataframe.columns if dataframe[name].dtypes == 'float64'][0]
    if integer_label != '':
      object_label = [name for name in dataframe.columns if not name.startswith(tuple(['uri', 'coordinate', 'pic'])) and dataframe[name].dtypes == 'object'][0]
      if object_label != '':
        #plot
        fig = px.box(dataframe, x=object_label, y=integer_label)
        fig.show()
      else:
        print("'BoxPlot' needs atleast 2 attributes of dataframe and one of them as label")
    else:
      print("'BoxPlot' needs 1 attribute with 'float' data type")

  @staticmethod
  def DonutChart(dataframe):
    """
    Generate DonutChart visualization

    :param dataframe (pandas.Dataframe): data for visualization
    """
    #Get column name based on data type
    integer_label = [name for name in dataframe.columns if dataframe[name].dtypes == 'float64'][0]
    if integer_label != '':
      object_label = [name for name in dataframe.columns if not name.startswith(tuple(['uri', 'coordinate', 'pic'])) and dataframe[name].dtypes == 'object'][0]
      if object_label != '':
        #plot
        fig = px.pie(dataframe, values=integer_label, names=object_label, hole=0.3)
        fig.show()
      else:
        print("'DonutChart' needs atleast 2 attributes of dataframe and one of them as label")
    else:
      print("'DonutChart' needs 1 attribute with 'float' data type")

  @staticmethod
  def PieChart(dataframe):
    """
    Generate PieChart visualization

    :param dataframe (pandas.Dataframe): data for visualization
    """
    #Get column name based on data type
    integer_label = [name for name in dataframe.columns if dataframe[name].dtypes == 'float64'][0]
    if integer_label != '':
      object_label = [name for name in dataframe.columns if not name.startswith(tuple(['uri', 'coordinate', 'pic'])) and dataframe[name].dtypes == 'object'][0]
      if object_label != '':
        #plot
        fig = px.pie(dataframe, values=integer_label, names=object_label)
        fig.show()
      else:
        print("'PieChart' needs atleast 2 attributes of dataframe and one of them as label")
    else:
      print("'PieChart' needs 1 attribute with 'float' data type")


  @staticmethod
  def HeatMap(dataframe):
    """
    Generate HeatMap visualization

    :param dataframe (pandas.Dataframe): data for visualization
    """
    integer_column = [name for name in dataframe.columns if dataframe[name].dtypes == 'float64']
    if len(integer_column) >= 2:
      #plot HeatMap
      sns.heatmap(dataframe.corr(), annot = True)
      pass
    else:
      print("'HeatMap' needs atleast 2 attributes with 'float' data type")


  @staticmethod
  def Histogram(dataframe):
    """
    Generate simple histogram visualization

    :param dataframe (pandas.Dataframe): data for visualization
    """
    integer_column = [name for name in dataframe.columns if dataframe[name].dtypes == 'float64']
    if len(integer_column) >= 1:
      #plot
      fig = px.histogram(dataframe, x=integer_column[0])
      fig.show()
    else:
      print("'Histogram' needs 1 attributes with 'float' data type")


  @staticmethod
  def SunBurstChart(dataframe):
    """
    Generate sunburst chart visualization

    :param dataframe (pandas.Dataframe): data for visualization
    """
    #Get column name based on data type
    integer_label = [name for name in dataframe.columns if dataframe[name].dtypes == 'float64'][0]
    if integer_label != '':
      object_columns = [name for name in dataframe.columns if not name.startswith(tuple(['uri', 'coordinate', 'pic'])) and dataframe[name].dtypes == 'object']
      if len(object_columns) == 0:
        object_columns = [name for name in dataframe.columns if name.startswith(tuple(['uri']))]
      if len(object_columns) >= 1:
        #plot
        fig = px.sunburst(dataframe, path=object_columns, values=integer_label)
        fig.show()
      else:
        print("'SunBurstChart' needs atleast 1 attribute of dataframe as label")
    else:
      print("'SunBurstChart' needs 1 attribute with 'float' data type")

  @staticmethod
  def TreeMap(dataframe):
    """
    Generate tree map visualization

    :param dataframe (pandas.Dataframe): data for visualization
    """
    #Get column name based on data type
    integer_label = [name for name in dataframe.columns if dataframe[name].dtypes == 'float64'][0]
    if integer_label != '':
      object_columns = [name for name in dataframe.columns if not name.startswith(tuple(['uri', 'coordinate', 'pic'])) and dataframe[name].dtypes == 'object']
      if len(object_columns) == 0:
        object_columns = [name for name in dataframe.columns if name.startswith(tuple(['uri']))]
      if len(object_columns) >= 1:
        #plot
        fig = px.treemap(dataframe, path=object_columns, values=integer_label)
        fig.show()
      else:
        print("'TreeMap' needs atleast 1 attribute of dataframe as label")
    else:
      print("'TreeMap' needs 1 attribute with 'float' data type")


  @staticmethod
  def DensityPlot(dataframe):
    """
    Generate simple density plot visualization

    :param dataframe (pandas.Dataframe): data for visualization
    """
    object_column = [name for name in dataframe.columns if not name.startswith(tuple(['uri', 'coordinate', 'pic'])) and dataframe[name].dtypes == 'object']
    integer_label = [name for name in dataframe.columns if dataframe[name].dtypes == 'float64'][0]
    if integer_label != '':
      #plot multiple density plot when there is a object column
      if len(dataframe[object_column[0]].unique()) != len(dataframe):
        sns.displot(data=dataframe, x=integer_label, hue=object_column[0], kind="kde")
        pass
      else:
        sns.displot(data=dataframe, x=integer_label, kind="kde")
        pass
    else:
      print("'DensityPlot' needs 1 attribute with 'float' data type")


  @staticmethod
  def BarChart(dataframe):
    """
    Generate simple bar chart visualization

    :param dataframe (pandas.Dataframe): data for visualization
    """
    #Get column name based on data type
    object_column = [name for name in dataframe.columns if not name.startswith(tuple(['uri', 'coordinate', 'pic'])) and dataframe[name].dtypes == 'object']
    integer_label = [name for name in dataframe.columns if dataframe[name].dtypes == 'float64'][0]

    num_object_column = len(object_column)
    num_uniq_obj_column0 = len(dataframe[object_column[0]].unique())
    num_uniq_obj_column1 = None

    if integer_label != '':
      if num_object_column > 0:
        #plot stacked bar when num_object_column == 2
        if num_object_column == 2:
          num_uniq_obj_column1 = len(dataframe[object_column[1]].unique())
          groupby_label = [object_column[0] if num_uniq_obj_column0 < num_uniq_obj_column1 else object_column[1]][0]
          item_label = [object_column[0] if num_uniq_obj_column0 > num_uniq_obj_column1 else object_column[1]][0]
          #plot stacked horizontal bar when unique value of item_label > 20
          if (len(item_label)) > 20:
            fig = px.bar(dataframe, x=integer_label, y=item_label, color=groupby_label, orientation='h')
            fig.show()
          else:        
            fig = px.bar(dataframe, x=item_label, y=integer_label, color=groupby_label)
            fig.show()
        else:
          item_label = object_column[0]
          #horizontal bar when unique value of item_label > 20
          if num_uniq_obj_column0 > 20:
            fig = px.bar(dataframe, x=integer_label, y=item_label,  orientation='h')
            fig.show()
          else:
            fig = px.bar(dataframe, x=item_label, y=integer_label)
            fig.show()
      else:
        print("'BarChart' needs atleast 1 attributes of dataframe as label")
    else:
      print("'BarChart' needs 1 attribute with 'float' data type")

  @staticmethod
  def LineChart(dataframe):
    """
    Generate simple table visualization

    :param dataframe (pandas.Dataframe): data for visualization
    """
    #Get column name based on data type
    object_column = [name for name in dataframe.columns if not name.startswith(tuple(['uri', 'coordinate', 'pic'])) and dataframe[name].dtypes == 'object']
    date_label = [name for name in dataframe.columns if dataframe[name].dtypes == 'datetime64[ns]'][0]
    integer_label = [name for name in dataframe.columns if dataframe[name].dtypes == 'float64'][0]

    num_object_column = len(object_column)

    if integer_label != '':
      if date_label != '':
        if num_object_column:
          sns.lineplot(data=dataframe, x=date_label, y=integer_label, hue=object_column[0])
          pass
        else:
          fig = px.line(dataframe, x=date_label, y=integer_label)
          fig.show()
      else:
        print("'LineChart' needs 1 attribute with 'date' data type as axis-x")
    else:
      print("'LineChart' needs 1 attribute with 'float' data type")


  @staticmethod
  def SimpleTable(dataframe):
    """
    Generate simple table visualization

    :param dataframe (pandas.Dataframe): data for visualization
    """
    fig = ff.create_table(dataframe)
    fig.show()


  @staticmethod
  def ImageGrid(dataframe):
    """
    Generate image grid visualization

    :param dataframe (pandas.Dataframe): data for visualization
    """
    #Check if dataframe has attribute pic
    if hasattr(dataframe, 'pic'):
      pic = [i for i in dataframe.pic]
      num_pic = len(pic)
      #get label column
      labels = [name for name in dataframe.columns if not name.startswith(tuple(['uri', 'pic', 'coordinate'])) and dataframe[name].dtypes == 'object']
      itemLabel = [i for i in dataframe[labels[0]]]

      #Check if itemLabel null
      if len(itemLabel) == 0:
        columns = 4
        width = 20
        height = max(20, int(num_pic/columns) * 20)
        plt.figure(figsize=(20,20))
        for i, url in enumerate(pic):
            plt.subplot(num_pic / columns + 1, columns, i + 1)
            try:
              image = imread(url)
              plt.imshow(image) #, plt.xticks([]), plt.yticks([])
              plt.axis('off')
            except:
              time.sleep(5)
              image = imread(url)
              plt.imshow(image) #, plt.xticks([]), plt.yticks([])
              plt.axis('off')
      else:
        columns = 4
        width = 20
        height = max(20, int(num_pic/columns) * 20)
        plt.figure(figsize=(20,20))
        for i, url in enumerate(pic):
            plt.subplot(num_pic / columns + 1, columns, i + 1)
            try:
              image = imread(url)
              plt.title(itemLabel[i])
              plt.imshow(image) #, plt.xticks([]), plt.yticks([])
              plt.axis('off')
            except:
              time.sleep(5)
              image = imread(url)
              plt.title(itemLabel[i])
              plt.imshow(image) #, plt.xticks([]), plt.yticks([])
              plt.axis('off')        
    else:
      print("'Dataframe' object has no attribute 'pic'")


  @staticmethod
  def Timeline(dataframe):
    """
    Generate timeline visualization

    :param dataframe (pandas.Dataframe): data for visualization
    """
    #get label column
    labels = [name for name in dataframe.columns if not name.startswith(tuple(['uri', 'pic', 'coordinate'])) and dataframe[name].dtypes == 'object']
    if len(labels) == 0:
      print("Timeline visualization needs 1 attributes as a 'label'")
    else:
      #get date column
      dateLabels = [name for name in dataframe.columns if dataframe[name].dtypes == 'datetime64[ns]']
      if len(dateLabels) >= 2:
        fig = px.timeline(dataframe, x_start=dateLabels[0], x_end=dateLabels[1], 
                          y=labels[0], color=labels[0])
        fig.update_yaxes(autorange="reversed")
        fig.show()
      else:
        print("Timeline visualization needs 2 attributes with 'date' data type")


  @staticmethod
  def Graph(dataframe):
    """
    Generate graph visualization

    :param dataframe (pandas.Dataframe): data for visualization
    """
    uri_column = [name for name in dataframe.columns if name.startswith('uri')]
    if len(uri_column) >= 2:
    #filter out column with reserved name and particular data types
      reserved_name = ['uri', 'pic', 'coordinate']
      object_column = [name for name in dataframe.columns if not name.startswith(tuple(reserved_name)) and dataframe[name].dtypes == 'object']
      
      if len(object_column) < 2:
        object_column = [name for name in dataframe.columns if name.startswith('uri')]

      #Create node list
      source = list(dataframe[object_column[0]].unique())
      target = list(dataframe[object_column[1]].unique())
      node_list = set(source+target)

      #create an empty graph
      G = nx.DiGraph()

      #add node to graph
      for node in node_list:
          G.add_node(node)

      #add edges to graph
      for key,value in dataframe.iterrows():
          G.add_edges_from([(value[object_column[0]],value[object_column[1]])])

      #Getting positions for each node.
      positions = nx.spring_layout(G, k=2)

      #Adding positions of the nodes to the graph
      for n, p in positions.items():
        G.nodes[n]['positions'] = p

      #Add edges as disconnected lines in a single trace 
      edge_trace = go.Scatter(
          x=[],
          y=[],
          line=dict(width=0.5,color='#888'),
          hoverinfo='text',
          mode='lines')

      for edge in G.edges():
          x0, y0 = G.nodes[edge[0]]['positions']
          x1, y1 = G.nodes[edge[1]]['positions']
          edge_trace['x'] += tuple([x0, x1, None])
          edge_trace['y'] += tuple([y0, y1, None])

      #Add nodes as a scatter trace
      node_trace = go.Scatter(
          x=[],
          y=[],
          text=[],
          mode='markers',
          hoverinfo='text',
          marker=dict(
              showscale=True,
              colorscale='Viridis',
              reversescale=True,
              color=[],
              size=12,
              colorbar=dict(
                  thickness=15,
                  title='Node Connections',
                  xanchor='left',
                  titleside='right'
              ),
              line=dict(width=2)))

      for node in G.nodes():
          x, y = G.nodes[node]['positions']
          node_trace['x'] += tuple([x])
          node_trace['y'] += tuple([y])

      # Creating the annotations, that will display the node name on the figure
      annotations = []
      for node, adjacencies in enumerate(G.adjacency()):
        annotations.append(
            dict(x=positions[adjacencies[0]][0],
                  y=positions[adjacencies[0]][1],
                  text=adjacencies[0], # node name that will be displayed
                  xanchor='left',
                  xshift=10,
                  font=dict(color='black', size=11),
                  showarrow=False, arrowhead=1, ax=-10, ay=-10)
            )

      #Create degree dictionary (degree, in_degree, out_degree)
      degree_dict = {}
      for key, value in (G.degree()):
        degree_dict.setdefault(key, []).append(value)
      for key, value in (G.in_degree()):
        degree_dict.setdefault(key, []).append(value)
      for key, value in (G.out_degree()):
        degree_dict.setdefault(key, []).append(value)

      for key, value in enumerate(degree_dict):
          node_trace['marker']['color']+=tuple([(degree_dict[value][0])])
          node_info = str(value) + ', Degree:'+ str(degree_dict[value][0]) + " In:" + str(degree_dict[value][1]) + " Out:" + str(degree_dict[value][2])
          node_trace['text']+=tuple([node_info])

      #Coloring based on the number of connections of each node.
      fig = go.Figure(data=[edge_trace, node_trace],
                  layout=go.Layout(
                      titlefont=dict(size=16),
                      showlegend=False,
                      hovermode='closest', 
                      margin=dict(b=20,l=5,r=5,t=40),
                      annotations=annotations, 
                      xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                      yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)))

      #Plot
      fig.show()
      print(nx.info(G))
      print(nx.density(G))

    else:
      print("'Graph' visualization needs 2 'uri' attributes as identifiers")


  @staticmethod
  def Dimensions(dataframe):
    """
    Generate dimension visualization

    :param dataframe (pandas.Dataframe): data for visualization    
    """
    #check number of dataframe colum for dimension
    dimension_column = [name for name in dataframe.columns if not name.startswith(tuple(['pic', 'coordinate']))]

    if len(dimension_column) >= 2:
      
      dataframe_to_list = []
      for column in dataframe:
        dataframe_to_list += dataframe[column].tolist()
      
      def index_data(type_link='source'):
        """
        Return indices correspond to labels
        """
        curr_key = 0
        indices = [0]
        curr_value = dataframe_to_list[0]
        first_row = [dataframe_to_list[0]] 
        data = dataframe_to_list[:-dataframe.shape[0]]

        if type_link == 'target':
          curr_value = dataframe_to_list[dataframe.shape[0]]
          first_row = [dataframe_to_list[dataframe.shape[0]]]
          data = dataframe_to_list[dataframe.shape[0]:]

        for key,value in enumerate(data):
          if value != curr_value :
            if value in first_row:
              curr_key = first_row.index(value)
              curr_value = value
              indices.append(curr_key)
              first_row.append(curr_value)
            else:
              indices.append(key)
              first_row.append(value)
              curr_value = value
              curr_key = key
          elif value == curr_value:
            if key != 0:
              indices.append(curr_key)
              first_row.append(curr_value)
              
        if type_link == 'target':
          indices = [i+dataframe.shape[0] for i in indices]

        return indices

      #plot
      fig = go.Figure(data=[go.Sankey(
          node = dict(
            label = dataframe_to_list,
          ),
          link = dict(
            source = index_data(type_link='source'), # indices correspond to labels, eg A1, A2, A1, B1, ...
            target = index_data(type_link='target'),
            value = [1 for i in range(len(dataframe_to_list)-dataframe.shape[0])]
        ))])

      fig.show()
    else:
      print("'Dimensions' visualization needs atleast 2 attributes of dataframe")


  @staticmethod
  def Map(dataframe):
    """
    Generate map visualization

    :param dataframe (pandas.Dataframe): data for visualization  
    """   
    data = dataframe.copy()

    if hasattr(data, 'coordinate'): 
      #Get coordinate data (latitude and longitude)
      data['coordinate_point'] = data['coordinate']
      dataframe_new = data.apply(lambda S:S.str.strip('Point()'))
      new = dataframe_new[dataframe_new.columns[-1]].str.split(" ", n = 1, expand = True)
      new = new.astype('float64')
      data['coordinate'] = new.apply(lambda x: list([x[1], x[0]]),axis=1)

      #Get label for corresponding coordinate 
      reserved_name = ['uri', 'pic', 'coordinate']
      object_column = [name for name in data.columns if not name.startswith(tuple(reserved_name)) and data[name].dtypes == 'object']

      #Initiate map folium object
      maps = folium.Map()

      #Set popup label with available column name
      popup_data = None
      if len(object_column) == 0:
          popup_data = data.coordinate_point
      else:
          popup_data = data[object_column[0]]

      #Marked the map folium object
      for i in range (len(dataframe)):
          folium.Marker(
              location=data.coordinate[i],
              popup=popup_data[i]
          ).add_to(maps)

      display(maps)
    
    else:
      print("'Dataframe' has no attribute 'coordinate'")


  @staticmethod
  def Tree(dataframe):
    """
    Generate tree visualization

    :param dataframe (pandas.Dataframe): data for visualization    
    """
    def add_nodes(nodes, parent, child):
      """
      Set parent nodes with corresponding child nodes
      """
      if parent not in nodes:
        nodes[parent] = Node(parent)  
      if child not in nodes:
        nodes[child] = Node(child)
        nodes[child].parent = nodes[parent]
    
    uri_column = [name for name in dataframe.columns if name.startswith('uri')]
    if len(uri_column) >= 2:
      #filter out column with reserved name and particular data types
      reserved_name = ['uri', 'pic', 'coordinate']
      object_column = [name for name in dataframe.columns if not name.startswith(tuple(reserved_name)) and dataframe[name].dtypes == 'object']
      
      if len(object_column) < 2:
        object_column = [name for name in dataframe.columns if name.startswith('uri')]

      #Extract selected column as new dataframe
      data = dataframe[object_column].copy()

      nodes = {}
      for parent, child in zip(data.iloc[:, -2],data.iloc[:, -1]):
        add_nodes(nodes, parent, child)

      roots = list(data[~data.iloc[:, -2].isin(data.iloc[:, -1])][data.columns[-2]].unique())
      for root in roots:         # you can skip this for roots[0], if there is no forest and just 1 tree
          for pre, _, node in RenderTree(nodes[root]):
              print("%s%s" % (pre, node.name))
    
    else:
      print("'Tree' visualization needs 2 'uri' attributes as identifiers")


  @staticmethod
  def WordCloud(dataframe):
    """
    Generate tree visualization

    :param dataframe (pandas.Dataframe): data for visualization    
    """
    #Get column name with object type
    object_column = [name for name in dataframe.columns if not name.startswith(tuple(['uri', 'coordinate', 'pic'])) and dataframe[name].dtypes == 'object']

    if len(object_column) > 0:
      #Merge into one column
      new_data = dataframe[object_column[0]]
      for i in range (1, len(object_column)):
          new_data += dataframe[object_column[i]]

      #Merge into one variable
      new_data = " ".join(new_data)

      #initiate wordcloud object
      wordcloud = WordCloud(
                      width = 800, height = 800, 
                      background_color ='white',
                      min_font_size = 10
                      ).generate(new_data) 
        
      # plot the WordCloud image                        
      plt.figure(figsize = (8, 8), facecolor = None) 
      plt.imshow(wordcloud) 
      plt.axis("off") 
      plt.tight_layout(pad = 0)

    else:
      print("'WordCloud' needs atleast 1 attribute (object data type) of dataframe excluding reserved name ['uri', 'coordinate', 'pic']")



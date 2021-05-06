import pandas as pd
import numpy as np
import pandas as pd
import plotly.express as px
import os
import shutil
import folium
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import seaborn as sns
from folium.plugins import FastMarkerCluster
import io
import requests
from sklearn.preprocessing import MinMaxScaler
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from plotly.offline import init_notebook_mode, iplot, plot
import plotly as py
init_notebook_mode(connected=True)
import plotly.graph_objs as go
from wordcloud import WordCloud


def matriz_correlacion_simple(df,
                              paleta=['#2596be', '#FFFFFF', '#e28743'],
                              size_matriz=(5, 5),
                              cbar=True,
                              cbar_orientacion='vertical',
                              annot=True,

                              ):
    # dimensiones font_size

    dim = size_matriz[0]
    dim_labels = 1.9 * dim
    sns.set(font_scale=0.1 * dim_labels)

    # matriz correlacion
    df_small = df.iloc[:, :]
    correlation_mat = df_small.corr()

    # tamaño matriz de correlacion
    fig, ax = plt.subplots(figsize=size_matriz)

    # paleta de colores divergente
    cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", paleta)

    # heatmap
    heatmap = sns.heatmap(correlation_mat, cbar=cbar, cmap=cmap,
                          annot=annot, annot_kws={"size": dim_labels})

    plt.show()

# if __name__ =="__main__":
#     dic={
#     'nume':[1,2,3,4,5],
#     'num':[10,203,405,4039,2],
#     'nu':[9,8,7,6,5],
#     'n':[10,20,10,20,12],
#     }

#     df = pd.DataFrame(dic)

#     matriz_correlacion_simple(df)

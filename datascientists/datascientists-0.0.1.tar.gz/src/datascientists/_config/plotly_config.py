import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio

# plotly.express Settings
# px.defaults.template = 'plotly_white' # "plotly", "plotly_white", "plotly_dark", "ggplot2", "seaborn", "simple_white", "none"
# px.defaults.width = 1200
# px.defaults.height = 600
# plotly.io Settings for both plotly.graph_objects and plotly.express
pio.templates.default = "plotly_white" # "plotly", "plotly_white", "plotly_dark", "ggplot2", "seaborn", "simple_white", "none"
pio.kaleido.scope.default_format = 'svg'
pio.kaleido.scope.default_scale = 1
# Plotly fig Config
# https://plotly.com/python/configuration-options/
# https://github.com/plotly/plotly.js/blob/master/src/plot_api/plot_config.js
fig_config = {
    'editable': True, 
    'toImageButtonOptions': {
        'format': 'svg', # one of png, svg, jpeg, webp
        'filename': 'fig',
        'height': None, # Set to download at the currently-rendered size by setting height and width to None
        'width': None, # # Set to download at the currently-rendered size by setting height and width to None
        'scale': 1 # Multiply title/legend/axis/canvas sizes by this factor
      }, 
    'scrollZoom': True, 
    'doubleClick': 'reset+autosize', 
    'showSources': False
}
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import datetime


def plot(
    df,
    x,
    y_line,
    y_bar,
    facet_dimension,
    ncols=2,
    percent_cols=[],
    style="fivethirtyeight",
):
    """Plots a grid of combo charts from a pandas dataframe.

    Parameters
    ----------
    df : pandas.core.frame.DataFrame
        The data you want to plot
    x : str
        The name of the column to plot on the horizontal axis
    y_line : str
        The name of the column to plot as a line
    y_bar : str
        The name of the column to plot as bars
    facet_dimension : str
        The name of the column to split the data into multiple charts
    ncols : int, optional
        The number of columns in the grid (default is 2)
    percent_cols : list of str, optional
        The name(s) of the column(s) whose scale should be X% not 0.X (default is [])
    style : str, optional
        The matplotlib style (theme) to use (default is "fivethirtyeight")

    Example
    ------
    plt = combogrid.plot(df, "date", "volume", "price", "color")
    plt.show()
    """
    y1, y2 = y_line, y_bar
    plt.style.use(style)

    @matplotlib.ticker.FuncFormatter
    def decimal_to_percentage(x, pos):
        return "{0:.0%}".format(x)

    facets = set(df[facet_dimension])
    nrows = int(np.ceil(len(facets) / ncols))
    indices = [(row, col) for row in range(nrows) for col in range(ncols)]
    mapping = {facet: indices.pop() for facet in facets}
    plt.rcParams.update({"figure.autolayout": True})
    fig, ax = plt.subplots(nrows, ncols, figsize=(6 * ncols, 5 * nrows))
    for facet in facets:
        row, col = mapping[facet]
        dff = df[df[facet_dimension] == facet]
        ax1 = ax[row][col]
        ax1.plot(dff[x], dff[y1], color="red")
        if y1 in percent_cols:
            ax1.yaxis.set_major_formatter(mtick.PercentFormatter)
        ax1.set(
            xlim=(df[x].min(), df[x].max()),
            ylim=(df[y1].min(), df[y1].max()),
            title=facet,
        )
        labels = ax1.get_xticklabels()
        plt.setp(labels, rotation=45, horizontalalignment="right")
        ax2 = ax1.twinx()
        ax2.bar(dff[x], dff[y2], alpha=0.4)
        if y2 in percent_cols:
            ax2.yaxis.set_major_formatter(mtick.PercentFormatter())
        ax2.set(xlim=(df[x].min(), df[x].max()), ylim=(df[y2].min(), df[y2].max()))
    return plt

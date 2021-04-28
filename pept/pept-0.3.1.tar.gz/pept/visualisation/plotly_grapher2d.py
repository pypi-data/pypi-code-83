#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#    pept is a Python library that unifies Positron Emission Particle
#    Tracking (PEPT) research, including tracking, simulation, data analysis
#    and visualisation tools.
#
#    If you used this codebase or any software making use of it in a scientific
#    publication, you must cite the following paper:
#        Nicuşan AL, Windows-Yule CR. Positron emission particle tracking
#        using machine learning. Review of Scientific Instruments.
#        2020 Jan 1;91(1):013329.
#        https://doi.org/10.1063/1.5129251
#
#    Copyright (C) 2019-2021 the pept developers
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.


# File   : plotly_grapher2d.py
# License: GNU v3.0
# Author : Andrei Leonard Nicusan <a.l.nicusan@bham.ac.uk>
# Date   : 19.04.2021


import  textwrap

import  numpy                   as          np

import  plotly.graph_objects    as          go
from    plotly.subplots         import      make_subplots

import  pept


class PlotlyGrapher2D:
    '''A class for PEPT data visualisation using Plotly-based 2D graphs.

    The **PlotlyGrapher** class can create and automatically configure an
    arbitrary number of 2D subplots for PEPT data visualisation.

    This class can be used to draw 2D scatter or line plots, with optional
    colour-coding using extra data columns (e.g. relative tracer activity or
    trajectory label).

    It also provides easy access to the most common configuration parameters
    for the plots, such as axes limits, subplot titles, colorbar titles, etc.
    It can work with pre-computed Plotly traces (such as the ones from the
    `pept` base classes), as well as with numpy arrays.

    Attributes
    ----------
    xlim : list or numpy.ndarray
        A list of length 2, formatted as `[x_min, x_max]`, where `x_min` is
        the lower limit of the x-axis of all the subplots and `x_max` is the
        upper limit of the x-axis of all the subplots.

    ylim : list or numpy.ndarray
        A list of length 2, formatted as `[y_min, y_max]`, where `y_min` is
        the lower limit of the y-axis of all the subplots and `y_max` is the
        upper limit of the y-axis of all the subplots.

    fig : Plotly.Figure instance
        A Plotly.Figure instance, with any number of subplots (as defined by
        `rows` and `cols`) pre-configured for PEPT data.

    Methods
    -------
    create_figure()
        Create a Plotly figure, pre-configured for PEPT data.

    add_points(points, row = 1, col = 1, size = 2.0, color = None,\
               opacity = 0.8, colorbar = True, colorbar_col = -1,\
               colorscale = "Magma", colorbar_title = None)
        Create and plot a trace for all the points in a numpy array, with
        possible color-coding.

    add_lines(lines, row = 1, col = 1, width = 2.0, color = None,\
              opacity = 0.6, colorbar = True, colorbar_col = 0,\
              colorscale = "Magma", colorbar_title = None)
        Create and plot a trace for all the lines in a numpy array, with
        possible color-coding.

    add_pixels(pixels, row = 1, col = 1, colorscale = "Magma",
               transpose = True, xgap = 0., ygap = 0.)
        Create and plot a trace with all the pixels in this class, with
        possible filtering.

    add_trace(trace, row = 1, col = 1)
        Add a precomputed Plotly trace to a given subplot.

    add_traces(traces, row = 1, col = 1)
        Add a list of precomputed Plotly traces to a given subplot.

    equalise_axes()
        Equalise the axes' limits of all subplots.

    to_html(filepath, equal_axes = True, include_plotlyjs = True)
        Save the current Plotly figure as a self-contained HTML webpage.

    show(equal_axes = True)
        Show the Plotly figure, optionally setting equal axes limits.

    Examples
    --------
    The figure is created when instantiating the class.

    >>> import numpy as np
    >>> from pept.visualisation import PlotlyGrapher2D

    >>> grapher = PlotlyGrapher2D()
    >>> lines = np.random.random((100, 5))      # columns [t, x1, y1, x2, y2]
    >>> points = np.random.random((100, 3))     # columns [t, x, y]

    Creating a trace based on a numpy array:

    >>> grapher.add_lines(lines)
    >>> grapher.add_points(points)

    Showing the plot:

    >>> grapher.show()

    If you'd like to show the plot in your browser, you can set the default
    Plotly renderer:

    >>> plotly.io.renderers.default = "browser"

    More examples are given in the docstrings of the `add_points`, `add_lines`
    methods.
    '''

    def __init__(
        self,
        rows = 1,
        cols = 1,
        xlim = None,
        ylim = None,
        subplot_titles = ["  "]
    ):
        '''`PlotlyGrapher` class constructor.

        Parameters
        ----------
        rows : int, optional
            The number of rows of subplots. The default is 1.

        cols : int, optional
            The number of columns of subplots. The default is 1.

        xlim : list or numpy.ndarray, optional
            A list of length 2, formatted as `[x_min, x_max]`, where `x_min` is
            the lower limit of the x-axis of all the subplots and `x_max` is
            the upper limit of the x-axis of all the subplots.

        ylim : list or numpy.ndarray, optional
            A list of length 2, formatted as `[y_min, y_max]`, where `y_min` is
            the lower limit of the y-axis of all the subplots and `y_max` is
            the upper limit of the y-axis of all the subplots.

        subplot_titles : list of str, default ["  "]
            A list of the titles of the subplots - e.g. ["plot a)", "plot b)"].
            The default is a list of empty strings.

        Raises
        ------
        ValueError
            If `rows` < 1 or `cols` < 1.

        ValueError
            If `xlim` or `ylim` are not lists of length 2.
        '''

        rows = int(rows)
        cols = int(cols)

        if rows < 1 or cols < 1:
            raise ValueError((
                "\n[ERROR]: The number of rows and cols have to be larger "
                f"than 1. Received rows = {rows}; cols = {cols}.\n"
            ))

        self._rows = rows
        self._cols = cols

        if xlim is not None:
            xlim = np.asarray(xlim, dtype = float)

            if xlim.ndim != 1 or xlim.shape[0] != 2:
                raise ValueError((
                    "\n[ERROR]: xlim needs to be a list of length 2, formatted"
                    f" as xlim = [x_min, x_max]. Received {xlim}.\n"
                ))

        if ylim is not None:
            ylim = np.asarray(ylim, dtype = float)

            if ylim.ndim != 1 or ylim.shape[0] != 2:
                raise ValueError((
                    "\n[ERROR]: ylim needs to be a list of length 2, formatted"
                    f" as ylim = [y_min, y_max]. Received {ylim}.\n"
                ))

        self._xlim = xlim
        self._ylim = ylim

        self._subplot_titles = subplot_titles
        # Pad the subplot titles that were not set with empty strings.
        self._subplot_titles.extend(['  '] * (rows * cols -
                                              len(subplot_titles)))

        self._fig = self.create_figure()


    def create_figure(self):
        '''Create a Plotly figure, pre-configured for PEPT data.

        This function creates a Plotly figure with an arbitrary number of
        subplots, as given in the class instantiation call.

        Returns
        -------
        fig : Plotly Figure instance
            A Plotly Figure instance, with any number of subplots (as defined
            when instantiating the class) pre-configured for PEPT data.
        '''

        # specs = [[{"type": "scatter3d"}] * self._cols] * self._rows

        self._fig = make_subplots(
            rows = self._rows,
            cols = self._cols,
            # specs = specs,
            subplot_titles = self._subplot_titles,
            horizontal_spacing = 0.05,
            vertical_spacing = 0.08,
        )

        self._fig['layout'].update(
            # plot_bgcolor = 'rgba(0, 0, 0, 0)',
            margin = dict(l = 0, r = 0, b = 30, t = 30),
            showlegend = False,
        )

        # For every subplot (scene), set axes' ratios and limits
        # Also set the y axis to point upwards
        # Plotly naming convention of scenes: 'scene', 'scene2', etc.
        for i in range(self._rows):
            for j in range(self._cols):
                index = i * self._cols + j + 1
                xaxis = f"xaxis{index}" if index != 1 else "xaxis"
                yaxis = f"yaxis{index}" if index != 1 else "yaxis"

                self._fig["layout"][xaxis].update(
                    range = self._xlim,
                    title = dict(text = "<i>x</i> (mm)"),
                )

                self._fig["layout"][yaxis].update(
                    range = self._ylim,
                    title = dict(text = "<i>y</i> (mm)"),
                    scaleanchor = f"x{index}" if index != 1 else "x",
                    scaleratio = 1,
                )

        return self._fig


    @property
    def xlim(self):
        return self._xlim


    @xlim.setter
    def xlim(self, xlim):
        xlim = np.asarray(xlim, dtype = float)

        if xlim.ndim != 1 or xlim.shape[0] != 2:
            raise ValueError((
                "\n[ERROR]: xlim needs to be a list of length 2, formatted as"
                f"xlim = [x_min, x_max]. Received {xlim}.\n"
            ))

        self._xlim = xlim

        # For every subplot (scene), update axes' limits
        # Plotly naming convention of scenes: 'scene', 'scene2', etc.
        for i in range(self._rows):
            for j in range(self._cols):
                index = i * self._cols + j + 1
                xaxis = f"xaxis{index}" if index != 1 else "xaxis"

                self._fig["layout"][xaxis].update(
                    range = self._xlim,
                )


    @property
    def ylim(self):
        return self._ylim


    @ylim.setter
    def ylim(self, ylim):
        ylim = np.asarray(ylim, dtype = float)

        if ylim.ndim != 1 or ylim.shape[0] != 2:
            raise ValueError((
                "\n[ERROR]: ylim needs to be a list of length 2, formatted as"
                f"ylim = [y_min, y_max]. Received {ylim}.\n"
            ))

        self._ylim = ylim

        # For every subplot (scene), update axes' limits
        # Plotly naming convention of scenes: 'scene', 'scene2', etc.
        for i in range(self._rows):
            for j in range(self._cols):
                index = i * self._cols + j + 1
                xaxis = f"xaxis{index}" if index != 1 else "xaxis"

                self._fig["layout"][xaxis].update(
                    range = self._xlim,
                )


    @property
    def fig(self):
        return self._fig


    def add_points(
        self,
        points,
        row = 1,
        col = 1,
        size = 6.0,
        color = None,
        opacity = 0.8,
        colorbar = True,
        colorbar_col = -1,
        colorscale = "Magma",
        colorbar_title = None
    ):
        '''Create and plot a trace for all the points in a numpy array, with
        possible color-coding.

        Creates a `plotly.graph_objects.Scatter` object for all the points
        included in the numpy array `points` and adds it to the subplot
        selected by `row` and `col`.

        The expected data columns are [time, x1, y1, ...].

        Parameters
        ----------
        points : (M, N >= 2) numpy.ndarray
            Points to plot. The expected data columns are: [t, x1, y1, etc.].

        row : int, default 1
            The row of the subplot to add a trace to.

        col : int, default 1
            The column of the subplot to add a trace to.

        size : float, default 2.0
            The marker size of the points.

        color : str or list-like, optional
            Can be a single color (e.g. "black", "rgb(122, 15, 241)") or a
            colorbar list. Overrides `colorbar` if set. For more information,
            check the Plotly documentation. The default is None.

        opacity : float, default 0.8
            The opacity of the lines, where 0 is transparent and 1 is fully
            opaque.

        colorbar : bool, default True
            If set to True, will color-code the data in the `points` column
            `colorbar_col`. Is overridden by `color` if set.

        colorbar_col : int, default -1
            The column in `points` that will be used to color the points. Only
            has an effect if `colorbar` is set to True. The default is -1 (the
            last column).

        colorscale : str, default "Magma"
            The Plotly scheme for color-coding the `colorbar_col` column in the
            input data. Typical ones include "Cividis", "Viridis" and "Magma".
            A full list is given at `plotly.com/python/builtin-colorscales/`.
            Only has an effect if `colorbar = True` and `color` is not set.

        colorbar_title : str, optional
            If set, the colorbar will have this title above it.

        Raises
        ------
        ValueError
            If `points` is not a numpy.ndarray with shape (M, N), where N >= 3.

        Examples
        --------
        Add an array of points (data columns: [time, x, y]) to a
        `PlotlyGrapher2D` instance:

        >>> grapher = PlotlyGrapher2D()
        >>> points_raw = np.random.random((10, 3))
        >>> grapher.add_points(points_raw)
        >>> grapher.show()

        If you have an extremely large number of points in a numpy array, you
        can plot every 10th point using slices:

        >>> pts = np.array(...)         # shape (N, M >= 3), N very large
        >>> grapher.add_points(pts[::10])

        '''

        points = np.asarray(points, dtype = float)

        # Check that points has shape (M, 3)
        if points.ndim != 2 or points.shape[1] < 3:
            raise ValueError((
                "\n[ERROR]: `points` should have dimensions (M, N), where "
                "N >= 3. Received {}\n".format(points.shape)
            ))

        # No need to type-check the other parameters as Plotly will do that
        # anyway...

        # Create the dictionary of marker properties
        marker = dict(
            size = size,
            color = color,
            opacity = opacity
        )

        # Update `marker` if a colorbar is requested AND color is None.
        if colorbar and color is None:
            marker.update(colorscale = colorscale)
            marker['color'] = points[:, colorbar_col]

            if colorbar_title is not None:
                marker["colorbar"] = dict(title = colorbar_title)

        coords_x = points[:, 1]
        coords_y = points[:, 2]

        trace = go.Scatter(
            x = coords_x,
            y = coords_y,
            mode = "markers",
            marker = marker
        )

        self._fig.add_trace(trace, row = row, col = col)


    def add_lines(
        self,
        lines,
        row = 1,
        col = 1,
        width = 2.0,
        color = None,
        opacity = 0.6,
    ):
        '''Create and plot a trace for all the lines in a numpy array, with
        possible color-coding.

        Creates a `plotly.graph_objects.Scatter` object for all the lines
        included in the numpy array `lines` and adds it to the subplot
        determined by `row` and `col`.

        It expects LoR-like data, where each line is defined by two points. The
        expected data columns are [x1, y1, x2, y2, ...].

        Parameters
        ----------
        lines : (M, N >= 5) numpy.ndarray
            The expected data columns are: [time, x1, y1, x2, y2, etc.].

        row : int, default 1
            The row of the subplot to add a trace to.

        col : int, default 1
            The column of the subplot to add a trace to.

        width : float, default 2.0
            The width of the lines.

        color : str or list-like, optional
            Can be a single color (e.g. "black", "rgb(122, 15, 241)").

        opacity : float, default 0.6
            The opacity of the lines, where 0 is transparent and 1 is fully
            opaque.

        Raises
        ------
        ValueError
            If `lines` is not a numpy.ndarray with shape (M, N), where N >= 5.

        Examples
        --------
        Add an array of lines (data columns: [time, x1, y1, x2, y2]) to a
        `PlotlyGrapher` instance:

        >>> grapher = PlotlyGrapher2D()
        >>> lines_raw = np.random.random((100, 5))
        >>> grapher.add_lines(lines_raw)
        >>> grapher.show()

        If you have a very large number of lines in a numpy array, you can plot
        every 10th point using slices:

        >>> lines_raw = np.array(...)       # shape (N, M >= 5), N very large
        >>> grapher.add_lines(lines_raw[::10])

        '''

        lines = np.asarray(lines, dtype = float)

        # Check that lines has shape (N, 5)
        if lines.ndim != 2 or lines.shape[1] < 5:
            raise ValueError((
                "\n[ERROR]: `lines` should have dimensions (M, N), where "
                "N >= 4. Received {}\n".format(lines.shape)
            ))

        marker = dict(
            width = width,
            color = color,
        )

        coords_x = []
        coords_y = []

        for line in lines:
            coords_x.extend([line[1], line[3], None])
            coords_y.extend([line[2], line[4], None])

        coords_x = np.array(coords_x, dtype = float)
        coords_y = np.array(coords_y, dtype = float)

        trace = go.Scatter(
            x = coords_x,
            y = coords_y,
            mode = 'lines',
            opacity = opacity,
            line = marker
        )

        self._fig.add_trace(trace, row = row, col = col)


    def add_pixels(
        self,
        pixels,
        row = 1,
        col = 1,
        colorscale = "Magma",
        transpose = True,
        xgap = 0.,
        ygap = 0.,
    ):
        '''Create and plot a trace with all the pixels in this class, with
        possible filtering.

        Creates a `plotly.graph_objects.Heatmap` object for the centres of
        all pixels encapsulated in a `pept.Pixels` instance, colour-coding the
        pixel value.

        The `condition` parameter is a filtering function that should return
        a boolean mask (i.e. it is the result of a condition evaluation). For
        example `lambda x: x > 0` selects all pixels that have a value larger
        than 0.

        Parameters
        ----------
        pixels : pept.Pixels
            The pixel space, encapsulated in a `pept.Pixels` instance (or
            subclass thereof). Only `pept.Pixels` are accepted as raw pixels on
            their own do not contain data about the spatial coordinates of the
            pixel box.

        row : int, default 1
            The row of the subplot to add a trace to.

        col : int, default 1
            The column of the subplot to add a trace to.

        colorscale : str, default "Magma"
            The Plotly scheme for color-coding the pixel values in the input
            data. Typical ones include "Cividis", "Viridis" and "Magma".
            A full list is given at `plotly.com/python/builtin-colorscales/`.
            Only has an effect if `colorbar = True` and `color` is not set.

        transpose : bool, default True
            Transpose the heatmap (i.e. flip it across its diagonal).

        Examples
        --------
        Pixellise an array of lines and add them to a `PlotlyGrapher` instance:

        >>> grapher = PlotlyGrapher2D()
        >>> lines = np.array(...)                   # shape (N, M >= 7)
        >>> lines2d = lines[:, [0, 1, 2, 4, 5]]     # select x, y of lines
        >>> number_of_pixels = [10, 10]
        >>> pixels = pept.Pixels.from_lines(lines2d, number_of_pixels)
        >>> grapher.add_lines(lines)
        >>> grapher.add_pixels(pixels)
        >>> grapher.show()

        '''

        if not isinstance(pixels, pept.Pixels):
            raise TypeError(textwrap.fill((
                "The input `pixels` must be an instance of `pept.Pixels` (or "
                f"subclass thereof. Received {type(pixels)}."
            )))

        trace = pixels.heatmap_trace(
            colorscale = colorscale,
            transpose = transpose,
        )

        self._fig.add_trace(trace, row = row, col = col)


    def add_trace(self, trace, row = 1, col = 1):
        '''Add a precomputed Plotly trace to a given subplot.

        The equivalent of the Plotly figure.add_trace method.

        Parameters
        ----------
        trace : Plotly trace
            A precomputed Plotly trace.

        row : int, default 1
            The row of the subplot to add a trace to.

        col : int, default 1
            The column of the subplot to add a trace to.
        '''

        # Add precomputed trace
        self._fig.add_trace(trace, row = row, col = col)


    def add_traces(self, traces, row = 1, col = 1):
        '''Add a list of precomputed Plotly traces to a given subplot.

        The equivalent of the Plotly figure.add_traces method.

        Parameters
        ----------
        traces : list [ Plotly trace ]
            A list of precomputed Plotly traces

        row : int, default 1
            The row of the subplot to add the traces to.

        col : int, default 1
            The column of the subplot to add the traces to.
        '''

        # Add precomputed traces
        self._fig.add_traces(
            traces,
            rows = [row] * len(traces),
            cols = [col] * len(traces)
        )


    def equalise_axes(self):
        '''Equalise the axes of all subplots by setting the system limits
        `xlim` and `ylim` to equal values, such that all data plotted is
        within the plotted bounds.
        '''
        # Compute min, max for the `x`, `y` dimensions for every
        # dataset added to `_fig`
        def get_min_max(fig_data):
            # Convert x, y attributes of `fig_data` to numpy arrays with
            # `dtype = float`, such that `None` entries are casted to
            # np.nan. Then find min, max for each dimension.
            x = np.asarray(fig_data.x, dtype = float)
            y = np.asarray(fig_data.y, dtype = float)

            # Find min, max, ignoring np.nans
            xmin = np.nanmin(x)
            xmax = np.nanmax(x)

            ymin = np.nanmin(y)
            ymax = np.nanmax(y)

            return [xmin, xmax, ymin, ymax]

        # `lims` columns: [xmin, xmax, ymin, ymax].
        lims = [get_min_max(fig_data) for fig_data in self._fig.data]
        lims = np.array(lims, order = "F")

        # Find global min and max for each dimension.
        mins = lims[:, [0, 2]].min(axis = 0)
        maxs = lims[:, [1, 3]].max(axis = 0)

        # Find greatest range in all dimensions.
        max_range = (maxs - mins).max()

        # Find mean for each dimension to centre plot around it.
        mean = (maxs + mins) / 2

        # Finally, set xlim, ylim to be centred around their mean,
        # with a span of max_range.
        self.xlim = [mean[0] - max_range / 2, mean[0] + max_range / 2]
        self.ylim = [mean[1] - max_range / 2, mean[1] + max_range / 2]


    def show(self, equal_axes = True):
        '''Show the Plotly figure, optionally setting equal axes limits.

        Note that the figure will be shown on the Plotly-configured renderer
        (e.g. browser, or PDF). The available renderers can be found by running
        the following code:

        >>> import plotly.io as pio
        >>> pio.renderers

        If you want an interactive figure in the browser, run the following:

        >>> pio.renderers.default = "browser"

        Parameters
        ----------
        equal_axes : bool, default True
            Set `xlim`, `ylim` to equal ranges such that the axes limits are
            equalised. Only has an effect if both `xlim` and `ylim` are `None`.
            If `False`, the default Plotly behaviour is used (i.e.
            automatically use min, max for each dimension).
        '''

        if equal_axes is True and self.xlim is None and self.ylim is None:
            self.equalise_axes()

        self._fig.show()


    def to_html(
        self,
        filepath,
        equal_axes = True,
        include_plotlyjs = True,
    ):
        '''Save the current Plotly figure as a self-contained HTML webpage.

        Parameters
        ----------
        filepath : str or writeable
            Path or open file descriptor to save the HTML file to.

        equal_axes : bool, default True
            Set `xlim`, `ylim` to equal ranges such that the axes limits are
            equalised. Only has an effect if both `xlim` and `ylim` are `None`.
            If `False`, the default Plotly behaviour is used (i.e.
            automatically use min, max for each dimension).

        include_plotlyjs : True or "cdn", default True
            If `True`, embed the Plotly.JS library in the HTML file, allowing
            the graph to be shown offline, but adding 3 MB. If "cdn", the
            Plotly.JS library will be downloaded dynamically.

        Examples
        --------
        Add 10 random points to a `PlotlyGrapher2D` instance and save the
        figure as an HTML webpage:

        >>> fig = pept.visualisation.PlotlyGrapher2D()
        >>> fig.add_points(np.random.random((10, 3)))
        >>> fig.to_html("random_points.html")

        '''
        if equal_axes is True and self.xlim is None and self.ylim is None:
            self.equalise_axes()

        self._fig.write_html(
            filepath,
            include_plotlyjs = include_plotlyjs,
        )


    def __str__(self):
        # Shown when calling print(class)
        docstr = (
            f"xlim = {self.xlim}\n"
            f"ylim = {self.ylim}\n"
            f"fig = \n{self.fig}"
        )

        return docstr


    def __repr__(self):
        # Shown when writing the class on a REPL
        docstr = (
            "Class instance that inherits from `pept.visualisation."
            "PlotlyGrapher2D`.\n"
            f"Type:\n{type(self)}\n\n"
            "Attributes\n----------\n"
            f"{self.__str__()}\n\n"
        )

        return docstr

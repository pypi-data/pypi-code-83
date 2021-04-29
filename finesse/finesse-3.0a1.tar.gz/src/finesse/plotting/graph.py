"""Graph plotting."""

from collections import defaultdict
import matplotlib.pyplot as plt
import networkx as nx
from ..utilities import graph_layouts, option_list


def plot_graph(
    network, layout, graphviz=False, **kwargs,
):
    from ..environment import has_pygraphviz

    if graphviz and not has_pygraphviz():
        raise ModuleNotFoundError(
            "The graphviz option requires pygraphviz and graphviz to be installed"
        )

    plotter = plot_graphviz if graphviz else plot_nx_graph
    plotter(network, layout, **kwargs)


def plot_nx_graph(
    network,
    layout,
    node_labels=True,
    node_attrs=False,
    edge_attrs=False,
    node_color_key=None,
    label_font_size=12,
    attr_font_size=6,
    edge_font_size=6,
    **kwargs,
):
    """Plot graph with NetworkX.

    Parameters
    ----------
    network : :class:`networkx.Graph`
        The network to plot.

    layout : str
        The layout type to use. Any layout algorithm provided by
        :mod:`networkx.drawing.layout` is supported.

    node_labels : :py:class:`bool`, optional
        Show node names; defaults to True.

    node_attrs : :py:class:`bool` or :py:class:`list`, optional
        Show node data. This can be `True`, in which case all node data is shown, or a
        list, in which case only the specified keys are shown. Defaults to `True`.

    edge_attrs : :py:class:`bool` or :py:class:`list`, optional
        Show edge data. This can be `True`, in which case all edge data is shown, or a list, in
        which case only the specified keys are shown. Defaults to `True`.

    node_color_key : callable, optional
        Key function accepting a node and a node attribute dict and returning a group. Each group is
        assigned a unique color. If not specified, nodes are not colored.

    label_font_size, attr_font_size, edge_font_size : :py:class:`int`, optional
        Font size for node labels, attributes and edges. Defaults to 12, 6 and 6, respectively.

    Other Parameters
    ----------------
    kwargs
        Anything else supported by :func:`networkx.drawing.nx_pylab.draw`.

    Raises
    ------
    ValueError
        If the specified layout is not supported.

    Exception
        If the graph cannot be represented with the specified layout.
    """
    from ..utilities import stringify

    if node_color_key is not None:
        if "node_color" in kwargs:
            raise ValueError(
                "cannot specify both 'node_color' and 'node_color_key' arguments"
            )

        # Assign node colors.
        cycler = iter(plt.rcParams["axes.prop_cycle"].by_key()["color"])
        group_colors = defaultdict(lambda: next(cycler))
        kwargs["node_color"] = [
            group_colors[node_color_key(node, data)]
            for node, data in network.nodes(data=True)
        ]

    layouts = graph_layouts()

    try:
        posfunc = layouts[layout.casefold()]
    except KeyError:
        choices = option_list(layouts)

        raise ValueError(
            f"Layout '{layout}' is not available in NetworkX (choose from {choices})."
        )

    try:
        pos = posfunc(network)
    except nx.NetworkXException as e:
        if "G is not planar" in str(e):
            raise Exception(
                "Graph cannot be represented with a planar layout. Try a different layout."
            ) from e

    nx.draw(
        network,
        pos,
        with_labels=node_labels,
        verticalalignment="bottom",
        font_size=label_font_size,
        **kwargs,
    )

    if node_attrs:
        data = network.nodes(data=True)

        if node_attrs is not True:  # Needs to be like this!
            # Show only certain data.
            data = [
                (
                    node,
                    {
                        key: value
                        for key, value in node_data.items()
                        if key in node_attrs
                    },
                )
                for node, node_data in data
            ]

        node_labels = {
            node: "\n".join(
                [f"{key}={stringify(value)}" for key, value in node_attrs.items()]
            )
            for node, node_attrs in data
        }
        nx.draw_networkx_labels(
            network,
            pos,
            labels=node_labels,
            verticalalignment="top",
            font_size=attr_font_size,
        )

    if edge_attrs:
        data = network.edges(data=True)

        if edge_attrs is not True:  # Needs to be like this!
            # Show only certain data.
            data = (
                (
                    u,
                    v,
                    {
                        key: value
                        for key, value in edge_data.items()
                        if key in edge_attrs
                    },
                )
                for u, v, edge_data in data
            )

        edge_labels = {
            (u, v): "\n".join(
                [f"{key}={stringify(value)}" for key, value in edge_attrs.items()]
            )
            for u, v, edge_attrs in data
        }
        nx.draw_networkx_edge_labels(
            network, pos, edge_labels=edge_labels, font_size=edge_font_size,
        )

    plt.show()


def plot_graphviz(network, layout):
    """Plot graph with graphviz.

    The `pygraphviz` Python package must be installed and available on the current
    Python path, and `graphviz` must be available on the system path.

    Parameters
    ----------
    network : :class:`networkx.Graph`
        The network to plot.

    layout : str
        The layout type to use. Any layout algorithm provided by graphviz is supported.

    Raises
    ------
    ValueError
        If the specified layout is not supported.

    ImportError
        If graphviz or pygraphviz is not installed.
    """
    from networkx.drawing.nx_agraph import view_pygraphviz

    layouts = ("neato", "dot", "fdp", "sfdp", "circo")
    gvlayout = layout.casefold()

    if gvlayout not in layouts:
        choices = option_list(layouts)

        raise ValueError(
            f"Layout '{layout}' is not available in graphviz (choose from {choices})."
        )

    view_pygraphviz(network, prog=gvlayout)

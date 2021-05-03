#!/usr/bin/env python3

from typing import Callable, Optional

from codoc.domain.model import Graph
from codoc.service.export import publish
from codoc.service.parsing.node import get_description, get_name


def view(
    label: str,
    graph_id: str = None,
    description: str = None,
):
    def decorator(initial_view_function):
        nonlocal description
        nonlocal graph_id

        if description is None:
            description = get_description(initial_view_function)
        if graph_id is None:
            graph_id = get_id(initial_view_function)

        def view_function(
            graph: Graph,
            api_key: str,
            publish_func: Optional[Callable] = None,
        ):
            filtered_graph = initial_view_function(graph)
            raise_if_graph_is_invalid(filtered_graph, label)

            if not publish_func:
                publish_func = publish
            # TODO remove this from the view. this should
            # be on the CLI, and not closely knitted.
            return publish_func(
                graph=filtered_graph,
                label=label,
                graph_id=graph_id,
                description=get_description(initial_view_function),
                api_key=api_key,
            )

        view_function = _set_view_function_attributes(
            view_function, graph_id=graph_id, label=label, description=description
        )

        return view_function

    return decorator


def raise_if_graph_is_invalid(graph, label):
    if not isinstance(graph, Graph):
        raise ValueError(f"Return type of '{label}' is not a Graph")

    if len(graph.nodes) == 0:
        raise ValueError(f"Graph '{label}' has no nodes")


def _set_view_function_attributes(view_function, graph_id, label, description):
    view_function.__name__ = graph_id

    view_function.__docs__ = description
    view_function.__is_codoc_view = True

    # Attributes for logging etc
    view_function.graph_id = graph_id
    view_function.label = label
    view_function.description = description

    return view_function


def get_id(func) -> str:
    prefix = getattr(func, "__module__", "root")

    return f"{prefix}.{get_name(func)}"

#!/usr/bin/env python3
import types
from typing import Set

from codoc.domain.model import Dependency, Graph, Node
from codoc.domain.helpers import get_identifiers, set_parent
from codoc.service.dependency_correcting import remove_non_connected_edges
from codoc.service.parsing.dependency import (
    get_dependency_nodes,
    get_dependency_nodes_with_parents,
)
from codoc.service.dependency_correcting import create_bubbled_dependencies
from codoc.service.parsing.node import create_node_from_object, get_identifier_of_object

from .object_unpacker import recursively_get_all_subobjects_in_object


def create_graph_of_module(
    module: types.ModuleType,
    include_external_dependencies: bool = True,
    strict_mode: bool = True,
) -> Graph:
    all_objects = frozenset(recursively_get_all_subobjects_in_object(module))
    nodes = set(
        node
        for obj in all_objects
        for node in {create_node_from_object(obj, external=False)}
        | get_dependency_nodes_with_parents(
            obj,
            include_external_dependencies=include_external_dependencies,
            strict_mode=strict_mode,
        )
    )
    edges = set(
        Dependency(
            from_node=get_identifier_of_object(obj),
            to_node=dependency.identifier,
        )
        for obj in all_objects
        for dependency in get_dependency_nodes(
            obj,
            include_external_dependencies=include_external_dependencies,
            strict_mode=strict_mode,
        )
    )
    return create_bubbled_dependencies(Graph(nodes=nodes, edges=edges))


# TODO move
def assert_is_graph_valid(graph: Graph) -> bool:
    assert _is_graph(graph), f"{type(graph)=} is not a graph"
    assert not _is_graph_empty(graph), "The graph is empty!"
    _assert_does_all_parents_exist(graph)
    # assert _does_edges_lead_somewhere(graph), "Not all edges lead to existing nodes!"


def _is_graph(graph: Graph) -> bool:
    return isinstance(graph, Graph)


def _assert_does_all_parents_exist(graph: Graph) -> bool:
    node_identifiers = get_identifiers(graph)
    parentless_nodes = set(
        (node.identifier, node.parent_identifier)
        for node in graph.nodes
        if node.parent_identifier is not None
        and node.parent_identifier not in node_identifiers
    )
    assert (
        parentless_nodes == set()
    ), f"The following parents could not be found: {parentless_nodes}"


def _does_edges_lead_somewhere(graph: Graph) -> bool:
    node_identifiers = get_identifiers(graph)
    return all(
        edge.from_node in node_identifiers and edge.to_node in node_identifiers
        for edge in graph.edges
    )
    ...


def _is_graph_empty(graph: Graph) -> bool:
    return len(graph.nodes) == 0


# TODO move
def clean_graph(graph: Graph) -> bool:
    return remove_parents_if_parent_is_discarded_in_nodes(
        remove_non_connected_edges(graph)
    )


def remove_parents_if_parent_is_discarded_in_nodes(graph: Graph):
    identifiers = get_identifiers(graph)
    return Graph(
        nodes={
            remove_parent_if_parent_is_discarded(node, identifiers)
            for node in graph.nodes
        },
        edges=graph.edges,
    )


def remove_parent_if_parent_is_discarded(
    node: Node, node_identifiers: Set[str]
) -> Node:
    parent_id = node.parent_identifier
    if parent_id is not None and parent_id not in node_identifiers:
        return set_parent(node, None)
    return node

import datetime
import logging
from typing import List

import networkx as nx

from .storage.file_storage import load_from_file, save_to_file

logger = logging.getLogger(__file__)


def sort_nodes(
    graph: nx.DiGraph,
    sort_by: str = "importance",
    limit: int = 10,
    ascending=False,
    only_leaves=True,
) -> List[int]:
    # can sort by 'importance','name','due', 'id'
    assert sort_by in ["importance", "name", "due", "id"]

    subgraph = graph.copy(as_view=False)

    for node_id in graph.nodes:
        if graph.nodes[node_id]["task"].completed:
            subgraph.remove_node(node_id)

    if only_leaves:
        node_ids = [node_id for node_id, degree in subgraph.in_degree() if degree == 0]
    else:
        node_ids = subgraph.nodes

    if sort_by == "importance":
        node_scores = [
            (node_id, subgraph.nodes[node_id]["task"].importance or 0)
            for node_id in node_ids
        ]
    elif sort_by == "id":
        node_scores = [(node_id, node_id) for node_id in node_ids]
    elif sort_by == "name":
        node_scores = [
            (node_id, subgraph.nodes[node_id]["task"].name or "")
            for node_id in node_ids
        ]
    elif sort_by == "due":
        node_scores = [
            (node_id, subgraph.nodes[node_id]["task"].due or datetime.datetime.now())
            for node_id in node_ids
        ]

    node_scores = sorted(node_scores, key=lambda x: x[1])

    if not ascending:
        node_scores = node_scores[::-1]

    if limit is not None:
        node_scores = node_scores[:limit]
    return [n[0] for n in node_scores]


# Create
def create_graph() -> nx.DiGraph:
    return nx.DiGraph()


def load() -> nx.DiGraph:
    fname = None
    try:
        graph = load_from_file(fname=fname)
        logger.debug(f"Graph Loaded:\n{graph}")
    except FileNotFoundError:
        graph = None
    if graph is None:
        logger.debug("Creating new graph")
        graph = create_graph()
        save_to_file(graph, fname=fname)

    return graph


def save(graph: nx.DiGraph):
    fname = None
    save_to_file(graph, fname=fname)

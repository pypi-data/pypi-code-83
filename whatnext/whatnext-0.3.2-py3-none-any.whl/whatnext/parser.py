import datetime
import getpass
import logging
import os
from typing import List

import networkx as nx
from dateparser.search import search_dates

from .data_model import Task
from .tasks import create_task

logger = logging.getLogger(__file__)


def is_url(s: str):
    return s.startswith("https://") or s.startswith("http://") or s.startswith("www.")


def is_email(s: str):
    return "@" in s and "." in s.split("@")[-1]


def get_importance(s: str):
    """counts the number of ! in the string"""
    return len([c for c in s if c == "!"])


def get_due_date(s: str) -> datetime.datetime:
    date_candidates = search_dates(s)
    if date_candidates is None or len(date_candidates) == 0:
        return None

    # removes weird false positive from search_dates
    if date_candidates[0][0] in {"on", "out"}:
        return None

    return date_candidates[0][1]


def parse_command(s: str, graph: nx.DiGraph = None) -> Task:

    s = s.strip()

    # TODO parse s to save only the main (noun, verb) pair, set the rest as a note
    name = s

    # Check if command is referencing an existing Task
    try:
        task_id = int(s)
    except ValueError:
        task_id = -1
    else:
        if graph is None or (task_id not in graph.nodes):
            task_id = -1

    # Check if name uniquely matches existing node, if so
    if task_id == -1:
        task_ids = [
            node_id
            for node_id in graph.nodes
            if graph.nodes[node_id]["task"].name == name
        ]
        if len(task_ids) == 1:
            task_id = task_ids[0]

    importance = get_importance(s)

    due = get_due_date(s)

    words = s.strip().split(" ")
    tags = [w.replace("!", "") for w in words if w.startswith("#")]
    urls = [w for w in words if is_url(w)]
    users = [w.replace("!", "") for w in words if w.startswith("@") or is_email(w)]
    notes = []

    if task_id >= 0:
        name = "_existing_node"

    return Task(
        user_id=getpass.getuser(),
        task_id=task_id,
        name=name,
        project=os.environ.get("WN_PROJECT", "MAIN"),
        importance=importance,
        due=due,
        tags=tags,
        urls=urls,
        users=users,
        notes=notes,
    )


def split_edges(s: str, pattern="->"):
    return [e.strip() for e in s.split(pattern)]


def split_multiple_commands(s: str, pattern="&"):
    return [e.strip() for e in s.split(pattern)]


def parse(graph: nx.DiGraph, s: str) -> nx.DiGraph:
    """parse potentially multple tasks in one statement"""
    edges: List[str] = split_edges(s)
    commands: List[List[str]] = [split_multiple_commands(e) for e in edges]
    tasks: List[List[Task]] = [
        [parse_command(c2, graph=graph) for c2 in c] for c in commands
    ]

    # create task nodes in graph
    task_ids: List[List[int]] = [
        [create_task(graph, task) for task in t] for t in tasks
    ]

    # now create edges if multiple tasks
    for step_num, t in enumerate(task_ids[:-1]):
        src_nodes = t
        dest_nodes = task_ids[step_num + 1]
        for src in src_nodes:
            for dest in dest_nodes:
                graph.add_edge(src, dest)
                logger.info(f"Creating Edge {src} -> {dest}")
    return graph

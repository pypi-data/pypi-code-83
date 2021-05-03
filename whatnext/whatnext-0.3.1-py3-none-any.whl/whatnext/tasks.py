"""CRUD operations on data_model.Tasks

"""
import datetime
import logging
import os
import re
from typing import List, Optional

import networkx as nx

from .data_model import Task, TimeLog
from .graph import sort_nodes

logger = logging.getLogger(__file__)


def create_task(graph: nx.DiGraph, task: Task) -> int:
    if task.task_id < 0:
        task.task_id = len(graph.nodes)
    else:
        if task.name == "_existing_node":
            return task.task_id

    graph.add_node(task.task_id, task=task)
    return task.task_id


def delete_task(graph: nx.DiGraph, task_id: int) -> int:
    raise NotImplementedError()


def get_task_from_graph(task_id: int, graph: nx.DiGraph) -> Task:

    task = graph.nodes[task_id]["task"]
    assert isinstance(task, Task)

    if task.time_logs is not None and len(task.time_logs):
        for time_logs_id, time_log in enumerate(task.time_logs):
            if isinstance(time_log, dict):
                raise TypeError("should be TimeLog")
    return task


def update_task_in_graph(task: Task, graph: nx.DiGraph) -> nx.DiGraph:
    graph._node[task.task_id]["task"] = task

    # task_spec["time_logs"] = [
    #     time_log
    #     if isinstance(time_log, dict)
    #     else time_log.dict(exclude_defaults=True, exclude_none=True, exclude_unset=True)
    #     for time_log in task_spec.get("time_logs", [])

    return graph


def update_task(
    graph: nx.DiGraph,
    task_id: int,
    user_id: str = None,
    name: str = None,
    completed: bool = None,
    importance: float = None,
    project: float = None,
    due: datetime.datetime = None,
) -> Task:
    """sets properties in a given task id by all values in kwargs
    if None, will remove property
    """
    if task_id in graph.nodes:

        task = get_task_from_graph(task_id, graph)

        if user_id is not None and len(str(user_id)):
            task.user_id = user_id
        if name is not None and len(name):
            task.name = name
        if completed is not None:
            task.completed = completed
        if project is not None:
            task.project = project
        if importance is not None:
            task.importance = float(importance)
        if due is not None:
            task.due = due

        graph = update_task_in_graph(task, graph)
        return task
    return None


def complete_task(
    graph: nx.DiGraph,
    task_id: int,
    end_time: datetime.datetime = None,
) -> Task:
    """sets the end_time to the last time_log (creates one if missing)
    and sets completed flag to True
    """
    end_time = end_time or datetime.datetime.now()

    task = get_task_from_graph(task_id, graph)

    if task is None:  # Cannot find task
        return None

    if task.completed:  # Nothing to update
        return task

    task.completed = True

    if len(task.time_logs):
        last_log = task.time_logs[-1]
        if last_log.end_time is None:
            last_log.end_time = end_time
        # else already exists, don't update
    else:  # no logs
        time_log = TimeLog(
            task_id=task.task_id,
            user_id=task.user_id,
            start_time=None,
            end_time=end_time,
            note=None,
        )
        task.time_logs.append(time_log)

    graph = update_task_in_graph(task, graph)
    return task


def add_tag(graph: nx.DiGraph, task_id: int, tag: str):
    task = get_task_from_graph(task_id, graph)
    tags = set(task.tags)
    tags.add(tag)
    task.tags = list(tags)
    graph = update_task_in_graph(task, graph)


def remove_tag(graph: nx.DiGraph, task_id: int, tag: str):
    task = get_task_from_graph(task_id, graph)
    tags = set(task.tags)
    tags.remove(tag)
    task.tags = list(tags)
    graph = update_task_in_graph(task, graph)


def add_url(graph: nx.DiGraph, task_id: int, url: str):
    task = get_task_from_graph(task_id, graph)
    urls = set(task.urls)
    urls.add(url)
    task.urls = list(urls)
    graph = update_task_in_graph(task, graph)


def remove_url(graph: nx.DiGraph, task_id: int, url: str):
    task = get_task_from_graph(task_id, graph)
    urls = set(task.urls)
    urls.remove(url)
    task.urls = list(urls)
    graph = update_task_in_graph(task, graph)


def add_user(graph: nx.DiGraph, task_id: int, user: str):
    task = get_task_from_graph(task_id, graph)
    users = set(task.users)
    users.add(user)
    task.users = list(users)
    graph = update_task_in_graph(task, graph)


def remove_user(graph: nx.DiGraph, task_id: int, user: str):
    task = get_task_from_graph(task_id, graph)
    users = set(task.users)
    users.remove(users)
    task.users = list(users)
    graph = update_task_in_graph(task, graph)


def add_note(graph: nx.DiGraph, task_id: int, note: str):
    task = get_task_from_graph(task_id, graph)
    if task.notes is None:
        task.notes = []
    task.notes.append(note)
    graph = update_task_in_graph(task, graph)


def update_note(graph: nx.DiGraph, task_id: int, note_id: int, note: str):
    task = get_task_from_graph(task_id, graph)
    if note_id < len(task.notes):
        task.notes[note_id] = note
    graph = update_task_in_graph(task, graph)


def remove_note(graph: nx.DiGraph, task_id: int, note_id: int):
    task = get_task_from_graph(task_id, graph)
    if 0 <= note_id < len(task.notes):
        task.notes.pop(note_id)
        graph = update_task_in_graph(task, graph)


# Multiple Task
def list_tasks(
    graph: nx.DiGraph,
    sort_by: str = "importance",
    limit: int = 10,
    ascending=False,
    only_leaves=False,
    all_projects=False,
    search: str = None,
    tags: Optional[List[str]] = None,
    urls: Optional[List[str]] = None,
    users: Optional[List[str]] = None,
):
    # can sort by 'importance','name','due'

    node_ids: List[int] = sort_nodes(
        graph,
        sort_by=sort_by,
        limit=limit,
        ascending=ascending,
        only_leaves=only_leaves,
    )

    current_project = os.environ.get("WN_PROJECT", None)
    if not all_projects and current_project is not None:
        node_ids = [
            node_id
            for node_id in node_ids
            if graph.nodes[node_id]["task"].project == current_project
        ]

    # Regexp
    if search is not None and len(search):
        pattern = re.compile(search)
        node_ids = [
            node_id
            for node_id in node_ids
            if pattern(graph.nodes[node_id]["task"].name or "")
        ]

    if tags is not None and len(tags):
        tags = set(tags)
        node_ids = [
            node_id
            for node_id in node_ids
            if len(set(graph.nodes[node_id]["task"].tags or []).intersection(tags))
        ]

    if urls is not None and len(urls):
        urls = set(urls)
        node_ids = [
            node_id
            for node_id in node_ids
            if len(set(graph.nodes[node_id]["task"].urls or []).intersection(urls))
        ]

    if users is not None and len(users):
        users = set(users)
        node_ids = [
            node_id
            for node_id in node_ids
            if len(set(graph.nodes[node_id]["task"].users or [])).intersection(users)
        ]

    return [graph.nodes[node_id]["task"] for node_id in node_ids]

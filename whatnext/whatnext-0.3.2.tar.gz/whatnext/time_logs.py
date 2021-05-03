"""CRUD operations on data_model.TimeLog

"""
import datetime
import logging

import networkx as nx

from .data_model import TimeLog
from .tasks import get_task_from_graph, update_task_in_graph

logger = logging.getLogger(__file__)


def create_timelog(graph: nx.DiGraph, task_id: int, note: str = None) -> nx.DiGraph:

    task = get_task_from_graph(task_id, graph)

    if task is None:  # Cannot find task
        return None

    if task.time_logs is None:
        task.time_logs = []

    time_log = TimeLog(
        user_id=task.user_id,
        task_id=task_id,
        note=note,
        start_time=datetime.datetime.now(),
    )
    task.time_logs.append(time_log)
    graph = update_task_in_graph(task, graph)
    return graph


def delete_timelog(graph: nx.DiGraph, task_id: int, time_log_id: int) -> int:

    task = get_task_from_graph(task_id, graph)

    if task is None:  # Cannot find task
        return None

    if task.time_logs is None:
        task.time_logs = []

    if 0 <= time_log_id <= len(task.time_logs):
        task.time_logs.pop(time_log_id)

    graph = update_task_in_graph(task, graph)


def update_timelog_note(
    graph: nx.DiGraph, task_id: int, time_log_id: int, note: str
) -> int:

    task = get_task_from_graph(task_id, graph)

    if task is None:  # Cannot find task
        return None

    if task.time_logs is None:
        task.time_logs = []

    if 0 <= time_log_id <= len(task.time_logs):
        task.time_logs[time_log_id].note = note
        graph = update_task_in_graph(task, graph)

    return graph


def start_timelog(
    graph: nx.DiGraph,
    task_id: int,
    time_log_id: int = None,
    start_time: datetime.datetime = None,
) -> datetime.datetime:

    task = get_task_from_graph(task_id, graph)

    if task is None:  # Cannot find task
        return None

    if task.time_logs is None:
        task.time_logs = []

    # update start time
    if time_log_id is not None and (0 <= time_log_id <= len(task.time_logs)):
        start_time = (
            task.time_logs[time_log_id].start_time
            or start_time
            or datetime.datetime.now()
        )
        task.time_logs[time_log_id].start_time = start_time
    else:
        task.time_logs.append(
            TimeLog(
                task_id=task.task_id,
                user_id=task.user_id,
                start_time=start_time or datetime.datetime.now(),
            )
        )
    graph = update_task_in_graph(task, graph)
    return graph


def end_timelog(
    graph: nx.DiGraph,
    task_id: int,
    time_log_id: int = None,
    end_time: datetime.datetime = None,
) -> datetime.datetime:

    task = get_task_from_graph(task_id, graph)

    if task is None:  # Cannot find task
        return None

    if task.time_logs is None:
        task.time_logs = []

    # update start time
    if time_log_id is not None and (0 <= time_log_id <= len(task.time_logs)):
        end_time = (
            task.time_logs[time_log_id].end_time or end_time or datetime.datetime.now()
        )
        task.time_logs[time_log_id].end_time = end_time
    else:
        task.time_logs.append(
            TimeLog(
                task_id=task.task_id,
                user_id=task.user_id,
                end_time=end_time or datetime.datetime.now(),
            )
        )
    graph = update_task_in_graph(task, graph)
    return graph

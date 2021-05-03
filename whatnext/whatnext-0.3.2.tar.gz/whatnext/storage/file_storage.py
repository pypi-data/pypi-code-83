import datetime
import json
import logging
import os
import shutil

import networkx as nx
from networkx.readwrite.gml import read_gml, write_gml

from ..data_model import Task

logger = logging.getLogger(__file__)

fields_to_encode = ["due", "tags", "urls", "users", "notes", "time_logs"]


def default(obj):
    if isinstance(obj, (datetime.datetime, datetime.date)):
        return {"_isoformat": obj.isoformat()}
    return super().default(obj)


def object_hook(obj):
    _isoformat = obj.get("_isoformat")
    if _isoformat is not None:
        return datetime.datetime.fromisoformat(_isoformat)
    return obj


def format_filename(fname: str = None) -> str:
    root_path = os.environ.get("WN_STORAGE_DIR", "~")
    if fname is None:
        fname = os.path.join(root_path, ".whatnext.gml")
    return fname


def copy_file(fname: str, new_fname: str):
    shutil.copyfile(fname, new_fname)


def cast_to_int(src_id):
    try:
        return int(src_id)
    except ValueError:
        return src_id


def load_from_file(fname: str = None, make_backup=True) -> nx.DiGraph:

    fname = format_filename(fname)

    if make_backup:
        copy_file(fname, fname + ".backup")

    src: nx.DiGraph = read_gml(fname)

    # rename notes from strings to integers where possible
    task_graph = nx.DiGraph()
    for src_id in src.nodes():
        task_graph.add_node(cast_to_int(src_id), **src._node[src_id])

    for src_id, dest_id in src.edges():
        task_graph.add_edge(cast_to_int(src_id), cast_to_int(dest_id))

    # convert dictionary properties back into Task and TimeLogs
    for node_id in task_graph.nodes:
        task = task_graph.nodes[node_id]["task"]

        for field in fields_to_encode:
            value = task.get(field, None)
            if value is not None:
                task[field] = json.loads(value, object_hook=object_hook)
        task_graph.nodes[node_id]["task"] = Task(**task)

    return task_graph


def save_to_file(graph, fname: str = None):
    g = graph.copy(as_view=False)  # copy data

    for node_id in g.nodes:
        if g.nodes[node_id]["task"]:
            task = g.nodes[node_id]["task"].dict(
                exclude_defaults=True, exclude_none=True, exclude_unset=True
            )
            for field in fields_to_encode:
                if field in task:
                    value = task[field]
                    if isinstance(value, list) and len(value) == 0:
                        del task[field]
                    elif value is None:
                        del task[field]
                    else:
                        task[field] = json.dumps(value, default=default)
            g.nodes[node_id]["task"] = task

    return write_gml(g, format_filename(fname))

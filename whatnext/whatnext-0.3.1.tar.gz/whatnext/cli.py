import logging
import os
from typing import List

import networkx as nx
import typer
from colorama import init as init_colorama
from tabulate import tabulate
from termcolor import colored

from .graph import create_graph, load, save
from .parser import parse
from .tasks import list_tasks
from .time_logs import create_timelog

# Global variables (I know, I know...)
app = typer.Typer()
graph: nx.DiGraph = None

# Configuration / Logging
init_colorama(autoreset=True)
logger = logging.getLogger(__file__)


def get_banner(color="green"):
    """JS Stick Letters
    https://github.com/pwaller/pyfiglet
    http://patorjk.com/software/taag/#p=testall&f=Acrobatic&t=WhatNext%20-%3E
    """
    # pylint: disable=anomalous-backslash-in-string
    banner = """
>>                ___          ___     ___
>> |  | |__|  /\\   |     |\\ | |__  \\_/  |   ___\\
>> |/\\| |  | /~~\\  |     | \\| |___ / \\  |      /
>>
"""
    # Coloring https://pypi.org/project/colorama/
    return colored(
        "\n".join([b for b in banner.splitlines() if len(b.strip())]),
        color=color,
    )


# https://pypi.org/project/tabulate/

# CRUD Task

# create_task
# update_task
#
# list_tasks
# view_task
# start -> adds a time


@app.command()
def show():
    # Taken from https://codegolf.stackexchange.com/questions/11693/ascii-visualize-a-graph#
    # https://stackoverflow.com/questions/834395/python-ascii-graph-drawing
    R = " ".join([",".join([str(e2) for e2 in e]) for e in graph.edges()])

    # TODO more sophisticed sorting
    V = sorted(list(set(R) - {","}))
    T = [" "] * 40
    lines = []
    for e in R.split():
        x, y = sorted(map(V.index, e[::2]))
        line = " ".join(T[:x] + ["+" + "--" * (y - x - 1) + "->"] + T[y + 1 :])
        lines.append(line)
        T[x] = T[y] = "|"
        line = " ".join(T)
        lines.append(line)
    line = colored(" ".join(V), color="green")
    lines.append(line)

    typer.echo("\n".join(lines))


@app.command("list")
def cli_list_tasks(
    sort_by: str = typer.Option(
        "importance",
        help="sort results by: importance, name, due, or id",
    ),
    limit: int = 10,
    ascending: bool = False,
    all_tasks: bool = False,
    search: str = None,
    tags: List[str] = None,
    urls: List[str] = None,
    users: List[str] = None,
    verbose: bool = False,
):

    tasks = list_tasks(
        graph,
        sort_by=sort_by,
        limit=limit,
        ascending=ascending,
        only_leaves=not all_tasks,
        search=search,
        tags=tags,
        urls=urls,
        users=users,
    )

    if verbose:
        fields = [
            "task_id",
            "importance",
            "name",
            "due",
            "tags",
            "urls",
            "users",
            "notes",
            "time_logs",
            "completed",
        ]
    else:
        fields = [
            "task_id",
            "importance",
            "name",
            "due",
            "tags",
            "users",
            "completed",
        ]

    table = tabulate(
        [[t.dict()[field] for field in fields] for t in tasks], headers=fields
    )
    typer.echo(table)


@app.command("task")
def next_task(
    sort_by: str = typer.Option(
        "importance",
        help="sort results by: importance, name, due, or id",
    ),
    ascending: bool = False,
    all_tasks: bool = False,
    search: str = None,
    tags: List[str] = None,
    urls: List[str] = None,
    users: List[str] = None,
    verbose: bool = False,
):

    tasks = list_tasks(
        graph,
        sort_by=sort_by,
        limit=1,
        ascending=ascending,
        only_leaves=not all_tasks,
        search=search,
        tags=tags,
        urls=urls,
        users=users,
    )

    if verbose:
        fields = [
            "task_id",
            "importance",
            "name",
            "due",
            "tags",
            "urls",
            "users",
            "notes",
            "time_logs",
            "completed",
        ]
    else:
        fields = [
            "task_id",
            "importance",
            "name",
            "due",
            "tags",
            "users",
            "completed",
        ]

    table = tabulate(
        [[t.dict()[field] for field in fields] for t in tasks], headers=fields
    )
    typer.echo(table)


@app.command()
def start(task_id: int, note: str = None):
    """Starts a task"""
    create_timelog(graph, task_id, note=note)
    save(graph)


@app.command()
def delete_all(
    force: bool = typer.Option(..., prompt="Are you sure you want to delete all tasks?")
):
    global graph
    if force:
        typer.echo("Deleting graph")
        graph = create_graph()
        save(graph)
    else:
        typer.echo("Aborted")


@app.command("add")
def add(new_task_or_tasks: str):
    global graph
    num_tasks = len(graph.nodes)
    graph = parse(graph, new_task_or_tasks)
    num_tasks2 = len(graph.nodes)
    typer.echo(f"Created {num_tasks2 - num_tasks} tasks")
    save(graph)


@app.command("set-storage")
def set_storage(new_directory: str):
    os.environ["WN_STORAGE_DIR"] = new_directory
    typer.echo(f"WN_STORAGE_DIR set to {new_directory}")


@app.command("set-project")
def set_project(project: str):
    os.environ["WN_PROJECT"] = project
    typer.echo(f"WN_PROJECT set to {project}")


def main():
    global graph
    typer.echo(get_banner())

    try:
        graph = load()
    except Exception as e:
        logger.error(f"Graph Load Exception {e}: graph data might be corrupted")
        return

    app()


if __name__ == "__main__":
    main()

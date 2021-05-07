import http.server
import re
import shutil
import socketserver
import webbrowser
from os import fspath, listdir, path
from pathlib import Path
from typing import Any, List, Set, Tuple, Union
from uuid import uuid1

import networkx as nx
import pydot
from graphviz import Digraph

from .parser import SqlParser


class LineageGraph:
    _node_attrs = {"color": "lightblue2", "style": "filled", "shape": "rect"}
    _clause_attrs = {"shape": "diamond", "color": "lightgrey"}
    _source_attrs = {"color": "palegreen"}
    _inner_query_attrs = {"shape": "ellipse", "color": "lightgoldenrod2"}
    _union_query_attrs = {"shape": "ellipse", "color": "lightcoral"}
    parser = SqlParser()

    def __init__(self):
        self.clear_graph()

    def __str__(self):
        return f"Lineage Graph with {len(self)} edges."

    def __len__(self):
        return len(self.edges)

    def _get_sources(self, parsed: Union[list, dict]) -> List[Any]:
        "Split parsed into sources. Will be iterated over to build edges."
        if isinstance(parsed, dict):
            # End-source or inner query
            return [
                (clause, value["content"])
                for clause, value in parsed.items()
                if "join" in clause or clause == "from"
            ]
        else:
            # Union query
            return [(None, parsed)]

    def _get_edges(
        self, target: str, parsed: Union[list, dict], edges: set
    ) -> Set[Tuple[str, str, str]]:
        "Get all edges for lineage graph to be extended."

        # Split parsed into standardized sources
        sources = self._get_sources(parsed)

        # Iterate over sources, handle three options differently
        for clause, source in sources:

            # 1. End target
            if isinstance(source, str):
                edges.add((target, clause, source))
            # 2. Inner query
            elif isinstance(source, dict):
                inner_query = f"Inner Query {uuid1()}"
                edges.add((target, clause, inner_query))
                edges.update(self._get_edges(inner_query, source, edges))
            # 3. Union query
            elif isinstance(source, list):
                union_query = f"Union Query {uuid1()}"
                edges.add((target, None, union_query))

                for union_source in source:
                    inner_query = f"Inner Query {uuid1()}"
                    edges.add((union_query, None, inner_query))
                    edges.update(self._get_edges(inner_query, union_source, edges))

        return edges

    def _extend_graph(self, top_level_target: str, parsed: Union[list, dict]) -> None:
        """Extend graph by collecting edges and adding conditionally based
        on source type."""
        edges = self._get_edges(top_level_target, parsed, edges=set())

        self.edges.update(edges)

        for target, clause, source in edges:
            # Standardize label for inner/union queries
            if "Inner Query" in target:
                self.graph.node(target, label="Inner Query", **self._inner_query_attrs)
            if "Union Query" in target:
                self.graph.node(target, label="Union Query", **self._union_query_attrs)

            if clause:
                # Unique connector with clause and target
                connector = f"Connector-{clause}-{target}"
                self.graph.node(connector, label=clause, **self._clause_attrs)
                # Add final edges, through connector
                self.graph.edge(source, connector)
                self.graph.edge(connector, target)
            else:
                self.graph.edge(source, target)

        targets, clauses, sources = zip(*self.edges)

        nodes = set(sources) | set(targets)
        source_nodes = set(sources) - set(targets)

        for node in nodes:
            if not node.startswith(("Connector", "Inner Query", "Union Query")):
                self.graph.node(
                    node,
                    **(
                        self._source_attrs if node in source_nodes else self._node_attrs
                    ),
                )

    def _get_top_level_target(self, query: str) -> str:
        "Find target: Table or View to be created."
        reg = r"^\s*(?:CREATE\s+(?:OR REPLACE\s+)?(?:VIEW|TABLE)\s+)([\S]+)"
        result = re.findall(reg, query, flags=re.I)
        if len(result) == 0:
            raise ValueError(
                "Please provide input string with a CREATE TABLE/VIEW statement."
            )
        target = result[0]
        return target

    def clear_graph(self) -> None:
        self.graph = Digraph(
            "Lineage Graph",
            # Standard node attrs for sources
            node_attr=self._node_attrs,
            # Disallow duplication
            strict=True,
        )
        self.edges: set = set()

    def extend_graph_from_input_string(self, input_string: str) -> None:
        "Provide a create statement to extend the data lineage graph."
        top_level_target = self._get_top_level_target(input_string)
        parsed = self.parser.parse(input_string)
        self._extend_graph(top_level_target, parsed)

    def extend_graph_from_directory(self, dir: str) -> None:
        "Build data lineage graph from data directory."
        files = listdir(dir)
        sql_files = filter(lambda f: f.endswith(".sql"), files)

        for file_name in sql_files:
            with open(path.join(dir, file_name), "r") as f:
                input_string = f.read()
                self.extend_graph_from_input_string(input_string)

    def get_execution_order(self) -> List[str]:
        "Get execution order of tables / views."
        dot_graph = pydot.graph_from_dot_data(self.graph.source)[0]
        nx_graph = nx.nx_pydot.from_pydot(dot_graph)

        execution_order = [
            node
            for node in nx.topological_sort(nx_graph)
            if not node.startswith(("Connector", "Inner Query", "Union Query"))
        ]

        return execution_order

    def serve_graph(self) -> None:
        "Serve graph as .html file"

        PORT = 8000
        DIRECTORY = "out"

        print(f"Writing files to /{DIRECTORY}")

        # Render graph as .gv and .gv.pdf
        self.graph.render(directory=DIRECTORY)

        # Copy template index.html to load .gv using d3-graphviz
        PACKAGE_PATH = fspath(Path(__file__).parent)
        shutil.copy(
            path.join(PACKAGE_PATH, "templates", "index.html"),
            f"{DIRECTORY}/index.html",
        )

        def start_server() -> None:
            class Handler(http.server.SimpleHTTPRequestHandler):
                def __init__(self, *args: Any, **kwargs: Any):
                    super().__init__(
                        directory=DIRECTORY, *args, **kwargs
                    )  # type: ignore

            with socketserver.TCPServer(("", PORT), Handler) as httpd:
                print(f"Serving at port {PORT}")
                httpd.serve_forever()

        def open_webbrowser() -> None:
            webbrowser.open(f"http://localhost:{PORT}", new=2)

        open_webbrowser()
        start_server()

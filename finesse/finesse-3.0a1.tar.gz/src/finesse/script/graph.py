"""Graph represening a parsed kat script file."""

# Can remove once Finesse requires at least Python 3.9.
from __future__ import annotations

from enum import auto, Flag
import networkx as nx


class KatNodeType(Flag):
    ROOT = auto()

    # Containers.
    ELEMENT = auto()
    FUNCTION = auto()
    EXPRESSION = auto()
    GROUPED_EXPRESSION = auto()
    ARRAY = auto()
    NUMERICAL_ARRAY = auto()

    # Terminals.
    VALUE = auto()
    PARAMETER = auto()
    PARAMETER_REFERENCE = auto()
    CONSTANT = auto()
    KEYWORD = auto()

    # Directive types.
    DIRECTIVE_NODES = ELEMENT | FUNCTION

    # Dependent types.
    DEPENDENT_NODES = PARAMETER | PARAMETER_REFERENCE

    # Nodes that don't have any further (incoming) dependencies. The compiler and
    # generator terminal nodes are slightly different due to the handling of references.
    COMPILER_TERMINAL_NODES = VALUE | KEYWORD
    GENERATOR_TERMINAL_NODES = (
        VALUE | KEYWORD | CONSTANT | PARAMETER | PARAMETER_REFERENCE
    )

    def __str__(self):
        return self.name


class KatEdgeType(Flag):
    ARGUMENT = auto()
    # Dependent parameter values/references.
    DEPENDENCY = auto()

    def __str__(self):
        return self.name


class KatGraph(nx.DiGraph):
    """Kat script graph."""

    ROOT_NODE_NAME = ".script"

    def is_tree(self):
        return nx.is_tree(self)

    def root_directive_graph(self):
        graph = self.subgraph(self.root_directive_nodes()).copy()

        # Reassign parameter dependencies so the source is from the owning element.
        for target_directive, source_argument, data in self.edges(data=True):
            if data["type"] != KatEdgeType.DEPENDENCY:
                continue

            source_directive = self.branch_base(source_argument)
            graph.add_edge(target_directive, source_directive, **data)

        return graph

    def _node_view(self, nodes, data=False, default=None):
        """Return a node view in the same way that calling :class:`nx.DiGraph.nodes`
        would."""
        nodegraph = self.subgraph(nodes)
        if data is False:
            return nodegraph.nodes
        return nx.reportviews.NodeDataView(nodegraph.nodes, data, default)

    def _in_edge_view(self, edges, data=False, default=None):
        edgegraph = self.edge_subgraph(edges)
        if data is False:
            return edgegraph.edges
        return nx.reportviews.InEdgeView(edgegraph).data(data=data, default=default)

    def _out_edge_view(self, edges, data=False, default=None):
        edgegraph = self.edge_subgraph(edges)
        if data is False:
            return edgegraph.edges
        return nx.reportviews.OutEdgeView(edgegraph).data(data=data, default=default)

    def nodes_by_node_type(self, node_type, **kwargs):
        """Get nodes by type, with optional data."""
        return self._node_view(
            [
                node
                for node, ntype in self.nodes(data="type")
                if ntype and ntype in node_type
            ],
            **kwargs,
        )

    def in_edges_by_edge_type(self, node, edge_types, **kwargs):
        return self._in_edge_view(
            [
                (u, v)
                for u, v, edge_type in self.in_edges(node, data="type")
                if edge_type and edge_type in edge_types
            ],
            **kwargs,
        )

    def out_edges_by_edge_type(self, node, edge_types, **kwargs):
        return self._out_edge_view(
            [
                (u, v)
                for u, v, edge_type in self.out_edges(node, data="type")
                if edge_type and edge_type in edge_types
            ],
            **kwargs,
        )

    def in_edge_source_nodes_by_edge_type(self, node, edge_types, **kwargs):
        edges = self.in_edges_by_edge_type(node, edge_types)
        return self._node_view([edge[0] for edge in edges], **kwargs)

    def out_edge_target_nodes_by_edge_type(self, node, edge_types, **kwargs):
        edges = self.out_edges_by_edge_type(node, edge_types)
        return self._node_view([edge[1] for edge in edges], **kwargs)

    def root_argument_edges(self, **kwargs):
        return self.in_edges_by_edge_type(
            self.ROOT_NODE_NAME, KatEdgeType.ARGUMENT, **kwargs
        )

    def directive_nodes(self, **kwargs):
        """All directive nodes."""
        return self.nodes_by_node_type(KatNodeType.DIRECTIVE_NODES, **kwargs)

    def root_directive_nodes(self, **kwargs):
        # Return nodes that are a DIRECTIVE_NODES type but don't have outgoing edges
        # (dependencies) of type ARGUMENT which would indicate they are not a root
        # directive.
        return self.in_edge_source_nodes_by_edge_type(
            self.ROOT_NODE_NAME, KatEdgeType.ARGUMENT, **kwargs
        )

    def dependent_argument_nodes(self, node, **kwargs):
        return self.in_edge_source_nodes_by_edge_type(
            node, KatEdgeType.ARGUMENT, **kwargs
        )

    def argument_node_order(self, node):
        edges = self.out_edges_by_edge_type(node, KatEdgeType.ARGUMENT, data="order")
        if (nedges := len(edges)) != 1:
            raise RuntimeError(f"expected 1 argument edge, got {nedges}")
        _, __, order = next(iter(edges))
        return order

    def filter_argument_nodes(self, node, key):
        for argument_node, data in self.dependent_argument_nodes(node, data=True):
            if key(argument_node, data):
                yield argument_node

    def filter_dependent_nodes(self, node, key):
        nodes = self.out_edge_target_nodes_by_edge_type(
            node, KatEdgeType.DEPENDENCY, data=True
        )
        for dependent_node, data in nodes:
            if key(dependent_node, data):
                yield dependent_node

    def is_independent(self, node):
        """Check if the node has no external dependencies.

        A node is independent if it is a terminal type or if its arguments have no non-
        argument incoming edges.
        """
        if dependencies := self.dependent_argument_nodes(node):
            return all(self.is_independent(dep) for dep in dependencies)
        node_type = self.nodes[node]["type"]
        if node_type not in KatNodeType.COMPILER_TERMINAL_NODES or self.in_edges(node):
            return False
        return True

    @classmethod
    def item_node_name(cls, name, parent_path):
        return f"{parent_path}.{name}"

    @classmethod
    def branch_base(cls, path, reference=ROOT_NODE_NAME):
        """The branch base node name for `path`, relative to `reference`."""
        prefix = f"{reference}."
        assert cls.is_subpath(path, prefix), f"{path} must start with {prefix}"
        path = path[len(prefix) :]
        return f"{prefix}{path.split('.')[0]}"

    @classmethod
    def is_subpath(cls, path, reference):
        """Check if `path` is a subpath of `reference`."""
        return path.startswith(reference)

    def param_target_element_path(self, target):
        """The owning element path for `target`.

        Target should be in the form "element_name{.param_name{.param_name {...}}}.
        """
        # Grab the target's element name.
        pieces = target.split(".")
        assert len(pieces) >= 1, f"{target} is an invalid param path"
        owner = pieces[0]

        for path, name_token in self.root_directive_nodes(data="name_token"):
            if not name_token:
                # Not an element.
                continue
            if name_token.value == owner:
                return path

        raise ValueError(f"target '{target}' not found")

import dataclasses
from typing import Any, Callable

from gamla import currying, dict_utils, functional, functional_generic


@currying.curry
def tree_reduce(get_children: Callable, reduce_fn: Callable, tree_node):
    """Reduces a tree from the bottom up.

    Given `get_children`, a function from a node to its children,
    and `reduce_fn`, which gets a node and the results of the reduce on the children,
    reduces a tree upwards.
    """
    return reduce_fn(
        tree_node,
        map(tree_reduce(get_children, reduce_fn), get_children(tree_node)),
    )


def tree_reduce_async(get_children: Callable, reduce_fn: Callable):
    """Async version of `tree_reduce`."""

    async def tree_reduce_async_inner(tree_node):
        return await reduce_fn(
            tree_node,
            await functional_generic.pipe(
                tree_node,
                get_children,
                functional_generic.curried_map(
                    tree_reduce_async(get_children, reduce_fn),
                ),
            ),
        )

    return tree_reduce_async_inner


@dataclasses.dataclass(frozen=True)
class KeyValue:
    key: Any
    value: Any


_is_terminal = functional_generic.anyjuxt(
    functional.is_instance(str),
    functional.is_instance(int),
    functional.is_instance(float),
)


def _get_children(element):
    return functional_generic.case_dict(
        {
            _is_terminal: functional.just(()),
            functional.is_instance(tuple): functional.identity,
            functional.is_instance(list): functional.identity,
            functional.is_instance(dict): functional_generic.compose_left(
                dict.items,
                functional.curried_map_sync(functional.star(KeyValue)),
            ),
            functional.is_instance(KeyValue): functional_generic.compose_left(
                lambda x: x.value,
                functional_generic.ternary(
                    _is_terminal,
                    functional.wrap_tuple,
                    _get_children,
                ),
            ),
        },
    )(element)


_MATCHED = "matched"
_UNMATCHED = "unmatched"
_get_matched = dict_utils.itemgetter(_MATCHED)
_get_unmatched = dict_utils.itemgetter(_UNMATCHED)


def _make_matched_unmatched(matched, unmatched):
    return {_MATCHED: matched, _UNMATCHED: unmatched}


_merge_children_as_matched = functional_generic.compose_left(
    functional_generic.mapcat(functional_generic.juxtcat(_get_matched, _get_unmatched)),
    tuple,
    functional_generic.pair_right(functional.just(())),
    functional.star(_make_matched_unmatched),
)

_merge_children = functional_generic.compose_left(
    functional_generic.bifurcate(
        functional_generic.compose_left(functional_generic.mapcat(_get_matched), tuple),
        functional_generic.compose_left(
            functional_generic.mapcat(_get_unmatched),
            tuple,
        ),
    ),
    functional.star(_make_matched_unmatched),
)


@currying.curry
def _get_anywhere_reducer(predicate: Callable, node, children):
    if _is_terminal(node):
        return _make_matched_unmatched((), (node,))
    if isinstance(node, KeyValue) and predicate(node.key):
        return _merge_children_as_matched(children)
    return _merge_children(children)


def get_leaves_by_ancestor_predicate(predicate: Callable):
    """Gets a predicate, and builds a function that gets a dictionary, potentially nested and returns an iterable of leaf values.
    The values returned are of leafs where some ancestor (possibly indirect) passes the predicate.

    >>> gamla.pipe({"x": {"y": (1, 2, 3)}}, gamla.get_leaves_by_ancestor_predicate(gamla.equals("x")), tuple)
    (1, 2, 3)
    >>> gamla.pipe({"x": {"y": (1, 2, 3)}}, gamla.get_leaves_by_ancestor_predicate(gamla.equals("z")), tuple)
    ()

    Useful for retrieving values from large json objects, where the exact path is unimportant.
    """
    return functional_generic.compose_left(
        tree_reduce(_get_children, _get_anywhere_reducer(predicate)),
        _get_matched,
    )


@currying.curry
def _filter_leaves_reducer(predicate, node, children):
    if _is_terminal(node) and predicate(node):
        return (node,)
    return functional_generic.concat(children)


def filter_leaves(predicate: Callable):
    """Gets a predicate, and builds a function that gets a dictionary, potentially nested and returns an iterable of leaf values.
    The values returned are of leafs that pass the predicate.

    >>> gamla.pipe({"x": {"y": (1, 2, 3)}}, gamla.filter_leaves(gamla.greater_than(2)), tuple)
    (3,)

    Useful for retrieving values from large json objects, where the exact path is unimportant.
    """
    return tree_reduce(_get_children, _filter_leaves_reducer(predicate))


#: Reduce a JSON like tree.
json_tree_reduce = tree_reduce(_get_children)

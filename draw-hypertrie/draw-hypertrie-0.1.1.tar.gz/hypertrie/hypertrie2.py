from collections import defaultdict
from typing import List, Tuple, DefaultDict, Dict, Union, Optional, Set

hash_t = str

HTKeyPart = int

HTKey = Tuple[HTKeyPart, ...]

children_t = Union[Tuple[Dict[HTKeyPart, Union[hash_t, HTKeyPart]], ...],  # uncompressed node depth > 1
                   HTKey,  # compressed node depth > 1
                   Tuple[Set[Union[hash_t, HTKeyPart]]]]  # uncompressed node depth == 1


def hash_keys(keys: List[HTKey]) -> hash_t:
    return hash_t(hash(tuple(keys)))


class HypertrieNode:
    def __init__(self, children: children_t, size=1, count: int = 1):
        self.children: children_t = children
        self.count: int = count
        self.size = size

    def inc(self):
        self.count += 1

    @property
    def n_dim(self):
        return len(self.children)


class HypertrieContext:
    def __init__(self, max_depth: int = 3):
        self._max_depth: int = max_depth
        self._storage: Tuple[Dict[hash_t, HypertrieNode], ...] = tuple(dict() for _ in range(max_depth))

    @property
    def max_depth(self):
        return self._max_depth

    @property
    def storage(self):
        return self._storage

    def create_hypertrie(self, keys: List[HTKey], depth=3, node_hash: Optional[hash_t] = None) -> hash_t:
        # not supported in this simplified version
        assert len(keys) >= 1
        assert not (len(keys) == 1 and depth == 1)

        if node_hash is None:
            keys.sort()
            node_hash: hash_t = hash_t(hash(tuple(keys)))

        if node_hash in self._storage[depth - 1]:
            self._storage[depth - 1][node_hash].inc()
        else:
            if len(keys) == 1:
                if depth > 1:
                    children: children_t = keys[0]
                else:
                    assert False, "currently not supported"
            else:

                if depth > 1:
                    children: children_t = tuple(dict() for _ in range(depth))
                else:
                    children: children_t = (set(),)

                for pos in range(depth):
                    # sort with key_part at pos as major
                    keys.sort(key=lambda x: (x[pos],) + x[:pos] + x[pos + 1:])
                    non_zero_slice_keys = sorted(set(key[pos] for key in keys))
                    slices: DefaultDict[HTKeyPart, List[HTKey]] = defaultdict(list)
                    for key in keys:
                        slices[key[pos]].append(key[:pos] + key[pos + 1:])
                    if depth > 1:
                        for slice_key_part, slice in slices.items():
                            if depth == 2 and len(slice) == 1:
                                # inlined depth 1 node in depth 2 node
                                children[pos][slice_key_part] = slice[0][0]
                            else:
                                # create and assign sub node hash
                                children[pos][slice_key_part] = self.create_hypertrie(
                                    keys=slice,
                                    depth=depth - 1
                                )
                    else:
                        for slice_key_part, _ in slices.items():
                            children[pos].add(slice_key_part)
            self._storage[depth - 1][node_hash] = HypertrieNode(children, len(keys))
        return node_hash

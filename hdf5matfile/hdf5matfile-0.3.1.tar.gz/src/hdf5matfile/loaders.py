from __future__ import annotations

import abc
from typing import Any

import h5py
import numpy as np


class AbstractLoader(abc.ABC):
    def __init__(self, matfile):
        self.matfile = matfile

    @abc.abstractmethod
    def load(self, item) -> Any:
        """Load the specified item from disk."""
        pass

    def _load_item(self, item):
        return self.matfile._load_item(item)


class StructLoader(AbstractLoader):
    """Loader for MATLAB type `struct`. Returns arrays of dict."""
    def load(self, struct: h5py.Group) -> np.ndarray:
        if self._is_struct_array(struct):
            s = self._load_array(struct)
        else:
            s = self._load_scalar(struct)
        return s

    def _load_scalar(self, struct: h5py.Group):
        d = {
            fieldname: self._load_item(item)
            for fieldname, item in struct.items()
        }
        return np.array([[d]], dtype='O')

    def _load_array(self, struct: h5py.Group):
        # Get an item from the struct to figure out how big it is, then stick it
        # back in the dict. I have no idea if there's a cleaner way, I just need
        # to inspect a single item *before* looping!
        pointers = dict(struct)
        fieldname, refarray = pointers.popitem()
        pointers[fieldname] = refarray

        # Initialize array of dict
        a = np.empty(refarray.shape, dtype='O')
        for i, _ in enumerate(a.flat):
            a[i] = dict()

        for fieldname, refarray in pointers.items():
            for i, ref in enumerate(refarray[()].flat):
                a.flat[i][fieldname] = self._load_item(ref)

        return a

    @staticmethod
    def _is_struct_array(struct: h5py.Group):
        """Determine whether the given MATLAB struct is scalar or not."""
        for field in struct.values():
            # MATLAB represents scalar structs and struct arrays differently
            # within HDF5. Scalar structs are ordinary groups with named
            # datasets and/or subgroups. Struct arrays, however, are represented
            # by a group with arrays of references. The arrays all have the same
            # size (that of the struct array itself), and are grouped by field
            # name.
            #
            # If the fields in the struct are *not* assigned a MATLAB_class,
            # then they're not actual objects. This is what differentiates a
            # struct array from a cell array -- the cell array is assigned a
            # MATLAB_class, and the fields of a struct array are not.
            try:
                matlab_class = field.attrs['MATLAB_class']
            except KeyError:
                isarray = True
                break
        else:
            # Executes if break doesn't fire
            isarray = False

        return isarray


class CellLoader(AbstractLoader):
    """Loader for the MATLAB type `cell`. Returns arrays with dtype 'object'."""
    def load(self, cell: h5py.Dataset) -> np.ndarray:
        a = np.empty(cell.shape, dtype='O')
        cellrefs = cell[()]
        for i, ref in enumerate(cellrefs.flat):
            a.flat[i] = self._load_item(ref)
        return a


class NumericLoader(AbstractLoader):
    """Loader for MATLAB numeric types."""
    def load(self, numeric: h5py.Dataset) -> np.ndarray:
        if 'MATLAB_empty' in numeric.attrs:
            return np.array([], dtype=numeric.dtype)
        return numeric[()]


class LogicalLoader(NumericLoader):
    """Loader for MATLAB type `logical`."""
    def load(self, logical: h5py.Dataset) -> np.ndarray:
        return super().load(logical).astype('bool8')


class CharLoader(AbstractLoader):
    """Loader for the MATLAB type `char`. Returns str.

    Multi-dimensional `char` arrays are flattened to 1-D and returned as str.
    """
    def load(self, char: h5py.Dataset) -> str:
        if 'MATLAB_empty' in char.attrs:
            return ''
        return char[()].tobytes('F').decode('utf-16')

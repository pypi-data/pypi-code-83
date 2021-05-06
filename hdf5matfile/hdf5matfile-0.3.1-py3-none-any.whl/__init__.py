import collections.abc
import importlib.resources
import os
import pathlib
from typing import Any, Dict, Generator, List, Type, Union

import h5py
import numpy as np

from .errors import MatlabDecodeError
from .loaders import (AbstractLoader, CellLoader, CharLoader, LogicalLoader,
                      NumericLoader, StructLoader)

__version__ = importlib.resources.read_text(__name__, '__version__')

__all__ = [
    'Hdf5Matfile',
    'load_hdf5mat',
]


class Hdf5Matfile(collections.abc.Mapping):
    """Load data from an v7.3 *.mat file. Only reading is supported, no writing.

    Usage
    -----

    To load all the variables from the file, use |load_file|:

    .. code-block:: python

        with Hdf5Matfile(filename) as file:
            data = file.load_file()

    To load a specific variable, use |load_variable|:

    .. code-block:: python

        with Hdf5Matfile(filename) as file:
            results = file.load_variable('results')

    A mapping/dict-like interface is also supported:

    .. code-block:: python

        with Hdf5Matfile(filename) as file:
            results = file['results']
            variables = list(file.keys())
            values = list(file.values())
            for var, value in file.items():
                ...

    If you're not using a context manager, make sure to close the file after
    you're done:

    .. code-block:: python

        file = Hdf5Matfile(filename)
        data = file.load_file()
        ...
        file.close()

    By default, arrays are not squeezed; since MATLAB represents even scalars
    as 2-D arrays, this means that something you expect to be a scalar will in
    fact be a 1-by-1 np.ndarray. You can change this by passing ``squeeze=True``
    to the constructor:

    .. code-block:: python

        with Hdf5Matfile(filename, squeeze=True) as file:
            data = file.load_file()

    Supported data types
    --------------------

    Data type support is pretty limited; this isn't a terribly fancy class.
    Supported MATLAB data types, and the Python objects or NumPy dtypes they map
    to:

    ===============  =============  =============
    MATLAB type      Python object  NumPy dtype
    ===============  =============  =============
    cell             np.ndarray     object
    char             str            n/a
    double           np.ndarray     double
    int8             np.ndarray     int8
    int16            np.ndarray     int16
    int32            np.ndarray     int32
    int64            np.ndarray     int64
    logical          np.ndarray     bool8
    single           np.ndarray     single
    struct (scalar)  dict           n/a
    struct (array)   np.ndarray     object (dict)
    uint8            np.ndarray     uint8
    uint16           np.ndarray     uint16
    uint32           np.ndarray     uint32
    uint64           np.ndarray     uint64
    ===============  =============  =============

    .. |load_file| :method:`Hdf5Matfile.load_file`
    .. |load_variable| :method:`Hdf5Matfile.load_variable`
    """
    def __init__(self, filename: os.PathLike, squeeze: bool = False):
        """Open a MATLAB v7.3 *.mat file.

        Parameters
        ----------
        filename : path_like
            Path to the *.mat file.

        squeeze : bool, int, optional
            If True, squeeze loaded arrays (remove dimensions with size 1). If
            the array only has one element, it is extracted from the array
            completely (instead of returning a 0-d array).
        """
        filepath = pathlib.Path(filename).resolve()
        try:
            self._h5file = h5py.File(filepath, 'r')
        except OSError as e:
            # Why are all the h5py errors just 'OSError'... ugh
            if 'No such file or directory' in str(e):
                raise FileNotFoundError(f'{filepath}') from e
            elif 'file signature not found' in str(e):
                raise OSError(f'Could not open {filepath} as HDF5 file') from e
            else:
                raise e
        self._loaders: Dict[str, AbstractLoader] = {}
        self.filepath = filepath
        self.squeeze = squeeze

    #=============================================
    # Context manager stuff
    #=============================================
    def __enter__(self):
        return self

    def __exit__(self, *exc):
        self.close()

    def __del__(self):
        self.close()

    def close(self):
        """Close the underlying h5py.File object."""
        # If object fails during creation (e.g., filename isn't valid), __del__
        # will throw an error due to missing attribute '_h5file'.
        try:
            self._h5file.close()
        except AttributeError:
            pass

    @property
    def closed(self):
        try:
            self._h5file.id.fileno
        except TypeError:
            return True
        return False

    #=============================================
    # Public interface
    #=============================================
    def load_file(self):
        """Load the entire file.

        Returns
        -------
        dict
            Dict whose keys are the top-level variable names.
        """
        d = {}
        for key, value in self._h5file.items():
            if key.startswith('#'):
                continue
            d[key] = self._load_item(value)
        return d

    def load_variable(self, varname: str):
        """Load a specific variable from the file.

        Parameters
        ----------
        varname : str
            The name of the variable to load.
        """
        if varname.startswith('#'):
            raise KeyError(f'{varname!r} is not a MATLAB variable.')

        return self._load_item(self._h5file[varname])

    #=============================================
    # Mapping interface
    #=============================================
    def __getitem__(self, varname: str):
        return self.load_variable(varname)

    def __iter__(self) -> Generator[str, Any, Any]:
        for key in self._h5file.keys():
            if key.startswith('#'):
                continue
            yield key

    def __len__(self):
        return len(list(iter(self)))

    #=============================================
    # Loaders
    #=============================================
    _loader_dispatch: Dict[str, Type[AbstractLoader]] = {}

    @classmethod
    def register_loader(cls, matlab_class: str, loader: Type[AbstractLoader]):
        cls._loader_dispatch[matlab_class] = loader

    def get_loader(self, matlab_class: str):
        try:
            loader = self._loaders[matlab_class]
        except KeyError:
            try:
                LoaderType = self._loader_dispatch[matlab_class]
            except KeyError as e:
                raise MatlabDecodeError('Unsupported MATLAB class'
                                        f' {matlab_class!r}') from e
            loader = self._loaders[matlab_class] = LoaderType(self)

        return loader

    def _load_item(self, item):
        if isinstance(item, h5py.Reference):
            return self._load_item(self._h5file[item])

        try:
            matlab_class = item.attrs['MATLAB_class'].decode()
        except KeyError:
            raise MatlabDecodeError('item does not have a MATLAB_class '
                                    'attribute and cannot be decoded')

        loader = self.get_loader(matlab_class)
        the_item = loader.load(item)
        return self._process(the_item)

    def _process(self, item):
        if isinstance(item, np.ndarray):
            # MATLAB arrays are column-major
            item = item.transpose()
            if self.squeeze:
                item = self._squeeze(item)

        return item

    @staticmethod
    def _squeeze(a: np.ndarray):
        if a.size == 1:
            squeezed = a.flat[0]
        else:
            squeezed = np.squeeze(a)
        return squeezed

# Collections
Hdf5Matfile.register_loader('struct', StructLoader)
Hdf5Matfile.register_loader('cell', CellLoader)

# Floats
Hdf5Matfile.register_loader('single', NumericLoader)
Hdf5Matfile.register_loader('double', NumericLoader)

# Integers
Hdf5Matfile.register_loader('logical', LogicalLoader)
Hdf5Matfile.register_loader('int8', NumericLoader)
Hdf5Matfile.register_loader('int16', NumericLoader)
Hdf5Matfile.register_loader('int32', NumericLoader)
Hdf5Matfile.register_loader('int64', NumericLoader)
Hdf5Matfile.register_loader('uint8', NumericLoader)
Hdf5Matfile.register_loader('uint16', NumericLoader)
Hdf5Matfile.register_loader('uint32', NumericLoader)
Hdf5Matfile.register_loader('uint64', NumericLoader)

# Strings
Hdf5Matfile.register_loader('char', CharLoader)


def load_hdf5mat(filename: os.PathLike,
                 variables: Union[str, List[str]] = None,
                 squeeze: bool = False):
    """Load a MATLAB v7.3 *.mat file. See |Hdf5Matfile| for limitations and
    supported data types.

    Parameters
    ----------
    filename : path_like
        Path to the *.mat file.

    variables : str, list[str], optional
        Variable name(s) to load. Default is None, which loads the entire file.

    squeeze : bool, optional
        If True, squeeze arrays and pop scalars. (default: False)


    .. |Hdf5Matfile| :class:`Hdf5Matfile`
    """
    with Hdf5Matfile(filename, squeeze=squeeze) as file:
        if variables is None:
            data = file.load_file()
        elif isinstance(variables, str):
            data = file.load_variable(variables)
        else:
            data = {var: file.load_variable(var) for var in variables}

    return data

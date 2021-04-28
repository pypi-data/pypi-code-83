from openamundsen.errors import RasterFileError
import rasterio


def read_raster_metadata(filename, crs=None):
    """
    Return metadata for a raster file.

    Parameters
    ----------
    filename : str or pathlib.Path

    crs : str, default None
        CRS to be set in the returned dict if the raster file does not contain
        CRS information. Must be a string parsable by rasterio.crs.CRS.from_string
        (e.g. "epsg:32632").

    Returns
    -------
    meta : dict
        Dictionary containing the following keys:
        - 'rows' (number of rows),
        - 'cols' (number of columns)
        - 'resolution' ((width, height) tuple)
        - 'crs': coordinate reference system
        - 'transform' (georeferencing transformation parameters)
    """
    meta = {}

    with rasterio.open(filename) as ds:
        if not (ds.res[0] == ds.res[1] == abs(ds.res[0])):
            raise RasterFileError('Raster file must have equal x and y resolution')

        meta['rows'] = ds.meta['height']
        meta['cols'] = ds.meta['width']
        meta['resolution'] = ds.res[0]
        meta['crs'] = ds.crs
        meta['transform'] = ds.meta['transform']

        if meta['crs'] is None and crs is not None:
            meta['crs'] = rasterio.crs.CRS.from_string(crs)

    return meta


def read_raster_file(filename, check_meta=None):
    """
    Read a raster file.

    Parameters
    ----------
    filename : str or pathlib.Path

    check_meta : dict, default None
        A metadata dictionary (as returned by `read_raster_metadata` to compare
        the current raster metadata with. If the metadata of the two rasters
        does not match (e.g., if the number of rows or columns differs) a
        RasterFileError is raised.

    Returns
    -------
    data : np.ndarray
    """
    if check_meta is not None:
        # compare only rows, cols, resolution and transform and not additional attributes
        # possibly stored in the check_meta object (such as x and y coordinates, CRS, etc.)
        cmp_keys = [
            'rows',
            'cols',
            'resolution',
            'transform',
        ]

        meta = read_raster_metadata(filename)

        d1 = {k: meta[k] for k in cmp_keys}
        d2 = {k: check_meta[k] for k in cmp_keys}

        if d1 != d2:
            raise RasterFileError(f'Metadata mismatch for {filename}')

    with rasterio.open(filename) as ds:
        data = ds.read(1)

    return data


def write_raster_file(filename, data, transform):
    """
    Write a raster file.

    Parameters
    ----------
    filename : str or pathlib.Path

    data : ndarray
        Array to be written.

    transform : rasterio.Affine
        Georeferencing transformation parameters.
    """
    meta = {
        'driver': 'AAIGrid',
        'dtype': data.dtype,
        'nodata': None,
        'width': data.shape[1],
        'height': data.shape[0],
        'count': 1,
        'crs': None,
        'transform': transform,
    }

    with rasterio.open(filename, 'w', **meta) as ds:
        ds.write(data, 1)

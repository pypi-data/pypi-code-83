""" Product, superclass of all EOReader satellites products """
# pylint: disable=W0107
from __future__ import annotations

import datetime as dt
import logging
import os
import tempfile
from abc import abstractmethod
from enum import unique
from functools import wraps
from typing import Any, Callable, Union

import geopandas as gpd
import numpy as np
import rasterio
import xarray as xr
from rasterio import crs as rcrs
from rasterio import warp
from rasterio.enums import Resampling

from eoreader import utils
from eoreader.bands import index
from eoreader.bands.alias import *
from eoreader.bands.bands import BandNames
from eoreader.env_vars import CI_EOREADER_BAND_FOLDER, DEM_PATH
from eoreader.reader import Platform, Reader
from eoreader.utils import EOREADER_NAME
from sertit import files, misc, rasters, strings
from sertit.misc import ListEnum
from sertit.rasters import XDS_TYPE
from sertit.snap import MAX_CORES

LOGGER = logging.getLogger(EOREADER_NAME)
PRODUCT_FACTORY = Reader()


def path_or_dst(method: Callable) -> Callable:
    """
    Path or dataset decorator: allows a function to ingest a path or a rasterio dataset

    ```python
    >>> # Create mock function
    >>> @path_or_dst
    >>> def fct(dst):
    >>>     read(dst)
    >>>
    >>> # Test the two ways
    >>> read1 = fct("path\\to\\raster.tif")
    >>> with rasterio.open("path\\to\\raster.tif") as dst:
    >>>     read2 = fct(dst)
    >>>
    >>> # Test
    >>> read1 == read2
    True
    ```
    Args:
        method (Callable): Function to decorate

    Returns:
        Callable: decorated function
    """

    @wraps(method)
    def path_or_dst_wrapper(
        self, path_or_ds: Union[str, rasterio.DatasetReader], *args, **kwargs
    ) -> Any:
        """
        Path or dataset wrapper
        Args:
            self: Class
            path_or_ds (Union[str, rasterio.DatasetReader]): Raster path or its dataset
            *args: args
            **kwargs: kwargs

        Returns:
            Any: regular output
        """
        if isinstance(path_or_ds, str):
            with rasterio.open(path_or_ds) as dst:
                out = method(self, dst, *args, **kwargs)
        else:
            out = method(self, path_or_ds, *args, **kwargs)
        return out

    return path_or_dst_wrapper


@unique
class SensorType(ListEnum):
    """
    Sensor type of the products, optical or SAR
    """

    OPTICAL = "Optical"
    """For optical data"""

    SAR = "SAR"
    """For SAR data"""


class Product:
    """Super class of EOReader Products"""

    def __init__(
        self, product_path: str, archive_path: str = None, output_path: str = None
    ) -> None:
        self.name = files.get_filename(product_path)
        """Product name (its filename without any extension)."""

        self.split_name = self._get_split_name()
        """Split name, to retrieve every information from its filename (dates, tile, product type...)."""

        self.archive_path = archive_path if archive_path else product_path
        """Archive path, same as the product path if not specified.
        Useful when you want to know where both the extracted and archived version of your product are stored."""

        self.path = product_path
        """Usable path to the product, either extracted or archived path, according to the satellite."""

        self.is_archived = os.path.isfile(self.path)
        """ Is the archived product is processed
        (a products is considered as archived if its products path is a directory)."""

        self.needs_extraction = True
        """Does this products needs to be extracted to be processed ? (`True` by default)."""

        # The output will be given later
        if output_path:
            self._tmp = None
            self._output = output_path
            os.makedirs(output_path, exist_ok=True)
        else:
            self._tmp = tempfile.TemporaryDirectory()
            self._output = self._tmp.name
        """Output directory of the product, to write orthorectified data for example."""

        # Get the products date and datetime
        self.date = self.get_date(as_date=True)
        """Acquisition date."""
        self.datetime = self.get_datetime(as_datetime=True)
        """Acquisition datetime."""

        self.tile_name = None
        """Tile if possible (for data that can be piled, for example S2 and Landsats)."""

        self.sensor_type = None
        """Sensor type, SAR or optical."""

        self.product_type = None
        """Product type, satellite-related field, such as L1C or L2A for Sentinel-2 data."""

        self.band_names = None
        """Band mapping between band wrapping names such as `GREEN` and band real number such as `03` for Sentinel-2."""

        self.is_reference = False
        """If the product is a reference, used for algorithms that need pre and post data, such as fire detection."""

        self.corresponding_ref = []
        """The corresponding reference products to the current one
         (if the product is not a reference but has a reference data corresponding to it).
         A list because of multiple ref in case of non-stackable products (S3, S1...)"""

        self.nodata = -9999
        """ Product nodata, set to 0 by default. Please do not touch this or all index will fail. """

        # Mask values
        self._mask_true = 1
        self._mask_false = 0

        self.platform = self._get_platform()
        """Product platform, such as Sentinel-2"""

        # Post initialization
        self._post_init()

        # Set product type, needs to be done after the post-initialization
        self._set_product_type()

        # Set the resolution, needs to be done when knowing the product type
        self.resolution = self._set_resolution()
        """
        Default resolution in meters of the current product.
        For SAR product, we use Ground Range resolution as we will automatically orthorectify the tiles.
        """

        self.condensed_name = self._get_condensed_name()
        """
        Condensed name, the filename with only useful data to keep the name unique
        (ie. `20191215T110441_S2_30TXP_L2A_122756`).
        Used to shorten names and paths.
        """

        self.sat_id = self.platform.name
        """Satellite ID, i.e. `S2` for Sentinel-2"""

        # TODO: manage self.needs_extraction

    def __del__(self):
        """Cleaning up _tmp directory"""
        if self._tmp:
            self._tmp.cleanup()

    @abstractmethod
    def _post_init(self) -> None:
        """
        Function used to post_init the products
        (setting sensor type, band names and so on)
        """
        raise NotImplementedError("This method should be implemented by a child class")

    def footprint(self) -> gpd.GeoDataFrame:
        """
        Get UTM footprint of the products (without nodata, *in french == emprise utile*)

        ```python
        >>> from eoreader.reader import Reader
        >>> path = r"S2A_MSIL1C_20200824T110631_N0209_R137_T30TTK_20200824T150432.SAFE.zip"
        >>> prod = Reader().open(path)
        >>> prod.footprint()
           index                                           geometry
        0      0  POLYGON ((199980.000 4500000.000, 199980.000 4...
        ```

        Returns:
            gpd.GeoDataFrame: Footprint as a GeoDataFrame
        """
        default_xda = self.load(self.get_default_band())
        return rasters.get_footprint(default_xda)

    @abstractmethod
    def extent(self) -> gpd.GeoDataFrame:
        """
        Get UTM extent of the tile

        ```python
        >>> from eoreader.reader import Reader
        >>> path = r"S2A_MSIL1C_20200824T110631_N0209_R137_T30TTK_20200824T150432.SAFE.zip"
        >>> prod = Reader().open(path)
        >>> prod.utm_extent()
                                                    geometry
        0  POLYGON ((309780.000 4390200.000, 309780.000 4...
        ```

        Returns:
            gpd.GeoDataFrame: Footprint in UTM
        """
        raise NotImplementedError("This method should be implemented by a child class")

    @abstractmethod
    def crs(self) -> rcrs.CRS:
        """
        Get UTM projection of the tile

        ```python
        >>> from eoreader.reader import Reader
        >>> path = r"S2A_MSIL1C_20200824T110631_N0209_R137_T30TTK_20200824T150432.SAFE.zip"
        >>> prod = Reader().open(path)
        >>> prod.utm_crs()
        CRS.from_epsg(32630)
        ```

        Returns:
            crs.CRS: CRS object
        """
        raise NotImplementedError("This method should be implemented by a child class")

    def _get_band_folder(self):
        """Manage the case of CI SNAP Bands"""

        # Manage CI SNAP band
        ci_band_folder = os.environ.get(CI_EOREADER_BAND_FOLDER)
        if ci_band_folder and os.path.isdir(ci_band_folder):
            band_folder = ci_band_folder
        else:
            band_folder = self.output

        return band_folder

    @abstractmethod
    def _set_resolution(self) -> float:
        """
        Set product default resolution (in meters)
        """
        raise NotImplementedError("This method should be implemented by a child class")

    @abstractmethod
    def _set_product_type(self) -> None:
        """
        Set product type
        """
        raise NotImplementedError("This method should be implemented by a child class")

    @classmethod
    def _get_platform(cls) -> Platform:
        class_module = cls.__module__.split(".")[-1]
        sat_id = class_module.split("_")[0].upper()
        return getattr(Platform, sat_id)

    @abstractmethod
    def _get_condensed_name(self) -> str:
        """
        Set product condensed name.

        Returns:
            str: Condensed name
        """
        raise NotImplementedError("This method should be implemented by a child class")

    def _get_split_name(self) -> list:
        """
        Get split name (erasing empty strings in it by precaution, especially for S1 and S3 data)

        Returns:
            list: Split products name
        """
        return [x for x in self.name.split("_") if x]

    @abstractmethod
    def get_datetime(self, as_datetime: bool = False) -> Union[str, dt.datetime]:
        """
        Get the product's acquisition datetime, with format `YYYYMMDDTHHMMSS` <-> `%Y%m%dT%H%M%S`

        ```python
        >>> from eoreader.reader import Reader
        >>> path = r"S2A_MSIL1C_20200824T110631_N0209_R137_T30TTK_20200824T150432.SAFE.zip"
        >>> prod = Reader().open(path)
        >>> prod.get_datetime(as_datetime=True)
        datetime.datetime(2020, 8, 24, 11, 6, 31)
        >>> prod.get_datetime(as_datetime=False)
        '20200824T110631'
        ```

        Args:
            as_datetime (bool): Return the date as a datetime.datetime. If false, returns a string.

        Returns:
             Union[str, datetime.datetime]: Its acquisition datetime
        """
        raise NotImplementedError("This method should be implemented by a child class")

    def get_date(self, as_date: bool = False) -> Union[str, dt.date]:
        """
        Get the product's acquisition date.

        ```python
        >>> from eoreader.reader import Reader
        >>> path = r"S2A_MSIL1C_20200824T110631_N0209_R137_T30TTK_20200824T150432.SAFE.zip"
        >>> prod = Reader().open(path)
        >>> prod.get_date(as_date=True)
        datetime.datetime(2020, 8, 24, 0, 0)
        >>> prod.get_date(as_date=False)
        '20200824'
        ```

        Args:
            as_date (bool): Return the date as a datetime.date. If false, returns a string.

        Returns:
            str: Its acquisition date
        """
        date = self.get_datetime().split("T")[0]

        if as_date:
            date = strings.str_to_date(date, date_format="%Y%m%d")

        return date

    @abstractmethod
    def get_default_band_path(self) -> str:
        """
        Get default band path (among the existing ones).

        Usually `GREEN` band for optical data and the first existing one between `VV` and `HH` for SAR data.

        ```python
        >>> from eoreader.reader import Reader
        >>> path = r"S2A_MSIL1C_20200824T110631_N0209_R137_T30TTK_20200824T150432.SAFE.zip"
        >>> prod = Reader().open(path)
        >>> prod.get_default_band_path()
        'zip+file://S2A_MSIL1C_20200824T110631_N0209_R137_T30TTK_20200824T150432.SAFE.zip!/S2A_MSIL1C_20200824T110631_N0209_R137_T30TTK_20200824T150432.SAFE/GRANULE/L1C_T30TTK_A027018_20200824T111345/IMG_DATA/T30TTK_20200824T110631_B03.jp2'
        ```
        Returns:
            str: Default band path
        """
        raise NotImplementedError("This method should be implemented by a child class")

    @abstractmethod
    def get_default_band(self) -> BandNames:
        """
        Get default band:
        Usually `GREEN` band for optical data and the first existing one between `VV` and `HH` for SAR data.

        ```python
        >>> from eoreader.reader import Reader
        >>> path = r"S2A_MSIL1C_20200824T110631_N0209_R137_T30TTK_20200824T150432.SAFE.zip"
        >>> prod = Reader().open(path)
        >>> prod.get_default_band()
        <OpticalBandNames.GREEN: 'GREEN'>
        ```

        Returns:
            str: Default band
        """
        raise NotImplementedError("This method should be implemented by a child class")

    def get_existing_bands(self) -> list:
        """
        Return the existing bands.

        ```python
        >>> from eoreader.reader import Reader
        >>> path = r"S2A_MSIL1C_20200824T110631_N0209_R137_T30TTK_20200824T150432.SAFE.zip"
        >>> prod = Reader().open(path)
        >>> prod.get_existing_bands()
        [<OpticalBandNames.CA: 'COASTAL_AEROSOL'>,
        <OpticalBandNames.BLUE: 'BLUE'>,
        <OpticalBandNames.GREEN: 'GREEN'>,
        <OpticalBandNames.RED: 'RED'>,
        <OpticalBandNames.VRE_1: 'VEGETATION_RED_EDGE_1'>,
        <OpticalBandNames.VRE_2: 'VEGETATION_RED_EDGE_2'>,
        <OpticalBandNames.VRE_3: 'VEGETATION_RED_EDGE_3'>,
        <OpticalBandNames.NIR: 'NIR'>,
        <OpticalBandNames.NNIR: 'NARROW_NIR'>,
        <OpticalBandNames.WV: 'WATER_VAPOUR'>,
        <OpticalBandNames.CIRRUS: 'CIRRUS'>,
        <OpticalBandNames.SWIR_1: 'SWIR_1'>,
        <OpticalBandNames.SWIR_2: 'SWIR_2'>]
        ```

        Returns:
            list: List of existing bands in the products
        """
        raise NotImplementedError("This method should be implemented by a child class")

    @abstractmethod
    def get_existing_band_paths(self) -> dict:
        """
        Return the existing band paths.

        ```python
        >>> from eoreader.reader import Reader
        >>> path = r"S2A_MSIL1C_20200824T110631_N0209_R137_T30TTK_20200824T150432.SAFE.zip"
        >>> prod = Reader().open(path)
        >>> prod.get_existing_band_paths()
        {
            <OpticalBandNames.CA: 'COASTAL_AEROSOL'>: 'zip+file://S2A_MSIL1C_20200824T110631_N0209_R137_T30TTK_20200824T150432.SAFE.zip!/S2A_MSIL1C_20200824T110631_N0209_R137_T30TTK_20200824T150432.SAFE/GRANULE/L1C_T30TTK_A027018_20200824T111345/IMG_DATA/T30TTK_20200824T110631_B01.jp2',
            ...,
            <OpticalBandNames.SWIR_2: 'SWIR_2'>: 'zip+file://S2A_MSIL1C_20200824T110631_N0209_R137_T30TTK_20200824T150432.SAFE.zip!/S2A_MSIL1C_20200824T110631_N0209_R137_T30TTK_20200824T150432.SAFE/GRANULE/L1C_T30TTK_A027018_20200824T111345/IMG_DATA/T30TTK_20200824T110631_B12.jp2'
        }
        ```

        Returns:
            dict: Dictionary containing the path of each queried band
        """
        raise NotImplementedError("This method should be implemented by a child class")

    def get_band_paths(self, band_list: list, resolution: float = None) -> dict:
        """
        Return the paths of required bands.

        ```python
        >>> from eoreader.reader import Reader
        >>> from eoreader.bands.alias import *
        >>> path = r"S2A_MSIL1C_20200824T110631_N0209_R137_T30TTK_20200824T150432.SAFE.zip"
        >>> prod = Reader().open(path)
        >>> prod.get_band_paths([GREEN, RED])
        {
            <OpticalBandNames.GREEN: 'GREEN'>: 'zip+file://S2A_MSIL1C_20200824T110631_N0209_R137_T30TTK_20200824T150432.SAFE.zip!/S2A_MSIL1C_20200824T110631_N0209_R137_T30TTK_20200824T150432.SAFE/GRANULE/L1C_T30TTK_A027018_20200824T111345/IMG_DATA/T30TTK_20200824T110631_B03.jp2',
            <OpticalBandNames.RED: 'RED'>: 'zip+file://S2A_MSIL1C_20200824T110631_N0209_R137_T30TTK_20200824T150432.SAFE.zip!/S2A_MSIL1C_20200824T110631_N0209_R137_T30TTK_20200824T150432.SAFE/GRANULE/L1C_T30TTK_A027018_20200824T111345/IMG_DATA/T30TTK_20200824T110631_B04.jp2'
        }
        ```

        Args:
            band_list (list): List of the wanted bands
            resolution (float): Band resolution

        Returns:
            dict: Dictionary containing the path of each queried band
        """
        raise NotImplementedError("This method should be implemented by a child class")

    @abstractmethod
    def read_mtd(self) -> Any:
        """
        Read metadata and outputs the metadata XML root and its namespace most of the time,
        except from L8-collection 1 data which outputs a pandas DataFrame

        ```python
        >>> from eoreader.reader import Reader
        >>> path = r"S1A_IW_GRDH_1SDV_20191215T060906_20191215T060931_030355_0378F7_3696.zip"
        >>> prod = Reader().open(path)
        >>> prod.read_mtd()
        (<Element product at 0x1832895d788>, '')
        ```

        Returns:
            Any: Metadata XML root and its namespace or pd.DataFrame
        """
        raise NotImplementedError("This method should be implemented by a child class")

    # pylint: disable=W0613
    @path_or_dst
    def _read_band(
        self,
        dataset,
        resolution: Union[tuple, list, float] = None,
        size: Union[list, tuple] = None,
    ) -> XDS_TYPE:
        """
        Read band from disk.

        .. WARNING::
            For optical data, invalid pixels are not managed here

        Args:
            dataset (Dataset): Band dataset
            resolution (Union[tuple, list, float]): Resolution of the wanted band, in dataset resolution unit (X, Y)
            size (Union[tuple, list]): Size of the array (width, height). Not used if resolution is provided.
        Returns:
            XDS_TYPE: Band xarray

        """
        raise NotImplementedError("This method should be implemented by a child class")

    @abstractmethod
    def _load_bands(
        self, band_list: list, resolution: float = None, size: Union[list, tuple] = None
    ) -> dict:
        """
        Load bands as numpy arrays with the same resolution (and same metadata).

        Args:
            band_list (list): List of the wanted bands
            resolution (int): Band resolution in meters
            size (Union[tuple, list]): Size of the array (width, height). Not used if resolution is provided.
        Returns:
            dict: Dictionary {band_name, band_xarray}
        """
        raise NotImplementedError("This method should be implemented by a child class")

    def _load_dem(
        self, band_list: list, resolution: float = None, size: Union[list, tuple] = None
    ) -> dict:
        """
        Load bands as numpy arrays with the same resolution (and same metadata).

        Args:
            band_list (list): List of the wanted bands
            resolution (int): Band resolution in meters
            size (Union[tuple, list]): Size of the array (width, height). Not used if resolution is provided.
        Returns:
            dict: Dictionary {band_name, band_xarray}
        """
        dem_path = os.environ.get(DEM_PATH, "")
        dem_bands = {}
        for band in band_list:
            assert is_dem(band)
            if band == DEM:
                path = self._warp_dem(dem_path, resolution=resolution, size=size)
            elif band == SLOPE:
                path = self._compute_slope(dem_path, resolution=resolution, size=size)
            elif band == HILLSHADE:
                path = self._compute_hillshade(
                    dem_path, resolution=resolution, size=size
                )
            else:
                raise InvalidTypeError(f"Unknown DEM band: {band}")

            dem_bands[band] = rasters.read(path, resolution=resolution, size=size)

        return dem_bands

    def load(
        self,
        bands: Union[list, BandNames, Callable],
        resolution: float = None,
        size: Union[list, tuple] = None,
    ) -> dict:
        """
        Open the bands and compute the wanted index.

        The bands will be purged of nodata and invalid pixels,
        the nodata will be set to 0 and the bands will be masked arrays in float.

        Bands that come out this function at the same time are collocated and therefore have the same shapes.
        This can be broken if you load data separately. Its is best to always load DEM data with some real bands.

        ```python
        >>> from eoreader.reader import Reader
        >>> from eoreader.bands.alias import *
        >>> path = r"S2A_MSIL1C_20200824T110631_N0209_R137_T30TTK_20200824T150432.SAFE.zip"
        >>> prod = Reader().open(path)
        >>> bands = prod.load([GREEN, NDVI], resolution=20)
        >>> bands
        '''
        {
            <function NDVI at 0x000001EFFFF5DD08>: <xarray.DataArray 'NDVI' (band: 1, y: 5490, x: 5490)>
            array([[[0.949506  , 0.92181516, 0.9279379 , ..., 1.8002278 ,
                     1.5424857 , 1.6747767 ],
                    [0.95369846, 0.91685396, 0.8957871 , ..., 1.5847116 ,
                     1.5248713 , 1.5011379 ],
                    [2.9928885 , 1.3031474 , 1.0076253 , ..., 1.5969834 ,
                     1.5590671 , 1.5018653 ],
                    ...,
                    [1.4245619 , 1.6115025 , 1.6201663 , ..., 1.2387121 ,
                     1.4025431 , 1.800678  ],
                    [1.5627214 , 1.822388  , 1.7245892 , ..., 1.1694248 ,
                     1.2573677 , 1.5767351 ],
                    [1.653781  , 1.6424649 , 1.5923225 , ..., 1.3072611 ,
                     1.2181134 , 1.2478763 ]]], dtype=float32)
            Coordinates:
              * band         (band) int32 1
              * y            (y) float64 4.5e+06 4.5e+06 4.5e+06 ... 4.39e+06 4.39e+06
              * x            (x) float64 2e+05 2e+05 2e+05 ... 3.097e+05 3.098e+05 3.098e+05
                spatial_ref  int32 0,
            <OpticalBandNames.GREEN: 'GREEN'>: <xarray.DataArray (band: 1, y: 5490, x: 5490)>
            array([[[0.0615  , 0.061625, 0.061   , ..., 0.12085 , 0.120225,
                     0.113575],
                    [0.061075, 0.06045 , 0.06025 , ..., 0.114625, 0.119625,
                     0.117625],
                    [0.06475 , 0.06145 , 0.060925, ..., 0.111475, 0.114925,
                     0.115175],
                    ...,
                    [0.1516  , 0.14195 , 0.1391  , ..., 0.159975, 0.14145 ,
                     0.127075],
                    [0.140325, 0.125975, 0.131875, ..., 0.18245 , 0.1565  ,
                     0.13015 ],
                    [0.133475, 0.1341  , 0.13345 , ..., 0.15565 , 0.170675,
                     0.16405 ]]], dtype=float32)
            Coordinates:
              * band         (band) int32 1
              * y            (y) float64 4.5e+06 4.5e+06 4.5e+06 ... 4.39e+06 4.39e+06
              * x            (x) float64 2e+05 2e+05 2e+05 ... 3.097e+05 3.098e+05 3.098e+05
                spatial_ref  int32 0
        }
        '''
        ```

        Args:
            bands (Union[list, BandNames, Callable]): Band list
            resolution (float): Resolution of the band, in meters
            size (Union[tuple, list]): Size of the array (width, height). Not used if resolution is provided.

        Returns:
            dict: {band_name, band xarray}
        """
        if not resolution and not size:
            resolution = self.resolution

        # Check if all bands are valid
        if not isinstance(bands, list):
            bands = [bands]

        band_dict = self._load(bands, resolution, size)

        # Manage the case of arrays of different size -> collocate arrays if needed
        band_dict = self._collocate_bands(band_dict)

        # Convert to xarray dataset when all the bands have the same size
        # TODO: cannot convert as we have non-string index
        # xds = xr.Dataset(band_dict)

        # Sort bands to the asked order
        # xds.reindex({"band": bands})

        return band_dict

    @abstractmethod
    def _load(
        self, bands: list, resolution: float = None, size: Union[list, tuple] = None
    ) -> dict:
        """
        Core function loading data bands

        Args:
            bands (list): Band list
            resolution (float): Resolution of the band, in meters
            size (Union[tuple, list]): Size of the array (width, height). Not used if resolution is provided.

        Returns:
            Dictionary {band_name, band_xarray}
        """
        raise NotImplementedError("This method should be implemented by a child class")

    def has_band(self, band: Union[BandNames, Callable]) -> bool:
        """
        Does this products has the specified band ?

        By band, we mean:

        - satellite band
        - index
        - DEM band
        - cloud band

        ```python
        >>> from eoreader.reader import Reader
        >>> from eoreader.bands.alias import *
        >>> path = r"S2A_MSIL1C_20200824T110631_N0209_R137_T30TTK_20200824T150432.SAFE.zip"
        >>> prod = Reader().open(path)
        >>> prod.has_band(GREEN)
        True
        >>> prod.has_band(TIR_2)
        False
        >>> prod.has_band(NDVI)
        True
        >>> prod.has_band(SHADOWS)
        False
        >>> prod.has_band(HILLSHADE)
        True
        ```

        Args:
            band (Union[obn, sbn]): Optical or SAR band

        Returns:
            bool: True if the products has the specified band
        """
        if is_dem(band):
            if self.sensor_type == SensorType.SAR and band == HILLSHADE:
                has_band = False
            else:
                has_band = True
        elif is_clouds(band):
            has_band = self._has_cloud_band(band)
        elif is_index(band):
            has_band = self._has_index(band)
        else:
            has_band = band in self.get_existing_bands()

        return has_band

    def _has_cloud_band(self, band: BandNames) -> bool:
        """
        Does this products has the specified cloud band ?

        ```python
        >>> from eoreader.reader import Reader
        >>> from eoreader.bands.alias import *
        >>> path = r"S2A_MSIL1C_20200824T110631_N0209_R137_T30TTK_20200824T150432.SAFE.zip"
        >>> prod = Reader().open(path)
        >>> prod.has_cloud_band(CLOUDS)
        True
        ```
        """
        raise NotImplementedError("This method should be implemented by a child class")

    def _has_index(self, idx: Callable) -> bool:
        """
        Cen the specified index be computed from this products ?

        ```python
        >>> from eoreader.reader import Reader
        >>> from eoreader.bands.alias import *
        >>> path = r"S2A_MSIL1C_20200824T110631_N0209_R137_T30TTK_20200824T150432.SAFE.zip"
        >>> prod = Reader().open(path)
        >>> prod.has_index(NDVI)
        True
        ```

        Args:
            idx (Callable): Index

        Returns:
            bool: True if the specified index can be computed with this products's bands
        """
        index_bands = index.get_needed_bands(idx)
        return all(np.isin(index_bands, self.get_existing_bands()))

    def __gt__(self, other: Product) -> bool:
        """
        Overload greater than for eoreader -> compare the dates:
        The greater products is the one acquired the last.

        Args:
            other (Product): Other products to be compared with this one

        Returns:
            bool: True if this products has been acquired after the other

        """
        return self.date > other.date

    def __ge__(self, other: Product) -> bool:
        """
        Overload greater than for eoreader -> compare the dates:
        The greater products is the one acquired the last.

        Args:
            other (Product): Other products to be compared with this one

        Returns:
            bool: True if this products has been acquired after or in the same time than the other

        """
        return self.date >= other.date

    def __eq__(self, other: Product) -> bool:
        """
        Overload greater than for eoreader -> compare the dates:
        The greater products is the one acquired the last.

        Args:
            other (Product): Other products to be compared with this one

        Returns:
            bool: True if this products has been acquired in the same time than the other

        """
        return self.date == other.date

    def __ne__(self, other: Product) -> bool:
        """
        Overload greater than for eoreader -> compare the dates:
        The greater products is the one acquired the last.

        Args:
            other (Product): Other products to be compared with this one

        Returns:
            bool: True if this products has been acquired not in the same time than the other

        """
        return self.date != other.date

    def __le__(self, other: Product) -> bool:
        """
        Overload greater than for eoreader -> compare the dates:
        The greater products is the one acquired the last.

        Args:
            other (Product): Other products to be compared with this one

        Returns:
            bool: True if this products has been acquired before or in the same time than the other

        """
        return self.date <= other.date

    def __lt__(self, other: Product) -> bool:
        """
        Overload greater than for eoreader -> compare the dates:
        The greater products is the one acquired the last.

        Args:
            other (Product): Other products to be compared with this one

        Returns:
            bool: True if this products has been acquired before the other

        """
        return self.date < other.date

    @property
    def output(self) -> str:
        """Output directory of the product, to write orthorectified data for example."""
        return self._output

    @output.setter
    def output(self, value: str):
        """Output directory of the product, to write orthorectified data for example."""
        self._output = value
        if not os.path.isdir(self._output):
            os.makedirs(self._output, exist_ok=True)

    def _warp_dem(
        self,
        dem_path: str = "",
        resolution: Union[float, tuple] = None,
        size: Union[list, tuple] = None,
        resampling: Resampling = Resampling.bilinear,
    ) -> str:
        """
        Get this products DEM, warped to this products footprint and CRS.

        If no DEM is giving (or non existing or non intersecting the products):

        - Using EUDEM over Europe
        - Using MERIT DEM everwhere else

        ```python
        >>> from eoreader.reader import Reader
        >>> from eoreader.bands.alias import *
        >>> path = r"S2A_MSIL1C_20200824T110631_N0209_R137_T30TTK_20200824T150432.SAFE.zip"
        >>> prod = Reader().open(path)
        >>> prod.warp_dem(resolution=20)  # In meters
        '/path/to/20200824T110631_S2_T30TTK_L1C_150432_DEM.tif'
        ```

        Args:
            dem_path (str): DEM path, using EUDEM/MERIT DEM if none
            resolution (Union[float, tuple]): Resolution in meters. If not specified, use the product resolution.
            resampling (Resampling): Resampling method
            size (Union[tuple, list]): Size of the array (width, height). Not used if resolution is provided.

        Returns:
            str: DEM path (as a VRT)
        """
        try:
            merit_dem = os.path.join(
                utils.get_db_dir(),
                "GLOBAL",
                "MERIT_Hydrologically_Adjusted_Elevations",
                "MERIT_DEM.vrt",
            )
            # eudem_path = os.path.join(utils.get_db_dir(), 'GLOBAL', "EUDEM_v2", "eudem_wgs84.tif")
        except NotADirectoryError as ex:
            LOGGER.debug("Non available default DEM: %s", ex)
            merit_dem = None

        warped_dem_path = os.path.join(
            self._get_band_folder(), f"{self.condensed_name}_DEM.tif"
        )
        if os.path.isfile(warped_dem_path):
            LOGGER.debug("Already existing DEM for %s. Skipping process.", self.name)
        else:
            LOGGER.debug("Warping DEM for %s", self.name)

            # Get products extent
            prod_extent_df = self.extent()

            # The MERIT is the default DEM as it covers almost the entire Earth
            if not dem_path:
                dem_path = merit_dem
            else:
                if not os.path.isfile(dem_path):
                    LOGGER.warning(
                        "Non existing DEM file: %s. Using default ones (EUDEM or MERIT)",
                        dem_path,
                    )
                    dem_path = merit_dem
                else:
                    dem_extent_df = rasters.get_footprint(dem_path).to_crs(
                        prod_extent_df.crs
                    )
                    if not dem_extent_df.contains(prod_extent_df)[0]:
                        LOGGER.warning(
                            "Input DEM file does not intersect %s. Using default ones (EUDEM or MERIT)",
                            self.name,
                        )
                        dem_path = merit_dem

            # Use EUDEM if the products is contained in it
            # TODO: DEBUG EUDEM FOOTPRINT
            # if dem_path == merit_dem and os.path.isfile(eudem_path):
            #     dem_extent_df = rasters.get_extent(eudem_path)
            #     if dem_extent_df.contains(prod_extent_df.to_crs(dem_extent_df.crs))[0]:
            #         dem_path = eudem_path

            # Check existence (SRTM)
            if not os.path.isfile(dem_path):
                if not merit_dem:
                    raise FileNotFoundError("Impossible to retrieve default DEM.")
                else:
                    raise FileNotFoundError(f"DEM file does not exist here: {dem_path}")

            # Reproject DEM into products CRS
            with rasterio.open(self.get_default_band_path()) as prod_dst:
                LOGGER.debug("Using DEM: %s", dem_path)
                with rasterio.open(dem_path) as dem_ds:
                    # Get adjusted transform and shape (with new resolution)
                    if size is not None and resolution is None:
                        try:

                            # Get destination transform
                            out_h = size[1]
                            out_w = size[0]

                            # Get destination transform
                            coeff_x = prod_dst.width / out_w
                            coeff_y = prod_dst.height / out_h
                            dst_tr = prod_dst.transform
                            dst_tr *= dst_tr.scale(coeff_x, coeff_y)

                        except (TypeError, KeyError):
                            raise ValueError(
                                f"Size should exist (as resolution is None)"
                                f" and castable to a list: {size}"
                            )

                    else:
                        # Refine resolution
                        if resolution is None:
                            resolution = self.resolution
                        res_x = (
                            resolution[0]
                            if isinstance(resolution, (tuple, list))
                            else resolution
                        )
                        res_y = (
                            resolution[1]
                            if isinstance(resolution, (tuple, list))
                            else resolution
                        )

                        # Get destination transform
                        dst_tr = prod_dst.transform
                        coeff_x = np.abs(res_x / dst_tr.a)
                        coeff_y = np.abs(res_y / dst_tr.e)
                        dst_tr *= dst_tr.scale(coeff_x, coeff_y)

                        # Get destination transform
                        out_w = int(np.round(prod_dst.width / coeff_x))
                        out_h = int(np.round(prod_dst.height / coeff_y))

                    # Get empty output
                    reprojected_array = np.zeros(
                        (prod_dst.count, out_h, out_w), dtype=np.float32
                    )

                    # Write reprojected DEM: here do not use utils.write()
                    out_meta = prod_dst.meta.copy()
                    out_meta["dtype"] = reprojected_array.dtype
                    out_meta["transform"] = dst_tr
                    out_meta["driver"] = "GTiff"
                    out_meta["width"] = out_w
                    out_meta["height"] = out_h
                    with rasterio.open(warped_dem_path, "w", **out_meta) as out_dst:
                        out_dst.write(reprojected_array)

                        # Reproject
                        warp.reproject(
                            source=rasterio.band(dem_ds, range(1, dem_ds.count + 1)),
                            destination=rasterio.band(
                                out_dst, range(1, out_dst.count + 1)
                            ),
                            resampling=resampling,
                            num_threads=MAX_CORES,
                        )

        return warped_dem_path

    @abstractmethod
    def _compute_hillshade(
        self,
        dem_path: str = "",
        resolution: Union[float, tuple] = None,
        size: Union[list, tuple] = None,
        resampling: Resampling = Resampling.bilinear,
    ) -> str:
        """
        Compute Hillshade mask

        Args:
            dem_path (str): DEM path, using EUDEM/MERIT DEM if none
            resolution (Union[float, tuple]): Resolution in meters. If not specified, use the product resolution.
            size (Union[tuple, list]): Size of the array (width, height). Not used if resolution is provided.
            resampling (Resampling): Resampling method

        Returns:
            str: Hillshade mask path

        """
        raise NotImplementedError("This method should be implemented by a child class")

    def _compute_slope(
        self,
        dem_path: str = "",
        resolution: Union[float, tuple] = None,
        size: Union[list, tuple] = None,
        resampling: Resampling = Resampling.bilinear,
    ) -> str:
        """
        Compute slope mask

        Args:
            dem_path (str): DEM path, using EUDEM/MERIT DEM if none
            resolution (Union[float, tuple]): Resolution in meters. If not specified, use the product resolution.
            size (Union[tuple, list]): Size of the array (width, height). Not used if resolution is provided.
            resampling (Resampling): Resampling method

        Returns:
            str: Slope mask path

        """
        # Warp DEM
        warped_dem_path = self._warp_dem(dem_path, resolution, size, resampling)

        # Get slope path
        slope_dem = os.path.join(self.output, f"{self.condensed_name}_SLOPE.tif")
        if os.path.isfile(slope_dem):
            LOGGER.debug(
                "Already existing slope DEM for %s. Skipping process.", self.name
            )
        else:
            LOGGER.debug("Computing slope for %s", self.name)
            cmd_slope = [
                "gdaldem",
                "--config",
                "NUM_THREADS",
                MAX_CORES,
                "slope",
                "-compute_edges",
                strings.to_cmd_string(warped_dem_path),
                strings.to_cmd_string(slope_dem),
                "-p",
            ]

            # Run command
            misc.run_cli(cmd_slope)

        return slope_dem

    @staticmethod
    def _collocate_bands(bands: dict, master_xds: XDS_TYPE = None) -> dict:
        """
        Collocate all bands from a dict if needed (if a raster shape is different)

        Args:
            bands (dict): Dict of bands to collocate if needed

        Returns:
            dict: Collocated bands
        """
        for band_id, band in bands.items():
            if master_xds is None:
                master_xds = band  # Master array is the first one in this case

            if band.shape != master_xds.shape:
                bands[band_id] = rasters.collocate(
                    master_xds=master_xds, slave_xds=band
                )

            bands[band_id] = bands[band_id].assign_coords(
                {
                    "x": master_xds.x,
                    "y": master_xds.y,
                }
            )  # Bug for now, tiny difference in coords

        return bands

    # pylint: disable=R0913
    # Too many arguments (6/5)
    def stack(
        self,
        bands: list,
        resolution: float = None,
        stack_path: str = None,
        save_as_int: bool = False,
    ) -> xr.DataArray:
        """
        Stack bands and index of a products.

        ```python
        >>> from eoreader.reader import Reader
        >>> from eoreader.bands.alias import *
        >>> path = r"S2A_MSIL1C_20200824T110631_N0209_R137_T30TTK_20200824T150432.SAFE.zip"
        >>> prod = Reader().open(path)
        >>> stack = prod.stack([NDVI, MNDWI, GREEN], resolution=20)  # In meters
        >>> stack
        '''
        <xarray.DataArray 'NDVI_MNDWI_GREEN' (z: 3, y: 5490, x: 5490)>
        array([[[ 0.949506  ,  0.92181516,  0.9279379 , ...,  1.8002278 ,
                  1.5424857 ,  1.6747767 ],
                [ 0.95369846,  0.91685396,  0.8957871 , ...,  1.5847116 ,
                  1.5248713 ,  1.5011379 ],
                [ 2.9928885 ,  1.3031474 ,  1.0076253 , ...,  1.5969834 ,
                  1.5590671 ,  1.5018653 ],
                ...,
                [ 1.4245619 ,  1.6115025 ,  1.6201663 , ...,  1.2387121 ,
                  1.4025431 ,  1.800678  ],
                [ 1.5627214 ,  1.822388  ,  1.7245892 , ...,  1.1694248 ,
                  1.2573677 ,  1.5767351 ],
                [ 1.653781  ,  1.6424649 ,  1.5923225 , ...,  1.3072611 ,
                  1.2181134 ,  1.2478763 ]],
               [[ 0.27066118,  0.23466069,  0.18792598, ..., -0.4611526 ,
                 -0.49751845, -0.4865216 ],
                [ 0.22425456,  0.28004232,  0.27851456, ..., -0.5032771 ,
                 -0.501796  , -0.502669  ],
                [-0.07466951,  0.06360884,  0.1207174 , ..., -0.50617427,
                 -0.50219285, -0.5034222 ],
                [-0.47076276, -0.4705828 , -0.4747971 , ..., -0.32138503,
                 -0.36619243, -0.37428448],
                [-0.4826967 , -0.5032287 , -0.48544118, ..., -0.278925  ,
                 -0.31404778, -0.36052078],
                [-0.488381  , -0.48253912, -0.4697526 , ..., -0.38105175,
                 -0.30813277, -0.27739233]],
               [[ 0.0615    ,  0.061625  ,  0.061     , ...,  0.12085   ,
                  0.120225  ,  0.113575  ],
                [ 0.061075  ,  0.06045   ,  0.06025   , ...,  0.114625  ,
                  0.119625  ,  0.117625  ],
                [ 0.06475   ,  0.06145   ,  0.060925  , ...,  0.111475  ,
                  0.114925  ,  0.115175  ],
                ...,
                [ 0.1516    ,  0.14195   ,  0.1391    , ...,  0.159975  ,
                  0.14145   ,  0.127075  ],
                [ 0.140325  ,  0.125975  ,  0.131875  , ...,  0.18245   ,
                  0.1565    ,  0.13015   ],
                [ 0.133475  ,  0.1341    ,  0.13345   , ...,  0.15565   ,
                  0.170675  ,  0.16405   ]]], dtype=float32)
        Coordinates:
          * y            (y) float64 4.5e+06 4.5e+06 4.5e+06 ... 4.39e+06 4.39e+06
          * x            (x) float64 2e+05 2e+05 2e+05 ... 3.097e+05 3.098e+05 3.098e+05
            spatial_ref  int32 0
          * z            (z) MultiIndex
          - variable     (z) object 'NDVI' 'MNDWI' 'GREEN'
          - band         (z) int64 1 1 1
        Attributes:
            long_name:  ['NDVI', 'MNDWI', 'GREEN']
        '''
        ```

        Args:
            bands (list): Bands and index combination
            resolution (float): Stack resolution. . If not specified, use the product resolution.
            stack_path (str): Stack path
            save_as_int (bool): Save stack as integers (uint16 and therefore multiply the values by 10.000)

        Returns:
            xr.DataArray: Stack as a DataArray
        """
        if not resolution:
            resolution = self.resolution

        # Create the analysis stack
        band_dict = self.load(bands, resolution)

        # Convert into dataset with str as names
        xds = xr.Dataset(
            data_vars={to_str(key)[0]: val for key, val in band_dict.items()},
            coords=band_dict[bands[0]].coords,
        )

        # Force nodata
        stack = xds.to_stacked_array(new_dim="z", sample_dims=("x", "y"))
        stack = stack.transpose("z", "y", "x")

        # Save as integer
        if save_as_int:
            dtype = np.uint16
            stack = (stack * 10000).astype(dtype)
        else:
            dtype = np.float32
            stack = stack.astype(dtype)

        # Some updates
        stack = rasters.set_nodata(stack, self.nodata)
        band_list = to_str(list(band_dict.keys()))
        stack.attrs["long_name"] = band_list
        stack = stack.rename("_".join(band_list))

        # Write on disk
        if stack_path:
            rasters.write(stack, stack_path, dtype=dtype)

        # Close datasets
        for val in band_dict.values():
            val.close()

        return stack

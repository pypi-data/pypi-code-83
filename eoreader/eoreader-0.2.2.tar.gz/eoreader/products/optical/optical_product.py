""" Super class for optical products """

import logging
import os
from abc import abstractmethod
from typing import Union

import geopandas as gpd
import numpy as np
import rasterio
import xarray as xr
from rasterio import crs as rcrs
from rasterio.enums import Resampling

from eoreader.bands import index
from eoreader.bands.alias import (
    is_clouds,
    is_dem,
    is_index,
    is_optical_band,
    is_sar_band,
)
from eoreader.bands.bands import BandNames
from eoreader.bands.bands import OpticalBandNames as obn
from eoreader.bands.bands import OpticalBands
from eoreader.exceptions import InvalidBandError, InvalidIndexError
from eoreader.products.product import Product, SensorType
from eoreader.utils import EOREADER_NAME
from sertit import misc, rasters, strings
from sertit.rasters import XDS_TYPE
from sertit.snap import MAX_CORES

LOGGER = logging.getLogger(EOREADER_NAME)


class OpticalProduct(Product):
    """Super class for optical products"""

    def _post_init(self) -> None:
        """
        Function used to post_init the products
        (setting sensor type, band names and so on)
        """
        self.band_names = OpticalBands()
        self._set_product_type()
        self.sensor_type = SensorType.OPTICAL

    def get_default_band(self) -> BandNames:
        """
        Get default band: `GREEN` for optical data as every optical satellite has a GREEN band.

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
        return obn.GREEN

    def get_default_band_path(self) -> str:
        """
        Get default band (`GREEN` for optical data) path.

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
        default_band = self.get_default_band()
        return self.get_band_paths([default_band])[default_band]

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
            rasterio.crs.CRS: CRS object
        """
        band_path = self.get_default_band_path()
        with rasterio.open(band_path) as dst:
            utm = dst.crs

        return utm

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
        # Get extent
        return rasters.get_extent(self.get_default_band_path())

    def get_existing_bands(self) -> list:
        """
        Return the existing band paths.

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
        return [name for name, nb in self.band_names.items() if nb]

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
        existing_bands = self.get_existing_bands()
        return self.get_band_paths(band_list=existing_bands)

    def _open_bands(
        self,
        band_paths: dict,
        resolution: float = None,
        size: Union[list, tuple] = None,
    ) -> dict:
        """
        Open bands from disk.

        Args:
            band_paths (dict): Band dict: {band_enum: band_path}
            resolution (float): Band resolution in meters
            size (Union[tuple, list]): Size of the array (width, height). Not used if resolution is provided.

        Returns:
            dict: Dictionary {band_name, band_xarray}

        """
        # Open bands and get array (resampled if needed)
        band_arrays = {}
        for band_name, band_path in band_paths.items():
            # Read band
            band_arrays[band_name] = self._read_band(
                band_path, resolution=resolution, size=size
            )
            band_arrays[band_name] = self._manage_invalid_pixels(
                band_arrays[band_name], band_name, resolution=resolution, size=size
            )

        return band_arrays

    # pylint: disable=R0913
    # R0913: Too many arguments (6/5) (too-many-arguments)
    @abstractmethod
    def _manage_invalid_pixels(
        self,
        band_arr: XDS_TYPE,
        band: obn,
        resolution: float = None,
        size: Union[list, tuple] = None,
    ) -> XDS_TYPE:
        """
        Manage invalid pixels (Nodata, saturated, defective...)

        Args:
            band_arr (XDS_TYPE): Band array
            band (obn): Band name as an OpticalBandNames
            resolution (float): Band resolution in meters
            size (Union[tuple, list]): Size of the array (width, height). Not used if resolution is provided.

        Returns:
            XDS_TYPE: Cleaned band array
        """
        raise NotImplementedError("This method should be implemented by a child class")

    def _set_nodata_mask(self, band_arr: XDS_TYPE, mask: np.ndarray) -> XDS_TYPE:
        """
        Create the correct xarray with well positioned nodata

        Args:
            band_arr (XDS_TYPE): Band array
            mask (np.ndarray): Mask array

        Returns:
            (XDS_TYPE): Corrected band array
        """
        # Binary mask
        if mask.dtype != np.uint8:
            mask = mask.astype(np.uint8)

        if len(mask.shape) < len(band_arr.shape):
            mask = np.expand_dims(mask, axis=0)

        # Set masked values to nodata
        band_arr = xr.where(mask, self.nodata, band_arr)

        return rasters.set_nodata(band_arr, self.nodata)

    def _load(
        self, bands: list, resolution: float = None, size: Union[list, tuple] = None
    ) -> dict:
        """
        Core function loading optical data bands

        Args:
            bands (list): Band list
            resolution (float): Resolution of the band, in meters
            size (Union[tuple, list]): Size of the array (width, height). Not used if resolution is provided.

        Returns:
            Dictionary {band_name, band_xarray}
        """
        band_list = []
        index_list = []
        dem_list = []
        clouds_list = []

        # Check if everything is valid
        for idx_or_band in bands:
            if is_index(idx_or_band):
                if self._has_index(idx_or_band):
                    index_list.append(idx_or_band)
                else:
                    raise InvalidIndexError(
                        f"{idx_or_band} cannot be computed from {self.condensed_name}."
                    )
            elif is_sar_band(idx_or_band):
                raise TypeError(
                    f"You should ask for Optical bands as {self.name} is an optical product."
                )
            elif is_optical_band(idx_or_band):
                if self.has_band(idx_or_band):
                    band_list.append(idx_or_band)
                else:
                    raise InvalidBandError(
                        f"{idx_or_band} cannot be retrieved from {self.condensed_name}."
                    )
            elif is_dem(idx_or_band):
                dem_list.append(idx_or_band)
            elif is_clouds(idx_or_band):
                clouds_list.append(idx_or_band)

        # Get all bands to be open
        bands_to_load = band_list.copy()
        for idx in index_list:
            bands_to_load += index.NEEDED_BANDS[idx]

        # Load band arrays (only keep unique bands: open them only one time !)
        bands = self._load_bands(
            list(set(bands_to_load)), resolution=resolution, size=size
        )

        # Compute index (they conserve the nodata)
        bands_dict = {idx: idx(bands) for idx in index_list}

        # Add bands
        bands_dict.update({band: bands[band] for band in band_list})

        # Add DEM
        bands_dict.update(self._load_dem(dem_list, resolution=resolution, size=size))

        # Add Clouds
        bands_dict.update(
            self._load_clouds(clouds_list, resolution=resolution, size=size)
        )

        return bands_dict

    @abstractmethod
    def get_mean_sun_angles(self) -> (float, float):
        """
        Get Mean Sun angles (Azimuth and Zenith angles)

        ```python
        >>> from eoreader.reader import Reader
        >>> path = r"S2A_MSIL1C_20200824T110631_N0209_R137_T30TTK_20200824T150432.SAFE.zip"
        >>> prod = Reader().open(path)
        >>> prod.get_mean_sun_angles()
        (149.148155074489, 32.6627897525474)
        ```

        Returns:
            (float, float): Mean Azimuth and Zenith angle
        """
        raise NotImplementedError("This method should be implemented by a child class")

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
        # Warp DEM
        warped_dem_path = self._warp_dem(dem_path, resolution, size, resampling)

        # Get Hillshade path
        hillshade_dem = os.path.join(
            self.output, f"{self.condensed_name}_HILLSHADE.tif"
        )
        if os.path.isfile(hillshade_dem):
            LOGGER.debug(
                "Already existing hillshade DEM for %s. Skipping process.", self.name
            )
        else:
            LOGGER.debug("Computing hillshade DEM for %s", self.name)

            # Get angles
            mean_azimuth_angle, mean_zenith_angle = self.get_mean_sun_angles()
            zenith = 90.0 - mean_zenith_angle
            azimuth = mean_azimuth_angle

            # Run cmd
            cmd_hillshade = [
                "gdaldem",
                "--config",
                "NUM_THREADS",
                MAX_CORES,
                "hillshade",
                strings.to_cmd_string(warped_dem_path),
                "-compute_edges",
                "-z",
                "1",
                "-az",
                azimuth,
                "-alt",
                zenith,
                "-of",
                "GTiff",
                strings.to_cmd_string(hillshade_dem),
            ]
            # Run command
            misc.run_cli(cmd_hillshade)

        return hillshade_dem

    def _load_clouds(
        self, bands: list, resolution: float = None, size: Union[list, tuple] = None
    ) -> dict:
        """
        Load cloud files as numpy arrays with the same resolution (and same metadata).

        Args:
            bands (list): List of the wanted bands
            resolution (int): Band resolution in meters
            size (Union[tuple, list]): Size of the array (width, height). Not used if resolution is provided.
        Returns:
            dict: Dictionary {band_name, band_xarray}
        """
        raise NotImplementedError("This method should be implemented by a child class")

    def _create_mask(
        self, xds: XDS_TYPE, cond: np.ndarray, nodata: np.ndarray
    ) -> XDS_TYPE:
        """
        Create a mask from a conditional array and a nodata mask.

        Args:
            xds (XDS_TYPE): xarray to retrieve attributes
            cond (np.ndarray): Conditional array
            nodata (np.ndarray): Nodata mask

        Returns:
            XDS_TYPE: Mask as xarray
        """
        mask = xds.copy(data=np.where(cond, self._mask_true, self._mask_false))
        mask = xr.where(nodata, self.nodata, mask)
        mask = rasters.set_nodata(mask, self.nodata)

        return mask

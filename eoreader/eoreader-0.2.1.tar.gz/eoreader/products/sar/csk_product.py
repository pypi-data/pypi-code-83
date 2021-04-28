"""
COSMO-SkyMed products.
More info [here](https://earth.esa.int/documents/10174/465595/COSMO-SkyMed-Mission-Products-Description).
"""
import datetime
import glob
import logging
import os
import warnings
from enum import unique
from typing import Union

import geopandas as gpd
import numpy as np
import rasterio
from lxml import etree
from shapely.geometry import Polygon

from eoreader.exceptions import InvalidProductError, InvalidTypeError
from eoreader.products.sar.sar_product import SarProduct
from eoreader.utils import DATETIME_FMT, EOREADER_NAME
from sertit import files, strings, vectors
from sertit.misc import ListEnum

LOGGER = logging.getLogger(EOREADER_NAME)

# Disable georef warnings here as the SAR products are not georeferenced
warnings.filterwarnings("ignore", category=rasterio.errors.NotGeoreferencedWarning)


@unique
class CskProductType(ListEnum):
    """
    COSMO-SkyMed products types.
    Take a look [here](https://earth.esa.int/documents/10174/465595/COSMO-SkyMed-Mission-Products-Description).
    """

    RAW = "RAW"
    """Level 0"""

    SCS = "SCS"
    """Level 1A, Single-look Complex Slant, (un)balanced"""

    DGM = "DGM"
    """Level 1B, Detected Ground Multi-look"""

    GEC = "GEC"
    """Level 1C, Geocoded Ellipsoid Corrected"""

    GTC = "GTC"
    """Level 1D, Geocoded Terrain Corrected"""


@unique
class CskSensorMode(ListEnum):
    """
    COSMO-SkyMed sensor mode.
    Take a look [here](https://earth.esa.int/documents/10174/465595/COSMO-SkyMed-Mission-Products-Description)
    """

    HI = "HI"
    """Himage"""

    PP = "PP"
    """PingPong"""

    WR = "WR"
    """Wide Region"""

    HR = "HR"
    """Huge Region"""

    S2 = "S2"
    """Spotlight 2"""


@unique
class CskPolarization(ListEnum):
    """
    COSMO-SkyMed polarizations used during the acquisition.
    Take a look [here](https://earth.esa.int/documents/10174/465595/COSMO-SkyMed-Mission-Products-Description).
    """

    HH = "HH"
    """Horizontal Tx/Horizontal Rx for Himage, ScanSAR and Spotlight modes"""

    VV = "VV"
    """Vertical Tx/Vertical Rx for Himage, ScanSAR and Spotlight modes"""

    HV = "HV"
    """Horizontal Tx/Vertical Rx for Himage, ScanSAR"""

    VH = "VH"
    """Vertical Tx/Horizontal Rx for Himage, ScanSAR"""

    CO = "CO"
    """Co-polar acquisition (HH/VV) for PingPong mode"""

    CH = "CH"
    """Cross polar acquisition (HH/HV) with Horizontal Tx polarization for PingPong mode"""

    CV = "CV"
    """Cross polar acquisition (VV/VH) with Vertical Tx polarization for PingPong mode"""


class CskProduct(SarProduct):
    """
    Class for COSMO-SkyMed Products
    ```python
    >>> from eoreader.reader import Reader
    >>> # CSK products could have any folder but needs to have a .h5 file correctly formatted
    >>> # ie. "CSKS1_SCS_B_HI_15_HH_RA_SF_20201028224625_20201028224632.h5"
    >>> path = r"1011117-766193"
    >>> prod = Reader().open(path)
    ```
    """

    def __init__(
        self, product_path: str, archive_path: str = None, output_path=None
    ) -> None:
        try:
            self._img_path = glob.glob(os.path.join(product_path, "*.h5"))[0]
        except IndexError as ex:
            raise InvalidProductError(
                f"Image file (*.h5) not found in {product_path}"
            ) from ex
        self._real_name = files.get_filename(self._img_path)

        # Initialization from the super class
        super().__init__(product_path, archive_path, output_path)

    def _set_resolution(self) -> float:
        """
        Set product default resolution (in meters)
        """
        def_res = None

        # Read metadata
        try:
            root, _ = self.read_mtd()

            for element in root:
                if element.tag == "ProductCharacteristics":
                    def_res = float(element.findtext("GroundRangeGeometricResolution"))
                    break
        except (InvalidProductError, AttributeError):
            pass

        # If we cannot read it in MTD, initiate survival mode
        if not def_res:
            if self.sensor_mode == CskSensorMode.S2:
                def_res = 1.0
            elif self.sensor_mode == CskSensorMode.HI:
                def_res = 5.0
            elif self.sensor_mode == CskSensorMode.PP:
                def_res = 20.0
            elif self.sensor_mode == CskSensorMode.WR:
                def_res = 30.0
            elif self.sensor_mode == CskSensorMode.HR:
                def_res = 100.0
            else:
                raise InvalidTypeError(f"Unknown sensor mode {self.sensor_mode}")

        return def_res

    def _post_init(self) -> None:
        """
        Function used to post_init the products
        (setting product-type, band names and so on)
        """

        # Private attributes
        self._raw_band_regex = "*_{}_*.h5"
        self._band_folder = self.path
        self._snap_path = self._img_path

        # Post init done by the super class
        super()._post_init()

    def wgs84_extent(self) -> gpd.GeoDataFrame:
        """
        Get the WGS84 extent of the file before any reprojection.
        This is useful when the SAR pre-process has not been done yet.

        ```python
        >>> from eoreader.reader import Reader
        >>> path = r"1011117-766193"
        >>> prod = Reader().open(path)
        >>> prod.wgs84_extent()
                                                    geometry
        0  POLYGON ((108.09797 15.61011, 108.48224 15.678...
        ```

        Returns:
            gpd.GeoDataFrame: WGS84 extent as a gpd.GeoDataFrame

        """
        # Open metadata file
        try:
            mtd_file = glob.glob(os.path.join(self.path, "*.h5.xml"))[0]
        except IndexError as ex:
            raise InvalidProductError(
                f"Metadata file ({self._real_name}.h5.xml) not found in {self.path}"
            ) from ex

        # Open and parse XML
        # pylint: disable=I1101
        xml_tree = etree.parse(mtd_file)
        root = xml_tree.getroot()

        # Open zenith and azimuth angle
        def from_str_to_arr(geo_coord: str):
            return np.array(strings.str_to_list(geo_coord), dtype=float)[:2][::-1]

        bl_corner = br_corner = tr_corner = tl_corner = None
        for element in root:
            if element.tag == "ProductDefinitionData":
                bl_corner = from_str_to_arr(element.findtext("GeoCoordBottomLeft"))
                br_corner = from_str_to_arr(element.findtext("GeoCoordBottomRight"))
                tl_corner = from_str_to_arr(element.findtext("GeoCoordTopLeft"))
                tr_corner = from_str_to_arr(element.findtext("GeoCoordTopRight"))
                break

        if bl_corner is None:
            raise InvalidProductError("Invalid XML: missing extent.")

        extent_wgs84 = gpd.GeoDataFrame(
            geometry=[Polygon([tl_corner, tr_corner, br_corner, bl_corner])],
            crs=vectors.WGS84,
        )

        return extent_wgs84

    def _set_product_type(self) -> None:
        """Get products type"""
        self._get_sar_product_type(
            prod_type_pos=1,
            gdrg_types=CskProductType.DGM,
            cplx_types=CskProductType.SCS,
        )

    def _set_sensor_mode(self) -> None:
        """
        Get products type from S2 products name (could check the metadata too)
        """
        sensor_mode_name = self.split_name[3]

        # Get sensor mode
        for sens_mode in CskSensorMode:
            if sens_mode.value in sensor_mode_name:
                self.sensor_mode = sens_mode

        if not self.sensor_mode:
            raise InvalidProductError(
                f"Invalid {self.platform.value} name: {self._real_name}"
            )

    def get_datetime(self, as_datetime: bool = False) -> Union[str, datetime.datetime]:
        """
        Get the product's acquisition datetime, with format `YYYYMMDDTHHMMSS` <-> `%Y%m%dT%H%M%S`

        ```python
        >>> from eoreader.reader import Reader
        >>> path = r"1011117-766193"
        >>> prod = Reader().open(path)
        >>> prod.get_datetime(as_datetime=True)
        datetime.datetime(2020, 10, 28, 22, 46, 25)
        >>> prod.get_datetime(as_datetime=False)
        '20201028T224625'
        ```

        Args:
            as_datetime (bool): Return the date as a datetime.datetime. If false, returns a string.

        Returns:
             Union[str, datetime.datetime]: Its acquisition datetime
        """
        # 20201008224018
        date = datetime.datetime.strptime(self.split_name[8], "%Y%m%d%H%M%S")

        if not as_datetime:
            date = date.strftime(DATETIME_FMT)

        return date

    def _get_split_name(self) -> list:
        """
        Get split name (erasing empty strings in it by precaution, especially for S1 data)

        Returns:
            list: Split products name
        """
        # Use the real name
        return [x for x in self._real_name.split("_") if x]

    def read_mtd(self) -> (etree._Element, str):
        """
        Read metadata and outputs the metadata XML root and its namespace

        ```python
        >>> from eoreader.reader import Reader
        >>> path = r"1001513-735093"
        >>> prod = Reader().open(path)
        >>> prod.read_mtd()
        (<Element DeliveryNote at 0x2454ad4ee88>, '')
        ```

        Returns:
            (etree._Element, str): Metadata XML root and its namespace
        """
        mtd_name = f"DFDN_{self._real_name}.h5.xml"
        try:
            mtd_file = glob.glob(os.path.join(self.path, mtd_name))[0]

            # pylint: disable=I1101:
            # Module 'lxml.etree' has no 'parse' member, but source is unavailable.
            xml_tree = etree.parse(mtd_file)
            root = xml_tree.getroot()
        except IndexError as ex:
            raise InvalidProductError(
                f"Metadata file ({mtd_name}) not found in {self.path}"
            ) from ex

        # Get namespace
        namespace = ""  # No namespace here

        return root, namespace

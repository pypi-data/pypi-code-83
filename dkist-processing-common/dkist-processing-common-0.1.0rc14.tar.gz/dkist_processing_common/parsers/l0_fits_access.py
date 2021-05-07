"""
By-frame header keywords that are not instrument specific
"""
from typing import Optional
from typing import Union

from astropy.io import fits

from dkist_processing_common.models.fits_access import FitsAccessBase


class L0FitsAccess(FitsAccessBase):
    def __init__(
        self,
        hdu: Union[fits.ImageHDU, fits.PrimaryHDU, fits.CompImageHDU],
        name: Optional[str] = None,
    ):
        super().__init__(hdu=hdu, name=name)

        self.elevation: float = self.header["TELEVATN"]
        self.azimuth: float = self.header["TAZIMUTH"]
        self.table_angle: float = self.header["TTBLANGL"]
        self.gos_polarizer_status: str = self.header["PAC__004"]
        self.gos_polarizer_angle: float = self.header["PAC__005"]
        self.gos_retarder_status: str = self.header["PAC__006"]
        self.gos_retarder_angle: float = self.header["PAC__007"]
        self.gos_level0_status: str = self.header["PAC__008"]
        self.time_obs: str = self.header["DATE-OBS"]
        self.ip_task_type: str = self.header["DKIST004"]
        self.ip_id: str = self.header["ID___004"]
        self.instrument: str = self.header["INSTRUME"]

import logging
import typing as t

from pydicom import values
from pydicom.datadict import keyword_for_tag, tag_for_keyword
from pydicom.dataelem import RawDataElement

log = logging.getLogger(__name__)


def handle_incorrect_unit(
    raw_elem: RawDataElement,
    data_element_callback: t.Callable[..., RawDataElement] = None,
    **kwargs: t.Dict
) -> RawDataElement:  # pylint: disable=invalid-name
    if data_element_callback and callable(data_element_callback):
        raw_elem = data_element_callback(raw_elem, **kwargs)
    # Check for incorrect unit on MagneticFieldStrength
    encoding = (kwargs.get("encoding", ["iso8859"]) or ["iso8859"])[0]
    if raw_elem.tag.real == tag_for_keyword("MagneticFieldStrength"):
        try:
            mfs = values.convert_value("DS", raw_elem, encoding)
            mfs = float(mfs)
        except:  # pragma: no cover
            log.error("Uncaught exception, not attempting to change value.", exc_info)
            return raw_elem
        if mfs:
            if mfs > 30:
                mfs /= 1000
                # DS "decimal string" VR, cast to string.
                raw_elem = raw_elem._replace(value=bytes(str(mfs).encode(encoding)))
    return raw_elem

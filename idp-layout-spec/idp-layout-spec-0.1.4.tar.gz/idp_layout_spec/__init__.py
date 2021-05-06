__version__ = "0.1.0"

import logging
import sys

from cached_property import cached_property
from pydantic import BaseModel as PydanticBaseModel

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter("%(name)s - %(levelname)s - %(message)s"))
logger.addHandler(handler)

class BaseModel(PydanticBaseModel):
    class Config:
        arbitrary_types_allowed = True
        keep_untouched = (cached_property,)



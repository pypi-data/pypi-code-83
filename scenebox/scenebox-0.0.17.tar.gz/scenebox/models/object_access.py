#  Copyright (c) 2020 Caliber Data Labs.
#  All rights reserved.
#
from typing import Dict, Optional

from ..tools import misc


class ObjectAccessError(Exception):
    pass


class ObjectAccessMedium:
    ASSET_MANAGER = "asset-manager"
    URL = "url"

# examples
# {
#   "medium": "url", #required
#   "id": "laksjdlkawsd" #required
#   "url": "http....", #required
#   "filename": "abc.png" #optional
# }
#
# {
#   "medium": "asset-manager", #required
#   "id": "laksjdlkawsd" #required
#   "filename": "abc.png" #optional
# }
#


class ObjectAccess(object):
    def __init__(self,
                 medium: str,
                 id: Optional[str] = None,
                 filename: Optional[str] = None,
                 url: Optional[str] = None):
        if medium == ObjectAccessMedium.URL:
            if not url:
                raise ObjectAccessError("url should be provided")
        elif medium == ObjectAccessMedium.ASSET_MANAGER:
            if not id:
                raise ObjectAccessError("id should be provided")
            if url:
                raise ObjectAccessError("url is irrelevant for asset-manager")
        else:
            raise ObjectAccessError("invalid medium {}".format(medium))

        self.medium = medium  # required
        self.id = id or misc.get_guid()  # required
        self.url = url  # optional
        self.filename = filename  # optional

    def to_dic(self) -> dict:
        object_access_dict = {
            "medium": self.medium,
            "id": self.id
        }

        if self.filename:
            object_access_dict["filename"] = self.filename

        if self.url:
            object_access_dict["url"] = self.url

        return object_access_dict

    @classmethod
    def from_dict(cls, data: Dict):
        fields = {
            "id",
            "filename",
            "medium",
            "url"
        }
        return cls(**{field: data.get(field) for field in fields})

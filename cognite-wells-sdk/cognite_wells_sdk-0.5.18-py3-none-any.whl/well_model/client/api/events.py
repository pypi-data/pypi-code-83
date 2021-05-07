import logging
from typing import List, Optional

from requests import Response

from cognite.well_model.client._api_client import APIClient
from cognite.well_model.client.api.api_base import BaseAPI
from cognite.well_model.client.models.resource_list import NPTList
from cognite.well_model.client.utils.multi_request import cursor_multi_request
from cognite.well_model.models import NPT, DoubleRange, LengthRange, NPTFilter, NPTItems

logger = logging.getLogger("WellsAPI")


class EventsAPI(BaseAPI):
    def __init__(self, wells_client: APIClient):
        super().__init__(wells_client)

    def list_npt_events(
        self,
        md: Optional[LengthRange] = None,
        duration: Optional[DoubleRange] = None,
        npt_code: Optional[str] = None,
        npt_code_detail: Optional[str] = None,
        limit: Optional[int] = 100,
    ) -> NPTList:
        def request(cursor):
            npt_filter = NPTFilter(
                measured_depth=md, duration=duration, npt_code=npt_code, npt_code_detail=npt_code_detail
            )

            path: str = self._get_path("/events/list")
            response: Response = self.wells_client.post(
                url_path=path, json=npt_filter.json(), params={"cursor": cursor}
            )
            well_items_data: NPTItems = NPTItems.parse_raw(response.text)
            return well_items_data

        items = cursor_multi_request(
            get_cursor=self._get_cursor, get_items=self._get_items, limit=limit, request=request
        )
        return NPTList(items)

    def list_nds_events(self):
        raise NotImplementedError

    @staticmethod
    def _get_items(npt_items: NPTItems) -> List[NPT]:
        items: List[NPT] = npt_items.items  # For mypy
        return items

    @staticmethod
    def _get_cursor(npt_items: NPTItems) -> Optional[str]:
        next_cursor: Optional[str] = npt_items.next_cursor  # For mypy
        return next_cursor

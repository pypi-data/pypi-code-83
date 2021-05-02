# flake8: noqa E501
from asyncio import get_event_loop
from typing import TYPE_CHECKING, Awaitable

from cowin_api import models as m

if TYPE_CHECKING:
    from cowin_api.api_client import ApiClient


class _AppointmentAvailabilityAPIsApi:
    def __init__(self, api_client: "ApiClient"):
        self.api_client = api_client

    def _build_for_public_calendar_by_district(
        self, district_id: str, date: str, accept_language: str = None
    ) -> Awaitable[m.Any]:
        """
        API to get planned vaccination sessions for 7 days from a specific date in a given district.
        """
        query_params = {"district_id": str(district_id), "date": str(date)}

        headers = {}
        if accept_language is not None:
            headers["Accept-Language"] = str(accept_language)

        return self.api_client.request(
            type_=m.Any,
            method="GET",
            url="/v2/appointment/sessions/public/calendarByDistrict",
            params=query_params,
            headers=headers,
        )

    def _build_for_public_calendar_by_pin(
        self, pincode: str, date: str, accept_language: str = None
    ) -> Awaitable[m.Any]:
        """
        API to get planned vaccination sessions for 7 days from a specific date in a given pin.
        """
        query_params = {"pincode": str(pincode), "date": str(date)}

        headers = {}
        if accept_language is not None:
            headers["Accept-Language"] = str(accept_language)

        return self.api_client.request(
            type_=m.Any,
            method="GET",
            url="/v2/appointment/sessions/public/calendarByPin",
            params=query_params,
            headers=headers,
        )

    def _build_for_public_find_by_district(
        self, district_id: str, date: str, accept_language: str = None
    ) -> Awaitable[m.Any]:
        """
        API to get planned vaccination sessions on a specific date in a given district.
        """
        query_params = {"district_id": str(district_id), "date": str(date)}

        headers = {}
        if accept_language is not None:
            headers["Accept-Language"] = str(accept_language)

        return self.api_client.request(
            type_=m.Any,
            method="GET",
            url="/v2/appointment/sessions/public/findByDistrict",
            params=query_params,
            headers=headers,
        )

    def _build_for_public_find_by_pin(self, pincode: str, date: str, accept_language: str = None) -> Awaitable[m.Any]:
        """
        API to get planned vaccination sessions on a specific date in a given pin.
        """
        query_params = {"pincode": str(pincode), "date": str(date)}

        headers = {}
        if accept_language is not None:
            headers["Accept-Language"] = str(accept_language)

        return self.api_client.request(
            type_=m.Any,
            method="GET",
            url="/v2/appointment/sessions/public/findByPin",
            params=query_params,
            headers=headers,
        )


class AsyncAppointmentAvailabilityAPIsApi(_AppointmentAvailabilityAPIsApi):
    async def public_calendar_by_district(self, district_id: str, date: str, accept_language: str = None) -> m.Any:
        """
        API to get planned vaccination sessions for 7 days from a specific date in a given district.
        """
        return await self._build_for_public_calendar_by_district(
            district_id=district_id, date=date, accept_language=accept_language
        )

    async def public_calendar_by_pin(self, pincode: str, date: str, accept_language: str = None) -> m.Any:
        """
        API to get planned vaccination sessions for 7 days from a specific date in a given pin.
        """
        return await self._build_for_public_calendar_by_pin(pincode=pincode, date=date, accept_language=accept_language)

    async def public_find_by_district(self, district_id: str, date: str, accept_language: str = None) -> m.Any:
        """
        API to get planned vaccination sessions on a specific date in a given district.
        """
        return await self._build_for_public_find_by_district(
            district_id=district_id, date=date, accept_language=accept_language
        )

    async def public_find_by_pin(self, pincode: str, date: str, accept_language: str = None) -> m.Any:
        """
        API to get planned vaccination sessions on a specific date in a given pin.
        """
        return await self._build_for_public_find_by_pin(pincode=pincode, date=date, accept_language=accept_language)


class SyncAppointmentAvailabilityAPIsApi(_AppointmentAvailabilityAPIsApi):
    def public_calendar_by_district(self, district_id: str, date: str, accept_language: str = None) -> m.Any:
        """
        API to get planned vaccination sessions for 7 days from a specific date in a given district.
        """
        coroutine = self._build_for_public_calendar_by_district(
            district_id=district_id, date=date, accept_language=accept_language
        )
        return get_event_loop().run_until_complete(coroutine)

    def public_calendar_by_pin(self, pincode: str, date: str, accept_language: str = None) -> m.Any:
        """
        API to get planned vaccination sessions for 7 days from a specific date in a given pin.
        """
        coroutine = self._build_for_public_calendar_by_pin(pincode=pincode, date=date, accept_language=accept_language)
        return get_event_loop().run_until_complete(coroutine)

    def public_find_by_district(self, district_id: str, date: str, accept_language: str = None) -> m.Any:
        """
        API to get planned vaccination sessions on a specific date in a given district.
        """
        coroutine = self._build_for_public_find_by_district(
            district_id=district_id, date=date, accept_language=accept_language
        )
        return get_event_loop().run_until_complete(coroutine)

    def public_find_by_pin(self, pincode: str, date: str, accept_language: str = None) -> m.Any:
        """
        API to get planned vaccination sessions on a specific date in a given pin.
        """
        coroutine = self._build_for_public_find_by_pin(pincode=pincode, date=date, accept_language=accept_language)
        return get_event_loop().run_until_complete(coroutine)

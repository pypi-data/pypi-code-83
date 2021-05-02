# flake8: noqa E501
from asyncio import get_event_loop
from typing import TYPE_CHECKING, Awaitable

from cowin_api import models as m

if TYPE_CHECKING:
    from cowin_api.api_client import ApiClient


class _MetadataAPIsApi:
    def __init__(self, api_client: "ApiClient"):
        self.api_client = api_client

    def _build_for_districts(self, state_id: str, accept_language: str = None) -> Awaitable[m.InlineResponse2003]:
        """
        API to get all the districts.
        """
        path_params = {"state_id": str(state_id)}

        headers = {}
        if accept_language is not None:
            headers["Accept-Language"] = str(accept_language)

        return self.api_client.request(
            type_=m.InlineResponse2003,
            method="GET",
            url="/v2/admin/location/districts/{state_id}",
            path_params=path_params,
            headers=headers,
        )

    def _build_for_find_by_lat_long(self, lat: float, long: float, accept_language: str = None) -> Awaitable[m.Any]:
        """
        API to get vaccination centers by latitude and longitude.
        """
        query_params = {"lat": str(lat), "long": str(long)}

        headers = {}
        if accept_language is not None:
            headers["Accept-Language"] = str(accept_language)

        return self.api_client.request(
            type_=m.Any,
            method="GET",
            url="/v2/appointment/centers/findByLatLong",
            params=query_params,
            headers=headers,
        )

    def _build_for_genders(self, accept_language: str = None) -> Awaitable[m.InlineResponse2006]:
        """
        API to get all gender details.
        """
        headers = {}
        if accept_language is not None:
            headers["Accept-Language"] = str(accept_language)

        return self.api_client.request(
            type_=m.InlineResponse2006,
            method="GET",
            url="/v2/registration/beneficiary/genders",
            headers=headers,
        )

    def _build_for_id_types(self, accept_language: str = None) -> Awaitable[m.InlineResponse2005]:
        """
        API to get list of beneficiary Ids that can be used as proof of identity for registration.
        """
        headers = {}
        if accept_language is not None:
            headers["Accept-Language"] = str(accept_language)

        return self.api_client.request(
            type_=m.InlineResponse2005,
            method="GET",
            url="/v2/registration/beneficiary/idTypes",
            headers=headers,
        )

    def _build_for_states(self, accept_language: str = None) -> Awaitable[m.InlineResponse2002]:
        """
        API to get all the states in India.
        """
        headers = {}
        if accept_language is not None:
            headers["Accept-Language"] = str(accept_language)

        return self.api_client.request(
            type_=m.InlineResponse2002,
            method="GET",
            url="/v2/admin/location/states",
            headers=headers,
        )


class AsyncMetadataAPIsApi(_MetadataAPIsApi):
    async def districts(self, state_id: str, accept_language: str = None) -> m.InlineResponse2003:
        """
        API to get all the districts.
        """
        return await self._build_for_districts(state_id=state_id, accept_language=accept_language)

    async def find_by_lat_long(self, lat: float, long: float, accept_language: str = None) -> m.Any:
        """
        API to get vaccination centers by latitude and longitude.
        """
        return await self._build_for_find_by_lat_long(lat=lat, long=long, accept_language=accept_language)

    async def genders(self, accept_language: str = None) -> m.InlineResponse2006:
        """
        API to get all gender details.
        """
        return await self._build_for_genders(accept_language=accept_language)

    async def id_types(self, accept_language: str = None) -> m.InlineResponse2005:
        """
        API to get list of beneficiary Ids that can be used as proof of identity for registration.
        """
        return await self._build_for_id_types(accept_language=accept_language)

    async def states(self, accept_language: str = None) -> m.InlineResponse2002:
        """
        API to get all the states in India.
        """
        return await self._build_for_states(accept_language=accept_language)


class SyncMetadataAPIsApi(_MetadataAPIsApi):
    def districts(self, state_id: str, accept_language: str = None) -> m.InlineResponse2003:
        """
        API to get all the districts.
        """
        coroutine = self._build_for_districts(state_id=state_id, accept_language=accept_language)
        return get_event_loop().run_until_complete(coroutine)

    def find_by_lat_long(self, lat: float, long: float, accept_language: str = None) -> m.Any:
        """
        API to get vaccination centers by latitude and longitude.
        """
        coroutine = self._build_for_find_by_lat_long(lat=lat, long=long, accept_language=accept_language)
        return get_event_loop().run_until_complete(coroutine)

    def genders(self, accept_language: str = None) -> m.InlineResponse2006:
        """
        API to get all gender details.
        """
        coroutine = self._build_for_genders(accept_language=accept_language)
        return get_event_loop().run_until_complete(coroutine)

    def id_types(self, accept_language: str = None) -> m.InlineResponse2005:
        """
        API to get list of beneficiary Ids that can be used as proof of identity for registration.
        """
        coroutine = self._build_for_id_types(accept_language=accept_language)
        return get_event_loop().run_until_complete(coroutine)

    def states(self, accept_language: str = None) -> m.InlineResponse2002:
        """
        API to get all the states in India.
        """
        coroutine = self._build_for_states(accept_language=accept_language)
        return get_event_loop().run_until_complete(coroutine)

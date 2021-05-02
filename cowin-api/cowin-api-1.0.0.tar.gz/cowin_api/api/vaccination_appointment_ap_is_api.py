# flake8: noqa E501
from asyncio import get_event_loop
from typing import TYPE_CHECKING, Awaitable

from fastapi.encoders import jsonable_encoder

from cowin_api.client import models as m

if TYPE_CHECKING:
    from cowin_api.client.api_client import ApiClient


class _VaccinationAppointmentAPIsApi:
    def __init__(self, api_client: "ApiClient"):
        self.api_client = api_client

    def _build_for_beneficiaries(
        self,
    ) -> Awaitable[m.Any]:
        """
        API to get the list of benefiaries linked to the logged in/authenticated user’s mobile number. This list can be useful to schedule one appointment for an entire family.
        """
        return self.api_client.request(
            type_=m.Any,
            method="GET",
            url="/v2/appointment/beneficiaries",
        )

    def _build_for_calendar_by_district(
        self, district_id: str, date: str, accept_language: str = None, vaccine: str = None
    ) -> Awaitable[m.Any]:
        """
        API to get planned vaccination sessions for 7 days from a specific date in a given district. An optional parameter <i>vaccine</i> can also used to get the sessions for a specific vaccine. This paramters is used to to get the sessions for dose 2 appointment.
        """
        query_params = {
            "district_id": str(district_id),
            "date": str(date),
        }
        if vaccine is not None:
            query_params["vaccine"] = str(vaccine)

        headers = {}
        if accept_language is not None:
            headers["Accept-Language"] = str(accept_language)

        return self.api_client.request(
            type_=m.Any,
            method="GET",
            url="/v2/appointment/sessions/calendarByDistrict",
            params=query_params,
            headers=headers,
        )

    def _build_for_calendar_by_pin(
        self, pincode: str, date: str, accept_language: str = None, vaccine: str = None
    ) -> Awaitable[m.Any]:
        """
        API to get planned vaccination sessions for 7 days from a specific date in a given pin. An optional parameter <i>vaccine</i> can also used to get the sessions for a specific vaccine. This paramters is used to to get the sessions for dose 2 appointment.
        """
        query_params = {
            "pincode": str(pincode),
            "date": str(date),
        }
        if vaccine is not None:
            query_params["vaccine"] = str(vaccine)

        headers = {}
        if accept_language is not None:
            headers["Accept-Language"] = str(accept_language)

        return self.api_client.request(
            type_=m.Any,
            method="GET",
            url="/v2/appointment/sessions/calendarByPin",
            params=query_params,
            headers=headers,
        )

    def _build_for_cancel_appointment(self, inline_object8: m.InlineObject8 = None) -> Awaitable[None]:
        """
        API to remove an individual from an appointment.
        """
        body = jsonable_encoder(inline_object8)

        return self.api_client.request(type_=None, method="POST", url="/v2/appointment/cancel", json=body)

    def _build_for_find_by_district(
        self, district_id: str, date: str, accept_language: str = None, vaccine: str = None
    ) -> Awaitable[m.Any]:
        """
        API to get planned vaccination sessions on a specific date in a given district. An optional parameter <i>vaccine</i> can also used to get the sessions for a specific vaccine. This paramters is used to to get the sessions for dose 2 appointment.
        """
        query_params = {
            "district_id": str(district_id),
            "date": str(date),
        }
        if vaccine is not None:
            query_params["vaccine"] = str(vaccine)

        headers = {}
        if accept_language is not None:
            headers["Accept-Language"] = str(accept_language)

        return self.api_client.request(
            type_=m.Any,
            method="GET",
            url="/v2/appointment/sessions/findByDistrict",
            params=query_params,
            headers=headers,
        )

    def _build_for_find_by_pin(
        self, pincode: str, date: str, accept_language: str = None, vaccine: str = None
    ) -> Awaitable[m.Any]:
        """
        API to get planned vaccination sessions on a specific date in a given pin. An optional parameter <i>vaccine</i> can also used to get the sessions for a specific vaccine. This paramters is used to to get the sessions for dose 2 appointment.
        """
        query_params = {
            "pincode": str(pincode),
            "date": str(date),
        }
        if vaccine is not None:
            query_params["vaccine"] = str(vaccine)

        headers = {}
        if accept_language is not None:
            headers["Accept-Language"] = str(accept_language)

        return self.api_client.request(
            type_=m.Any,
            method="GET",
            url="/v2/appointment/sessions/findByPin",
            params=query_params,
            headers=headers,
        )

    def _build_for_reschedule_appointment(self, inline_object7: m.InlineObject7 = None) -> Awaitable[None]:
        """
        API to reschedule an appointment for vaccination.
        """
        body = jsonable_encoder(inline_object7)

        return self.api_client.request(type_=None, method="POST", url="/v2/appointment/reschedule", json=body)

    def _build_for_schedule(self, inline_object6: m.InlineObject6 = None) -> Awaitable[m.Any]:
        """
        API to schedule an appointment for vaccination. An appointment can be scheduled for a selected center, on a selected date and for a selected session. An appointment can be scheduled for multiple beneficiaries provided their registered mobile number is same as the registered mobile number of the logged in or authenticated beneficiary.
        """
        body = jsonable_encoder(inline_object6)

        return self.api_client.request(type_=m.Any, method="POST", url="/v2/appointment/schedule", json=body)


class AsyncVaccinationAppointmentAPIsApi(_VaccinationAppointmentAPIsApi):
    async def beneficiaries(
        self,
    ) -> m.Any:
        """
        API to get the list of benefiaries linked to the logged in/authenticated user’s mobile number. This list can be useful to schedule one appointment for an entire family.
        """
        return await self._build_for_beneficiaries()

    async def calendar_by_district(
        self, district_id: str, date: str, accept_language: str = None, vaccine: str = None
    ) -> m.Any:
        """
        API to get planned vaccination sessions for 7 days from a specific date in a given district. An optional parameter <i>vaccine</i> can also used to get the sessions for a specific vaccine. This paramters is used to to get the sessions for dose 2 appointment.
        """
        return await self._build_for_calendar_by_district(
            district_id=district_id, date=date, accept_language=accept_language, vaccine=vaccine
        )

    async def calendar_by_pin(self, pincode: str, date: str, accept_language: str = None, vaccine: str = None) -> m.Any:
        """
        API to get planned vaccination sessions for 7 days from a specific date in a given pin. An optional parameter <i>vaccine</i> can also used to get the sessions for a specific vaccine. This paramters is used to to get the sessions for dose 2 appointment.
        """
        return await self._build_for_calendar_by_pin(
            pincode=pincode, date=date, accept_language=accept_language, vaccine=vaccine
        )

    async def cancel_appointment(self, inline_object8: m.InlineObject8 = None) -> None:
        """
        API to remove an individual from an appointment.
        """
        return await self._build_for_cancel_appointment(inline_object8=inline_object8)

    async def find_by_district(
        self, district_id: str, date: str, accept_language: str = None, vaccine: str = None
    ) -> m.Any:
        """
        API to get planned vaccination sessions on a specific date in a given district. An optional parameter <i>vaccine</i> can also used to get the sessions for a specific vaccine. This paramters is used to to get the sessions for dose 2 appointment.
        """
        return await self._build_for_find_by_district(
            district_id=district_id, date=date, accept_language=accept_language, vaccine=vaccine
        )

    async def find_by_pin(self, pincode: str, date: str, accept_language: str = None, vaccine: str = None) -> m.Any:
        """
        API to get planned vaccination sessions on a specific date in a given pin. An optional parameter <i>vaccine</i> can also used to get the sessions for a specific vaccine. This paramters is used to to get the sessions for dose 2 appointment.
        """
        return await self._build_for_find_by_pin(
            pincode=pincode, date=date, accept_language=accept_language, vaccine=vaccine
        )

    async def reschedule_appointment(self, inline_object7: m.InlineObject7 = None) -> None:
        """
        API to reschedule an appointment for vaccination.
        """
        return await self._build_for_reschedule_appointment(inline_object7=inline_object7)

    async def schedule(self, inline_object6: m.InlineObject6 = None) -> m.Any:
        """
        API to schedule an appointment for vaccination. An appointment can be scheduled for a selected center, on a selected date and for a selected session. An appointment can be scheduled for multiple beneficiaries provided their registered mobile number is same as the registered mobile number of the logged in or authenticated beneficiary.
        """
        return await self._build_for_schedule(inline_object6=inline_object6)


class SyncVaccinationAppointmentAPIsApi(_VaccinationAppointmentAPIsApi):
    def beneficiaries(
        self,
    ) -> m.Any:
        """
        API to get the list of benefiaries linked to the logged in/authenticated user’s mobile number. This list can be useful to schedule one appointment for an entire family.
        """
        coroutine = self._build_for_beneficiaries()
        return get_event_loop().run_until_complete(coroutine)

    def calendar_by_district(
        self, district_id: str, date: str, accept_language: str = None, vaccine: str = None
    ) -> m.Any:
        """
        API to get planned vaccination sessions for 7 days from a specific date in a given district. An optional parameter <i>vaccine</i> can also used to get the sessions for a specific vaccine. This paramters is used to to get the sessions for dose 2 appointment.
        """
        coroutine = self._build_for_calendar_by_district(
            district_id=district_id, date=date, accept_language=accept_language, vaccine=vaccine
        )
        return get_event_loop().run_until_complete(coroutine)

    def calendar_by_pin(self, pincode: str, date: str, accept_language: str = None, vaccine: str = None) -> m.Any:
        """
        API to get planned vaccination sessions for 7 days from a specific date in a given pin. An optional parameter <i>vaccine</i> can also used to get the sessions for a specific vaccine. This paramters is used to to get the sessions for dose 2 appointment.
        """
        coroutine = self._build_for_calendar_by_pin(
            pincode=pincode, date=date, accept_language=accept_language, vaccine=vaccine
        )
        return get_event_loop().run_until_complete(coroutine)

    def cancel_appointment(self, inline_object8: m.InlineObject8 = None) -> None:
        """
        API to remove an individual from an appointment.
        """
        coroutine = self._build_for_cancel_appointment(inline_object8=inline_object8)
        return get_event_loop().run_until_complete(coroutine)

    def find_by_district(self, district_id: str, date: str, accept_language: str = None, vaccine: str = None) -> m.Any:
        """
        API to get planned vaccination sessions on a specific date in a given district. An optional parameter <i>vaccine</i> can also used to get the sessions for a specific vaccine. This paramters is used to to get the sessions for dose 2 appointment.
        """
        coroutine = self._build_for_find_by_district(
            district_id=district_id, date=date, accept_language=accept_language, vaccine=vaccine
        )
        return get_event_loop().run_until_complete(coroutine)

    def find_by_pin(self, pincode: str, date: str, accept_language: str = None, vaccine: str = None) -> m.Any:
        """
        API to get planned vaccination sessions on a specific date in a given pin. An optional parameter <i>vaccine</i> can also used to get the sessions for a specific vaccine. This paramters is used to to get the sessions for dose 2 appointment.
        """
        coroutine = self._build_for_find_by_pin(
            pincode=pincode, date=date, accept_language=accept_language, vaccine=vaccine
        )
        return get_event_loop().run_until_complete(coroutine)

    def reschedule_appointment(self, inline_object7: m.InlineObject7 = None) -> None:
        """
        API to reschedule an appointment for vaccination.
        """
        coroutine = self._build_for_reschedule_appointment(inline_object7=inline_object7)
        return get_event_loop().run_until_complete(coroutine)

    def schedule(self, inline_object6: m.InlineObject6 = None) -> m.Any:
        """
        API to schedule an appointment for vaccination. An appointment can be scheduled for a selected center, on a selected date and for a selected session. An appointment can be scheduled for multiple beneficiaries provided their registered mobile number is same as the registered mobile number of the logged in or authenticated beneficiary.
        """
        coroutine = self._build_for_schedule(inline_object6=inline_object6)
        return get_event_loop().run_until_complete(coroutine)

# flake8: noqa E501
from asyncio import get_event_loop
from typing import TYPE_CHECKING, Awaitable
from uuid import UUID

from cowin_api import models as m

if TYPE_CHECKING:
    from cowin_api.api_client import ApiClient


class _CertificateAPIsApi:
    def __init__(self, api_client: "ApiClient"):
        self.api_client = api_client

    def _build_for_download(self, beneficiary_reference_id: str) -> Awaitable[m.IO]:
        """
        API to download vaccination certificate in PDF format by beneficiary reference id.
        """
        query_params = {"beneficiary_reference_id": str(beneficiary_reference_id)}

        return self.api_client.request(
            type_=m.IO,
            method="GET",
            url="/v2/registration/certificate/download",
            params=query_params,
        )

    def _build_for_download_appointment_slip(self, appointment_id: UUID) -> Awaitable[m.IO]:
        """
        API to download vaccination appointment slip in PDF format by appointment id.
        """
        query_params = {"appointment_id": str(appointment_id)}

        return self.api_client.request(
            type_=m.IO,
            method="GET",
            url="/v2/appointment/appointmentslip/download",
            params=query_params,
        )

    def _build_for_public_download(self, beneficiary_reference_id: str) -> Awaitable[m.IO]:
        """
        API to download vaccination certificate in PDF format by beneficiary reference id. This API requires a <i>Bearer</i> token acquired with user mobile OTP validation as defined in User Authentication APIs.
        """
        query_params = {"beneficiary_reference_id": str(beneficiary_reference_id)}

        return self.api_client.request(
            type_=m.IO,
            method="GET",
            url="/v2/registration/certificate/public/download",
            params=query_params,
        )


class AsyncCertificateAPIsApi(_CertificateAPIsApi):
    async def download(self, beneficiary_reference_id: str) -> m.IO:
        """
        API to download vaccination certificate in PDF format by beneficiary reference id.
        """
        return await self._build_for_download(beneficiary_reference_id=beneficiary_reference_id)

    async def download_appointment_slip(self, appointment_id: UUID) -> m.IO:
        """
        API to download vaccination appointment slip in PDF format by appointment id.
        """
        return await self._build_for_download_appointment_slip(appointment_id=appointment_id)

    async def public_download(self, beneficiary_reference_id: str) -> m.IO:
        """
        API to download vaccination certificate in PDF format by beneficiary reference id. This API requires a <i>Bearer</i> token acquired with user mobile OTP validation as defined in User Authentication APIs.
        """
        return await self._build_for_public_download(beneficiary_reference_id=beneficiary_reference_id)


class SyncCertificateAPIsApi(_CertificateAPIsApi):
    def download(self, beneficiary_reference_id: str) -> m.IO:
        """
        API to download vaccination certificate in PDF format by beneficiary reference id.
        """
        coroutine = self._build_for_download(beneficiary_reference_id=beneficiary_reference_id)
        return get_event_loop().run_until_complete(coroutine)

    def download_appointment_slip(self, appointment_id: UUID) -> m.IO:
        """
        API to download vaccination appointment slip in PDF format by appointment id.
        """
        coroutine = self._build_for_download_appointment_slip(appointment_id=appointment_id)
        return get_event_loop().run_until_complete(coroutine)

    def public_download(self, beneficiary_reference_id: str) -> m.IO:
        """
        API to download vaccination certificate in PDF format by beneficiary reference id. This API requires a <i>Bearer</i> token acquired with user mobile OTP validation as defined in User Authentication APIs.
        """
        coroutine = self._build_for_public_download(beneficiary_reference_id=beneficiary_reference_id)
        return get_event_loop().run_until_complete(coroutine)

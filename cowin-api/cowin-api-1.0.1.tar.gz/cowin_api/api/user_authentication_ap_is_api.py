# flake8: noqa E501
from asyncio import get_event_loop
from typing import TYPE_CHECKING, Awaitable

from fastapi.encoders import jsonable_encoder

from cowin_api import models as m

if TYPE_CHECKING:
    from cowin_api.api_client import ApiClient


class _UserAuthenticationAPIsApi:
    def __init__(self, api_client: "ApiClient"):
        self.api_client = api_client

    def _build_for_public_confirm_otp(self, inline_object1: m.InlineObject1 = None) -> Awaitable[m.InlineResponse2001]:
        """
        API to confirm the OTP for authentication.
        """
        body = jsonable_encoder(inline_object1)

        return self.api_client.request(
            type_=m.InlineResponse2001, method="POST", url="/v2/auth/public/confirmOTP", json=body
        )

    def _build_for_public_generate_otp(self, inline_object: m.InlineObject = None) -> Awaitable[m.InlineResponse200]:
        """
        Initiate beneficiary authentication using mobile and OTP
        """
        body = jsonable_encoder(inline_object)

        return self.api_client.request(
            type_=m.InlineResponse200, method="POST", url="/v2/auth/public/generateOTP", json=body
        )


class AsyncUserAuthenticationAPIsApi(_UserAuthenticationAPIsApi):
    async def public_confirm_otp(self, inline_object1: m.InlineObject1 = None) -> m.InlineResponse2001:
        """
        API to confirm the OTP for authentication.
        """
        return await self._build_for_public_confirm_otp(inline_object1=inline_object1)

    async def public_generate_otp(self, inline_object: m.InlineObject = None) -> m.InlineResponse200:
        """
        Initiate beneficiary authentication using mobile and OTP
        """
        return await self._build_for_public_generate_otp(inline_object=inline_object)


class SyncUserAuthenticationAPIsApi(_UserAuthenticationAPIsApi):
    def public_confirm_otp(self, inline_object1: m.InlineObject1 = None) -> m.InlineResponse2001:
        """
        API to confirm the OTP for authentication.
        """
        coroutine = self._build_for_public_confirm_otp(inline_object1=inline_object1)
        return get_event_loop().run_until_complete(coroutine)

    def public_generate_otp(self, inline_object: m.InlineObject = None) -> m.InlineResponse200:
        """
        Initiate beneficiary authentication using mobile and OTP
        """
        coroutine = self._build_for_public_generate_otp(inline_object=inline_object)
        return get_event_loop().run_until_complete(coroutine)

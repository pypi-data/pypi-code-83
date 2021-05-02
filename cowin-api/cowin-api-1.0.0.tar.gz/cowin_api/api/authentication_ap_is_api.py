# flake8: noqa E501
from asyncio import get_event_loop
from typing import TYPE_CHECKING, Awaitable

from fastapi.encoders import jsonable_encoder

from cowin_api.client import models as m

if TYPE_CHECKING:
    from cowin_api.client.api_client import ApiClient


class _AuthenticationAPIsApi:
    def __init__(self, api_client: "ApiClient"):
        self.api_client = api_client

    def _build_for_confirm_otp(self, inline_object3: m.InlineObject3 = None) -> Awaitable[m.InlineResponse2004]:
        """
        API to confirm the OTP for authentication.
        """
        body = jsonable_encoder(inline_object3)

        return self.api_client.request(type_=m.InlineResponse2004, method="POST", url="/v2/auth/confirmOTP", json=body)

    def _build_for_generate_otp(self, inline_object2: m.InlineObject2 = None) -> Awaitable[m.InlineResponse200]:
        """
        Initiate beneficiary authentication using mobile and OTP
        """
        body = jsonable_encoder(inline_object2)

        return self.api_client.request(type_=m.InlineResponse200, method="POST", url="/v2/auth/generateOTP", json=body)


class AsyncAuthenticationAPIsApi(_AuthenticationAPIsApi):
    async def confirm_otp(self, inline_object3: m.InlineObject3 = None) -> m.InlineResponse2004:
        """
        API to confirm the OTP for authentication.
        """
        return await self._build_for_confirm_otp(inline_object3=inline_object3)

    async def generate_otp(self, inline_object2: m.InlineObject2 = None) -> m.InlineResponse200:
        """
        Initiate beneficiary authentication using mobile and OTP
        """
        return await self._build_for_generate_otp(inline_object2=inline_object2)


class SyncAuthenticationAPIsApi(_AuthenticationAPIsApi):
    def confirm_otp(self, inline_object3: m.InlineObject3 = None) -> m.InlineResponse2004:
        """
        API to confirm the OTP for authentication.
        """
        coroutine = self._build_for_confirm_otp(inline_object3=inline_object3)
        return get_event_loop().run_until_complete(coroutine)

    def generate_otp(self, inline_object2: m.InlineObject2 = None) -> m.InlineResponse200:
        """
        Initiate beneficiary authentication using mobile and OTP
        """
        coroutine = self._build_for_generate_otp(inline_object2=inline_object2)
        return get_event_loop().run_until_complete(coroutine)

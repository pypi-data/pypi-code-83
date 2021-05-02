# flake8: noqa E501
from asyncio import get_event_loop
from typing import TYPE_CHECKING, Awaitable

from fastapi.encoders import jsonable_encoder

from cowin_api.client import models as m

if TYPE_CHECKING:
    from cowin_api.client.api_client import ApiClient


class _BeneficiaryRegistrationAPIsApi:
    def __init__(self, api_client: "ApiClient"):
        self.api_client = api_client

    def _build_for_beneficiary_registration_for_partner_applications(
        self, inline_object4: m.InlineObject4 = None
    ) -> Awaitable[m.InlineResponse2007]:
        """
        API for beneficiary registration from partner applications. This API returns a beneficiary reference id as a unique identifier of the registered user.
        """
        body = jsonable_encoder(inline_object4)

        return self.api_client.request(
            type_=m.InlineResponse2007, method="POST", url="/v2/registration/beneficiary/new", json=body
        )

    def _build_for_delete_beneficiary(self, inline_object5: m.InlineObject5 = None) -> Awaitable[None]:
        """
        API to delete a beneficiary by benefiary reference id.
        """
        body = jsonable_encoder(inline_object5)

        return self.api_client.request(type_=None, method="POST", url="/v2/registration/beneficiary/delete", json=body)


class AsyncBeneficiaryRegistrationAPIsApi(_BeneficiaryRegistrationAPIsApi):
    async def beneficiary_registration_for_partner_applications(
        self, inline_object4: m.InlineObject4 = None
    ) -> m.InlineResponse2007:
        """
        API for beneficiary registration from partner applications. This API returns a beneficiary reference id as a unique identifier of the registered user.
        """
        return await self._build_for_beneficiary_registration_for_partner_applications(inline_object4=inline_object4)

    async def delete_beneficiary(self, inline_object5: m.InlineObject5 = None) -> None:
        """
        API to delete a beneficiary by benefiary reference id.
        """
        return await self._build_for_delete_beneficiary(inline_object5=inline_object5)


class SyncBeneficiaryRegistrationAPIsApi(_BeneficiaryRegistrationAPIsApi):
    def beneficiary_registration_for_partner_applications(
        self, inline_object4: m.InlineObject4 = None
    ) -> m.InlineResponse2007:
        """
        API for beneficiary registration from partner applications. This API returns a beneficiary reference id as a unique identifier of the registered user.
        """
        coroutine = self._build_for_beneficiary_registration_for_partner_applications(inline_object4=inline_object4)
        return get_event_loop().run_until_complete(coroutine)

    def delete_beneficiary(self, inline_object5: m.InlineObject5 = None) -> None:
        """
        API to delete a beneficiary by benefiary reference id.
        """
        coroutine = self._build_for_delete_beneficiary(inline_object5=inline_object5)
        return get_event_loop().run_until_complete(coroutine)

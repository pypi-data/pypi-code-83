from asyncio import get_event_loop
from typing import Any, Awaitable, Callable, Dict, Generic, Type, TypeVar, overload

from httpx import AsyncClient, Request, Response
from pydantic import ValidationError, parse_obj_as

from cowin_api.client.api.appointment_availability_ap_is_api import (
    AsyncAppointmentAvailabilityAPIsApi,
    SyncAppointmentAvailabilityAPIsApi,
)
from cowin_api.client.api.authentication_ap_is_api import AsyncAuthenticationAPIsApi, SyncAuthenticationAPIsApi
from cowin_api.client.api.beneficiary_registration_ap_is_api import (
    AsyncBeneficiaryRegistrationAPIsApi,
    SyncBeneficiaryRegistrationAPIsApi,
)
from cowin_api.client.api.certificate_ap_is_api import AsyncCertificateAPIsApi, SyncCertificateAPIsApi
from cowin_api.client.api.metadata_ap_is_api import AsyncMetadataAPIsApi, SyncMetadataAPIsApi
from cowin_api.client.api.user_authentication_ap_is_api import (
    AsyncUserAuthenticationAPIsApi,
    SyncUserAuthenticationAPIsApi,
)
from cowin_api.client.api.vaccination_appointment_ap_is_api import (
    AsyncVaccinationAppointmentAPIsApi,
    SyncVaccinationAppointmentAPIsApi,
)
from cowin_api.client.exceptions import ResponseHandlingException, UnexpectedResponse

ClientT = TypeVar("ClientT", bound="ApiClient")


class AsyncApis(Generic[ClientT]):
    def __init__(self, client: ClientT):
        self.client = client

        self.appointment_availability_ap_is_api = AsyncAppointmentAvailabilityAPIsApi(self.client)
        self.authentication_ap_is_api = AsyncAuthenticationAPIsApi(self.client)
        self.beneficiary_registration_ap_is_api = AsyncBeneficiaryRegistrationAPIsApi(self.client)
        self.certificate_ap_is_api = AsyncCertificateAPIsApi(self.client)
        self.metadata_ap_is_api = AsyncMetadataAPIsApi(self.client)
        self.user_authentication_ap_is_api = AsyncUserAuthenticationAPIsApi(self.client)
        self.vaccination_appointment_ap_is_api = AsyncVaccinationAppointmentAPIsApi(self.client)


class SyncApis(Generic[ClientT]):
    def __init__(self, client: ClientT):
        self.client = client

        self.appointment_availability_ap_is_api = SyncAppointmentAvailabilityAPIsApi(self.client)
        self.authentication_ap_is_api = SyncAuthenticationAPIsApi(self.client)
        self.beneficiary_registration_ap_is_api = SyncBeneficiaryRegistrationAPIsApi(self.client)
        self.certificate_ap_is_api = SyncCertificateAPIsApi(self.client)
        self.metadata_ap_is_api = SyncMetadataAPIsApi(self.client)
        self.user_authentication_ap_is_api = SyncUserAuthenticationAPIsApi(self.client)
        self.vaccination_appointment_ap_is_api = SyncVaccinationAppointmentAPIsApi(self.client)


T = TypeVar("T")
Send = Callable[[Request], Awaitable[Response]]
MiddlewareT = Callable[[Request, Send], Awaitable[Response]]


class ApiClient:
    def __init__(self, host: str = None, **kwargs: Any) -> None:
        self.host = host
        self.middleware: MiddlewareT = BaseMiddleware()
        self._async_client = AsyncClient(**kwargs)

    @overload
    async def request(
        self, *, type_: Type[T], method: str, url: str, path_params: Dict[str, Any] = None, **kwargs: Any
    ) -> T:
        ...

    @overload  # noqa F811
    async def request(
        self, *, type_: None, method: str, url: str, path_params: Dict[str, Any] = None, **kwargs: Any
    ) -> None:
        ...

    async def request(  # noqa F811
        self, *, type_: Any, method: str, url: str, path_params: Dict[str, Any] = None, **kwargs: Any
    ) -> Any:
        if path_params is None:
            path_params = {}
        url = (self.host or "") + url.format(**path_params)
        request = Request(method, url, **kwargs)
        return await self.send(request, type_)

    @overload
    def request_sync(self, *, type_: Type[T], **kwargs: Any) -> T:
        ...

    @overload  # noqa F811
    def request_sync(self, *, type_: None, **kwargs: Any) -> None:
        ...

    def request_sync(self, *, type_: Any, **kwargs: Any) -> Any:  # noqa F811
        """
        This method is not used by the generated apis, but is included for convenience
        """
        return get_event_loop().run_until_complete(self.request(type_=type_, **kwargs))

    async def send(self, request: Request, type_: Type[T]) -> T:
        response = await self.middleware(request, self.send_inner)
        if response.status_code in [200, 201]:
            try:
                return parse_obj_as(type_, response.json())
            except ValidationError as e:
                raise ResponseHandlingException(e)
        raise UnexpectedResponse.for_response(response)

    async def send_inner(self, request: Request) -> Response:
        try:
            response = await self._async_client.send(request)
        except Exception as e:
            raise ResponseHandlingException(e)
        return response

    def add_middleware(self, middleware: MiddlewareT) -> None:
        current_middleware = self.middleware

        async def new_middleware(request: Request, call_next: Send) -> Response:
            async def inner_send(request: Request) -> Response:
                return await current_middleware(request, call_next)

            return await middleware(request, inner_send)

        self.middleware = new_middleware


class BaseMiddleware:
    async def __call__(self, request: Request, call_next: Send) -> Response:
        return await call_next(request)

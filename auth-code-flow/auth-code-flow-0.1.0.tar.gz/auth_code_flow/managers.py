import abc
import uuid
from urllib.parse import urlencode

import requests

from . import adapters, exceptions


class AbstractBaseFlowManager(abc.ABC):
    access_token_path = "/access_token"
    authorization_path = "/authorize"
    base_uri = None
    client_id = None
    client_secret = None
    grant_type = "authorization_code"
    redirect_uri = None
    response_type = "code"
    scope = None

    class Meta:
        required_attributes = [
            "authorization_path",
            "base_uri",
            "client_id",
            "client_secret",
            "grant_type",
            "redirect_uri",
            "response_type",
            "scope",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        not_configured = [
            attribute
            for attribute in self.Meta.required_attributes
            if getattr(self, attribute, None) is None
        ]
        if len(not_configured) > 0:
            raise exceptions.ImproperlyConfigured(
                obj=self, keys=not_configured, abstract_base=AbstractBaseFlowManager
            )

    def make_state(self):
        return str(uuid.uuid4())

    def get_authorization_endpoint(self, state):
        return (
            self.base_uri
            + self.authorization_path
            + "?"
            + urlencode(self.get_authorization_endpoint_params(state=state))
        )

    def get_authorization_endpoint_params(self, state):
        return {
            "client_id": self.client_id,
            "redirect_uri": self.redirect_uri,
            "response_type": self.response_type,
            "scope": self.scope,
            "state": state,
        }

    def get_access_token_endpoint(self):
        return self.base_uri + self.access_token_path

    def get_access_token_endpoint_params(self, code, state):
        return {
            "code": code,
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "grant_type": self.grant_type,
            "redirect_uri": self.redirect_uri,
            "state": state,
        }

    def fetch_access_token(
        self, user, code, state, post_form_data=False, check_state=True
    ):
        if check_state and not self.check_user_state(user=user, state=state):
            raise exceptions.StateForgeryError

        with requests.Session() as session:
            session.mount(self.base_uri, adapters.exponential_backoff_adapter)
            try:
                resp = self._perform_fetch(session, code, state, post_form_data)
                resp.raise_for_status()
            except requests.exceptions.HTTPError as exc:
                raise exceptions.AuthCodeFlowError(response=resp) from exc
            except requests.exceptions.RequestException as exc:
                raise exceptions.AuthCodeFlowError(response=None) from exc

        return resp

    def _perform_fetch(self, session, code, state, post_form_data):
        if post_form_data:
            return session.post(
                self.get_access_token_endpoint(),
                data=self.get_access_token_endpoint_params(code=code, state=state),
                timeout=(5, 5),
            )
        return session.post(
            self.get_access_token_endpoint(),
            json=self.get_access_token_endpoint_params(code=code, state=state),
            timeout=(5, 5),
        )

    @abc.abstractmethod
    def store_user_state(self, user, state):
        pass

    @abc.abstractmethod
    def check_user_state(self, user, state):
        pass

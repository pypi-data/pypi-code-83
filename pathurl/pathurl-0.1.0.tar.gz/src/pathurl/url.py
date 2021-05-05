from urllib.parse import urlparse

from pathurl.constants import DEFAULT_SCHEME, Port
from pathurl.path import Path
from pathurl.query import Query


class URL:
    __slots__ = [
        "scheme",
        "username",
        "password",
        "hostname",
        "port",
        "path",
        "params",
        "query",
        "fragment",
    ]

    def __init__(
        self,
        scheme: str = "",
        username: str = None,
        password: str = None,
        hostname: str = None,
        port: int = None,
        path: str = "",
        params: str = "",
        query: str = "",
        fragment: str = "",
    ):
        self.scheme = scheme or DEFAULT_SCHEME
        self.username = username
        self.hostname = hostname
        self.password = password
        self.port = port or self._infer_port(self.scheme)
        self.path = Path(path)
        self.params = params
        self.query = Query(query)
        self.fragment = fragment

    def __str__(self) -> str:
        parts = [f"{self.scheme}://"]
        if self.username or self.password:
            if self.username:
                parts.append(self.username)
            if self.password:
                parts.append(f":{self.password}")
            parts.append("@")
        parts.append(self.hostname)
        if self.port and self.port != self._infer_port(self.scheme):
            parts.append(f":{self.port}")
        parts.append(str(self.path))
        if self.params:
            parts.append(f";{self.params}")
        if self.query:
            parts.append(f"?{self.query}")
        if self.fragment:
            parts.append(f"#{self.fragment}")
        return "".join(parts)

    @staticmethod
    def _infer_port(scheme: str) -> int:
        try:
            port = Port[scheme]
        except KeyError:
            return None

        return port.value

    @classmethod
    def parse(cls, url: str) -> "URL":
        parsed_url = urlparse(url)
        return cls(
            scheme=parsed_url.scheme,
            username=parsed_url.username,
            password=parsed_url.password,
            hostname=parsed_url.hostname,
            port=parsed_url.port,
            path=parsed_url.path,
            params=parsed_url.params,
            query=parsed_url.query,
            fragment=parsed_url.fragment,
        )

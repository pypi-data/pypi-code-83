from urllib.parse import parse_qs, urlencode


class Query:
    __slots__ = ["_data"]

    def __init__(self, query_string: str = ""):
        self._data = parse_qs(query_string)

    def __str__(self) -> str:
        return urlencode(self._data, doseq=True)

    def __bool__(self) -> bool:
        return bool(self._data)

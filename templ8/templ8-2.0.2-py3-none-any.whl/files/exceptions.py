class FileParsingError(Exception):
    def __init__(self, path: str) -> None:
        super().__init__(f"Failed to parse {path}")


class UnsupportedFormat(Exception):
    def __init__(self, path: str) -> None:
        super().__init__(f"Unable to parse {path}")

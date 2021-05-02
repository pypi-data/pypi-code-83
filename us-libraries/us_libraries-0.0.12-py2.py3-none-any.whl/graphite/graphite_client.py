from typing import Dict, Optional

import graphyte


class GraphiteClient:

    def __init__(self, url: str = 'graphite', interval: int = 60, prefix: Optional[str] = None) -> None:
        graphyte.init(url, prefix=prefix, interval=interval)

    @staticmethod
    def send(stats: str, value: float, tags: Optional[Dict] = {}) -> None:
        graphyte.send(stats, value=value, tags=tags)

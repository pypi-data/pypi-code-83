# -*- coding: utf-8


from sortedcontainers.sorteddict import SortedDict


class TsdbConfig(SortedDict):
    """Tsdb client config

    Args:
        host ([str]): connection host
        port ([int]): port
        user ([str]): auth user
        password ([str]): auth password
    """

    def __init__(
        self,
        host: str = "localhost",
        port: int = 3306,
        user: str = "root",
        password: str = "root",
    ):
        super().__init__(host=host, user=user, password=password, port=port)
        self.host = host
        self.port = port
        self.user = user
        self.password = password

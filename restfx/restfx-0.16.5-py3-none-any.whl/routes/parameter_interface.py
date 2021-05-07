from abc import ABC, abstractmethod


class IParam(ABC):
    """

    """

    @classmethod
    @abstractmethod
    def parse(cls, value: (list, dict)):
        raise NotImplemented()

from abc import ABCMeta, abstractmethod


class Element(metaclass=ABCMeta):
    
    @abstractmethod
    def _getEleKey(self):
        ...

    @abstractmethod
    def __str__(self):
        ...

    def _getAttrs(self) -> dict:
        return {}

    def _getAttrStr(self) -> str:
        attrs = self._getAttrs()
        if len(attrs) > 0:
            rt = ''
            for k in attrs.keys():
                rt += f' {k}="{attrs[k]}"'
            return rt
        return ''

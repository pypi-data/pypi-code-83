import json
from collections import UserDict


class PyAmis:
    pass


class PyAmisComponent(dict, UserDict):

    def __init__(self, **kwargs) -> None:
        for k in dict(kwargs):
            if kwargs[k] is None:
                del kwargs[k]
        super().__init__(**kwargs)

    def with_value(self,k,v):
        self[k] = v
        return self
    def to_json(self, indent=None):
        return json.dumps(self)

    def to_dict(self):
        return json.loads(self.to_json())



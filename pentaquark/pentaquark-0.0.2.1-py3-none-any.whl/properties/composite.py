import json
from .scalars import StringProperty, Property
from ..exceptions import PentaQuarkValidationError


class JSONProperty(StringProperty):
    def from_cypher(self, __value):
        if __value:
            return json.loads(__value)

    def to_cypher(self, __value):
        if __value:
            return json.dumps(__value)

    def _validate(self, __value, **kwargs):
        if __value is None:
            return None
        try:
            json.dumps(__value)
        except TypeError as e:
            raise PentaQuarkValidationError(f"'{__value}' is not json serializable ({e})")
        return __value

    def to_graphql(self, __value):
        return json.dumps(__value)


class ArrayProperty(Property):
    def __init__(self, internal_type=StringProperty, max_length=None, **kwargs):
        super().__init__(**kwargs)
        self.internal_type = internal_type
        self.max_length = max_length

    def _validate(self, __value, **kwargs):
        if __value is None:
            return None
        if isinstance(__value, (list, set, tuple)):
            if self.max_length and len(__value) > self.max_length:
                raise PentaQuarkValidationError(
                    f"'{__value}' is too long: {len(__value)} > {self.max_length}"
                )
            return list(__value)
        raise PentaQuarkValidationError(f"'{__value}' is not an iterable")

    def get_graphql_type(self):
        return f"[{self.internal_type.get_graphql_type()}]"

from ..models.abstract_model import DeleteFailed
from .object import Object


class RequiredAttributes(Exception):
    pass


class AbstractModelObject(Object):
    """
    attributes: defined on Object
    protected_attributes: defined on Object

    required_attributes: attributes that must be include when creating a new object in the database

    _model: the instantiated model that AbstractModelObject will use to connect to the database
    """
    required_attributes = []
    _model = None

    def __init__(self, attributes_or_id={}):
        if type(attributes_or_id) is dict:
            super().__init__(attributes_or_id)
        elif type(attributes_or_id) is str:
            super().__init__(self._model.get(attributes_or_id))

    def insert(self):
        missing_required_attributes = self._get_missing_required_attributes()
        if missing_required_attributes:
            raise RequiredAttributes('missing the following required attributes: ' + ', '.join(missing_required_attributes))
        self.deserialize(self._model.insert(self.serialize(hide_protected_attributes=False)))

    def update(self):
        self.deserialize(self._model.update(self.id, self.serialize(hide_protected_attributes=False)))

    def save(self):
        if self.id and bool(self._model.get(self.id)):
            self.update()
        else:
            self.insert()

    def delete(self):
        if self.id:
            return self._model.delete(self.id)
        else:
            raise DeleteFailed('id is required to delete')

    def _get_missing_required_attributes(self):
        missing_required_attributes = []
        for required_attribute in self.required_attributes:
            if self.__dict__.get(required_attribute, None) is None:
                missing_required_attributes.append(required_attribute)
        return missing_required_attributes

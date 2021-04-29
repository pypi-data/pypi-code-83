from django.contrib.contenttypes.models import ContentType
from jsonschema.validators import Draft7Validator

from huscy.attributes.models import AttributeSchema, AttributeSet
from huscy.pseudonyms.services import get_or_create_pseudonym


def get_or_create_attribute_set(subject):
    content_type = ContentType.objects.get_by_natural_key('attributes', 'attributeset')
    pseudonym = get_or_create_pseudonym(subject, content_type)

    attribute_set, created = AttributeSet.objects.get_or_create(pseudonym=pseudonym.code)
    return attribute_set


def update_attribute_set(attribute_set, attributes, attribute_schema_version=None):
    if attribute_schema_version is None:
        attribute_schema = attribute_set.attribute_schema
    else:
        if attribute_schema_version < attribute_set.attribute_schema.pk:
            raise Exception('New version for attribute schema must be greater than or equals with '
                            'current attribute schema version.')
        attribute_schema = AttributeSchema.objects.get(pk=attribute_schema_version)

    Draft7Validator(attribute_schema.schema).validate(attributes)

    attribute_set.attributes = attributes
    attribute_set.attribute_schema = attribute_schema
    attribute_set.save()

    return attribute_set


def get_attribute_schema(version=None):
    queryset = AttributeSchema.objects

    try:
        if version is None:
            return queryset.latest('pk')
        else:
            return queryset.get(pk=version)
    except AttributeSchema.DoesNotExist:
        return _create_initial_attribute_schema()


def _create_initial_attribute_schema():
    if AttributeSchema.objects.exists():
        raise Exception('Initial attribute schema already exist!')

    return AttributeSchema.objects.create(schema={
        'type': 'object',
        'properties': {},
    })

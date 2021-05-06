from rest_framework import serializers

from huscy.attributes.services import get_or_create_attribute_set
from huscy.attributes.serializer import AttributeSetSerializer
from huscy.subjects.serializers import SubjectSerializer


class DataRequestSerializer(serializers.Serializer):
    attributes = serializers.SerializerMethodField()
    subject = serializers.SerializerMethodField()

    def get_attributes(self, subject):
        attribute_set = get_or_create_attribute_set(subject)
        return AttributeSetSerializer(attribute_set).data

    def get_subject(self, subject):
        return SubjectSerializer(subject).data

from .models import EventLocalization, Superevent

from rest_framework import serializers


class SupereventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Superevent
        fields = ['superevent_id', 'superevent_url',
                  'id', 'created', 'modified']


class EventLocalizationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EventLocalization
        fields = [
            'id', 'created', 'modified']

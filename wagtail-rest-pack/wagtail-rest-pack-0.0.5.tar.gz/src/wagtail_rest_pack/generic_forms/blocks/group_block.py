from wagtail.core import blocks
from wagtail_rest_pack.generic_forms.blocks.generic_input import GenericInputBlock
from django.core.exceptions import ValidationError
from django.db import models
from modelcluster.models import ClusterableModel
from wagtail.snippets.models import register_snippet
from django.db import models
from rest_framework import serializers
from wagtail.core import blocks

from wagtail.core.fields import StreamField
from wagtail_rest_pack.generic_forms.blocks.text_block import InputBlockSerializer
from wagtail_rest_pack.streamfield.serializers import StreamFieldSerializer, SettingsStreamFieldSerializer
choices = [
    ('always', "Vždy"),
    ('anonymous_user_only', "Pouze nepřihlášený uživatel")
]

class GroupBlockSerializer(serializers.Serializer):
    block_name = 'form_group'
    name = serializers.CharField(max_length=80)
    row = serializers.BooleanField()
    required = serializers.ChoiceField(choices=choices)
    stream = SettingsStreamFieldSerializer()
    class Meta:
        fields = ('name', 'row', 'required', 'stream',)

    @staticmethod
    def block_definition():
        return GroupBlockSerializer.block_name, GroupBlock(stream_blocks=[
            InputBlockSerializer.block_definition()
        ])

    def to_representation(self, instance):
        return super(GroupBlockSerializer, self).to_representation(instance)

    # def get_api_representation(self, value, context=None):
    #     # we dont want to send action to frontend
    #     result = {a[0]: a[1] for a in value.items() if isinstance(a[1], str)}
    #     result['stream'] = self.stream_definition.get_api_representation(value['stream'])
    #     return result

class GroupBlock(blocks.StructBlock):

    def __init__(self, stream_blocks, **kwargs):
        self.stream_definition = blocks.StreamBlock(local_blocks=stream_blocks)
        local_blocks = [
            ('name', blocks.CharBlock(max_length=80)),
            ('row', blocks.BooleanBlock(required=False, default=False, label="Zobrazit na jednom řádku.")),
            ('required', blocks.ChoiceBlock(choices=choices, default="always", label="Podmínka zobrazení pole")),
            ('stream', self.stream_definition)
        ]
        super().__init__(local_blocks=local_blocks, **kwargs)


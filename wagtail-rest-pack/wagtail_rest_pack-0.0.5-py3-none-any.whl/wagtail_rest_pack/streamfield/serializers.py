from wagtail.api.v2.serializers import Field
from importlib import import_module

class StreamFieldSerializer(Field):
    def __init__(self, *args, **kwargs):
        self.serializers_instances = kwargs.pop('serializers', object())
        super(StreamFieldSerializer, self).__init__(*args, **kwargs)

    def get_serializers(self):
        return self.serializers_instances

    def to_representation(self, value):
        representation = []
        if value is None:
            return representation
        serializers = self.get_serializers()
        for child in value:
            if child.block.name not in serializers.keys():
                child_representation = child.block.get_api_representation(child.value, context=self.context)
            else:
                ser = serializers[child.block.name](context=self.context)
                child_representation = ser.to_representation(child.value)
            representation.append({
                'type': child.block.name,
                'value': child_representation,
                'id': child.id
            })
        return representation


class SettingsStreamFieldSerializer(StreamFieldSerializer):
    def __init__(self, *args, **kwargs):
        kwargs.pop('serializers', {})
        super(SettingsStreamFieldSerializer, self).__init__(*args, **kwargs)

    def get_serializers(self):
        # todo add serializers from django.conf.settings
        # kwargs['serializers'] = ''
        form_serializers = {
            'form_text': 'wagtail_rest_pack.generic_forms.blocks.text_block.InputBlockSerializer',
            'form_group': 'wagtail_rest_pack.generic_forms.blocks.group_block.GroupBlockSerializer',
            'form_submit': 'wagtail_rest_pack.generic_forms.blocks.submit_block.SubmitBlockSerializer',
        }
        from django.apps import apps
        classes = {}
        for key,value in form_serializers.items():
            try:
                module_path, class_name = value.rsplit('.', 1)
                module = import_module(module_path)
                classes[key] = getattr(module, class_name)
            except (ImportError, AttributeError) as e:
                raise ImportError(class_str)

        # add caching ?
        return classes

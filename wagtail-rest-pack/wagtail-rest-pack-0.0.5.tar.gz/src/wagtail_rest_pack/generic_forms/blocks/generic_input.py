import re

from django.core.exceptions import ValidationError
from wagtail.core import blocks

from rest_framework import serializers
def is_form_field(value):
    if not isinstance(value, str):
        raise ValidationError("Only string is allowed.")
    pattern = "^[a-zA-Z0-9_-]+$"
    pass
    if re.match(pattern, value) is None:
        raise ValidationError("Does not match a-z, A-Z")


class GenericInputBlock(blocks.StructBlock):
    def __init__(self, specific: [] = None, **kwargs):
        # todo validace na unikátnost name
        local_blocks = [
            ('name', blocks.TextBlock(max_length=30, help_text='Název pole v ascii (např. user_email)',
                                      label='Technický název pole', validators=[is_form_field])),
            ('label', blocks.TextBlock(max_length=50, label='Popisek zobrazený před inputem.')),
            ('max_length',
             blocks.IntegerBlock(label='Max', help_text='Maximální délka vstupu', default=100, min_value=10,
                                 max_value=2000)),
            ('required', blocks.ChoiceBlock(choices=[
                ('always', 'Vždy'),
                ('anonymous_user_only', 'Pouze nepřihlášený uživatel')
            ], default='always', label='Podmínka zobrazení pole')),
            ('placeholder',
             blocks.CharBlock(max_length=80, required=False, help_text='Hodnota zobrazená, když nic není vyplněno.')),
            ('validation', blocks.ChoiceBlock(choices=[
                ('none', 'Žádné'),
                ('email', 'Email')
            ], default='none', label='Validace'))
        ]
        if specific is not None:
            local_blocks.extend(specific)
        super().__init__(local_blocks=local_blocks, **kwargs)


# def validator(request, value, validated_field, value_field, field, add_error):
#     # Required
#     if value and value_field['required'] == 'anonymous_user_only' and request.user.is_authenticated:
#         add_error(validated_field, 'Pole je povinné pouze pro nepřihlášené uživatele')
#         return
#     if not value:
#         if value_field['required'] == 'anonymous_user_only' and not request.user.is_authenticated:
#             add_error(validated_field, 'Toto pole je požadováno.')
#         return
#
#     # Type
#     if field['type'] == get_form_base_name() + 'text':
#         if not isinstance(value, str):
#             add_error(validated_field, 'Hodnota není typu str')
#     else:
#         add_error(validated_field, 'Neočekávaný typ ' + field['type'])
#
#     # Max Length
#     if len(value) > value_field['max_length']:
#         # todo template string
#         add_error(validated_field, 'Délka hodnoty je moc velká. Očekáváno max ' + str(
#             value_field['max_length']) + ', ale je ' + str(len(value)))
#
#     # Custom Validation
#     if value_field['validation'] == 'email':
#         try:
#             validate_email(value)
#         except ValidationError as err:
#             add_error(validated_field, 'Toto není validní email.')

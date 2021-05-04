from wagtail.core import blocks

from wagtail_rest_pack.generic_forms.actions.action import FormAction


class SendEmailAction(FormAction):
    type = 'send_email'

    @staticmethod
    def block_definition() -> tuple:
        return SendEmailAction.type, blocks.StructBlock(local_blocks=[
            ('sender', blocks.CharBlock(max_length=50, label="Nazev technického pole, ve kterém bude vyplněn odesílatel.")),
            ('address', blocks.EmailBlock(max_length=150, label="Adresát."))
        ])

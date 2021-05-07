import ast

import click


class MultipleArguments(click.Option):

    def type_cast_value(self, ctx, value):
        try:
            value = str(value)
            assert value.count('[') == 1 and value.count(']') == 1
            list_as_str = value.replace('"', "'").split('[')[1].split(']')[0]
            list_of_items = [item.strip().strip("'") for item in list_as_str.split(',')]
            return list_of_items
        except:
            raise click.BadParameter(value)

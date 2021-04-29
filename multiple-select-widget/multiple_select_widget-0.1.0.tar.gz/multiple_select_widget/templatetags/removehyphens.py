from django.template import Library

register = Library()

@register.filter
def remove_hyphens(value):
    return value.replace("-", "_")

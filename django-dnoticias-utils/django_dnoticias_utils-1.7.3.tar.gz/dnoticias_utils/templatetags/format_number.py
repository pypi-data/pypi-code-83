from django import template

register = template.Library()

@register.assignment_tag
def format_number(value,limit):
    array_number = []
    for digit in str(value):
        array_number.append(digit)
    formated = ""
    counter = 0
    for i in array_number:
        formated += str(i)
        counter += 1
        if counter == limit:
            formated += " "
            counter = 0
    return formated

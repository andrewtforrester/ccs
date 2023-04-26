from django import template

register = template.Library()

@register.filter(name='multiply')
def multiply(value,v2):
    return value*v2


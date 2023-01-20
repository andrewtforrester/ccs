from django import template

register = template.Library()

@register.filter(name='replace')
def replace(value,arg):
    arg1 = arg.split(";")[0]
    arg2 = arg.split(";")[1]
    return value.replace(arg1,arg2)

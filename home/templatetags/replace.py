from django import template
import json

register = template.Library()

@register.filter(name='replace')
def replace(value,arg):
    arg1 = arg.split(";")[0]
    arg2 = arg.split(";")[1]
    return value.replace(arg1,arg2)

@register.filter(name='json_ready')
def json_ready(nav_streamfield):
    # return json.dumps(nav_streamfield)

    result = []

    for item in nav_streamfield:
        if item.block_type == "category":
            result = result + [{
                "name": item.value["category_name"],
            }]
        elif item.block_type == "internal_button":
            pass
        elif item.block_type == 'external_button':
            pass

    return json.dumps(result)

    # result = []
    # for item in nav_streamfield:
    #     result = result + [
    #         {
    #             "name": json.dumps(item.value["name"]),
    #             "description": json.dumps(item.value["description"].source),
    #         }
    #     ]
    # return result


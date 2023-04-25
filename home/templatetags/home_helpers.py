from django import template
import json

register = template.Library()

def json_ready(nav_streamfield):
    return json.dumps(nav_streamfield)

    result = []
    for item in nav_streamfield:
        result = result + [
            {
                "name": json.dumps(item.value["name"]),
                "description": json.dumps(item.value["description"].source),
            }
        ]
    return result


register.filter("json_ready", json_ready)
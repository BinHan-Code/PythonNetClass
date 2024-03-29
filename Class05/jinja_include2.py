
from __future__ import unicode_literals, print_function
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment 
from pprint import pprint

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader(".")


template_vars = {
    "template_var": "second_template.j2",
}


template_file = "template2.j2"
template = env.get_template(template_file)
output = template.render(**template_vars)
print(output)

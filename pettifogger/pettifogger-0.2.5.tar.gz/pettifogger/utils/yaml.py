# -*- coding: UTF-8 -*-
__author__ = 'Aki Mäkinen'

from ruamel.yaml import YAML
from ruamel.yaml.compat import StringIO

yaml=YAML(typ="rt") # Just to be explicit

def dict_to_yaml_str(source):
    stream = StringIO()
    yaml.dump(source, stream)
    return stream.getvalue()
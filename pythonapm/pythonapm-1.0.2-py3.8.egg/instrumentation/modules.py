
from pythonapm import constants
from pythonapm.instrumentation.packages import django
from pythonapm.instrumentation.packages import flask
from pythonapm.instrumentation.packages import jinja2

modules_info = {}
modules_info.update(django.module_info)
modules_info.update(flask.module_info)
modules_info.update(jinja2.module_info)

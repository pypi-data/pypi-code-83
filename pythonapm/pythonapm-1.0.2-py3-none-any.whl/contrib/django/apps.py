

from django.apps import AppConfig
from django.conf import settings
from pythonapm.agentfactory import get_agent
from .wrapper import instrument_middlewares


class PythonApmConfig(AppConfig):
    name = 'pythonapm'

    def __init__(self, *args, **kwargs):
        super(PythonApmConfig, self).__init__(*args, **kwargs)
        self.client = get_agent()

    def ready(self):
        instrument_middlewares()


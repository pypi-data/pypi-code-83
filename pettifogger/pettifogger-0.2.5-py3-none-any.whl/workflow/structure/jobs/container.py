# -*- coding: UTF-8 -*-
__author__ = 'Aki Mäkinen'

from pettifogger.workflow.structure.env import Env


class Container:
    def __init__(self, definition, *args, **kwargs):
        self.image = definition.get("image")
        self.credentials = definition.get("credentials")
        self.ports = definition.get("ports")
        self.volumes = definition.get("volumes")
        self.options = definition.get("options")

        self.env = Env(definition.get("env")) if "env" in definition else None

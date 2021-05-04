import click
import time
import slai

from pathlib import Path
from slai.clients.project import ProjectClient
from slai_cli import log


def call_model(*, model_name, input):
    project_client = ProjectClient()

    project_name = project_client.get_project()["name"]

    my_model = slai.model(model_name=model_name, project_name=project_name)
    response = my_model(weight=1.0)
    log.info(str(response))

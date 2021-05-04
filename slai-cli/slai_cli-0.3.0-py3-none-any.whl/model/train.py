import importlib.util
import sys
import docker
import click

from pathlib import Path

from slai.clients.model import ModelClient
from slai.clients.project import get_project_client
from slai_cli.create.local_config_helper import LocalConfigHelper
from slai_cli import log
from slai_cli.modules.docker_client import DockerClient

RETURN_CODE_SUCCESS = 0
RETURN_CODE_MISSING_DEP = 1
RETURN_CODE_IMPORT_ERROR = 2
RETURN_CODE_EXIT = 3


def _install_requirement_interactively(*, model_name, docker_client, requirement):
    exit_code = docker_client.install_requirement(
        model_name=model_name, requirement=requirement
    )
    if exit_code != 0:
        log.warn(f"Failed to install: {requirement}")


def _check_imports(*, model_name, model_version_id, docker_client):
    exit_code = docker_client.check_trainer_imports(
        model_name=model_name, model_version_id=model_version_id
    )
    if exit_code == RETURN_CODE_MISSING_DEP:
        if log.action_confirm(
            "Looks like a dependency is missing, would you like to add it interactively?"
        ):
            requirement = log.action_prompt(
                "Add python dependency (e.g. numpy==1.20.1): ",
                type=str,
            )
            return _install_requirement_interactively(
                model_name=model_name,
                docker_client=docker_client,
                requirement=requirement,
            )

            return RETURN_CODE_MISSING_DEP
        else:
            return RETURN_CODE_EXIT

    elif exit_code == RETURN_CODE_IMPORT_ERROR:
        log.warn("Trainer script failed due to import error.")
        return RETURN_CODE_EXIT

    return 0


def _run_trainer(*, model_name, model_version_id, docker_client):
    docker_client.create_model_environment(model_name=model_name)

    log.info("Checking if model trainer imports are valid...")
    import_return_code = _check_imports(
        model_name=model_name,
        model_version_id=model_version_id,
        docker_client=docker_client,
    )

    while (
        import_return_code != RETURN_CODE_SUCCESS
        and import_return_code != RETURN_CODE_EXIT
    ):
        import_return_code = _check_imports(
            model_name=model_name,
            model_version_id=model_version_id,
            docker_client=docker_client,
        )

    if import_return_code == RETURN_CODE_SUCCESS:
        log.info("Dependencies look valid, running training script...")
        exit_code = docker_client.run_trainer(
            model_name=model_name,
            model_version_id=model_version_id,
        )
    else:
        exit_code = import_return_code

    if exit_code != 0:
        log.warn(f"Trainer script failed with return code: {exit_code}")
        log.warn("Training failed.")
        return False
    else:
        log.action("Training complete.")
        return True


def train_model(name):
    log.action(f"Training model: {name}")

    project_client = get_project_client(project_name=None)
    project_name = project_client.get_project_name()

    docker_client = DockerClient(project_name)
    model_client = ModelClient(
        model_name=name, project_name=project_client.get_project_name()
    )

    local_config_helper = LocalConfigHelper()
    local_config = local_config_helper.get_local_config()

    try:
        model_version_id = local_config["models"][name]["model_version_id"]
    except KeyError:
        log.action("No local config set, using default model version.")
        model_version_id = model_client.model["model_version_id"]

    log.action(f"Using model version: {model_version_id}")
    if not log.warn_confirm(
        "If your training script saves a model artifact, this will be uploaded to the slai backend, continue?",  # noqa
    ):
        return

    success = _run_trainer(
        model_name=name,
        model_version_id=model_version_id,
        docker_client=docker_client,
    )

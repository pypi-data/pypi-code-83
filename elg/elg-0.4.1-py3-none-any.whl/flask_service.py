import inspect
import re
from pathlib import Path
from typing import Dict

import docker
from flask import Flask
from flask import request as flask_request
from flask_json import JsonError, as_json
from loguru import logger

from .model import AudioRequest, StructuredTextRequest, TextRequest
from .utils.docker import COPY_FOLDER, DOCKERFILE, ENTRYPOINT


class FlaskService:

    requirements = ["Flask", "Flask-JSON", "gunicorn", "elg", "docker", "flask", "flask_json"]

    def __init__(self, name):
        self.name = name
        self.app = Flask(name)
        # Don't add an extra "status" property to JSON responses - this would break the API contract
        self.app.config["JSON_ADD_STATUS"] = False
        # Don't sort properties alphabetically in response JSON
        self.app.config["JSON_SORT_KEYS"] = False
        self.app.add_url_rule("/process", "process", self.process, methods=["POST"])

    def run(self):
        self.app.run()

    @as_json
    def process(self):
        """
        Main request processing logic - accepts a JSON request and returns a JSON response.
        """
        data = flask_request.get_json()
        if data.get("type") == "text":
            request = TextRequest(**data)
        elif data.get("type") == "structuredText":
            request = StructuredTextRequest(**data)
        elif data.get("type") == "audio":
            request = AudioRequest(**data)
        else:
            self.invalid_request_error()
        logger.info(f"Call with the input: {request}")
        response = self.process_request(request)
        logger.info(f"Get response: {response}")
        response = {"response": response.dict()}
        logger.info(f"Return: {response}")
        return response

    def invalid_request_error(self):
        """
        Generates a valid ELG "failure" response if the request cannot be parsed
        """
        raise JsonError(
            status_=400, failure={"errors": [{"code": "elg.request.invalid", "text": "Invalid request message"}]}
        )

    def process_request(self, request):
        if request.type == "text":
            return self.process_text(request)
        elif request.type == "structuredText":
            return self.process_structured_text(request)
        elif request.type == "audio":
            return self.process_audio(request)
        self.invalid_request_error()

    def process_text(self, request):
        raise NotImplementedError()

    def process_structured_text(self, request):
        raise NotImplementedError()

    def process_audio(self, request):
        raise NotImplementedError()

    @classmethod
    def create_requirements(cls, requirements=[], path=None):
        if path == None:
            path = Path(inspect.getsourcefile(cls))
        else:
            path = Path(path)
        requirements = cls.requirements + requirements
        with open(path.parent / "requirements.txt", "w") as f:
            f.write("\n".join(set(requirements)))

    @classmethod
    def create_docker_files(cls, required_files=[], required_folders=[], path=None):
        if path == None:
            path = Path(inspect.getsourcefile(cls))
        else:
            path = Path(path)
        required_files = [path.name] + required_files
        required_folders = "\n".join(
            [COPY_FOLDER.format(folder_name=str(Path(folder))) for folder in required_folders]
        )
        service_script = path.name[:-3]  # to remove .py
        with open(path.parent / "docker-entrypoint.sh", "w") as f:
            f.write(ENTRYPOINT.format(service_script=service_script))
        with open(path.parent / "Dockerfile", "w") as f:
            f.write(DOCKERFILE.format(required_files=" ".join(required_files), required_folders=required_folders))

    @classmethod
    def docker_build_image(cls, tag: str, pull: bool = True, path=None, **kwargs):
        if path == None:
            path = Path(inspect.getsourcefile(cls))
        else:
            path = Path(path)
        client = docker.from_env()
        image, _ = client.images.build(path=str(path.parent), tag=tag, pull=pull, **kwargs)
        return image

    @classmethod
    def docker_push_image(cls, repository: str, tag: str, username: str = None, password: str = None, **kwargs):
        client = docker.from_env()
        if username is not None and password is not None:
            auth_config = {"username": username, "password": password}
            client.images.push(repository=repository, tag=tag, auth_config=auth_config, stream=True, **kwargs)
        client.images.push(repository=repository, tag=tag, stream=True, **kwargs)
        return

    @classmethod
    def docker_build_push_image(
        cls,
        repository: str,
        tag: str,
        pull: bool = True,
        username: str = None,
        password: str = None,
        build_kwargs: Dict = {},
        push_kwargs: Dict = {},
    ):
        cls.docker_build_image(tag=f"{repository}:{tag}", pull=pull, **build_kwargs)
        cls.docker_push_image(repository=repository, tag=tag, username=username, password=password, **push_kwargs)
        return None

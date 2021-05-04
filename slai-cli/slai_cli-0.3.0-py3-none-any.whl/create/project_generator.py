import uuid
import os
import click
import configparser
import json
import git

from jinja2 import Template
from pathlib import Path
from shutil import rmtree
from git import Repo
from requests.exceptions import HTTPError

from slai_cli import log
from slai.clients.project import ProjectClient
from slai.clients.s3 import S3Client
from slai.clients.gdrive import GoogleDriveClient
from slai.clients.cli import SlaiCliClient

from slai_cli.constants import TEMPLATE_REPO_URLS
from slai_cli.exceptions import (
    InvalidPathException,
    InvalidAWSProfile,
    ProjectExistsException,
)


class ProjectGenerator:
    def __init__(
        self,
        *,
        aws_profile,
        aws_region,
        project_name,
        client_id,
        client_secret,
        profile,
    ):
        self.s3_client = S3Client(
            aws_profile=aws_profile,
            aws_region=aws_region,
        )
        self.cli_client = SlaiCliClient(
            client_id=client_id, client_secret=client_secret
        )

        self.aws_region = aws_region
        self.aws_profile = aws_profile
        self.client_id = client_id
        self.client_secret = client_secret
        self.profile = profile
        self.project_name = project_name

    def create_new_project(self):
        click.clear()
        log.action(f"Creating a new project with name: {self.project_name}")

        try:
            local_path = self._create_project_directory()
            os.chdir(local_path)
        except InvalidPathException as e:
            log.warn(f"Invalid project name: {e}\n")
            return

        # clone template repository
        self._clone_template_repo(local_path=local_path)

        # generate template files
        self.project_variables = self._generate_project_variables(self.project_name)
        self._create_project_files(local_path=local_path)

        # create s3 bucket
        self._create_data_bucket()

    def _create_project_directory(self):
        cwd = os.getcwd()
        local_path = f"{cwd}/{self.project_name}"
        if not os.path.exists(local_path):
            os.makedirs(local_path)

        if os.path.exists(f"{cwd}/{self.project_name}/.slai"):
            raise InvalidPathException("project_already_exists")

        return local_path

    def _generate_project_variables(self, project_name):
        try:
            self.project = self.cli_client.create_project(name=self.project_name)
        except HTTPError as e:
            if e.response.status_code == 400:
                raise ProjectExistsException("duplicate_project_name")
            elif e.response.status_code == 401:
                log.warn("Invalid client id/secret")
                raise
            else:
                raise

        self.service_name = f"{project_name}-{self.project['id']}"

        variables = {
            "SLAI_SERVICE_NAME": self.service_name,
            "SLAI_PROJECT_ID": self.project["id"],
            "SLAI_PROJECT_NAME": project_name,
            "SLAI_AWS_PROFILE": self.aws_profile,
            "SLAI_AWS_REGION": self.aws_region,
            "SLAI_CLIENT_ID": self.client_id,
            "SLAI_CLIENT_SECRET": self.client_secret,
            "SLAI_PROFILE_NAME": self.profile,
        }

        return variables

    def _write_template_file(self, *, project_files, path, filename):
        with open(f"{path}/{filename}", "w") as f_out:
            f_out.write(project_files[filename])

    def _create_project_files(self, *, local_path):
        project_files = {}
        template_files = ["config.yml", "docker-compose.yml"]

        pwd = Path(__file__).parent

        # populate serverless project files
        for fname in template_files:
            log.action(f"Generating: {fname} ")
            template_contents = None

            with open(f"{pwd}/templates/{fname}", "r") as f_in:
                template_contents = f_in.read()
                t = Template(template_contents)
                rendered_template = t.render(**self.project_variables)

                project_files[fname] = rendered_template
                log.action("Done.")

        # write populated template files

        self._write_template_file(
            project_files=project_files,
            path=f"{local_path}/.slai",
            filename="config.yml",
        )

        self._write_template_file(
            project_files=project_files,
            path=f"{local_path}",
            filename="docker-compose.yml",
        )

    def _clone_template_repo(self, local_path):
        log.action("Cloning template repository")

        cloned = False
        for repo_url in TEMPLATE_REPO_URLS:

            try:
                Repo.clone_from(repo_url, local_path)
                rmtree(f"{local_path}/.git")
                cloned = True
                log.action("Done.")
            except git.exc.GitCommandError:
                pass

            if cloned:
                break

        if not cloned:
            log.warn("Unable to clone template repository")
            raise RuntimeError("unable_to_clone_template_repo")

        return local_path

    def _create_data_bucket(self):
        log.action("Creating S3 bucket for model data.")

        bucket_name = f"slai-{self.project_variables['SLAI_SERVICE_NAME']}"
        self.s3_client.create_bucket(bucket_name)

        log.action("Done.")

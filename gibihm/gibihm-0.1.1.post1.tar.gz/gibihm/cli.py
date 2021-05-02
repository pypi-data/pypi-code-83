# Copyright 2021 Dominik George <nik@naturalnet.de>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""GitLab Issue Bot for Isochronal Heads-up Monitoring - CLI wrapper"""

import logging
import os
from typing import Optional, Union

import click
import click_logging
from gitlab.client import Gitlab
from gitlab.v4.objects.projects import Project

from .gitlab import get_gitlab
from .task import Task

logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("gibihm")


def run_single_project(gitlab: Gitlab, project: Union[int, Project]) -> None:
    """Run task scheduling/issue creation for a single projcet by reference or ID."""
    if isinstance(project, int):
        logger.debug("Getting project for id %d", project)
        project = gitlab.projects.get(project)

    tasks = Task.tasks_for_project(project)
    logger.debug("Found %d tasks", len(tasks))
    for task in tasks:
        task.schedule_if_necessary()


def run_all_projects(gitlab: Gitlab) -> None:
    logger.info("Getting all projects the user is member in")
    projects = gitlab.projects.list(membership=True)
    logger.debug("Found %d projects", len(projects))

    for project in projects:
        run_single_project(gitlab, project)


@click.command()
@click_logging.simple_verbosity_option(logger)
@click.option("-p", "--project-id", type=int, help="ID of single project to work on")
def gibihm(project_id: Optional[int] = None):
    """GitLab Issue Bot for Isochronal Heads-up Monitoring"""
    if project_id is None:
        # Support for pre-defined GitLab CI/CD variable CI_PROJECT_ID
        project_id = int(os.environ.get("CI_PROJECT_ID", "0"))

    gitlab = get_gitlab()

    if project_id:
        run_single_project(gitlab, project_id)
    else:
        run_all_projects(gitlab)

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

import logging
import os

import dateparser
import pytz
import yaml
from croniter import CroniterBadCronError, croniter
from datetime import datetime

from .gitlab import get_gitlab
from .util import get_file_content

logger = logging.getLogger("gibihm")


class Task:
    """Definition of one task to be scheduled."""

    def __init__(
        self,
        project,
        template,
        title,
        assignee=None,
        due="in one week",
        labels=None,
        confidential=False,
        schedule="@weekly",
        tag=None,
    ):
        self.gitlab = get_gitlab()

        if labels is None:
            labels = []
        if tag is None:
            tag = template

        self.project = project
        self.labels = labels
        self.confidential = confidential
        self.title = title
        self.tag = tag

        content = get_file_content(project, f".gitlab/issue_templates/{template}.md")
        if content is None:
            raise ValueError(f"Issue template {template} not found")
        self.template = content.decode("utf-8")
        self.template += f"\n\n<!-- {self.full_tag} -->"

        if assignee:
            users = self.gitlab.users.list(username=assignee)
            if not users:
                raise ValueError(f"Username {assignee} not found")
            self.assignee = users[0]
        else:
            self.assignee = None

        self.due = dateparser.parse(due)
        if not self.due:
            raise ValueError(f"Failed to parse date expression {due}")

        try:
            croniter(schedule)
        except CroniterBadCronError as err:
            raise ValueError from err
        else:
            self.schedule = schedule

    @property
    def full_tag(self):
        return f":gibihm:{self.tag}:"

    @property
    def issues(self):
        return self.project.issues.list(search=self.full_tag)

    @property
    def last_issue_date(self):
        issues = self.issues
        if issues:
            return dateparser.parse(self.issues[0].created_at)
        else:
            now = pytz.timezone("UTC").localize(datetime.utcnow())
            cron = croniter(self.schedule, now)
            cron.get_prev()
            return cron.get_prev(datetime)

    @property
    def schedule_next(self):
        cron = croniter(self.schedule, self.last_issue_date)
        return cron.get_next(datetime)

    @property
    def should_schedule(self):
        schedule_next = self.schedule_next
        now = schedule_next.tzinfo.localize(datetime.now())
        return now >= schedule_next

    def schedule_if_necessary(self):
        if self.should_schedule:
            logger.debug("Scheduling %s is necessary", self.tag)

            self.create_issue()
        else:
            logger.debug("Scheduling %s is not necessary", self.tag)

    def create_issue(self):
        args = {
            "title": self.title,
            "description": self.template,
            "due_date": self.due.strftime("%Y-%m-%d"),
            "confidential": self.confidential,
        }
        if self.assignee:
            args["assignee_id"] = self.assignee.id
        if self.labels:
            args["labels"] = self.labels

        logger.info("Creating issue for %s", self.tag)
        logger.debug("Issue payload: %s", repr(args))

        self.project.issues.create(args)

    @classmethod
    def tasks_for_project(cls, project):
        for candidate in [
            ".gitlab/issue_schedule.yaml",
            ".gitlab/issue_schedule.yml",
            ".issue_schedule.yaml",
            ".issue_schedule.yml",
        ]:
            logger.debug("Looking for schedule config in %s", candidate)

            content = get_file_content(project, ".gitlab/issue_schedule.yaml")
            if content is not None:
                logger.info("Loading schedule config from %s", candidate)
                break

        tasks = []
        if content:
            content = content.decode("utf-8")
            data = yaml.load(content, Loader=yaml.BaseLoader)
            for entry in data:
                try:
                    tasks.append(cls(project, **entry))
                except ValueError as err:
                    logger.error("Error creating task: %s", str(err))

        return tasks

# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['gibihm']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=5.4.1,<6.0.0',
 'click-logging>=1.0.1,<2.0.0',
 'click>=7.1.2,<8.0.0',
 'croniter>=1.0.12,<2.0.0',
 'dateparser>=1.0.0,<2.0.0',
 'python-gitlab>=2.7.1,<3.0.0',
 'pytz>=2021.1,<2022.0']

entry_points = \
{'console_scripts': ['gibihm = gibihm.cli:gibihm']}

setup_kwargs = {
    'name': 'gibihm',
    'version': '0.1.1',
    'description': 'GitLab Issue Bot for Isochronal Heads-Up Monitoring',
    'long_description': 'GitLab Issue Bot for Isochronal Heads-up Monitoring\n===================================================\n\nAbout\n-----\n\nThis bot can be used to periodically create issues in a GitLab project.\nIt uses an arbitrary set of issue templates and a schedule configuraiton\nto create matching issues.\n\ngibihm was developed at [Tecids e.V.](https://www.teckids.org) for the\nscenario of managing infrastructure in a GitLab project, and the need\nfor creating issues / to-dos for periodic maintenance tasks\n\n### The name\n\n> Man bräuchte ein Tool, in das man Templates mit Checklisten und so \'ne\n> Art crontab schmeißt, und dann gib ihm!\n\nIn English, freely translated:\n\n> One could use a tool to throw templates with checklists and\n> some kind of crontab at, and off it goes!\n\nUsage\n-----\n\n### General\n\nThe bot\'s configuration lives entirely inside the project the bot will\nbe used in. To start using the bot in a project, invite the bot user to\nthe project. The bot user is a regular GitLab user.\n\nAdd templates and a schedule configuration to your repository, as\ndescribed below. You can find an example project in the `example/`\ndirectory.\n\n### Defining tasks\n\nTasks are defined as [issue\ntemplates](https://docs.gitlab.com/ee/user/project/description_templates.html).\nFor every kind of tasks that has to be scheduled, a template has to be\ncreated. Ideally, the template contains a good description on what has\nto be done, including a checklist of action items for the task\'s\ncompletion.\n\n### Scheduling tasks\n\nThe schedule is a YAML document living either at\n`.gitlab/issue_schedule.yaml` or `.issue_schedule.yaml`. It must contain\nan array of dictionaries, each containing the following keys:\n\n  ------------------------------------------------------------------------------------------\n  Key              Description                                               Default\n  ---------------- --------------------------------------------------------- ---------------\n  `template`       Base filename (without `.md`) of the issue template to    \n                   use                                                       \n\n  `title`          Title for the issue to create                             \n\n  `assignee`       User name of responsible user                             \n\n  `due`            Date expression (parsable by                              `in one week`\n                   [dateparser](https://github.com/scrapinghub/dateparser)   \n                   when task is due                                          \n\n  `labels`         Array of labels to assign to the created issue            \n\n  `confidential`   Set created issue as confidential                         `false`\n\n  `schedule`       A [crontab](https://linux.die.net/man/5/crontab)-like     `@weekly`\n                   schedule defining when the task has to be scheduled       \n\n  `tag`            Short tag to identify issues related to this task         Same as\n                                                                             `template`\n  ------------------------------------------------------------------------------------------\n\n### Configuration\n\nThe bot is configured through environment variables.\n\n  Variable             Description                                      Default\n  -------------------- ------------------------------------------------ --------------------------\n  `GIBIHM_API_URL`     URL of GitLab v4 API endpoint                    Value of `CI_API_V4_URL`\n  `GIBIHM_API_TOKEN`   Access Token with `api` and `read_user` scopes   \n\n### Installation\n\nYou can either use the bot from a Docker image directly in GitLab CI\n(see below), or install it whereever you want and run it\n\n### Installing and running using pip\n\nInstallation from PyPI using pip and running is straightforward:\n\n``` {.shell}\npip3 install gibihm\n\nexport GIBIHM_API_URL=https://gitlab.example.com\nexport GIBIHM_API_TOKEN=Foo_Bar_Token\n\ngibihm\n```\n\n### Installing and running using Docker\n\nThe bot is also available using Docker:\n\n``` {.shell}\ndocker pull natureshadow/gibihm\ndocerk run \\\n    -e GIBIHM_API_URL=https://gitlab.example.com-it \\\n    -e GIBIHM_API_TOKEN=Foo_Bar_Token \\\n    natureshadow/gibihm \n```\n\n### Running for a single project\n\nNormally, the bot will operate on all projects its user is a member of.\n\nYou can pass it a numeric project ID using the `--project-id`\ncommand-line argument to run for only one project.\n\n### Running from project CI\n\nIf you do not want to use a site-wide installation, but rather add the\nbot to a single project, you can configure and run it directly in GitLab\nCI.\n\nA minimal `.gitlab-ci.yml` looks like this:\n\n``` {.yaml}\nschedule_issues:\n  only:\n    - schedules\n  image: natureshadow/gibihm\n  script: [ "true" ]\n```\n\nIn your project settings. add the `GIBIHM_API_TOKEN` variable.\n\nYou can then use [GitLab\'s Pipeline\nschedules](https://docs.gitlab.com/ee/ci/pipelines/schedules.html) to\nperiodically run the bot and schedule your issues.\n',
    'author': 'Dominik George',
    'author_email': 'nik@naturalnet.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://edugit.org/nik/gibihm',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)

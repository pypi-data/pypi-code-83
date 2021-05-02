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
    'version': '0.1.1.post1',
    'description': 'GitLab Issue Bot for Isochronal Heads-Up Monitoring',
    'long_description': 'GitLab Issue Bot for Isochronal Heads-up Monitoring\n===================================================\n\nAbout\n-----\n\nThis bot can be used to periodically create issues in a GitLab project.\nIt uses an arbitrary set of issue templates and a schedule configuraiton\nto create matching issues.\n\ngibihm was developed at `Tecids e.V. <https://www.teckids.org>`__ for\nthe scenario of managing infrastructure in a GitLab project, and the\nneed for creating issues / to-dos for periodic maintenance tasks\n\nThe name\n~~~~~~~~\n\n   Man bräuchte ein Tool, in das man Templates mit Checklisten und so\n   ’ne Art crontab schmeißt, und dann gib ihm!\n\nIn English, freely translated:\n\n   One could use a tool to throw templates with checklists and some kind\n   of crontab at, and off it goes!\n\nUsage\n-----\n\nGeneral\n~~~~~~~\n\nThe bot’s configuration lives entirely inside the project the bot will\nbe used in. To start using the bot in a project, invite the bot user to\nthe project. The bot user is a regular GitLab user.\n\nAdd templates and a schedule configuration to your repository, as\ndescribed below. You can find an example project in the ``example/``\ndirectory.\n\nDefining tasks\n~~~~~~~~~~~~~~\n\nTasks are defined as `issue\ntemplates <https://docs.gitlab.com/ee/user/project/description_templates.html>`__.\nFor every kind of tasks that has to be scheduled, a template has to be\ncreated. Ideally, the template contains a good description on what has\nto be done, including a checklist of action items for the task’s\ncompletion.\n\nScheduling tasks\n~~~~~~~~~~~~~~~~\n\nThe schedule is a YAML document living either at\n``.gitlab/issue_schedule.yaml`` or ``.issue_schedule.yaml``. It must\ncontain an array of dictionaries, each containing the following keys:\n\n+------------+-------------------------------------------+-----------+\n| Key        | Description                               | Default   |\n+============+===========================================+===========+\n| ``         | Base filename (without ``.md``) of the    |           |\n| template`` | issue template to use                     |           |\n+------------+-------------------------------------------+-----------+\n| ``title``  | Title for the issue to create             |           |\n+------------+-------------------------------------------+-----------+\n| ``         | User name of responsible user             |           |\n| assignee`` |                                           |           |\n+------------+-------------------------------------------+-----------+\n| ``due``    | Date expression (parsable by              | ``in o    |\n|            | `dateparser <http                         | ne week`` |\n|            | s://github.com/scrapinghub/dateparser>`__ |           |\n|            | when task is due                          |           |\n+------------+-------------------------------------------+-----------+\n| ``labels`` | Array of labels to assign to the created  |           |\n|            | issue                                     |           |\n+------------+-------------------------------------------+-----------+\n| ``conf     | Set created issue as confidential         | ``false`` |\n| idential`` |                                           |           |\n+------------+-------------------------------------------+-----------+\n| ``         | A                                         | ``        |\n| schedule`` | `crontab <htt                             | @weekly`` |\n|            | ps://linux.die.net/man/5/crontab>`__-like |           |\n|            | schedule defining when the task has to be |           |\n|            | scheduled                                 |           |\n+------------+-------------------------------------------+-----------+\n| ``tag``    | Short tag to identify issues related to   | Same as   |\n|            | this task                                 | ``t       |\n|            |                                           | emplate`` |\n+------------+-------------------------------------------+-----------+\n\nConfiguration\n~~~~~~~~~~~~~\n\nThe bot is configured through environment variables.\n\n+----------------------+----------------------+----------------------+\n| Variable             | Description          | Default              |\n+======================+======================+======================+\n| ``GIBIHM_API_URL``   | URL of GitLab v4 API | Value of             |\n|                      | endpoint             | ``CI_API_V4_URL``    |\n+----------------------+----------------------+----------------------+\n| ``GIBIHM_API_TOKEN`` | Access Token with    |                      |\n|                      | ``api`` and          |                      |\n|                      | ``read_user`` scopes |                      |\n+----------------------+----------------------+----------------------+\n\nInstallation\n~~~~~~~~~~~~\n\nYou can either use the bot from a Docker image directly in GitLab CI\n(see below), or install it whereever you want and run it\n\nInstalling and running using pip\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\nInstallation from PyPI using pip and running is straightforward:\n\n.. code:: shell\n\n   pip3 install gibihm\n\n   export GIBIHM_API_URL=https://gitlab.example.com\n   export GIBIHM_API_TOKEN=Foo_Bar_Token\n\n   gibihm\n\nInstalling and running using Docker\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\nThe bot is also available using Docker:\n\n.. code:: shell\n\n   docker pull natureshadow/gibihm\n   docerk run \\\n       -e GIBIHM_API_URL=https://gitlab.example.com-it \\\n       -e GIBIHM_API_TOKEN=Foo_Bar_Token \\\n       natureshadow/gibihm \n\nRunning for a single project\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\nNormally, the bot will operate on all projects its user is a member of.\n\nYou can pass it a numeric project ID using the ``--project-id``\ncommand-line argument to run for only one project.\n\nRunning from project CI\n~~~~~~~~~~~~~~~~~~~~~~~\n\nIf you do not want to use a site-wide installation, but rather add the\nbot to a single project, you can configure and run it directly in GitLab\nCI.\n\nA minimal ``.gitlab-ci.yml`` looks like this:\n\n.. code:: yaml\n\n   schedule_issues:\n     only:\n       - schedules\n     image: natureshadow/gibihm\n     script: [ "true" ]\n\nIn your project settings. add the ``GIBIHM_API_TOKEN`` variable.\n\nYou can then use `GitLab’s Pipeline\nschedules <https://docs.gitlab.com/ee/ci/pipelines/schedules.html>`__ to\nperiodically run the bot and schedule your issues.\n',
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

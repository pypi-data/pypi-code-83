# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['django_lightweight_queue',
 'django_lightweight_queue.backends',
 'django_lightweight_queue.management',
 'django_lightweight_queue.management.commands',
 'django_lightweight_queue.middleware']

package_data = \
{'': ['*']}

install_requires = \
['daemonize>=2.5.0,<2.6.0', 'django>=2.2', 'prometheus-client>=0.7,<1.0']

extras_require = \
{'progress': ['tqdm>=4.54.1,<5.0.0'], 'redis': ['redis']}

setup_kwargs = {
    'name': 'django-lightweight-queue',
    'version': '4.0.1',
    'description': 'Lightweight & modular queue and cron system for Django',
    'long_description': "# Django Lightweight Queue\n\nDLQ is a lightweight & modular queue and cron system for Django. It powers\nmillions of production jobs every day at Thread.\n\n## Installation\n\n```shell\npip install django-lightweight-queue[redis]\n```\n\nCurrently the only production-ready backends are redis-based, so the `redis`\nextra is essentially required. Additional non-redis backed production-ready\nbackends are great candidates for community contributions.\n\n## Basic Usage\n\n```python\nimport time\nfrom django_lightweight_queue import task\n\n# Define a task\n@task()\ndef long_running_task(first_arg, second_arg):\n    time.sleep(first_arg * second_arg)\n\n# Request that the task be executed at some point\nlong_running_task(4, second_arg=9)\n```\n\nSee the docstring on the [`task`](django_lightweight_queue/task.py) decorator\nfor more details.\n\n## Configuration\n\nAll automatically picked up configuration options begin with `LIGHTWEIGHT_QUEUE_`\nand can be found in `app_settings.py`. They should be placed in the usual Django\nsettings files, for example:\n\n```python\nLIGHTWEIGHT_QUEUE_BACKEND = 'django_lightweight_queue.backends.redis.RedisBackend'\n```\n\n#### Special Configuration\n\nIf desired, specific configuration overrides can be placed in a standalone\npython file which passed on the command line. This is useful for applying\ncustomisations for specific servers.\n\nFor example, given a `special.py` containing:\n\n```python\nLIGHTWEIGHT_QUEUE_REDIS_PORT = 12345\n```\n\nand then running:\n\n```\n$ python manage.py queue_runner --config=special.py\n```\n\nwill result in the runner to use the settings from the specified configuration\nfile in preference to settings from the Django environment. Any settings not\npresent in the specified file are inherited from the global configuration.\n\n## Backends\n\nThere are four built-in backends:\n\n| Backend        | Type        | Description                                                                                                                                                                       |\n| -------------- | ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |\n| Synchronous    | Development | Executes the task inline, without any actual queuing.                                                                                                                             |\n| Redis          | Production  | Executes tasks at-most-once using [Redis][redis] for storage of the enqueued tasks.                                                                                               |\n| Reliable Redis | Production  | Executes tasks at-least-once using [Redis][redis] for storage of the enqueued tasks (subject to Redis consistency). Does not guarantee the task _completes_.                      |\n| Debug Web      | Debugging   | Instead of running jobs it prints the url to a view that can be used to run a task in a transaction which will be rolled back. This is useful for debugging and optimising tasks. |\n\n[redis]: https://redis.io/\n\n## Running Workers\n\nThe queue runner is implemented as a Django management command:\n\n```\n$ python manage.py queue_runner\n```\n\nWorkers can be distributed over multiple hosts by telling each runner that it is\npart of a pool:\n\n```\n$ python manage.py queue_runner --machine 2 --of 4\n```\n\nAlternatively a runner can be told explicitly which configuration to use:\n\n```\n$ python manage.py queue_runner --exact-configuration --config=special.py\n```\n\nWhen using `--exact-configuration` the number of workers is configured exactly,\nrather than being treated as the configuration for a pool. Additionally,\nexactly-configured runners will _not_ run any cron workers.\n\n#### Example\n\nGiven a Django configuration containing:\n\n```python\nLIGHTWEIGHT_QUEUE_WORKERS = {\n    'queue1': 3,\n}\n```\n\nand a `special.py` containing:\n\n```python\nLIGHTWEIGHT_QUEUE_WORKERS = {\n    'queue1': 2,\n}\n```\n\nRunning any of:\n\n```\n$ python manage.py queue_runner --machine 1 --of 3 # or,\n$ python manage.py queue_runner --machine 2 --of 3 # or,\n$ python manage.py queue_runner --machine 3 --of 3\n```\n\nwill result in one worker for `queue1` on the current machine, while:\n\n```\n$ python manage.py queue_runner --exact-configuration --config=special.py\n```\n\nwill result in two workers on the current machine.\n\n## Cron Tasks\n\nDLQ supports the use of a cron-like specification of Django management commands\nto be run at certain times.\n\nTo specify that a management command should be run at a given time, place a\n`cron.py` file in the root folder of the Django app which defines the command\nand which contains a `CONFIG` variable:\n\n```python\nCONFIG = (\n    {\n        'command': 'my_cron_command',\n        # Day values 1-7 to match datetime.datetime.utcnow().isoweekday()\n        'days': '*',\n        'hours': '*',\n        'minutes': '*',\n        # Equivalent behaviour to the kwarg to `task` of the same name\n        'sigkill_on_stop': True,\n    },\n)\n```\n\n## Maintainers\n\nThis repository was created by [Chris Lamb](https://github.com/lamby) at\n[Thread](https://www.thread.com/), and continues to be maintained by the [Thread\nengineering team](https://github.com/thread).\n",
    'author': 'Thread Engineering',
    'author_email': 'tech@thread.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.6',
}


setup(**setup_kwargs)

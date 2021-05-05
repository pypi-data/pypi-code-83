# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['asyncio_gevent']

package_data = \
{'': ['*']}

install_requires = \
['gevent']

setup_kwargs = {
    'name': 'asyncio-gevent',
    'version': '0.1.0',
    'description': 'asyncio & gevent in harmony',
    'long_description': '# asyncio-gevent\n\nasyncio-gevent makes asyncio and gevent compatible. It provides utilities for\n\n- running gevent on asyncio (by using asyncio as gevent\'s event loop, work in progress)\n- running asyncio on gevent (by using gevent as asyncio\'s event loop)\n- converting greenlets to asyncio futures\n- converting futures to asyncio greenlets\n\nasyncio-gevent is a fork and complete rewrite of `aiogevent` and `tulipcore` for modern python 3.\n\n## Install\n\nInstall `asyncio-gevent` from pypi using your favourite package manager.\n\n```sh\n# If you use poetry\npoetry add asyncio-gevent\n\n# If you use pip\npip install asyncio-gevent\n```\n\n## Usage\n\n### Running gevent on asyncio\n\nIn order to run `gevent` on `asyncio`, `gevent` needs to be initialised to use the asyncio event loop. This is done by setting the environment variable `GEVENT_LOOP` to `asyncio_gevent.gevent_loop.GeventLoop` and then starting python.\n\n```sh\nGEVENT_LOOP=asyncio_gevent.gevent_loop.GeventLoop python3 myscript.py\n```\n\ngevent will now run on asyncio.\n\nAlternatively, you can also set the loop configuration setting, preferably right after importing `gevent` and before monkey patching.\n\n```py3\nimport gevent\ngevent.config.loop = "asyncio_gevent"\n```\n\n### Running asyncio on gevent\n\nIn order to run `asyncio` on `gevent`, we need to set the (default) `EventLoopPolicy` to use `asyncio_gevent.EventLoopPolicy`.\n\n```py3\nimport gevent.monkey\ngevent.monkey.patch_all()\n\nimport asyncio\n\nimport asyncio_gevent\n\nasyncio.set_default_event_loop_policy(asyncio_gevent.EventLoopPolicy)\n```\n\n### Converting greenlets to asyncio futures\n\nUse `asyncio_gevent.wrap_greenlet` to convert a greenlet to an asyncio future. The future yields once the greenlet has finished execution.\n\n```py3\n# The following assumes that the gevent/asyncio bindings have already been initialised\nimport gevent\n\nimport asyncio\n\nimport asyncio_gevent\n\n\ndef blocking_function() -> int:\n    gevent.sleep(10)\n    return 42\n\n\nasync def main() -> None:\n    greenlet = gevent.spawn(blocking_function)\n    future = asyncio_gevent.wrap_greenlet()\n    result = await future\n\n\nasyncio.run(main())\n```\n\n### Converting asyncio futures to greenlets\n\nUse `asyncio_gevent.yield_future` to convert a future to a greenlet.\n\n```py3\n# The following assumes that the gevent/asyncio bindings have already been initialised\n\nimport gevent\n\nimport asyncio\n\nimport asyncio_gevent\n\n\nasync def async_function() -> int:\n    await asyncio.sleep(10)\n    return 42\n\n\ndef main() -> None:\n    future = async_function()\n    greenlet = asyncio_gevent.yield_future(future)\n    greenlet.join()\n\nmain()\n```\n\n## License\n\n[MIT](LICENSE)\n',
    'author': 'Frédérique Mittelstaedt',
    'author_email': 'hi@gfm.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/gfmio/asyncio-gevent',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)

# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['generic_pool']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'generic-pool',
    'version': '0.1.0',
    'description': 'A generic object pool implementation',
    'long_description': '# generic-pool\n\ngeneric-pool is a generic object pool for python inspired by the node.js library.\n\nYou can use it to build your own resource pools, e.g. to manage file handles, connections or similar.\n\n## Install\n\nInstall `generic-pool` from pypi using your favourite package manager.\n\n```sh\n# If you use poetry\npoetry add generic-pool\n\n# If you use pip\npip install generic-pool\n```\n\n## Usage\n\n```py3\nfrom random\n\nfrom generic_pool import Factory\nfrom generic_pool import Pool\n\nclass IntValue:\n    def __init__(self):\n        self.value = random.rand\n    pass\n\nclass FortyTwoFactory(Factory):\n    def create(self) -> IntValue:\n        return IntValue()\n\n    def validate(self, item: IntValue) -> bool:\n        return item.value == 42\n\n    def destroy(self):\n        # free resources, not applicable here\n        pass\n\nfactory = FortyTwoFactory()\npool = Pool(factory)\n\nitem = pool.acquire()\ntry:\n    assert item.value == 42\nfinally:\n    pool.release(item)\n\nwith pool.acquire(item):\n    assert item.value == 42\n```\n\n## License\n\n[MIT](LICENSE)\n',
    'author': 'Frédérique Mittelstaedt',
    'author_email': 'pypi@gfm.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/gfmio/generic-pool',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6.2',
}


setup(**setup_kwargs)

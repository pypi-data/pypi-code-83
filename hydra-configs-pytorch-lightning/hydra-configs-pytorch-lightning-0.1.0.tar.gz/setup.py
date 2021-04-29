# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'hydra-configs-pytorch-lightning'}

packages = \
['hydra_configs',
 'hydra_configs.pytorch_lightning',
 'hydra_configs.pytorch_lightning.metrics']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'hydra-configs-pytorch-lightning',
    'version': '0.1.0',
    'description': 'Hydra Lightning',
    'long_description': '## Quick Start:\n\n```\npip install git+https://github.com/romesco/hydra-lightning/#subdirectory=hydra-configs-pytorch-lightning\n```\n\n```python\nfrom hydra_configs.pytorch_lightning.trainer import TrainerConf\n```\n\n## What is this?\n\nThis is a collection of auto-generated configuration files to enable using [Pytorch Lightning](https://github.com/pytorchlightning/pytorch-lightning) with [Hydra](https://hydra.cc). The emphasis on this repository is to provide a stable set of base configs that track the current versions of Lightning and Hydra. If either changes its API, these configs will update automatically as well.\n\nHere is an example of the base config for the `EarlyStopping` Callback from Pytorch Lightning:\n\n```python\n@dataclass\nclass EarlyStoppingConf:\n    _target_: str = "pytorch_lightning.callbacks.EarlyStopping"\n    monitor: str = "early_stop_on"\n    min_delta: float = 0.0\n    patience: int = 3\n    verbose: bool = False\n    mode: str = "auto"\n    strict: bool = True\n```\n\nThis is useful because it allows you to quickly import these configs like:\n\n```python\nfrom hydra_configs.pytorch_lightning.callbacks import EarlyStoppingConf\n```\n\nNow you are free to use this config with its pre-set defaults and override any values programatically using one of:\n\n1. command line args\n2. yaml files\n3. structured configs (dataclasses)\n\n## Looking for `torch` configs?\n\nIf you\'re interested in configuring Lightning classes, you\'re probably interested in configuring normal torch classes as well.\nThings like:\n\n```python\nAdam\nLRStep\nLinear\nDataset\nDataLoader\n...\n```\n\nPlease find those in the pytorch repository:\nhttps://github.com/pytorch/hydra-torch/\n\n## Tutorials\n\n#### Configuring Pytorch with Hydra:\n\n1. [Basic Tutorial](https://github.com/pytorch/hydra-torch/blob/master/examples/mnist_00.md)\n2. Intermediate Tutorial (coming soon)\n3. Advanced Tutorial (coming soon)\n\n#### Lightning\n\n1. Basic Tutorial (coming soon - for now see [examples/mnist_00.py](examples/mnist_00.py)).\n2. Intermediate Tutorial (coming soon)\n\n## Dev Installation\n\n`poetry install`\n\n## Regenerate configs\n\n`poetry run generate-configs`\n',
    'author': 'Rosario Scalise',
    'author_email': 'rosario@cs.uw.edu',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/romesco/hydra-lightning',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)

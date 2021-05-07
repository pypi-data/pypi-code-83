# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['hiraishin', 'hiraishin.models', 'hiraishin.schema', 'hiraishin.scripts']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.1.2,<8.0.0',
 'hydra-core==1.1.0.dev5',
 'overrides>=3.1.0,<4.0.0',
 'pydantic>=1.8.1,<2.0.0',
 'pytorch-lightning>=1.0.8,<2.0.0']

entry_points = \
{'console_scripts': ['hiraishin = hiraishin.cli:cmd']}

setup_kwargs = {
    'name': 'hiraishin',
    'version': '0.1.0',
    'description': 'A thin PyTorch-Lightning wrapper for building configuration-based DL pipelines with Hydra.',
    'long_description': "# Hiraishin\nA thin PyTorch-Lightning wrapper for building configuration-based DL pipelines with Hydra.\n\n# Dependencies\n- PyTorch Lightning\n- Hydra\n- Pydantic\n- etc.\n\n# Installation\n\n```shell\n$ pip install -U hiraishin\n```\n\n# Basic workflow\n## 1. Model initialization with type annotations\nDefine a model class that has training components of PyTorch as instance variables.\n\n```python\nimport torch.nn as nn\nimport torch.optim as optim\n\nfrom hiraishin.models import BaseModel\n\n\nclass ToyModel(BaseModel):\n\n    net: nn.Linear\n    criterion: nn.CrossEntropyLoss\n    optimizer: optim.Adam\n    scheduler: optim.lr_schedulers.ExponentialLR\n\n    def __init__(self, config: DictConfig) -> None:\n        self.initialize(config)  # call `initialize()` instead of `super()__init__()`\n```\n\nWe recommend that they have the following prefix to indicate their role.\n\n- `net` for networks. It must be a subclass of `nn.Module` to initialize and load weights.\n- `criterion` for loss functions. \n- `optimizer` for optimizers. It must be subclass of `Optimizer`.\n- `scheduler` for schedulers. It must be subclass of `_LRScheduler` and the suffix must match to the corresponding optimizer.\n\nIf you need to define modules besides the above components (e.g. tokenizers), feel free to define them. The modules will be defined with the names you specify.\n\n## 2. Generating configuration file\nHiraishin has the functionality to generate configuration files on the command line.\nIf the above class was written in `model.py` at the same level as the current directory, you can generate it with the following command.\n\n```shell\n$ hiraishin configen model.ToyModel\nThe config has been generated! --> config/model/toy.yaml\n```\n\nLet's take a look at the generated file.\nThe positional arguments are filled with `???` that indicates mandatory parameters in Hydra.\nWe recommend overwriting them with the default value, otherwise, you must give them through command-line arguments for every run.\n\n```yaml\n_target_: model.ToyModel\n_recursive_: false\nconfig:\n  networks:\n  - name: net\n    args:\n      _target_: torch.nn.Linear\n      _recursive_: true\n      in_features: ???  # -> 1\n      out_features: ???  # -> 1\n    init:\n      weight_path: null\n      init_type: null\n      init_gain: null\n  losses:\n  - name: criterion\n    args:\n      _target_: torch.nn.CrossEntropyLoss\n      _recursive_: true\n    weight: 1.0\n  optimizers:\n  - name: optimizer\n    args:\n      _target_: torch.optim.Adam\n      _recursive_: true\n    params:\n    - ???  # -> net\n    scheduler:\n      args:\n        _target_: torch.optim.lr_scheduler.ExponentialLR\n        _recursive_: true\n        gamma: ???  # -> 1\n      interval: epoch\n      frequency: 1\n      strict: true\n      monitor: null\n  modules: null\n```\n\n## 3. Training routines definition\nThe rest of model definition is only defining your training routine along with the style of PyTorch Lightning.\n```python\nclass ToyModel(BaseModel):\n    \n    ...\n\n    def forward(self, x: torch.Tensor) -> torch.Tensor:\n        return self.net(x)\n\n    def training_step(self, batch, *args, **kwargs) -> torch.Tensor:\n        x, target = batch\n        pred = self.forward(x)\n        loss = self.criterion(pred, target)\n        self.log('loss/train', loss)\n        return loss\n```\n\n## 4. Model Instantiation\nThe defined model can be instantiated from configuration file. Try to train and test models!\n```python\nfrom hydra.utils import inatantiate\nfrom omegeconf import OmegaConf\n\n\ndef app():\n    ...\n\n    config = OmegaConf.load('config/model/toy.yaml')\n    model = inatantiate(config)\n\n    print(model)\n    # ToyModel(\n    #     (net): Linear(in_features=1, out_features=1, bias=True)\n    #     (criterion): CrossEntropyLoss()\n    # )\n\n    trainer.fit(model, ...)\n```\n\n# License\nHiraishin is licensed under the Apache License, Version 2.0. See [LICENSE](LICENSE) for the full license text.\n",
    'author': 'So Uchida',
    'author_email': 's.aiueo32@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)

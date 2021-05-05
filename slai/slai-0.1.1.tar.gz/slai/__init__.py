from slai.model_version import ModelVersion
from slai.model_inputs import ModelInputs
from slai.base_handler import BaseModelHandler
from slai import loaders
from slai.model import Model

__version__ = "0.1.1"


# most used slai actions go here
model = Model
model_version = ModelVersion
loaders = loaders
inputs = ModelInputs
base_handler = BaseModelHandler


__all__ = ["__version__", "model_version", "model", "inputs", "base_handler", "loaders"]

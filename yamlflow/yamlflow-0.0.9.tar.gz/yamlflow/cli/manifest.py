import os
import sys
from dataclasses import dataclass, asdict

import yaml

from yamlflow.cli.constants import(
    BASE_DIR,
    WEB_CONCURRENCY
)

@dataclass(frozen=True, order=True)
class _meta:
    registry: str
    user: str


@dataclass(frozen=True, order=True)
class _project:
    name: str
    version: str


@dataclass(frozen=True, order=True)
class _backend:
    runtime: str
    device: str
    

class Manifest:

    def __init__(self, mainfest_path: str):
        super().__init__()
        with open(mainfest_path, 'r') as fp:
            try:
                self._data = yaml.safe_load(fp)
            except yaml.YAMLError as err:
                print(err)
                sys.exit(1)
        self._meta_data = self._data["meta"]
        self._project_data = self._data["project"]
        self._backend_data = self._data["backend"]
        self._publish_port = self._data["port"]

    @property
    def meta(self):
        return _meta(**self._meta_data)

    @property
    def project(self):
        return _project(**self._project_data)

    @property
    def backend(self):
        return _backend(**self._backend_data)

    def build_info(self):
        return {
            "path": os.path.abspath(os.path.join(BASE_DIR, os.pardir)),
            "tag": f"{self.meta.registry}/{self.meta.user}/{self.project.name}:{self.project.version}",
            "buildargs": {"BACKEND": f"{self.backend.runtime}-{self.backend.device}"},
            "dockerfile": f"{BASE_DIR}/Dockerfile"
        }

    def run_info(self):
        return {
            "image": f"{self.meta.registry}/{self.meta.user}/{self.project.name}:{self.project.version}",
            "name": self.project.name,
            "environment": {"WEB_CONCURRENCY": WEB_CONCURRENCY},
            "ports": {"8000": self._publish_port}
        }

#!/usr/bin/env python3
from typing import Callable, List
from types import ModuleType
import importlib.util
import inspect
from pathlib import Path
from codoc.domain.model import Graph
from codoc.service.finder.files import (
    get_all_python_files,
)

CodocView = Callable[[Graph], Graph]


def get_views_in_file(py_file: Path) -> List[CodocView]:
    module = get_module_from_file(py_file)

    views = [
        value for key, value in inspect.getmembers(module) if is_a_codoc_view(value)
    ]

    return views


def is_a_codoc_view(obj: object) -> bool:
    return getattr(obj, "__is_codoc_view", False)


def get_module_from_file(py_file: Path) -> ModuleType:
    file_name = py_file.name[:-3]

    spec = importlib.util.spec_from_file_location(file_name, py_file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    return module


def get_views_in_folder(folder: Path) -> List[CodocView]:
    files = get_all_python_files(folder)
    return [view for f in files for view in get_views_in_file(f)]

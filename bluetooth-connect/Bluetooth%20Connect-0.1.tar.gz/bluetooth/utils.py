import subprocess
from typing import Any, Union
import json
from pathlib import Path


def externalcommand(command: str, args: list, raise_error: bool = False, **kwargs):
    op = subprocess.run(
        [command, *args], capture_output=True, check=raise_error, **kwargs
    )
    result = op.stdout
    error = op.stderr
    return result, error


def to_id_name(p: str):
    # sample format 'Device 00:1E:7C:93:AB:49 Infinity Glide 501'
    arr = p.split(" ")
    b_id = arr[1]
    name = " ".join(arr[2:])
    return b_id, name


def decode(b: bytes, encoder="utf-8", strip=False):
    s = b.decode(encoding=encoder)
    if strip:
        s = s.strip()
    return s


def read_json(filepath: Union[str, Path]):
    with open(filepath) as file:
        data = json.load(file)
    return data

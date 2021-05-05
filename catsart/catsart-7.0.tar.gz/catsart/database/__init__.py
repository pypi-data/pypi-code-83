import json
import os
import random


def save(name, catsart):
    dir_ = os.path.dirname(__file__)
    path = os.path.join(dir_, name + '.json')

    with open(path, 'w') as f:
        json.dump(catsart, f, indent=0)


def get_random():
    catsart = _load_catsart()
    return random.choice(catsart)


def _load_catsart():
    dir_ = os.path.dirname(__file__)

    catsart = []

    for fn in os.listdir(dir_):
        _, ext = os.path.splitext(fn)
        if ext != '.json':
            continue

        with open(os.path.join(dir_, fn)) as f:
            catsart.extend(json.load(f))

    return catsart

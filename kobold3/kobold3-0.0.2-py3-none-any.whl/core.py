from shelve import DbfilenameShelf as db
from pathlib import Path
from fire import Fire
import warnings

warnings.filterwarnings("ignore")


KB_HOME = Path().home() / ".kobold"


def user_dot_default(name=None):
    path = KB_HOME
    if name != None:
        path = path / name
    path.mkdir(parents=True, exist_ok=True)
    return str(path)


def stores():
    path = KB_HOME
    return [x.name for x in path.glob("*")]


class Store:
    def __init__(self, filename, protocol=2, writeback=True):
        self.db = db(filename, protocol=protocol, writeback=writeback)

    def __setitem__(self, key, value):
        self.db[key] = value
        self.db.sync()

    def __getitem__(self, key, default=None):
        return self.db.get(key, default)

    def dict(self):
        return dict(self.db)

    def get(self, key):
        value = self[key]
        return value

    def set(self, **kwargs):
        for k, v in kwargs.items():
            self[k] = v

    def __delitem__(self, key):
        self.db.__delitem__(self, key)
        self.db.sync()

    @classmethod
    def from_ns(cls, name="default"):
        return cls(user_dot_default(name))


def kset(store, key, value, namespace=True):
    if namespace:
        o = Store.from_ns(store)
    else:
        o = Store(store)
    o[key] = value


def kget(store, key, default=None, namespace=True):
    if namespace:
        o = Store.from_ns(store)
    else:
        o = Store(store)
    return o.get(key, default)


cmds = {"store": Store.from_ns, "stores": stores, "set": kset, "get": kget}


def main():
    return Fire(cmds)


if __name__ == "__main__":
    main()

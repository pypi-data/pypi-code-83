# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

modules = \
['clattr']
install_requires = \
['attrs>=20.3.0,<21.0.0']

setup_kwargs = {
    'name': 'clattr',
    'version': '0.0.0',
    'description': 'Construct a comand line interface based on a function or class',
    'long_description': '# clattr\n\nSimple specification of a command line interface with an attrs class or a function. \n\nYou define the inputs to your program in the form of a (possibly nested) attrs class (dataclass). `clattr` will collect the fields of that class from command line arguments, environment variables and config files.\n\nIn the simplest form, let\'s consider a case where you are writing a program that wants two inputs of which one is optional\n\n```\nimport attr\nimport clattr\n\n\n@attr.s(auto_attribs=True, frozen=True)\nclass Basic:\n    a: int\n    b: str = "not provided"\n\ndef my_program(data: Basic):\n    # Your actual program will go here. For this example we just print the input.\n    print(data)\n\n\nif __name__ == "__main__":\n    data = clattr.build(Basic)\n    my_program(data)\n```\n\nThis could be invoked as\n```\npython examples/basic.py --a 1 --b hi\n```\nclattr will construct this object\n```\nBasic(a=1, b=\'hi\')\n```\nWhich you can then pass into the rest of your code as you please. The example simply prints it and then exits.\n\nOr if you have environment variables defined\n\n```\nexport A=1\nexport B=hi\npython example.py\n```\nagain yields\n```\nBasic(a=1, b=\'hi\')\n```\n\n`clattr` also supports nested objects\n\n```\nfrom typing import Optional\nimport datetime as dt\n\nimport attr\nimport clattr\n\n\n@attr.s(auto_attribs=True, frozen=True)\nclass Foo:\n    a: dt.datetime\n    b: Optional[str] = None\n\n\n@attr.s(auto_attribs=True, frozen=True)\nclass Bar:\n    f: Foo\n    c: int\n\ndef my_program(data: Bar):\n    print(data)\n\nif __name__ == "__main__":\n    bar = clattr.build(Bar)\n    my_program(bar)\n```\n\nYou specify values for the fields in the nested class by referring to them with a their field name in the outer class\n\n```\npython examples/advanced.py --c 1 --f.a 1 --f.b hi\n```\n```\nBar(f=Foo(a=1, b=\'hi\'), c=1)\n```\n\nYou can also supply `json` one or more formatted `config` files. Provide the name(s) of these files as positional arguments. datacli will search them, last file first, for any keys fields that are not provided at the command line before searching the environment.\n\n```\npython examples/advanced.py --c 1 examples/foo.json\n```\n```\nBar(f=Foo(a=1, b=\'str\'), c=1)\n```\n\nInspired by [clout](https://github.com/python-clout/clout). `clout` appeared somewhat abandoned at the time I started `clattr`, and I wanted to try some things with treating type annotations as first class information to reduce boilerplate.\n\n\n',
    'author': 'Tom Dimiduk',
    'author_email': 'tom@dimiduk.net',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=3.6',
}


setup(**setup_kwargs)

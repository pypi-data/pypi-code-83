# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['charmonium', 'charmonium.cache']

package_data = \
{'': ['*']}

install_requires = \
['attrs>=20.3.0,<21.0.0', 'bitmath>=1.3.3,<2.0.0', 'fasteners>=0.16,<0.17']

entry_points = \
{'console_scripts': ['cache = charmonium.cache._cli:main']}

setup_kwargs = {
    'name': 'charmonium.cache',
    'version': '1.0.0',
    'description': 'Provides a decorator for caching a function and an equivalent command-line util.',
    'long_description': '================\ncharmonium.cache\n================\n\nProvides a decorator for caching a function. Whenever the function is called\nwith the same arguments, the result is loaded from the cache instead of\ncomputed. If the arguments, source code, or enclosing environment have changed,\nthe cache recomputes the data transparently (no need for manual invalidation).\n\nThe use case is meant for iterative development, especially on scientific\nexperiments. Many times a developer will tweak some of the code but not\nall. Often, reusing prior intermediate computations saves a significant amount\nof time every run.\n\nQuickstart\n----------\n\nIf you don\'t have ``pip`` installed, see the `pip install\nguide`_. Then run:\n\n::\n\n    $ pip install charmonium.cache\n\n.. code:: python\n\n    >>> from charmonium.cache import memoize\n    >>> import shutil; shutil.rmtree(".cache")\n    >>> i = 0\n    >>> @memoize()\n    ... def square(x):\n    ...     print("recomputing")\n    ...     return x**2 + i\n    ...\n    >>> square(4)\n    recomputing\n    16\n    >>> square(4)\n    16\n    >>> i = 1\n    >>> square(4)\n    recomputing\n    17\n\nThe function must be pure with respect to its arguments and its `closure`_ (``i``\npart of the closure in the previous example). This library will not detect:\n\n- Reading **directly** from the filesystem (this library offers a wrapper over files\n  that permits it to detect changes; use that instead).\n\n- Non-static references (the caching library can\'t detect a dependency if the\n  function references ``globals()["i"]``).\n\nAdvantages\n----------\n\nWhile there are other libraries and techniques for memoization, I believe this\none is unique because it is:\n\n1. **Correct with respect to source-code changes:** The cache detects if you\n   edit the source code or change a file which the program reads (provided they\n   use this library\'s right file abstraction). Users never need to manually\n   invalidate the cache, so long as the functions are pure.\n\n2. **Useful between runs and across machines:** A cache can be shared on the\n   network, so that if *any* machine has computed the function for the same\n   source-source and arguments, this value can be reused by *any other* machine.\n\n3. **Easy to adopt:** Only requires adding one line (`decorator`_) to\n   the function definition.\n\n4. **Bounded in size:** The cache won\'t take up too much space. This\n   space is partitioned across all memoized functions according to the\n   heuristic.\n\n5. **Supports smart heuristics:** They can take into account time-to-recompute\n   and storage-size in addition to recency, unlike naive `LRU`_.\n\n6. **Overhead aware:** The library measures the time saved versus overhead. It\n   warns the user if the overhead of caching is not worth it.\n\nMemoize CLI\n-----------\n\n::\n\n   memoize -- command arg1 arg2 ...\n\n``memoize`` memoizes ``command arg1 arg2 ...``. If the command, its arguments,\n or its input files change, then ``command arg1 arg2 ...`` will be\n rerun. Otherwise, the output files (including stderr and stdout) will be\n produced from a prior run.\n\nMake is good, but it has a hard time with dependencies that are not files. Many\ndependencies are not well-contained in files. For example, you may want\nrecompute some command every time some status command returns a different\nvalue.\n\nTo get correct results you would have to incorporate *every* key you depend on\ninto the filename, which can be messy, so most people don\'t do that. ``memoize``\nis easier to use correctly, for example:\n\n::\n\n    # `make status=$(status)` will not do the right thing.\n    make var=1\n    make var=2 # usually, nothing recompiles here, contrary to user\'s intent\n\n    # `memoize --key=$(status) -- command args` will do the right thing\n    memoize --key=1 -- command args\n    memoize --key=2 -- command args # key changed, command is recomptued.\n\n``memoize`` also makes it easy to memoize commands within existing shell scripts.\n\nCode quality\n------------\n\n- The code base is strictly and statically typed with `pyright`_. I export type\n  annotations in accordance with `PEP 561`_; clients will benefit from the type\n  annotations in this library.\n\n- I have unittests with >95% coverage.\n\n- I use pylint with few disabled warnings.\n\n- All of the above methods are incorporated into per-commit continuous-testing\n  and required for merging with the ``main`` branch; This way they won\'t be\n  easily forgotten.\n\n..\n   - I\'ve implemented the complete feature-set in under 1,000 LoC. LoC\n\t count is an imperfect but reasonable metric of how hard something is\n\t to maintain and how likely it is to contain bugs according to\n\t [Zhang]_.\n\n.. _`PEP 561`: https://www.python.org/dev/peps/pep-0561/\n.. _`LRU`: https://en.wikipedia.org/wiki/Cache_replacement_policies#Least_recently_used_(LRU)\n.. _`closure`: https://en.wikipedia.org/wiki/Closure_(computer_programming)\n.. _`decorator`: https://en.wikipedia.org/wiki/Python_syntax_and_semantics#Decorators\n.. _`pip install guide`: https://pip.pypa.io/en/latest/installing/\n.. _`pyright`: https://github.com/microsoft/pyright\n',
    'author': 'Samuel Grayson',
    'author_email': 'sam+dev@samgrayson.me',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/charmoniumQ/charmonium.cache.git',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<3.10',
}


setup(**setup_kwargs)

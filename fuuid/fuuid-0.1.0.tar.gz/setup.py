# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fuuid']

package_data = \
{'': ['*']}

install_requires = \
['base58>=2.1.0,<3.0.0']

setup_kwargs = {
    'name': 'fuuid',
    'version': '0.1.0',
    'description': 'Functional UUIDs for Python.',
    'long_description': '# 🏷️ fuuid\n\nFUUID stands for Functional Universally Unique IDentifier. FUUIDs are compatible with regular UUIDs but are naturally ordered by generation time, collision-free and support succinct representations such as raw binary and base58-encoded strings.\n\nIn short, running FUUIDs through the UNIX sort command will result in a list ordered by generation time.\n\n# Installation\n\nYou can install this package using `pip` or build it from source using `poetry`:\n\n    # Using pip\n    pip install fuuid\n\n    # Using poetry\n    pip install poetry\n    poetry build\n\n# Snapshots\n\n```python\nfrom fuuid import fuuid, fuuid_ns, raw_fuuid, raw_fuuid_ns, b58_fuuid, b58_fuuid_ns, b64_fuuid, b64_fuuid_ns\n\nfuuid()\n# UUID(\'01324332-f66a-054a-76e4-fbdc7f772cd1\')\n\nfuuid_ns()\n# UUID(\'00474eaa-b5d8-3844-338c-e77ecd424b06\')\n\nraw_fuuid()\n# b\'\\x012C2\\xc5\\xfc\\x18\\xca\\x96N\\xe5_\\xaaU86\'\n\nraw_fuuid_ns()\n# b\'\\x00GN\\xaa\\xb5\\xd88D\\xfb\\xfe%\\xcf_\\x90\\xb8\\xa8\'\n\nb58_fuuid()\n# 9ZxgTVssa99BdQF3n5tSj\n\nb58_fuuid_ns()\n# 12zi36Vm1zaBQmpmpZ2xXk\n\nb64_fuuid()\n# ATJDMhbpQxNUfC7BL3F3kQ==\n\nb64_fuuid_ns()\n# AEdOqrXYOES+VjlfTHElKw==\n```\n\n# License\n```text\nBSD 3-Clause License\n\nCopyright (c) 2021, Phil Demetriou\nAll rights reserved.\n\nRedistribution and use in source and binary forms, with or without\nmodification, are permitted provided that the following conditions are met:\n\n* Redistributions of source code must retain the above copyright notice, this\n  list of conditions and the following disclaimer.\n\n* Redistributions in binary form must reproduce the above copyright notice,\n  this list of conditions and the following disclaimer in the documentation\n  and/or other materials provided with the distribution.\n\n* Neither the name of the copyright holder nor the names of its\n  contributors may be used to endorse or promote products derived from\n  this software without specific prior written permission.\n\nTHIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"\nAND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE\nIMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE\nDISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE\nFOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL\nDAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR\nSERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER\nCAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,\nOR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE\nOF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.\n```',
    'author': 'Phil Demetriou',
    'author_email': 'inbox@philonas.net',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/kpdemetriou/fuuid',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)

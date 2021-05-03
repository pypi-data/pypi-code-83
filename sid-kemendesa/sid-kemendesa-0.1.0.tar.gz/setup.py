# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sid_kemendesa']

package_data = \
{'': ['*']}

install_requires = \
['attrs>=20.3.0,<21.0.0',
 'beautifulsoup4>=4.9.3,<5.0.0',
 'cattrs>=1.6.0,<2.0.0',
 'requests>=2.25.1,<3.0.0']

setup_kwargs = {
    'name': 'sid-kemendesa',
    'version': '0.1.0',
    'description': 'Module python untuk mencari dan melihat data desa dari sid kemendesa.',
    'long_description': '# sid-kemendesa\n\n[![sid-kemendesa - PyPi](https://img.shields.io/pypi/v/sid-kemendesa)](https://pypi.org/project/sid-kemendesa/)\n[![Supported Python versions](https://img.shields.io/pypi/pyversions/sid-kemendesa)](https://pypi.org/project/sid-kemendesa/)\n[![LISENSI](https://img.shields.io/github/license/hexatester/sid-kemendesa)](https://github.com/hexatester/sid-kemendesa/blob/main/LISENSI)\n\nModule python untuk mencari dan melihat data desa dari sid kemendesa.\n\n## Install\n\nPastikan [python 3.7+](https://www.python.org/ftp/python/3.7.9/python-3.7.9-amd64.exe) terinstall, kemudian jalankan perintah di bawah dalam Command Prompt atau Powershell (di Windows + X):\n\n```bash\npip install --upgrade sid-kemendesa\n```\n\n## Penggunaan\n\nContoh penggunaan\n\n```python\nfrom sid_kemendesa import search\n\nnama_desa = "desaku"\nhasil_pencarian = search(nama_desa)\nfor desa in hasil_pencarian:\n    print(desa)\n```\n\n## Legal / Hukum\n\nKode ini sama sekali tidak berafiliasi dengan, diizinkan, dipelihara, disponsori atau didukung oleh [Kemendesa](https://kemendesa.go.id/) atau afiliasi atau anak organisasinya. Ini adalah perangkat lunak yang independen dan tidak resmi. _Gunakan dengan risiko Anda sendiri._\n',
    'author': 'hexatester',
    'author_email': 'hexatester@protonmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)

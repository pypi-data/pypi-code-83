# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['wyzecam', 'wyzecam.mock', 'wyzecam.tutk']

package_data = \
{'': ['*']}

install_requires = \
['pydantic>=1.8.1,<2.0.0', 'xxtea>=2.0.0.post0,<3.0.0']

extras_require = \
{':python_version < "3.8"': ['importlib_metadata>=1.6.0,<2.0.0']}

setup_kwargs = {
    'name': 'wyzecam',
    'version': '1.0.1',
    'description': 'Python package for communicating with wyze cameras over the local network',
    'long_description': '# wyzecam\n\n<div align="center">\n\n[![Build status](https://github.com/kroo/wyzecam/workflows/build/badge.svg?branch=master&event=push)](https://github.com/kroo/wyzecam/actions?query=workflow%3Abuild)\n[![Python Version](https://img.shields.io/pypi/pyversions/wyzecam.svg)](https://pypi.org/project/wyzecam/)\n[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/kroo/wyzecam/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)\n\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n[![Security: bandit](https://img.shields.io/badge/security-bandit-green.svg)](https://github.com/PyCQA/bandit)\n[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/kroo/wyzecam/blob/master/.pre-commit-config.yaml)\n[![Semantic Versions](https://img.shields.io/badge/%F0%9F%9A%80-semantic%20versions-informational.svg)](https://github.com/kroo/wyzecam/releases)\n[![License](https://img.shields.io/github/license/kroo/wyzecam)](https://github.com/kroo/wyzecam/blob/master/LICENSE)\n\nPython package for communicating with wyze cameras over the local network.\n</div>\n\n## Features\n\n- Send local commands (via `WyzeIOTC` class)\n- Support for all wyze camera types (including wyzecam v3!)\n- Uses the [tutk](https://github.com/nblavoie/wyzecam-api/tree/master/wyzecam-sdk) protocol for communicating over the\n  local network.\n\n## Usage\n\n```python\nimport wyzecam\nimport cv2\nimport os\n\npath_to_libiotc = "./libIOTCAPIs_ALL.dylib"  # see instructions\ncred = wyzecam.login(os.environ["WYZE_EMAIL"], os.environ["WYZE_PASSWORD"])\naccount = wyzecam.get_user_info(cred)\ncams = wyzecam.get_camera_list(cred)\n\ncam = cams[0]\n\nwith wyzecam.WyzeIOTC(path_to_libiotc) as wyze_iotc:\n  with wyze_iotc.connect_and_auth(account, cam) as sess:\n    session_info = sess.session_check()\n    print(f"{sess.state}, session_info = {session_info}")\n    for frame, frame_info, video_stats in sess.recv_video_frame_ndarray_with_stats():\n      cv2.imshow(\'Video Feed\', frame)\n      cv2.waitKey(1)\n      if cv2.waitKey(1) & 0xFF == ord(\'q\'):\n        break\n\n```\n\n## Installation\n\n```bash\npip install -U wyzecam\n```\n\nYou will then need a copy of the shared library `libIOTCAPIs_ALL`. You will need\nto [download this SDK](https://github.com/nblavoie/wyzecam-api/tree/master/wyzecam-sdk), unzip it, then convert the\nappropriate copy of the library to a shared library, and copy the resultant `.so` or `.dylib` file to somewhere\nconvenient.\n\n### On Mac:\n\n```shell\nunzip TUTK_IOTC_Platform_14W42P1.zip\ncd Lib/MAC/\ng++ -fpic -shared -Wl,-all_load libIOTCAPIs_ALL.a -o libIOTCAPIs_ALL.dylib\ncp libIOTCAPIs_ALL.dylib  zg\n```\n\n### On Linux:\n\n```bash\nunzip TUTK_IOTC_Platform_14W42P1.zip\ncd Lib/Linux/x64/\ng++ -fpic -shared -Wl,-whole-archive libAVAPIs.a libIOTCAPIs.a -o libIOTCAPIs_ALL.so\ncp libIOTCAPIs_ALL.so /usr/local/lib/\n```\n\nNote: you will need to pick the appropriate architecture.\n\n## 🛡 License\n\n[![License](https://img.shields.io/github/license/kroo/wyzecam)](https://github.com/kroo/wyzecam/blob/master/LICENSE)\n\nThis project is licensed under the terms of the `MIT` license.\nSee [LICENSE](https://github.com/kroo/wyzecam/blob/master/LICENSE) for more details.\n\n## 📃 Citation\n\n```\n@misc{wyzecam,\n  author = {kroo},\n  title = {Python package for communicating with wyze cameras over the local network},\n  year = {2021},\n  publisher = {GitHub},\n  journal = {GitHub repository},\n  howpublished = {\\url{https://github.com/kroo/wyzecam}}\n}\n```\n\n## Credits\n\nSpecial thanks to the work by folks at [nblavoie/wyzecam-api](https://github.com/nblavoie/wyzecam-api), without which\nthis project would have been much harder.\n',
    'author': 'kroo',
    'author_email': 'elliot@kroo.net',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/kroo/wyzecam',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)

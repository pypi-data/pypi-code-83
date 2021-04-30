# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['assumerole']

package_data = \
{'': ['*']}

install_requires = \
['boto3>=1.15.1']

entry_points = \
{'console_scripts': ['assume = assumerole.main:app']}

setup_kwargs = {
    'name': 'assumerole',
    'version': '0.6.1',
    'description': 'Python  utility that allows users to perform aws assume-role operation between different profiles',
    'long_description': '## assumerole\n\nThis python package was inspired by the GO implementation of [assume-role](https://github.com/remind101/assume-role).\nThis utility makes it easier to switch between multiple AWS profiles.\n\n\n### Pre-requisite\n- aws sdk should be installed\n- aws credentials are provided under ~/.aws/credentials\n- all the aws profiles are created correctly under ~/.aws/config\n\nThis utility uses sts utility within the [boto3 package](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sts.html).\nYou can learn more about sts command under [awscli](https://docs.aws.amazon.com/cli/latest/reference/sts/assume-role.html)\n\n\n### Installation:\n```pip install --index-url https://test.pypi.org/simple/  assumerole```\nFor updating existing package use\n```pip install -U --index-url https://test.pypi.org/simple/  assumerole```\n\n\n### Usage\n```assume --profile <aws-profile-name>```\nor\n```assume -p <aws-profile-name>```\n\nYou may be prompted to pass your MFA code if its required\n\nBy default, the tokens returned are cached under the folder ```~/.aws/cached_tokens```\nOnly if the token has expired, will new tokens be requested from AWS.\nYou can also find a history of all successful commands in the file ```~/.aws/assume_role_history```\n\nIn case you do not want to use your cached tokens use the optional refresh parameter\n\n```assume --profile <aws-profile-name> --refresh``` or\n```assume -p <aws-profile-name> -r```\n\n\nIn case you do not want to set the expirty time on the token optional duration parameter\nDefault is 8 hours and maximum value is 12 (set by AWS)\n\n```assume --profile <aws-profile-name> --duration 10``` or\n```assume -p <aws-profile-name> -d 10```\n\n\n### TODO:\n- Perform comprehensive coverage testing. Once package is tested fully, it will be made available in pypi.org\n- In the meantime, do test it out and feel free to submit PRs\n\n',
    'author': 'Kartik Ramasubramanian',
    'author_email': 'r.kartik@berkeley.edu',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/kartikra/assumerole',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6.1,<4.0',
}


setup(**setup_kwargs)

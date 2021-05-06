# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['vpic']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.25.1,<3.0.0']

setup_kwargs = {
    'name': 'vpic-api',
    'version': '0.1.1',
    'description': 'A client for the United States National Highway Traffic Safety Administration (NHTSA) Vehicle Product Information Catalog (vPIC) API',
    'long_description': "# vpic-api\nPython client library for decoding VINs and querying the United States \nNational Highway Traffic Safety Administration (NHTSA) [Vehicle Product \nInformation Catalog Vehicle Listing (vPIC) API](https://vpic.nhtsa.dot.gov/api/).\n\nUse this to gather information on vehicles and their specifications,\nand to decode VINs to extract information for specific vehicles. vPIC\nhas information about these types of vehicles sold or imported in\nthe USA:\n\n* Bus\n* Incomplete Vehicle\n* Low Speed Vehicle (LSV)\n* Motorcycle\n* Multipurpose Passenger Vehicle (MPV)\n* Passenger Car\n* Trailer\n* Truck\n\nvPIC has information about how manufacturers assign a VIN that\nencodes a vehicle's characteristics. Vehicle manufacturers provide this\ninformation to NHTSA under U.S. law 49 CFR Part 565.\n\nThe API available 24/7, is free to use, and does not require registration. NHTSA uses automatic traffic rate controls to maintain the performance of the API and their websites that use the API.\n\nSee https://vpic.nhtsa.dot.gov/api/home/index/faq for more on the API.\n\n",
    'author': 'David Peckham',
    'author_email': 'dave.peckham@icloud.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/davidpeckham/vpic-api',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)

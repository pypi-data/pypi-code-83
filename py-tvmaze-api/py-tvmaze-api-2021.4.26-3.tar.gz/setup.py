# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tvmaze']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.25.1,<3.0.0']

entry_points = \
{'poetry.application.plugin': ['plugin = '
                               'poetry_date_version_plugin.plugin:VersionPlugin']}

setup_kwargs = {
    'name': 'py-tvmaze-api',
    'version': '2021.4.26-3',
    'description': 'A Python client for the TvMaze API.',
    'long_description': '# python-tvmaze\n\nA library that provides a Python interface to [the TvMaze API](http://www.tvmaze.com/api).\n\n## Installation\n\nThe easiest way to install the latest version\nis by using pip/easy_install to pull it from PyPI:\n\n    pip install git+https://github.com/sickchill/python-tvmaze.git\n\nYou may also use Git to clone the repository from\nGithub and install it manually:\n\n    git clone https://github.com/sickchill/python-tvmaze.git\n    cd python-tvmaze\n    python setup.py install\n\nPython 2.7 and 3.6+, is supported for now.\n\n## Usage\n\n    from tvmaze.api import Api\n    api = Api()\n\n### Shows\n\n##### Show list\n\nA list of all shows, with all primary information included. \n\n    api.show.list()  # default page is 0\n    api.show.list(page=1)\n\n##### Show get\n\nRetrieve all primary information for a given show.\n\n    api.show.get(1)\n\n##### Show episode list\n\nA complete list of episodes for the given show.\n\n    api.show.episodes(1)\n\n##### Show episode by number\n\nRetrieve one specific episode from this show given its season number and episode number.\n\n    api.show.episode_by_number(1)\n\n##### Show episode by number\n\nRetrieve one specific episode from this show given its season number and episode number.\n\n    api.show.episode_by_number(1, season=1, number=1)\n\n##### Show episode by date\n\nRetrieve all episodes from this show that have aired on a specific date.\n\n    api.show.episodes_by_date(1, "2013-07-01")\n\n##### Show seasons\n\nA complete list of seasons for the given show.\n\n    api.show.seasons(1)\n\n##### Show cast\n\nA list of main cast for a show.\n\n    api.show.cast(1)\n\n##### Show crew\n\nA list of main crew for a show.\n\n    api.show.crew(1)\n\n##### Show AKA\'s\n\nA list of AKA\'s (aliases) for a show. \nAn AKA with its country set to null indicates an AKA in the show\'s original country.\n\n    api.show.akas(1)\n\n\n---\n\n\n### People\n\n##### Person get\n\nRetrieve all primary information for a given person.\n\n    api.people.get(1)\n\n##### Person cast credits\n\nRetrieve all (show-level) cast credits for a person.\n\n    api.people.cast_credits(1)\n\n##### Person crew credits\n\nRetrieve all (show-level) crew credits for a person.\n\n    api.people.crew_credits(100)\n\n\n---\n\n\n### Schedule\n\n##### Today schedule\n\nThe schedule is a complete list of episodes that air today.\n\n    api.schedule.today()\n\n##### Schedule by country and date\n\nThe schedule is a complete list of episodes that air in a given country on a given date.\n\n    api.schedule.filter(country_code="US", date="2014-12-01")\n\n##### Full schedule\n\nThe full schedule is a list of all future episodes known to TVmaze, regardless of their country.\n\n    api.schedule.full()\n\n\n---\n\n\n### Search\n\n##### Search show\n\nSearch through all the shows by the show\'s name.\n\n    api.search.shows("girls")\n\n##### Search single show\n\nSearch through all the shows by the show\'s name and the \nsingle search endpoint which either returns exactly one result, or no result at all.\n\n    api.search.single_show("girls")\n\n##### Lookup show\n\nIf you already know a show\'s tvrage, thetvdb or IMDB ID, \nyou can use this endpoint to find this exact show on TVmaze\n\n    api.search.lookup_show("tvrage", "24493")\n    api.search.lookup_show("thetvdb", "81189")\n    api.search.lookup_show("imdb", "tt0944947")\n\n##### Search people\n\nSearch through all the people by the name.\n\n    api.search.people("lauren")\n\n\n---\n\n\n### Character\n\n##### Character get\n\nRetrieve all primary information for a given character.\n\n    api.character.get(1)\n\n\n---\n\n\n### Episode\n\n##### Episode get\n\nRetrieve all primary information for a given episode.\n\n    api.episode.get(1)\n\n\n---\n\n\n### Network\n\n##### Network get\n\nRetrieve all primary information for a given network.\n\n    api.network.get(1)\n\n\n---\n\n\n### WebChannel\n\n##### Web Channel get\n\nRetrieve all primary information for a given web channel.\n\n    api.web_channel.get(1)\n',
    'author': 'Yakup Adaklı',
    'author_email': 'yakup.adakli@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/sickchill/python-tvmaze',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6',
}


setup(**setup_kwargs)

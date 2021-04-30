# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['notebooks',
 'notebooks.bin',
 'notebooks.co_occurrence',
 'notebooks.legacy',
 'notebooks.legacy.concept_co_occurrences',
 'notebooks.legacy.prepare_riksdagens_protokoll',
 'notebooks.legacy.scrachpads',
 'notebooks.legacy.tfidf_word_siginificance',
 'notebooks.legacy.word_trends',
 'notebooks.most_discriminating_words',
 'notebooks.named_entity_recognition',
 'notebooks.political_in_newspapers',
 'notebooks.political_in_newspapers.notebook_gui',
 'notebooks.political_in_newspapers.scripts',
 'notebooks.pos_statistics',
 'notebooks.statens_offentliga_utredningar',
 'notebooks.textblock_politiskt',
 'notebooks.word_distribution_trends',
 'notebooks.word_trends']

package_data = \
{'': ['*']}

install_requires = \
['bokeh',
 'click',
 'cython',
 'decorator',
 'gensim',
 'holoviews',
 'humlab-penelope>=0.4.1,<0.5.0',
 'ipycytoscape',
 'ipyfilechooser',
 'ipykernel',
 'ipympl',
 'ipywidgets',
 'jupyter-bokeh',
 'jupyterlab',
 'loguru>=0.5.3,<0.6.0',
 'markdown',
 'matplotlib',
 'more-itertools',
 'nltk',
 'numpy',
 'openpyxl',
 'pandas',
 'pandas-bokeh',
 'python-dotenv',
 'python-louvain',
 'scikit-learn',
 'scipy',
 'sklearn',
 'textacy==0.10.1',
 'tqdm',
 'traitlets==4.3.3',
 'xlrd']

setup_kwargs = {
    'name': 'humlab-westac',
    'version': '0.3.1',
    'description': 'Welfare State Analytics',
    'long_description': '# The Welfare State Analytics Text Analysis Repository\n\n## About the Project\n\nWelfare State Analytics. Text Mining and Modeling Swedish Politics, Media & Culture, 1945-1989 (WeStAc) is a digital humanities research project with five co-operatings partners: Umeå University, Uppsala University, Aalto University (Finland) and the National Library of Sweden.\n\nThe project will digitise literature, curate already digitised collections, and perform research via probabilistic methods and text mining models. WeStAc will both digitise and curate three massive textual datasets—in all, Big Data of almost four billion tokens—from the domains of Swedish politics, news media and literary culture during the second half of the 20th century.\n\n## Installation\n\n### Local install using pipenv\n\nSee [this page](https://github.com/humlab/welfare_state_analytics/wiki/How-to:-Install-notebooks-on-local-machine).\n\n### JupyterHub installation\n\nThe `westac_hub` repository contains a ready-to-use Docker setup (`Dockerfile` and `docker-compose.yml`) for a Jupyter Hub using `nginx` as reverse-proxy. The default setup uses `DockerSpawner` that spawns containers as specified in `westac_lab`, and Github for autorization (OAuth2). See the Makefile on how to build the project.\n\n### Single Docker container\n\nYou can also run the `westac_lab` container as a single Docker container if you have Docker installed on your computer.\n',
    'author': 'Roger Mähler',
    'author_email': 'roger.mahler@hotmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://westac.se',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '==3.8.5',
}


setup(**setup_kwargs)

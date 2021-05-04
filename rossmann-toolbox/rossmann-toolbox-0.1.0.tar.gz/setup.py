# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rossmann_toolbox', 'rossmann_toolbox.models', 'rossmann_toolbox.utils']

package_data = \
{'': ['*'],
 'rossmann_toolbox': ['weights/0.pt',
                      'weights/0.pt',
                      'weights/0.pt',
                      'weights/0.pt',
                      'weights/0.pt',
                      'weights/0.pt',
                      'weights/1.pt',
                      'weights/1.pt',
                      'weights/1.pt',
                      'weights/1.pt',
                      'weights/1.pt',
                      'weights/1.pt',
                      'weights/2.pt',
                      'weights/2.pt',
                      'weights/2.pt',
                      'weights/2.pt',
                      'weights/2.pt',
                      'weights/2.pt',
                      'weights/3.pt',
                      'weights/3.pt',
                      'weights/3.pt',
                      'weights/3.pt',
                      'weights/3.pt',
                      'weights/3.pt',
                      'weights/4.pt',
                      'weights/4.pt',
                      'weights/4.pt',
                      'weights/4.pt',
                      'weights/4.pt',
                      'weights/4.pt',
                      'weights/coredetector.pt',
                      'weights/coredetector.pt',
                      'weights/coredetector.pt',
                      'weights/coredetector.pt',
                      'weights/coredetector.pt',
                      'weights/coredetector.pt',
                      'weights/seqvec/uniref50_v2/options.json',
                      'weights/struct_ensemble/*'],
 'rossmann_toolbox.utils': ['hhdb/*']}

install_requires = \
['aiohttp>=3.7.4,<4.0.0',
 'atomium==1.0.9',
 'biopython==1.78',
 'captum==0.3.1',
 'conditional>=1.3,<2.0',
 'csb>=1.2.5,<2.0.0',
 'dgl==0.6.1',
 'overrides>=3.0,<4.0',
 'pandas==1.1.5',
 'seqvec==0.4.1']

setup_kwargs = {
    'name': 'rossmann-toolbox',
    'version': '0.1.0',
    'description': 'Prediction and re-engineering of the cofactor specificity of Rossmann-fold proteins',
    'long_description': "![logo](https://github.com/labstructbioinf/rossmann-toolbox/blob/main/logo.png?raw=true)\n\n![python-ver](https://img.shields.io/badge/python-%3E=3.6.1-blue)\n[![codecov](https://codecov.io/gh/labstructbioinf/rossmann-toolbox/branch/main/graph/badge.svg)](https://codecov.io/gh/labstructbioinf/rossmann-toolbox)\n\n<b> Prediction and re-engineering of the cofactor specificity of Rossmann-fold proteins</b>\n\n### Installation\n\n```\npip install rossmann-toolbox\n```\n\nAlternatively, to get the most recent changes, install directly from the repository:\n```\npip install git+https://github.com/labstructbioinf/rossmann-toolbox.git\n```\n\n#### For some of the features additional dependencies are required:\n| Package                                       | Sequence variant | Structure variant |\n|-----------------------------------------------|:----------------:|:-----------------:|\n|[**FoldX4**](http://foldxsuite.crg.eu/)        | -                | **required**      |\n|[**DSSP3**](https://github.com/cmbi/dssp)      | -                | **required**      |\n|[**HH-suite3**](https://github.com/soedinglab/hh-suite) | optional| optional          |\n\n### Getting started\n\n#### Sequence-based approach\nThe input is a full-length sequence. The algorithm first detects <b>Rossmann cores</b> (i.e. the β-α-β motifs that interact with the cofactor) in the sequence and later evaluates their cofactor specificity:\n```python\nfrom rossmann_toolbox import RossmannToolbox\nrtb = RossmannToolbox(use_gpu=True)\n\ndata = {'3m6i_A': 'MASSASKTNIGVFTNPQHDLWISEASPSLESVQKGEELKEGEVTVAVRSTGICGSDVHFWKHGCIGPMIVECDHVLGHESAGEVIAVHPSVKSIKVGDRVAIEPQVICNACEPCLTGRYNGCERVDFLSTPPVPGLLRRYVNHPAVWCHKIGNMSYENGAMLEPLSVALAGLQRAGVRLGDPVLICGAGPIGLITMLCAKAAGACPLVITDIDEGRLKFAKEICPEVVTHKVERLSAEESAKKIVESFGGIEPAVALECTGVESSIAAAIWAVKFGGKVFVIGVGKNEIQIPFMRASVREVDLQFQYRYCNTWPRAIRLVENGLVDLTRLVTHRFPLEDALKAFETASDPKTGAIKVQIQSLE'}\n\npreds = rtb.predict(data, mode='seq')\npreds = {'3m6i_A': {'FAD': 0.0008955444,\n                    'NAD': 0.998446,\n                    'NADP': 0.00015508455,\n                    'SAM': 0.0002544397, ...}}\n```\n\n#### Structure-based approach\nThe input is a protein structure. Preparation steps are the same as above, but additionally, structural features are calculated via **FOLDX** software, and secondary structure features via **DSSP**\n```python\n# required binaries\nPATH_FOLDX = ...\nPATH_HHPRED = ...\nPATH_DSSP = ...\n\npath_to_structures = ...  # path to pdb files\nchains_to_use = ... # chains to load from `path_to_structures`\nrtb = RossmannToolbox(use_gpu=False, foldx_loc = PATH_FOLDX, \n                                     hhsearch_loc = PATH_HHPRED,\n                                     dssp_loc = PATH_DSSP)\n\npreds = rtb.predict_structure(path_to_structures, chains_to_use, mode='seq', core_detect_mode='dl')\npreds = [{'NAD': 0.99977881,\n  'NADP': 0.0018195,\n  'SAM': 0.00341983,\n  'FAD': 3.62e-05,\n  'seq': 'AGVRLGDPVLICGAGPIGLITMLCAKAAGACPLVITDIDEGRL',\n  'NAD_std': 0.0003879,\n  'NADP_std': 0.00213571,\n  'SAM_std': 0.00411747,\n  'FAD_std': 3.95e-05}]\n```\n\n\n#### What next?\nTo learn about other features of the `rossmann-toolbox`, such as <b>visualization of the results</b>, please refer to the notebook `examples/example_minimal.ipynb`. \n\n### Contact\nIf you have any questions, problems or suggestions, please contact us.  The `rossmann-toolbox` was developed by Kamil Kaminski, Jan Ludwiczak, Maciej Jasinski, Adriana Bukala, \nRafal Madaj, Krzysztof Szczepaniak, and Stanislaw Dunin-Horkawicz.\n\nThis work was supported by the First TEAM program of the Foundation for Polish Science co-financed by the European Union under the European Regional Development Fund.\n",
    'author': 'Kamil Kaminski',
    'author_email': 'k.kaminski@cent.uw.edu.pl',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/labstructbioinf/rossmann-toolbox',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.1,<4.0.0',
}


setup(**setup_kwargs)

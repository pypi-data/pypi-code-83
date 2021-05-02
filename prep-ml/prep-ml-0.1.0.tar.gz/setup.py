# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['prep_ml']

package_data = \
{'': ['*']}

install_requires = \
['category-encoders>=2.2.2,<3.0.0',
 'pandas>=1.2.4,<2.0.0',
 'scikit-learn>=0.24.2,<0.25.0']

setup_kwargs = {
    'name': 'prep-ml',
    'version': '0.1.0',
    'description': 'Preprocessing for ML models made easy.',
    'long_description': '<h1 align="center">Prep-ML</h1>\n\n## What is Prep-ML?\nprep-ml is an open-source pre-processing library aimed at simplifying the data processing steps and streamlining the transformation techniques before feeding it to your choice of machine learning algorithm.\n\n<br>\n\n## Why Prep-ML?\nProduction grade machine learning is quite different from the standard notebook building. Notebook building is aimed at fast development, interactive code, and visual feedback system. While the scripts aim to cater models to large groups of audience or companies.\n\nFor eg, consider one of the key features of your model is DATE_OF_BIRTH, in real-time, due to various database schemas, the feature could be available in any of its synonyms (say, DOB, BIRTH_DATE). This is where prep-ml tries to fill in, like a heavily inspired from ETL tools and other design patterns.\n\n<br>\n\n## Installation\n\n``` $ pip install prep-ml```\n\n<br>\n\n## Documentation\n\nThis is the schema currently supported by the library. This can take python dict or JSON string.\n```\n{\n    "FEATURE_NAME": {\n        "required": bool,\n        "encoding": str,\n        "alias": str,\n        "imputation": str,\n        "derived_eq": str\n    }\n}\n```\n### Schema Definitions:\n\n#### required: bool\n\n> accepted values: **True**, **False**\n\ndetermines if the feature is required for the model. \n- If **required** is set to **False**, the **FEATURE_NAME** is discarded for further processing.\n\n#### encoding: str\n\n> accepted values: **label**, **ohe**\n\nperforms the given encoding strategy on the **FEATURE_NAME**. \n\n- If **encoding** is set to "**label**", LabelEncoding or OrdinalEncoding is performed on the **FEATURE_NAME**\n- If **encoding** is set to "**ohe**", OneHotEncoding is performed on the **FEATURE_NAME**\n\n\n#### alias: str\n\n> accepted values: any string\n\nthis is a synonym or alias for the given **FEATURE_NAME**. \n\n- For eg, If **alias** is set to **"FEATURE_OTHER_NAME"**, the alias name will be mapped to the **FEATURE_NAME**\n\n\n#### imputation: str\n\n> accepted values: **mean**, **median**, **most_frequent**\n\nperforms the given imputation strategy on the **FEATURE_NAME**. This is a wrapper of SimpleImputer. \n\n- If "**mean**", then replace missing values using the mean for the **FEATURE_NAME**. Can only be used with numeric data.\n- If "**median**", then replace missing values using the median for the **FEATURE_NAME**. Can only be used with numeric data.\n- If "**most_frequent**", then replace missing using the most frequent value for the **FEATURE_NAME**. Can be used with strings or numeric data. If there is more than one such value, only the smallest is returned.\n\n\n#### derived_eq: str\n\n> accepted values: eval equation as a string\n\nevaluated the given equation and then assigns the response to **FEATURE_NAME**. The reference to dataframe should be **df**\n\n- For eg consider the above feature *DOB*, If **derived_eq** is set to "**pd.to_datetime(df.DOB, format=\'%m/%d/%Y\')**", the expression will be evaluated and assigned to **FEATURE_NAME**. Note that, **df** is reference to the provided input df.\n\n\n### Usage Example:\nThis is the input data \n\n![input_data](https://github.com/vi3m/vi3m_image_host/blob/master/prep-ml/readme_input.png?raw=true)\n\n#### Data Explanation:\n\nThis is randomly generated data for the purposes of demo. All references are assumptions.\n\nThis is a company employee data. We have various features, which are self explanatory.\n\nIdeally, we would want to remove the NAMES, as they are uniques and serve no purpose in model. Transform DOB to say a derived feature called AGE. Encode, GENDER, DESIGNATION and PROMOTED. Impute RATING.\n\nSo, on using the driver code.\n\n```\nfrom prep_ml.pre_processor import Prep\nimport pandas as pd\n\n# Reading the csv data.\ndf = pd.read_csv(\'MOCK_DATA.csv\')\n\n\np = Prep.from_dict(prep_ob, df)\nresult_df = p.get_data()\n\n```\n\n<br>\n\n## Future Development Roadmap\n- Performance improvements.\n- Add support for more imputation and encoding strategies.\n- Support for feature scaling.\n- Support for multiple schemas.\n- Support for multiple input sources.\n- Support for enforcing column types.\n- Feasibility for model training.\n\n<br>\n\n## Changelog\n\n2nd May, 2021 :: v0.1.0:\n- This is a very early dev version. This further needs development and code optimization.',
    'author': 'vijaymlv',
    'author_email': 'dev.vijaymlv@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.1',
}


setup(**setup_kwargs)

# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cclm', 'cclm.augmentation', 'cclm.pretrainers']

package_data = \
{'': ['*']}

install_requires = \
['datasets>=1.1.3,<2.0.0',
 'mlflow>=1.16.0,<2.0.0',
 'tensorflow>=2.0.0,<3.0.0',
 'tokenizers>=0.10.0,<0.11.0',
 'tqdm>=4.0.0,<5.0.0']

setup_kwargs = {
    'name': 'cclm',
    'version': '0.1.1',
    'description': 'NLP framework for composing together models modularly',
    'long_description': '## CCLM\n\n### Composable, Character-Level Models\n\n#### What are the goals of the project?\n\n1) Modularity: Fine-tuning large language models is expensive. `cclm` seeks to decompose models into subcomponents that can be readily mixed and matched, allowing for a wider variety of sizes, architectures, and pretraining methods. Rather than fine-tuning a huge model on your own data, fit a smaller one on your dataset and combine it with off-the-shelf models.\n\n2) Character-level input: Many corpora used in pretraining are clean and typo-free, but a lot of input in real world applications aren\'t - leaving you at a disadvantage if your tokenization scheme isn\'t flexible enough. Using characters as input also makes it simple define many \'heads\' of a model with the same input space.\n\n3) Ease of use: It should be quick to get started and easy to deploy. \n\n\n#### How does it work?\n\nThe way `cclm` aims to achieve the above is by making the model building process composable. There are many ways to pretrain a model on text, and infinite corpora on which to train, and each application has different needs.\n\n`cclm` makes it possible to define a `base` input on which to build many different computational graphs, then combine them. For instance, if there is a standard, published `cclm` model trained with masked language modeling (MLM) on (`wikitext` + `bookcorpus`), you might start with that, but add a second \'tower\' to that model that uses the same `base`, but is pretrained to extract entities from `wiki-ner`. By combining the two pretrained \'towers\', you get a model with information from both tasks that you can then use as a starting point for your downstream model.\n\nAs the package matures, the goal is to make available many pretraining methods (starting with Masked Language Modeling) and to publish standard pretrained models (like huggingface/transformers, spacy, tensorflowhub, ...).\n\n\n#### Basic concepts\n\nThe main output of a training job with `cclm` is a `ComposedModel`, which consists of a preprocessor that turns text into a vector[int], a base model that embeds that vector input, and one or more models that accept the output of the embedder. The `ComposedModel` concatenates the output from those models together to produce its final output.\n\nThe package uses `datasets` and `tokenizers` from `huggingface` for a standard interface - but to fit models, you can pass a `List[str]` directly.\n\nTo start, you need a `Preprocessor`. Currently, there is only an `MLMPreprocessor` that computes extra data at training time for its pretraining task, but that is subject to change.\n\n```\nfrom cclm.preprocessing import MLMPreprocessor\n\nprep = MLMPreprocessor()  # set max_example_len to specify a maximum input length\nprep.fit(dataset) # defines the characters the model knows about and the output tokens for MLM\n```\n\nOnce you have that, you can create a `CCLMModelBase`, which is the common base on which all the separate models will sit.\n\n```\nfrom cclm.models import CCLMModelBase\n\nbase = CCLMModelBase(preprocessor=prep)\n```\n\nThe base doesn\'t need to be fit, as you can fit it while you do your first pretraining task.\n\nNow you\'re ready to build your first model using a pretraining task (here masked language modeling)\n\n```\nfrom cclm.pretraining import MaskedLanguagePretrainer\n\npretrainer = MaskedLanguagePretrainer(\n    base=base,\n    downsample_factor=16,  # how much we want to reduce the length of the input sequence\n    n_strided_convs=4,  # how many strided conv layers we have. stride_len**n_strided_convs must == downsample_factor\n)\n\npretrainer.fit(dataset, epochs=10)\n```\n\nThe `MaskedLanguagePretrainer` defines a transformer model (which uses strided convolutions to reduce the size before the transformer layer, then upsamples to match the original size), and calling `.fit()` will use the `MLMPreprocessor` associated with the `base` to produce masked inputs and try to identify the missing input token(s) using `sampled_softmax` loss or negative sampling.\n\nOnce you\'ve trained one or more models with `Pretrainer` objects, you can compose them together into one model.\n\n```\ncomposed = ComposedModel(base, [pretrainer_a.model, pretrainer_b.model])\n```\n\nYou can then use `composed.model(x)` to embed input\n\n```\nx = prep.string_to_array("cclm SURE is useful!!", prep.max_example_len)\nemb = composed.model(x)   # has shape (1, prep.max_example_len, pretrainer_a_model_shape[-1]+pretrainer_b_model_shape[-1])\n```\n\n... or create a new model with something like\n\n```\n# pool the output across the character dimension\ngmp = tf.keras.layers.GlobalMaxPool1D()\n# add a classification head on top\nd = tf.keras.layers.Dense(1, activation="sigmoid")\nkeras_model = tf.keras.Model(composed.model.input, d(gmp(composed.model.output)))\n```',
    'author': 'jamesmf',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/jamesmf/cclm',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)

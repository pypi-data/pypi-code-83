from setuptools import setup, find_packages

with open("README.md", mode="r", encoding="utf-8") as readme_file:
    readme = readme_file.read()



setup(
    name="steadynlp",
    version="0.0.2",
    author="Teo Jao Ming",
    author_email="jaomingteo@gmail.com",
    description="A collection of simple NLP focused functions to support your main projects",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/jaotheboss/Hermione",
    project_urls = {
        "Bug Tracker": "https://github.com/jaotheboss/Hermione/issues"
    },
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.8",
    include_package_data=True,
    package_data={'': ['resources/*.txt']},
    install_requires=[
        'spacy',
        'networkx',
        'sentence-transformers',
        'scikit-learn',
        'pandas',
        'numpy',
        'nltk',
        'flask'
    ],
    dependency_links=[
        'en_core_web_sm @ https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.0.0/en_core_web_sm-3.0.0.tar.gz',
    ]  
)
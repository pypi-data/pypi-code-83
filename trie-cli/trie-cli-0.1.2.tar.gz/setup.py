from setuptools import setup, find_packages

def read_requirements():
    with open("cli_requirements.txt") as req:
        content = req.read()
        requirements = content.split("\n")
    return requirements

with open("README.md", "r", encoding="utf-8") as file:
    long_desc = file.read()

setup(
    name='trie-cli',
    version='0.1.2',
    author = 'Pranav Mathur',
    author_email = 'pranavmathur001@gmail.com',
    description = 'A CLI to interact with a global trie data structure.',
    long_description=long_desc,
    long_description_content_type='text/markdown',
    url='https://github.com/pmathur007/trie-cli',
    packages=find_packages(),
    include_package_data=True,
    install_requires=read_requirements(),
    entry_points = {
        'console_scripts': [
            'trie-cli=triecli.cli:main'
        ]
    }
)
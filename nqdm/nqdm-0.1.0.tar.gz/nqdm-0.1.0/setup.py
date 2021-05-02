from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

setup_args = dict(
    name='nqdm',
    version='0.1.0',
    description='Multiple iteration in single progress bar',
    long_description_content_type="text/markdown",
    long_description=README,
    license='MIT',
    packages=find_packages(),
    author='Yamac Eren Ay',
    author_email='yamacerenay2001@gmail.com',
    keywords=['nqdm', 'NQDM', 'progress bar', "tqdm"],
    url='https://github.com/yamaceay/nqdm',
    download_url='https://pypi.org/project/nqdm/'
)

install_requires = [
    "numpy",
    "tqdm",
    "pandas"
]

setup(
    include_package_data=True,
    setup_requires=['wheel'],
    name="nqdm",
    version="0.1.0"
)

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)
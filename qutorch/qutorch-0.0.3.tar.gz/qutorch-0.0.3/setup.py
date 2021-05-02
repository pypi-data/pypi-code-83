from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

with open('HISTORY.md') as history_file:
    HISTORY = history_file.read()

setup_args = dict(
    name='qutorch',
    version='0.0.3',
    description='Quantum circuit simulator based in PyTorch.',
    long_description_content_type="text/markdown",
    long_description=README + '\n\n' + HISTORY,
    license='MIT',
    packages=find_packages(),
    author='Mario Duran-Vega',
    author_email='mario.duran.vega@gmail.com',
    keywords=['PyTorch', 'Quantum', 'Circuit', 'Simulator', 'Python 3'],
    url='https://github.com/MarioDuran/qutorch',
    download_url='https://pypi.org/project/elastictools/'
)

install_requires = [
    'torch>=1.8.1',
    'numpy>=1.19.5'
]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)
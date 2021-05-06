from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()
#
with open('LICENSE.md') as f:
    license = f.read()

setup(
    name='draw-hypertrie',
    version='0.1.1',
    description="A tool to print hypertrie.",
    author='Alexander Bigerl',
    author_email='info@dice-research.org',
    url='https://github.com/dice-group/print_hypertrie',
    license="AGPL v3",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)", ],
    install_requires=[
        "Cython>=0.29.23",
        "pycairo>=1.20.0",
        "click>=7.1.2",
    ],
    python_requires='>=3.8',
    entry_points='''
        [console_scripts]
        draw_hypertrie2=hypertrie.draw_hypertrie2.run:cli
    ''',
    long_description=readme,
    long_description_content_type="text/markdown",
)

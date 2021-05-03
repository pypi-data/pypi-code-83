import setuptools

setuptools.setup(
    name = 'propshot-bot',
    version = '0.0.1',
    author = 'Kyle Tibbetts',
    author_email = 'fuzzylemma@gmail.com',
    description = 'a discord plugin for snapshot proposal alerts',
    url = 'https://gitlab.com/fuzzylemma/pgps',
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True
)

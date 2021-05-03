from setuptools import setup, find_packages

_packages = find_packages(where='src')
_packages.append('labascraper\\models')
_packages.append('labascraper\\scraper')

setup(
    name='labascraper',  
    version='2.0.0',  
    description='Labascraper is a package for investing.com comment scraping',  
    author='Kazım Anıl Aydın', 
    keywords='scraper, investing.com, comments',
    package_dir={'': 'src'},  
    packages= _packages, 
    python_requires='>=3.6, <4',
    install_requires=[
        'requests >= 2.23.0',
        'beautifulsoup4 >= 4.8.2'
    ],  
)

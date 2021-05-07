from setuptools import setup, find_packages

version = '2.0.0'

setup(
    name='plone.recipe.haproxy',
    version=version,
    description="Buildout recipe to install haproxy",
    long_description=(
        open('README.rst').read() + '\n' +
        open('CONTRIBUTORS.txt').read() + '\n' +
        open('CHANGES.txt').read()),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        'Framework :: Buildout',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3',
        "Programming Language :: Python :: 3 :: Only",
    ],
    keywords='buildout haproxy proxy loadbalancer',
    author='Helge Tesdal',
    author_email='tesdal@jarn.com',
    url='https://pypi.org/project/plone.recipe.haproxy',
    project_urls={"Source Code": "https://github.com/plone/plone.recipe.haproxy"},
    license='ZPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['plone', 'plone.recipe'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'zc.buildout'
    ],
    entry_points={
        "zc.buildout": ["default = plone.recipe.haproxy:Recipe"],
    },
    )

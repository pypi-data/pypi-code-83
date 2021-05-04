#!/usr/bin/env python
# coding=utf-8
from setuptools import setup, find_packages
from reportWaysonQi import HTMLTestRunner
# python setup.py sdist
# python setup.py bdist
# python setup.py bdist_egg
# python setup.py bdist_wheel
# twine upload dist/*0.1.4*
setup(
    name="reportWaysonQi",
    version='1.0.2',
    keywords=("test report", "python unit testing"),
    url="",
    author="",
    author_email="",
    package_dir={'reportWaysonQi': 'reportWaysonQi'},
    packages=['reportWaysonQi'],
    include_package_data=True,
    package_data={'reportWaysonQQQ': ['static/*', 'templates/*']},
    py_modules=[],
    data_files=[
        'reportWaysonQi/static/js/capture.js',
        'reportWaysonQi/templates/default.html',
        'reportWaysonQi/static/css/default.css',
        'reportWaysonQi/static/js/default.js',
        'reportWaysonQi/templates/legency.html',
        'reportWaysonQi/static/css/legency.css',
        'reportWaysonQi/static/js/legency.js'
    ],
    platforms="any",
    install_requires=[
        'Jinja2==2.10',
        'Flask==1.0.2'
    ],
    scripts=[],
    entry_points={
        'console_scripts': [
            'reportWaysonQi.shell = reportWaysonQi:shell',
            'reportWaysonQi.web = reportWaysonQi:web'
        ], "pytest11": ["reportWaysonQi = reportWaysonQi.PyTestReportPlug"]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Framework :: Pytest"
    ],
    zip_safe=False
)

import os.path

from setuptools import setup


def readme():
    try:
        with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as f:
            return f.read()
    except (IOError, OSError):
        pass


setup(
    name='flake8-import-order-tridge',
    version='1.0.1',
    description="Tridge's import order style for flake8-import-order",
    long_description=readme(),
    url='https://github.com/OdysseyJ/flake8-import-order-spoqa',
    author='seongwoon.jeong',
    author_email='seongwoon.jeong' '@' 'tridge.com',
    maintainer='Tridge',
    maintainer_email='seongwoon.jeong' '@' 'tridge.com',
    license='GPLv3 or later',
    py_modules=['flake8_import_order_Tridge'],
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
    install_requires=['flake8-import-order >= 0.18, < 0.19'],
    entry_points='''
        [flake8_import_order.styles]
        tridge = flake8_import_order_tridge:Tridge
    ''',
    test_suite='flake8_import_order_tridge.TestCase',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Flake8',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',  # noqa
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Quality Assurance',
    ]
)

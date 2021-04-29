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
    version='1.0.5',
    description="Tridge's import order style for flake8-import-order",
    long_description=readme(),
    author='seongwoon.jeong',
    author_email='seongwoon.jeong' '@' 'tridge.com',
    maintainer='Tridge',
    maintainer_email='seongwoon.jeong' '@' 'tridge.com',
    license='GPLv3 or later',
    py_modules=['flake8_import_order_tridge'],
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
    install_requires=['flake8-import-order >= 0.18, < 0.19'],
    entry_points='''
        [flake8_import_order.styles]
        tridge = flake8_import_order_tridge:Tridge
    ''',
    test_suite='flake8_import_order_tridge.TestCase',
)

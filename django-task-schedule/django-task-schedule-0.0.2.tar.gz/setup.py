from setuptools import setup, find_packages

version = __import__('task_schedule').__version__

setup(
    name='django-task-schedule',
    version=version,
    description='Task schedule grid app for Django',
    license="MIT",
    author='Mikhail Gavrin',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django>=2.2',
        'djangorestframework>=3.10',
    ],
    classifiers=[
        'Framework :: Django',
    ]
)

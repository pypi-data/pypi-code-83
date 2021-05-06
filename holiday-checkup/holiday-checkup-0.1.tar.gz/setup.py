from setuptools import setup


setup(
    name='holiday-checkup',
    version='0.1',
    url='https://github.com/khalooei/holiday-checkup',
    license='MIT',
    description='A python library for checking and detecting the holiday status of the Gregorian date in solar Hijri and lunar Hijri calendar ',
    author='Mohammad Khalooei',
    packages=['SalavatiHolidayCheckup'],
    install_requires=[
          'jdatetime',
          'hijri_converter',
      ],
    project_urls={
        'Changelog': ('https://github.com/khalooei/holiday-checkup/README.md'),
        'Docs': 'https://github.com/khalooei/holiday-checkup/README.md',
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    
)
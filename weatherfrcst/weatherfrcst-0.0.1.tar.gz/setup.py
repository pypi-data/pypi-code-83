from setuptools import setup

setup(name='weatherfrcst',
      version='0.0.1',
      description='Location based weather forecast package',
      long_description= 'The pip package provides weather forecasting information based on location or address. Using address, the w-forecast provides location specific forecast. Currently only one function is included i.e forecast.',
      url='https://github.com/RishiKr3101/weather-forecast.git',
      author='Rishi',
      author_email='rishikrofficial@gmail.com',
      license="MIT",
      packages=['weatherfrcst'],
      install_requires=[
          'geopy',
      ],
      zip_safe=False)
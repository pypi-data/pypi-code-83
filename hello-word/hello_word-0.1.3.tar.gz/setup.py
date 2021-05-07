from setuptools import setup

setup(name='hello_word',
      version='0.1.3',
      description='Hello Word Project',
      url='https://gitlab.com/arcesium/private/users/guptmani/hello_word',
      author='guptmani',
      author_email='guptmani@arcesium.com',
      license='MIT',
      packages=['hello_word'],
      install_requires=[
          'dnspython',
	      'sockets',
      ],
      zip_safe=False)

from distutils.core import setup

# try:
#     import pypandoc
#     long_description = pypandoc.convert('README.md', 'rst')
# except(IOError, ImportError):
#     long_description = open('README.md').read()

setup(
  name = 'ggwp',
  packages = ['ggwp'],
  version = '0.0.10',
  license='MIT',
  description = 'Prepare Fast, Analyze Faster',
  # long_description = long_description,
  author = 'pathompol',
  author_email = 'data.noob.lol@gmail.com',
  url = 'https://github.com/datanooblol/ggwp',
  # check url everytime you release new version
  download_url = 'https://github.com/datanooblol/ggwp/archive/refs/tags/0.0.10.tar.gz',
  keywords = ['ez','rfm','prep', 'data model', 'cohort', 'customer'],
  # dependencies used in your library
  install_requires=[
          'numpy',
          'pandas',
      ],
  classifiers=[  # Optional
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 4 - Beta',

    # Indicate who your project is intended for
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',

    # Pick your license as you wish
    'License :: OSI Approved :: MIT License',

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7'
  ],
)
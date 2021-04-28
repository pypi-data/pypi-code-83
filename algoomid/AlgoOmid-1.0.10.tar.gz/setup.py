from distutils.core import setup
setup(
  name = 'AlgoOmid',         # How you named your package folder (MyLib)
  packages = ['AlgoOmid'],   # Chose the same as "name"
  version = '1.0.10',      # Start with a small number and increase it with every change you make
  license='OmidAnalyzer',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'A few Classes and Functions for Algorithmic Trading++',   # Give a short description about your library
  author = 'Behzad Azadie faraz',                   # Type in your name
  author_email = 'b.azadi@webmail.omid.ir',      # Type in your E-Mail
  url = 'https://github.com/behzadazadie/OmidAlgo',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/behzadazadie/AlgoOmid/archive/refs/tags/v1.0.10.tar.gz',    # I explain this later on
  keywords = ['Algorithmic Trading', 'Finance', 'Trading'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'pandas',
	'numpy',
	'statistics',
	'datetime',
	'requests',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)
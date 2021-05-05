from distutils.core import setup
setup(
  name = 'ext-var',         # How you named your package folder (MyLib)
  packages = ['ext-var'],   # Chose the same as "name"
  version = '1.0',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'External Variables in Python.',   # Give a short description about your library
  author = 'Cube.py',                   # Type in your name
  author_email = 'kisto1981.2010@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/SoilFoil64/ext-var',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/SoilFoil64/ext-var/archive/refs/tags/v1.0.tar.gz',    # I explain this later on
  keywords = ['variables', 'files'],   # Keywords that define your package best
  install_requires=[  ],
  classifiers=[
    'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.9'])

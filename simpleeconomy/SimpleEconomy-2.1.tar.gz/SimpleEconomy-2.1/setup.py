from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='SimpleEconomy',
  version='2.1',
  description='Very easy to use discord.py economy creator',
  long_description="SimpleEconomy is made for using it as a db and getting stats from your bot. Read our docs at https://docs.simpleco.xyz\nDiscord support server: https://discord.gg/ptC9CaQFRe" + '\n\n' + "Change Log\n===========\n\n2.1 (30/04/2021)\n------------------\n- Command tracking\n- Command usage on dashboard",
  url='',  
  author='MrStretch',
  author_email='mrstretchd@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='Ecomomy, Simple, discord.py, command tracking,tracking,usage,stats', 
  packages=find_packages(),
  install_requires=['discord.py']
)

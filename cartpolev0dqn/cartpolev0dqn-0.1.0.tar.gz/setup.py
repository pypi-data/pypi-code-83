import setuptools

with open("README.md", "r") as fh:
  long_description = fh.read()

setuptools.setup(
  name="cartpolev0dqn",
  version="0.1.0",
  author="Jiangbei Li",
  author_email="lijiangbei@4paradigm.com",
  description="A package for CartPole V0 problem using dqn",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/AimAlex/CartPoleV0-dqn.git",
  packages=setuptools.find_packages(),
  install_requires=[
        'tensorflow==0.12.0',
        'gym==0.8.0',
        'pyglet==1.2.0',
        'matplotlib',
        'pyvirtualdisplay==1.3.2'
  ],
  classifiers=[
  "Programming Language :: Python :: 2.7",
  "License :: OSI Approved :: MIT License",
  "Operating System :: POSIX :: Linux",
  ],
)
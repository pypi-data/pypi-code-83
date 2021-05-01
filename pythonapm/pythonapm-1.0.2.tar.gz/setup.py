import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

requirements = ['requests']

setuptools.setup(name='pythonapm',
      version='1.0.2',
      description='Monitor Django and Flask python web applications',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://nextapm.dev',
      author='Chan Anan',
      author_email='chan@nextapm.dev',
      license='MIT',
      zip_safe=False,
      packages=setuptools.find_packages(),
      python_requires='>=3.6',
      install_requires=requirements)

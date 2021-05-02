from setuptools import setup, find_packages

with open("README.md", "r") as fh:
      long_description = fh.read()

setup(name='pyezxl',
      version='1.2.0',
      url='https://github.com/sjpark/pyezxl',
      download_url='https://github.com/sjpark/pyezxl/archive/v0.0.6.tar.gz',
      author='sjpark',
      author_email='sjpkorea@yahoo.com',
      description='Read / Write Excel using Python',

      packages=find_packages("src"),
      package_dir={"": "src"},
      include_package_data=True,
      package_data={
            "pyezxl": ["excel_addin/*.*"],
            "pyezxl": ["pyezxl_code/*.*"],
            "pyezxl": ["pyezxl_history/*.*"],
            "pyezxl": ["pyezxl_manual/*.*"],
            "pyezxl": ["pyezxl_menu/*.*"],
            "pyezxl": ["user_code/*.*"],
            "pyezxl": ["user_menu/*.*"],
      },
      long_description=open('README.md').read(),
      install_requires=[''],
      python_requires='>=3.5',
      zip_safe=False,
      classifiers=[
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
      ],
)


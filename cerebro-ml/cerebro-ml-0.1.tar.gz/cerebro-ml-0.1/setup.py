# ------------------------------------------------------------------------------
#  Copyright (c) 2021, Hieu Tr.Pham. All rights reserved.
#
#  This program is a part of Cerebro.
#  <https://github.com/hieupth/cerebro>
#
#  Cerebro is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Cerebro is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
# ------------------------------------------------------------------------------

import sys
from distutils.core import setup
from setuptools import find_packages

if sys.version_info[0] < 3:
    with open('README.md') as f:
        long_description = f.read()
else:
    with open('README.md', encoding='utf-8') as f:
        long_description = f.read()

setup(
  name='cerebro-ml',
  packages=find_packages(),
  version='0.1',
  license='GPLv3',
  description='Deep Learning library extended from Google Tensorflow which focus on flexible prototyping features',
  long_description=long_description,
  long_description_content_type='text/markdown',
  author='Hieu Tr. Pham',
  author_email='hieupt.ai@gmail.com',
  url='https://github.com/hieupth/cerebro',
  download_url='https://github.com/hieupth/cerebro/archive/v_01.tar.gz',
  keywords=['machine learning', 'deep learning'],
  install_requires=['pydps', 'opencv-python'],
  classifiers=[
    'Development Status :: 1 - Planning',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8'
  ],
)
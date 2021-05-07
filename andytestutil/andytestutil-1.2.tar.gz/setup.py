import io
from setuptools import find_packages, setup

setup(
    name             = 'andytestutil',
    version          = '1.2',
    description      = 'For testing python app deploy',
    author           = 'behappytwice',
    author_email     = '4youwith@gmail.com',
    url              = 'https://gitlab.com/latteonterrace/python_start.git',
    download_url     = 'https://gitlab.com/latteonterrace/python_start.git',
    install_requires = [ ],
    #packages= find_packages(),
    #packages         = find_packages(where='src', exclude = ['docs', 'tests*']),
    #packages         = find_packages(exclude = ['docs', 'tests*']),
    #packages = ['andyutil'],
    packages         = find_packages(where='src'),
    package_dir={'': 'src'},
    keywords         = ['test', 'lesson'],
    python_requires  = '>=3',
    package_data={"andyutil":[
      'data/domains.txt'
    ]},
    zip_safe=False,
    classifiers      = [
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ]
)




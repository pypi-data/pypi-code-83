# python setup.py sdist
# python setup.py bdist_wheel
# twine upload dist/*0.2.1*

import setuptools

setuptools.setup(
    name='osm2rail',
    version='0.0.1',
    author='Jiawei Lu, Qian Fu, Zanyang Cui, Dr.Junhua Chen',
    author_email='jiaweil9@asu.edu, qian.fu@outlook.com, zanyangcui@outlook.com, cjh@bjtu.edu.cn',
    url='https://github.com/PariseC/osm2rail',
    description='An open-source education tool for constructing modeling datasets of railway transportation',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    license='Apache License 2.0',
    packages=['osm2rail'],
    include_package_data=True,
    python_requires=">=3.6.0",
    install_requires=[
        'pyhelpers==1.2.15',
        'bs4',
        'matplotlib<=3.3.0',
        'google',
        'protobuf==3.15.6'
    ],
    classifiers=['License :: OSI Approved :: Apache Software License',
                 'Programming Language :: Python :: 3']
)

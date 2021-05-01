from setuptools import setup, find_packages

setup(
    name='flyflow',
    version='0.0.2',
    description=(
        'Flyflow make python effectively!'
    ),
    scripts=['./client.py'],
    long_description=open('README.rst').read(),
    author='yuanjiexiong',
    author_email='finally@email.cn',
    maintainer='yuanjiexiong',
    maintainer_email='flyflow@email.cn',
    license='MIT License',
    packages=find_packages(),
    platforms=["all"],
    url='http://zuizhongkeji.com/',
    classifiers=[
        'License :: OSI Approved :: MIT License'
    ],
    install_requires=[
        'flask >= 1.1.2',
        'urllib3 >= 1.26.4',
        'psutil >= 5.8.0'
    ]
)

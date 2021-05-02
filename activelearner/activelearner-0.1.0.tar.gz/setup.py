from setuptools import setup, find_packages


def readme():
    with open('README.md') as f:
        README = f.read()
    return README


classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='activelearner',
    version='0.1.0',
    description='This is a library to use Active Learning in Text Classification and Topic Modeling.',
    long_description=readme(),
    long_description_content_type="text/markdown",
    url='https://github.com/ArshadSameemdeen/Text-Classification-Topic-Modeling-Active-Learner',
    author='Arshad Sameemdeen',
    author_email='arshadsameemdeen@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords='active learning',
    packages=find_packages(),
    install_requires=['']
)

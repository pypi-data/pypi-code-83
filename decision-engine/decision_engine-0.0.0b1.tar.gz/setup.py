from setuptools import setup, find_packages

PACKAGE_NAME = 'decision_engine'
PACKAGE_VERSION = "0.0.0-beta1"

def readme():
    with open('README.md') as readme_file:
        return readme_file.read()


if __name__ == "__main__":  # lets me import the above constants elsewhere
    setup(
        name=PACKAGE_NAME,
        version=PACKAGE_VERSION,
        description="Models for decision optimization and automation",
        long_description=readme(),
        long_description_content_type='text/markdown',

        classifiers=[
            'Development Status :: 4 - Beta',
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: Apache Software License",
            "Operating System :: OS Independent",
        ],
        keywords='sample, setuptools, development',

        python_requires='>=3.6, <4',

        url="https://github.com/BellwethrInc/decision_engine",
        author="Allen Grimm, Matt Moody, Jordan Roth",
        author_email="",

        packages=find_packages(include=["bandits"]),
        install_requires=[
            'numpy',
            'scipy',
        ]
    )

import setuptools


setuptools.setup(
    name='awyes',
    version='0.1.5',
    entry_points={
        'console_scripts': [
            'deploy=awyes.deployment:main'
        ]
    },
    install_requires=[
        'boto3',
        'requests',
    ],
    author="Truman Purnell",
    author_email="truman.purnell@gmail.com",
    description="Simplify AWS deployment",
    url="https://github.com/toobox/awyes",
    packages=setuptools.find_packages(),
)

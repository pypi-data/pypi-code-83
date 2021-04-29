from setuptools import setup

VERSION = "1.0.7"

requirements = ["websocket-client!=0.49"]


def readme():
    with open('README.md', encoding="utf8") as f:
        return f.read()

setup(
    name="elytica-pysher",
    version=VERSION,
    description="Pusher websocket client for python, based on Erik Kulyk's PythonPusherClient and Nils Diefenbach Pysher. This package has some fixes to support laravel-websockets(beyondcode) support.",
    long_description=readme(),
    long_description_content_type='text/markdown',
    keywords="pusher websocket client",
    author="Ruan Luies",
    author_email="ruan@elytica.com",
    license="MIT",
    url="https://github.com/baggins800/Pysher",
    install_requires=requirements,
    packages=["pysher"],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries ',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)

from setuptools import setup, find_packages

VERSION = '0.0A'
DESCRIPTION = 'Sending messages and requesting function parameters with telegram bot.'
long_description = 'A package allows easy message sending using a telegram bot and calling functions with parameters chosen in the dialogue basing on Python-telegram-bot package.'


# Setting up
setup(
    name="mlgram",
    version=VERSION,
    author="f3ss1 (Sergey Zakharov)",
    author_email="<n3ffar1an@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['telegram', 'os', 'stat'],
    keywords=['python', 'telegram', 'messages', 'parameters', 'functions', 'call'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)

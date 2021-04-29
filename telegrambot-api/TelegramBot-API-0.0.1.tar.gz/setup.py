from setuptools import setup, find_packages

VERSION = "0.0.1"
DESCRIPTION = "Simple Telegram Bot API"

# Setting up
setup(
    name="TelegramBot-API",
    version=VERSION,
    author="IHosseini",
    author_email="IHosseini@pm.me",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=["requests"],
    keywords=["python", "telegram", "bot", "api"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)

from setuptools import setup


setup(
    name="discord-ext-games",
    author="Wiper-R",
    url="https://github.com/Wiper-R/discord-ext-games",
    version="1.0.5",
    packages=["discord.ext.games", "discord.ext.games.tic_tac_toe"],
    license="MIT",
    description="This library provides bunch of games that can be played on discord.",
    install_requires=["discord.py>=1.6.1"],
    python_requires=">=3.6.0",
)
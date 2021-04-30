from setuptools import setup, find_packages

setup(name="message_server_Rutkevich",
      version="0.7",
      description="It's alive, ALIVE!",
      author="Yaroslav Rutkevich",
      author_email="Fenix12121995@mail.ru",
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex']
      )

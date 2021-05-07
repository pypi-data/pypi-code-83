
from setuptools import setup

setup(
    name='py-envfile',
    version='1.0.0',
    description='Python wrapper for .env',
    long_description='Help on package py_envfile:\n\nNAME\n    py_envfile\n\nPACKAGE CONTENTS\n\n\nFUNCTIONS\n    dict2envs(objectr)\n    \n    envs2dict(envs)\n    \n    envs2file(envname, envs)\n    \n    getenv(key)\n    \n    getenvfile(envfile, key)\n    \n    setenv(key, value)\n    \n    setenvfile(envname, key, value)\n\nFILE\n    VARIES\n\n\n',
    packages=["py_envfile"]
    )


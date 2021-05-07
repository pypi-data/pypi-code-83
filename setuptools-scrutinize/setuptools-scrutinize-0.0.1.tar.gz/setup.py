from setuptools import setup

setup(
    entry_points={
        "distutils.commands": [
            "scrutinize = setuptools_scrutinize.setuptools_command:Scrutinize"
            ],
        "distutils.setup_keywords": [
            "scrutinize_config = setuptools_scrutinize.setuptools_command:validate_config_file_exists"
            ],
    },
)

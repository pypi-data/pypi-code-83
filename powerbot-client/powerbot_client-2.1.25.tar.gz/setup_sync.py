import setuptools

setuptools.setup(
    name='powerbot_client',
    version='2.1.25',
    description='PowerBot client for sync operations',
    author="PowerBot GmbH",
    author_email="support@powerbot-trading.com",
    packages=['powerbot_client'],
    package_data={'powerbot_client': ['api/*', 'models/*']},
    python_requires='>=3.7',
    zip_safe=True,
    install_requires=['certifi', 'python-dateutil', 'urllib3', 'six']
)

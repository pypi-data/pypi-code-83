import setuptools

setuptools.setup(
    name='powerbot_asyncio_client',
    version='2.1.25',
    description='PowerBot client for async operations',
    author="PowerBot GmbH",
    author_email="support@powerbot-trading.com",
    packages=['powerbot_asyncio_client'],
    package_data={'powerbot_asyncio_client': ['api/*', 'models/*']},
    python_requires='>=3.7',
    zip_safe=True,
    install_requires=['certifi', 'python-dateutil', 'aiohttp==3.7.4', 'urllib3', 'six']
)
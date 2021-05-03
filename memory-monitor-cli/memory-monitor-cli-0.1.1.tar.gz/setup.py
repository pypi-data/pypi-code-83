import setuptools

import memory_monitor_cli


setuptools.setup(
    name='memory-monitor-cli',
    version=memory_monitor_cli.__version__,
    author=memory_monitor_cli.__author__,
    author_email='guallo.username@gmail.com',
    description='Memory Monitor CLI',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/guallo/memory-monitor-cli',
    packages=[memory_monitor_cli.__name__],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        'psutil',
        'plotext',
        'watchdog',
    ],
    entry_points={
        'console_scripts': [
            'mm-cli = memory_monitor_cli:main',
        ],
    },
)
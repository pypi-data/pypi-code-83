from setuptools import setup, find_packages

setup(
    long_description=open("README.md", "r").read(),
    name="pyug",
    version="0.44",
    description="python username generator library",
    author="Pascal Eberlein",
    author_email="pascal@eberlein.io",
    url="https://github.com/nbdy/pyug",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    keywords="username generator",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'pyug = pyug.__main__:main'
        ]
    },
    long_description_content_type="text/markdown"
)

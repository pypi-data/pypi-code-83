
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="araugment",
    version="1.0.0",
    author="Abdulshaheed Alqunber",
    author_email="abdulshaheed.qunber@kaust.edu.sa",
    license="MIT",
    description="Augment Arabic data for deep learning tasks",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords='arabic, arabic nlp, nlp',
    url="https://github.com/ashaheedq/araugment",
    project_urls={
        'Documentation': 'https://github.com/ashaheedq/araugment',
        'Bug Reports':
        'https://github.com/ashaheedq/araugment/issues',
        'Source Code': 'https://github.com/ashaheedq/araugment',
    },
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    classifiers=[
        # see https://pypi.org/classifiers/
        'Development Status :: 5 - Production/Stable',
        'Natural Language :: Arabic',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'markovify', 'google_trans_new', 'requests'
    ],
    extras_require={
        'dev': ['check-manifest'],
        # 'test': ['coverage'],
    },
)
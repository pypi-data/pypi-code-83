from setuptools import setup, find_packages

setup(
    name="cryptogym",
    version='0.0.13',
    license="MIT",
    description="CryptoCurrency Trading environment",
    author="Alan Tessier",
    author_email="alantessier.cr@gmail.com",
    url="https://github.com/alantess/cryptogym",
    keywords=[
        "cryptocurrency", "reinforcement learning", "deep learning",
        "artifical intelligence"
    ],
    install_requires=["matplotlib", "gym", "pandas", "numpy", "scikit_learn"],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
    packages=find_packages())

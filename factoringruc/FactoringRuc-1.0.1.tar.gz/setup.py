import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='FactoringRuc',
    version='1.0.1',
    packages=setuptools.find_packages(),
    url='https://github.com/leasingtotal/consulta-ruc',
    license='GNU General Public License v3.0',
    author='Jose Sakuda',
    author_email='jsakuda@josesakuda.com.de',
    description='Eliges un tipo de documento y realizas la consulta obteniendo los resultados de sunat.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[

        'requests'
    ],
    python_requires='>=3.6',
)
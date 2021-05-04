from setuptools import setup

setup(
    name='M6UF4Cine',
    packages=['cine/cine'],  # Mismo nombre que en la estructura de carpetas de arriba
    version='0.3',
    license='LGPL v3',  # La licencia que tenga tu paquete
    description='La cosa de UF4 de M6',
    author='David Duran Cunill',
    author_email='ranaMarrana@gmail.com',
    url='https://github.com/daviduvi99/M6UF4Cine',  # Usa la URL del repositorio de GitHub
    download_url='https://github.com/daviduvi99/M6UF4Cine/archive/refs/heads/master.zip',
    # Te lo explico a continuación
    keywords='test example develop',  # Palabras que definan tu paquete
    classifiers=['Programming Language :: Python',
                 # Clasificadores de compatibilidad con versiones de Python para tu paquete
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3.3',
                 'Programming Language :: Python :: 3.4',
                 'Programming Language :: Python :: 3.5',
                 'Programming Language :: Python :: 3.6',
                 'Programming Language :: Python :: 3.7'],
)
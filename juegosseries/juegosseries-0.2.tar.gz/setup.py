from setuptools import setup
 
setup(
    name='juegosseries',
    packages=['seriesjuegos'], # Mismo nombre que en la estructura de carpetas de arriba
    version='0.2',
    license='LGPL v3', # La licencia que tenga tu paquete
    description='Academic Project',
    author='GN',
    author_email='ranamarrana@gmail.com',
    url='https://github.com/Gabrinev/seriesjuegos', # Usa la URL del repositorio de GitHub
    download_url='https://github.com/Gabrinev/seriesjuegos/archive/refs/heads/master.zip', # Te lo explico a continuacion
    keywords='python objects games series', # Palabras que definan tu paquete
    classifiers=['Programming Language :: Python',  # Clasificadores de compatibilidad con versiones de Python para tu paquete
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3.3',
                 'Programming Language :: Python :: 3.4',
                 'Programming Language :: Python :: 3.5',
                 'Programming Language :: Python :: 3.6',
                 'Programming Language :: Python :: 3.7'],
)

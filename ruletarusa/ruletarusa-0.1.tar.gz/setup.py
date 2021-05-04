from setuptools import setup
 
setup(
    name='ruletarusa',
    packages=['ruletarusa'], # Mismo nombre que en la estructura de carpetas de arriba
    version='0.1',
    license='LGPL v3', # La licencia que tenga tu paquete
    description='Ruleta rusa para la UF4 del modulo M06.',
    author='SLG',
    author_email='mapacheador@gmail.com',
    url='https://github.com/cfsergio/RuletaRusa', # Usa la URL del repositorio de GitHub
    download_url='https://github.com/cfsergio/RuletaRusa/archive/refs/heads/main.zip',
    keywords='ruleta rusa', # Palabras que definan tu paquete
    classifiers=['Programming Language :: Python',  # Clasificadores de compatibilidad con versiones de Python para tu paquete
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3.3',
                 'Programming Language :: Python :: 3.4',
                 'Programming Language :: Python :: 3.5',
                 'Programming Language :: Python :: 3.6',
                 'Programming Language :: Python :: 3.7'],
)

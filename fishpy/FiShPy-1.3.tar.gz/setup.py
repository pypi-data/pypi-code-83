from distutils.core import setup
setup(
  name = 'FiShPy',         
  packages = ['FiShPy'],   
  version = '1.3',      
  license='MIT',        
  description = 'Fisher-Shannon method. Proposes non-parametric estimates of the Fisher Information Measure and the Shannon Entropy Power. The package contains also some bandwidth selectors for kernel density estimate', 
  author = 'Fabian Guignard and Mohamed Laib',               
  author_email = 'fabian.guignard@protonmail.ch',    
  url = 'https://fishinfo.github.io', 
  download_url = 'https://github.com/fishinfo/FiShPy/archive/refs/tags/v1.3-alpha.tar.gz',   
  keywords = [
      'Fisher Shannon plane', 
      'Fisher information measure', 
      'Fisher-Shannon complexity', 
      'Statistical complexity',
      ],  
  install_requires=[     
          'numpy',
          'scipy',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha', 
    'Topic :: Software Development :: Build Tools',    'License :: OSI Approved :: MIT License',  
    'Programming Language :: Python :: 3.7',
    ],
)
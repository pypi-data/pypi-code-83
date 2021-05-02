from distutils.core import setup
import setuptools
setup(
  name = 'FortiJson',         
  packages = ['FortiJson'],   
  version = '0.1',      
  license='MIT',        
  description = 'Json formating tool that conforms to Fortinets Json RPC protocol',
  author = 'Todd Albiston',                   
  author_email = 'foxtrot711@gmail.com',      
  url = 'https://github.com/talbiston/fortijson-rpc',   
  download_url = 'https://github.com/talbiston/fortijson-rpc/archive/refs/tags/0.0.2.tar.gz',    # I explain this later on
  keywords = ['Fortigate', 'Fortinet', 'Fortinet api'],   

  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',  
    'Programming Language :: Python :: 3',  
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)
#!/usr/bin/env python
# coding: utf-8

# In[1]:


import setuptools

with open('C:/Users/Hindy/Desktop/Container_pairs_trading/README.md', 'r') as fh:
    long_descripion = fh.read()
    
setuptools.setup(
    name='Simple_PairsTrading', 
    version='1.0.1',
    author='Hindy Yuen', 
    author_email='hindy888@hotmail.com',
    license='MIT',
    description='Find ideal candidates', 
    long_description=long_descripion, 
    long_description_content_type='text/markdown', 
    url='https://github.com/HindyDS/Pairs-Trading', 
    classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
],
    keywords='Pairs Trading',
    package_dir={"":"Simple_PairsTrading"},
    packages=['Simple_PairsTrading'],
    python_requires='>=3.6',
)


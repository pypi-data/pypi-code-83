import setuptools

setuptools.setup(
 name="pip_vulnerable_package",
 version="10000.0",
 author="nguna", 
 description="Malicious package which gets replaced due to confusion", 
 package_dir={'':'pip_vulnerable_package/src'},
 install_requires=[]
)

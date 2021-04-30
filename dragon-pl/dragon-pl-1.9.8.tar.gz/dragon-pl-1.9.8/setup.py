from setuptools import setup

setup(
   name='dragon-pl',
   version='1.9.8',
   description='The Dragon Programming Language',
   py_modules=["dragon-pl"],
   package_dir ={'':'src'},
   author='Aavesh Jilani',
   author_email='aavesh@dragon-lang.org',
   url='https://github.com/aaveshdev/dragon-for-py',
   data_files=[('lib\\site-packages\\',["src\\libdragon.dll","src\\dragon.dll"])],
    classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'Environment :: Web Environment',
          'Intended Audience :: End Users/Desktop',
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'Operating System :: Microsoft :: Windows',
          'Programming Language :: Python',
          ],
)
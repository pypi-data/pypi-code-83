''' setup.py
'''


import setuptools


setuptools.setup(
        name='tarpy',
        version='0.0.3',
        author='m1ghtfr3e',
        description='Python Version of tar.',
        packages=setuptools.find_packages(),
	entry_points={
            'console_scripts' : [
                'tarpy = tarpy.cli.run:cli'
                ]
        },

        classifiers=[
            'Programming Language :: Python :: 3',
            'Environment :: Console',
        ],

        python_requires='>=3',
        project_urls={
            'Source' : 'https://github.com/m1ghtfr3e/tarpy'
            }
)

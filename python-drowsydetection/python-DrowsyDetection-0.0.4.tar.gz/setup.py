from setuptools import  setup,find_packages

classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Education',
        'Operating System :: Microsoft :: Windows :: Windows 10',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
]

install_required = [
        'pygame',
        'opencv-python',
        'tensorflow==2.5.0rc2',
        'Keras==2.4.3',
        'numpy==1.19.5',
]

setup(
        name='python-DrowsyDetection',
        version='0.0.4',
        description='Library for drowsiness detection using deep learning',
        long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
        long_description_content_type='text/plain',
        url='',
        author='Ajit Singh Rathore',
        author_email='ajitsinghrathore64277@gmail.com',
        license='MIT',
        classifiers=classifiers,
        keywords='Drowsiness',
        packages=find_packages(),
        install_requires=install_required,
        include_package_data=True
)



from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()

setup(
    name='dingdingrobot',
    version='1.0.4',
    keywords='dingding, dingtalk, robot, dingdingrobot, dingtalk-robot, dingtalk-webhook',
    description='send message to dingtalk robot',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='zhanghe',
    author_email='x_hezhang@126.com',
    url='https://github.com/x-hezhang/dingtalk-robot',
    license='GNU GPLv3',
    packages=find_packages(),
    install_requires=['requests']
)

from setuptools import setup

with open("README.md", "r",encoding='utf-8') as f:
  long_description = f.read()
  
setup(name='iwaratool',  # 包名
      version='0.1.0',  # 版本号
      description='批量获取iwara的内容',
      long_description=long_description,
      author='白色羽毛',
      author_email='1665169869@qq.com',
      url='http://baiyu.fun',
      install_requires=['requests>=2.22.0','setuptools>=16.0'],
      license='LGPL-3.0 License',
      packages=['iwaratool'],
      platforms=["all"],
      classifiers=[
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Natural Language :: Chinese (Simplified)',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Topic :: Software Development :: Libraries'
      ],
      )
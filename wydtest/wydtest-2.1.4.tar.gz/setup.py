
#############################################
# File Name: setup.py
# Author: LiangjunFeng
# Mail: zhumavip@163.com
# Created Time:  2018-4-16 19:17:34
#############################################

from setuptools import setup, find_packages            #这个包没有的可以pip一下

setup(
    name = "wydtest",      #这里是pip项目发布的名称
    version = "2.1.4",  #版本号，数值大的会优先被pip
    keywords = ("pip", "wyd","featureextraction"),
    description = "Is your pytorch cuda available?",
    long_description = "s your pytorch cuda available?",
    license = "MIT Licence",

    url = "https://github.com/bro3/wydtest",     #项目相关文件地址，一般是github
    author = "bro3",
    author_email = "yudwang@outlook.com",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = ["torch"]          #这个项目需要的第三方库
)

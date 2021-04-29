from distutils.core import setup

setup(
    name='baizhan1Math',  # 对外我们模块的名字
    version='1.0', # 版本号
    description='这是第一个对外发布的模块，里面只有数学方法，用于测试哦',  #描述
    author='liyanming', # 作者
    author_email='974434895@qq.com',
    py_modules=['baizhan1Math.demo1','baizhan1Math.demo2'] # 要发布的模块
)
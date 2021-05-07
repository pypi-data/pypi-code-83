from setuptools import setup

setup(
    name='verilog_axi4',
    version='v0.12',
    description='A module for generating verilog axi4 code',
    py_modules=['verilog_axi4', 'axi_ar_channel', 'axi_aw_channel', 'axi_b_channel',
                'axi_r_channel', 'axi_w_channel', 'axi_parameter', 'axi_connectN'],
    author='likmi',
    author_email='likmi@qq.com',
    license='MIT'
)

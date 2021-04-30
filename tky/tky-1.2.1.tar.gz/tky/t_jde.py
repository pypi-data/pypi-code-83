# _*_ coding:utf-8 _*_
"""
常用判断类集合
\n 目前支持方法有：
\n null (数据空判断)
\n val_list （数据匹配，自有；依赖re）
\n val_case (转换传入字符串内容)
\n Jde_o 新方法 (时间计算：change_time)
\n @author: 'TangKaiYue'
"""

# 引入时间组件
import time
from datetime import datetime, timedelta


# 数据空判断
def null(val: str = 'null'):
    """
    【数据为空判断】\n
    :param val : str 传入的内容；
    :return 为空输出'N'，不为空则输出传入内容；
    """
    try:
        if str(val) == 'null' or str(val) == '' or str(val) == [] or str(val) is None or str(val) == 'Null' or str(
                val) == 'NULL':
            return 'N'
        else:
            return str(val)
    except EnvironmentError as err:
        return '发生异常：%s' % err


# 转换传入字符串内容（大小写）
def val_case(self: str = 'null', tp: str = 'l'):
    """
    【转换传入字符串内容】\n
    :param self: 传入要转换的英文字符串（支持：转换全字符串大小写、首字母大写、各单词首字母大写）；
    :param tp: 需要输出的结果值(u:全大写/l:全小写/c:首字母大写/t:各单词首字母大写;默认输出全小写)；
    :return: 输出匹配结果；
    """
    try:
        if null(self) == 'N':
            return '异常：请传入self不为空的数据 ...'
        if tp == 'u' or tp == 'U':
            return self.upper()
        if tp == 'l' or tp == 'L':
            return self.lower()
        if tp == 'c' or tp == 'C':
            return self.capitalize()
        if tp == 't' or tp == 'T':
            return self.title()
    except EnvironmentError as err:
        return '发生异常：%s' % err


# 匹配传入的数据并返回第一个匹配结果，未传入的参数默认为空
def val_list(self: str = 'null', user: str = 'null') -> str:
    """
    【匹配传入的数据并返回第一个匹配结果】\n
    :param  self : str 用户组,前后加英文逗号.如：',用户1,用户2,用户3,'；
    :param  user : str 用户,如：用户1 (用户组内包含的部分内容)；
    :return 输出匹配结果；
    """
    try:
        import re
        if null(self) == 'N' or null(user) == 'N':
            return '异常：请传入self & user不为空的数据 ...'
        else:
            emp_name = self
            emp_code = user
        bcd = re.search('[,][^,]*' + emp_code + '[^,]*[,]', emp_name, re.M | re.I)  # 对传入的数据进行匹配处理
        if bcd is None:  # 判断匹配的结果
            return '未匹配到对应结果，None'
        val = bcd.group()
        new_name = val[1:-1]  # 截取匹配的结果内容
        return new_name
    except EnvironmentError as err:
        return '发生异常：%s' % err


# 新方法类
class Jde_o:
    # 时间计算
    def change_time(days=0, hours=0, minutes=0):
        """
        [时间计算]\n
        :param days: 要计算的天
        :param hours: 要计算的时
        :param minutes: 要计算的分
        :return: 计算后的结果
        """
        # 定义现在时间
        new_time = time.strftime("%Y-%m-%d %H:%M:%S")
        if type(new_time) == str:
            time_str = datetime.strptime(new_time, '%Y-%m-%d %H:%M:%S')
            ret = time_str + timedelta(days=days, hours=hours, minutes=minutes)
            return ret

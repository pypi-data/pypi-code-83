# coding:utf-8

from configparser import ConfigParser


def rq_util_cfg_initial(CONFIG_FILE):
    """[summary]
    Arguments:
        CONFIG_FILE {[type]} -- [description]
    """

    pass


def rq_util_get_cfg(__file_path, __file_name):
    """
    explanation:
        获取配置信息
    params:
        * __file_path ->
            含义: 配置文件地址
            类型: str
            参数支持: []
        * __file_name ->
            含义: 文件名
            类型: str
            参数支持: []
    """
    __setting_file = ConfigParser()
    try:
        return __setting_file.read(__file_path + __file_name)
    except:
        return 'wrong'

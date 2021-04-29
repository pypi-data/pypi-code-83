# coding=utf8
import pytest
import os
import sys
from src.pylong.api.common import copy_history


# *按需更改*
RUN_PARAM = {
    "collect": ['test_suits', '--collect-only'],
    "by_dir": ['test_suits'],
    "by_mod": ['test_suits/test_01_demo.py'],
    "by_class": ['test_suits/test_01_demo.py::TestDemo'],
    "by_func": ['test_suits/test_01_demo.py::TestDemo::test_demo_valid'],
    "by_search": ['-k', 'test_demo_valid'],
    "by_severity": ['--allure-severities', 'blocker'],
    "by_feature": ['--allure-features', 'Demo'],
    "by_story": ['--allure-stories', 'List Demo'],
}

# 不需更改
ALLURE_PARAM = [
    '-v',
    '--alluredir',
    'allure-result',
    "--clean-alluredir"
]


def run_by(run_param):
    # *按需调用*
    run = run_param

    # 切换工作空间
    BASE_PATH = os.path.abspath(sys.path[0])
    os.chdir(f'{BASE_PATH}')
    # 执行测试用例
    pytest.main(run + ALLURE_PARAM)
    # 复制历史结果，并生成报告
    copy_history("report", "allure-result")
    os.system(f"allure generate allure-result -o report --clean")

    # 打开报告， 生成url
    os.system(f"allure open report")

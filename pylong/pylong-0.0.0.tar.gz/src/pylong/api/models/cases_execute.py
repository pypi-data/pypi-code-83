# coding=utf8
"""
execute cases and extract results
input:
{
    # "env": {},
    "project_name": "DEMO",
    "project_path": "DEMO",
    "output_path": "",
    "cases": [{
        "case_id": 1,
        # "case_name": "",
        # "case_category": "",
        # "project_name": "",
        # "output_path": "",
        "extra": {}
    }]
}
output:
{
    "report_file": "",
    "log_file": "",
    "cases": [
        {
            "case_id": None,
            "case_status": "string",
            "variables": {
                "in_puts": {},  # 数据输入
                "out_puts": {}  # 数据输出（供后面用例使用）
            },
            "attachment": {
                "log_file": "string",  # 详细执行过程文件路径
                "html_file": "string"  # html报告文件路径
            },
            "steps": [{
                "name": "string",  # 测试步骤名字
                "status": "string",  # 测试步骤状态（pass/fail/error）
                "request": {},  # 请求
                "response": {},  # 响应
                "validators": [{  # 校验项
                    "comparator": "equal",
                    "check": "status_code",
                    "check_value": None,
                    "expect_value": None,
                    "message": None,
                    "check_result": None
                }],
                "erroes": "error msg"
            }]
        }
    ]
}
"""
CASE_LIST_JSON = {
    "env": {},
    "project_name": "DEMO",
    "project_path": "DEMO",
    "output_path": "/Users/jiukunzhang/PycharmProjects/dl_cms/tmp/output.json",
    "cases": [
        {
            "case_id": 1,
            "case_name": "ListDemoInValid",
            "case_category": "PY",
            "project_name": "DEMO",
            "output_path": "/Users/jiukunzhang/PycharmProjects/dl_cms/tmp/1",
            "extra": {
                'class': "TestDemo",
                'function': 'test_demo_invalid',
                'module': 'tests.DEMO.test_suits.test_01_demo',
                'nodeID': 'DEMO/test_suits/test_01_demo.py: : TestDemo: : test_demo_invalid',
                'path': 'DEMO/test_suits/test_01_demo.py',
                'severity': 'blocker',
                'story': 'ListDemo'
            }
        },
        {
            "case_id": 2,
            "case_name": "ListDemoValid",
            "case_category": "PY",
            "project_name": "DEMO",
            "output_path": "/Users/jiukunzhang/PycharmProjects/dl_cms/tmp/1",
            "extra": {
                'class': "TestDemo",
                'function': 'test_demo_valid',
                'module': 'tests.DEMO.test_suits.test_01_demo',
                'nodeID': 'DEMO/test_suits/test_01_demo.py: : TestDemo: : test_demo_valid1',
                'path': 'DEMO/test_suits/test_01_demo.py',
                'severity': 'blocker',
                'story': 'ListDemo'
            }
        }]
}

CASE_RESULTS_JSON = {
    "report_file": "",
    "log_file": "",
    "cases": [
        {
            "case_id": None,
            "case_status": "passed",
            "variables": {
                "in_puts": {},  # 数据输入
                "out_puts": {}  # 数据输出（供后面用例使用）
            },
            "attachment": {
                "log_file": "",  # 详细执行过程文件路径
                "html_file": ""  # html报告文件路径
            },
            "steps": [{
                "name": "step 1",  # 测试步骤名字
                "status": "passed",  # 测试步骤状态（pass/fail/error）
                "request": {},  # 请求
                "response": {},  # 响应
                "validators": [{  # 校验项
                    "comparator": "equal",
                    "check": "status_code",
                    "check_value": None,
                    "expect_value": None,
                    "message": None,
                    "check_result": None
                }],
                "erroes": "error msg"
            }]
        }
    ]
}

import os
import sys
from src.pylong.api import Config, ROOT_PATH, TEST_PATH
from subprocess import Popen, PIPE
from src.pylong.api.utils.log import logger
from src.pylong.api.common import copy_history
from src.pylong.api import extract
from src.pylong.api import rec_merge
from copy import deepcopy
import shutil
from src.pylong.api import UpdateCase


# # 读取输入参数 CASE_LIST_JSON
# PR_PATH = extract("project_path", CASE_LIST_JSON)
# OUTPUT_PATH = extract("output_path", CASE_LIST_JSON)
# # 系统路径配置（基础路径、测试执行路径、项目空间）
# BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
# TEST_PATH = os.path.join(BASE_PATH, "tests")
# PR_PATH = os.path.join(TEST_PATH, PR_PATH)
# sys.path.extend([BASE_PATH, TEST_PATH, PR_PATH])
# # 额外路径配置（数据路径、allure结果路径、allure报告路径）
# DATA_PATH = os.path.join(PR_PATH, "data")
# RESULT_PATH = os.path.join(PR_PATH, "allure-result")
# REPORT_PATH = os.path.join(PR_PATH, "report")
# # 进入测试执行路径
# os.chdir(TEST_PATH)


class ExecTests(object):
    """批量执行测试用例，生成指定格式json，保存在指定位置"""

    def get_base_paths(self, case_list_json):
        """
        0 获取基础路径，准备执行环境
        """
        project_path = extract("project_path", case_list_json)
        self.output_path = extract("output_path", case_list_json)
        self.project_path = os.path.join(TEST_PATH, project_path)

        # 额外路径配置（数据路径、allure结果路径、allure报告路径）
        self.data_path = os.path.join(self.project_path, "data")
        self.result_path = os.path.join(self.project_path, "allure-result")
        self.report_path = os.path.join(self.project_path, "report")

        sys.path.extend([ROOT_PATH, TEST_PATH, self.project_path])

    def get_case_nodes(self, case_list_json):
        """
        1 提取nodeID信息，供批量执行
        return:
        {
            "DEMO/test_suits/test_01_demo.py::TestDemo::test_demo_valid":
                {"case_id": 123}
        }
        """
        case_nodes = {}
        case_list = extract("cases", case_list_json)

        real_node_list = UpdateCase().get_case_node_list(self.project_path)
        logger.info(f"real_node_list: {real_node_list}")
        for case in case_list:
            case_id = extract("case_id", case)
            nodeID = extract("extra.nodeID", case).strip().replace(": ", ":")
            if nodeID in real_node_list:
                case_nodes.update({nodeID: {"case_id": case_id}})
            else:
                case_nodes.update({nodeID: {"case_id": case_id, "case_status": "NotFound"}})

        logger.info(f"case_nodes_id: {case_nodes}")
        return case_nodes

    def run_test(self, case_nodes):
        """2 运行测试用例"""
        try:
            # 1. backup pytets.ini
            if os.path.exists("pytest.ini"):
                shutil.copy("pytest.ini", "pytest.ini.bak")
            # 2. update pytest.ini by case_nodes
            self._pytest_config(case_nodes)
            # 3. execute testcases by pytets.ini
            self._run_pytest_cases()
        except Exception as e:
            logger.error(e)
        finally:
            # 4. recovery pytest.ini
            if os.path.exists("pytest.ini.bak") and os.path.exists("pytest.ini"):
                shutil.move("pytest.ini.bak", "pytest.ini")

        case_results = self._get_case_results()
        rec_merge(case_results, case_nodes)
        logger.info(f"case_nodes_results: {case_results}")
        return case_results

    def _pytest_config(self, case_nodes):
        """2.1 把nodeid写到pytest.ini，批量执行(*跳过NotFound的用例*）"""
        os.chdir(TEST_PATH)
        with open("pytest.ini", "w") as f:
            f.write('[pytest]\ntestpaths =\n')
            for node, node_info in case_nodes.items():
                if node_info.get("case_status") != 'NotFound':
                    f.write("\t" + node)

    def _run_pytest_cases(self):
        """2.2 批量执行测试用例, 生成allure报告"""
        PYTEST_PARAM = [
            'pytest',
            '--case-execute',
            '--tb=short',
            '-n',
            'auto'
        ]
        ALLURE_PARAM = [
            '--alluredir',
            self.result_path,
            "--clean-alluredir"
        ]

        os.chdir(TEST_PATH)
        with Popen(PYTEST_PARAM + ALLURE_PARAM, stdout=PIPE, bufsize=1, universal_newlines=True) as p:
            for line in p.stdout:
                logger.info(line)
                # print(line, end='')

        if not os.path.exists(self.report_path): os.makedirs(self.report_path)
        copy_history(self.report_path, self.result_path)
        os.system(f"allure generate {self.result_path} -o {self.report_path} --clean")

    def _get_case_results(self):
        """
        2.3 获取用例执行结果
        return:
        {
            "DEMO/test_suits/test_01_demo.py::TestDemo::test_demo_valid":
                {
                    "case_status": 'passed',
                    "steps": [
                        {"name": "", "case_status": "passed"},
                        ]
                }
        }
        """
        REPORT_CASE_PATH = os.path.join(self.project_path, "report/data/test-cases")

        if not os.path.exists(REPORT_CASE_PATH):
            raise BaseException("test case excuted block, no report file generated")

        case_result = {}
        for c in os.listdir(REPORT_CASE_PATH):
            res = Config(os.path.join(REPORT_CASE_PATH, c)).json_get()
            name = extract("name", res)
            case_path = res["fullName"]
            nodeID = self._convert_allure_to_pytest_nodeid(case_path)
            case_status = extract("testStage.status", res)

            step_result = deepcopy(extract("cases[0].steps[0]", CASE_RESULTS_JSON))
            step_result.update({"name": name, "status": case_status})

            if not case_result.get(nodeID):
                node_result = deepcopy(extract("cases[0]", CASE_RESULTS_JSON))
                node_result.update({"case_status": case_status, "steps": [step_result]})

                case_result[nodeID] = node_result
            else:
                case_result[nodeID]['steps'].append(step_result)
                if case_status != 'passed': case_result[nodeID]['case_status'] = 'failed'

        logger.info(f"case_nodes_status: {case_result}")
        return case_result

    def _convert_allure_to_pytest_nodeid(self, case_path):
        """ 2.3.1
        case_path: 'DEMO.test_suits.test_01_demo.TestDemo#test_demo_valid'
        to
        case_nodeid: 'DEMO/test_suits/test_01_demo.py::TestDemo::test_demo_valid'
        """
        _module, func = case_path.split("#")
        _path = _module.split(".")
        if _path[-1].startswith("Test"):
            cls = _path[-1]
            module = _path[-2]
            path = _path[:-2]
            case_nodeid = '/'.join(path) + '/' + module + '.py' + "::" + cls + "::" + func
        else:
            case_nodeid = _module.replace('.', '/') + '.py' + "::" + func
        # logger.info(f"case_nodeid: {case_nodeid}")
        return case_nodeid

    def export_json(self, case_result, log_file_name):
        """
        3. 返回指定格式json输出到指定路径
        """
        output_json = deepcopy(CASE_RESULTS_JSON)

        output_json["report_file"] = self.report_path
        output_json["log_file"] = log_file_name
        output_json["cases"] = list(case_result.values())

        logger.info(f"output_json: {output_json}")
        Config(self.output_path).json_put(output_json)
        return output_json


def backup_log():
    logger.info("备份日志")
    log_file_name = logger.log_file_name
    log_file_name_bak = f"{logger.log_file_name}.bak"
    os.system(
        f"touch {log_file_name} {log_file_name_bak}; "
        f"cat {log_file_name} >> {log_file_name_bak}; "
        f"cat /dev/null > {log_file_name}"
    )
    return log_file_name


def run_plan(case_list_json=CASE_LIST_JSON):
    log_file_name = backup_log()

    et = ExecTests()
    et.get_base_paths(case_list_json)
    case_nodes = et.get_case_nodes(case_list_json)
    case_results = et.run_test(case_nodes)
    res = et.export_json(case_results, log_file_name)
    return res


if __name__ == "__main__":
    """只需要读取一个输入参数，定义名称为 CASE_LIST_JSON，就可以了"""
    run_plan(CASE_LIST_JSON)
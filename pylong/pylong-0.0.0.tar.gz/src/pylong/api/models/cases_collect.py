# coding=utf8
"""
generate cases mapping relationship
upstream param:
{
    "project_id": "",
    "project_path": ""
}
call case/many api param:
[
  {
    "primary_key": "anyitem or extra.xxxx",
    "author": "string",
    "name": "string",
    "category": "string",
    "priority": "string",
    "description": "string",
    "project_id": 0,
    "group_id": 0,
    "extra": {}
  }
]
"""

import os
import sys
from src.pylong.api import Config, ROOT_PATH, TEST_PATH
from subprocess import Popen, PIPE
from src.pylong.thirdparty import CaseManage
from src.pylong.api import extract
from src.pylong.api.utils.log import logger

PROJECT_JSON = {
    "project_id": 35,
    "project_path": "DEMO"
}


# # 读取输入参数 PR_LIST_JSON
# PR_LIST_JSON = PR_LIST_JSON
# PR_PATH = extract("project_path", PR_LIST_JSON)
# # 系统路径配置（基础路径、测试执行路径、项目空间）
# TEST_PATH = os.path.join(BASE_PATH, "tests")
# PR_PATH = os.path.join(TEST_PATH, PR_PATH)
# sys.path.extend([BASE_PATH, TEST_PATH, PR_PATH])
# # 额外路径配置（数据路径、allure结果路径、allure报告路径）
# DATA_PATH = os.path.join(PR_PATH, "data")
# # 进入测试执行路径
# os.chdir(TEST_PATH)


class UpdateCase(object):
    """批量更新用例到平台"""

    def get_base_paths(self, project_json=PROJECT_JSON):
        """
        0 获取基础路径，准备执行环境
        """
        project_path = project_json["project_path"]
        self.project_id = project_json["project_id"]
        self.project_path = os.path.join(TEST_PATH, project_path)
        self.data_path = os.path.join(self.project_path, "data")
        sys.path.extend([ROOT_PATH, TEST_PATH, self.project_path])

    def get_case_base_info(self, project_path=None):
        """
        1. 获取用例映射关系等基本信息， 以nodeID为判断基准
        """
        project_path = project_path if project_path else self.project_path
        case_base_info = []

        os.chdir(TEST_PATH)
        with Popen(['pytest',
                    '--collect-only',
                    '--case-manage',
                    '--tb=short',  # shorter traceback format
                    project_path
                    ], stdout=PIPE, bufsize=1,
                   universal_newlines=True) as p:
            for line in p.stdout:
                print(line, end='')

        case_manage_yml = os.path.join(project_path, "data/.tmp_case_manage.yml")
        if os.path.exists(case_manage_yml):
            case_base_info = Config(case_manage_yml).get()
            os.remove(case_manage_yml)
        logger.info(f"case_base_info: {case_base_info}")
        return case_base_info

    def get_case_info(self, case_base_info):
        """
        2. 补全case信息（根据case的三级模块，判断并创建三级分组;暂时不用）
        """
        # for case in case_base_info:
        #     epic = case["extra"].get("epic")
        #     feature = case["extra"].get("feature")
        #     story = case["extra"].get("story")
        #
        #     mum_id = 1
        #     for group in [epic, feature, story]:
        #         project_name =

        for case in case_base_info:
            case.update({"project_id": self.project_id})
        case_info = case_base_info
        logger.info(f"本次发现{len(case_info)}条测试用例")
        return case_info

    def update_case_to_platform(self, case_info):
        """
        3 更新用例到平台
        """
        cm = CaseManage()
        res = cm.import_case(cases=case_info)
        return res

    def get_case_node_list(self, project_path):
        """
        4 获取用例的nodeid列表, 仅供用例执行的查询
        """
        project_path = project_path if project_path else self.project_path

        case_base_info = self.get_case_base_info(project_path)
        case_node_list = []
        for case in case_base_info:
            nodeID = extract("extra.nodeID", case).strip().replace(": ", ":")
            case_node_list.append(nodeID)
        return case_node_list


def update_case(project_json=PROJECT_JSON):
    uc = UpdateCase()
    uc.get_base_paths(project_json)
    case_base_info = uc.get_case_base_info()
    case_info = uc.get_case_info(case_base_info)
    res = uc.update_case_to_platform(case_info)
    return res


def list_case(project_json=PROJECT_JSON):
    logger.info(project_json)
    uc = UpdateCase()
    uc.get_base_paths(project_json)
    case_base_info = uc.get_case_base_info()
    case_info = uc.get_case_info(case_base_info)
    return case_info


if __name__ == "__main__":
    """传入PR_LIST_JSON = {project_path、project_id、group_id}就可以了"""
    # update_case(PROJECT_JSON)
    list_case(PROJECT_JSON)

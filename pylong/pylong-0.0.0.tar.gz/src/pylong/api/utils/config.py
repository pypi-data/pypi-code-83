"""
读取配置。采用yaml格式配置文件，也可以采用xml、ini等，需要在file_rader添加响应Reader处理。
❗️ 注意：基础脚本【config， support】，不能import更高级的脚本如logger， Sql
"""
import os
from src.pylong.api.utils.file_reader import YamlReader, JsonReader, RawReader
from src.pylong.api.utils.file_writer import YamlWriter, JsonWriter, RawWriter
from src.pylong.api import to_list, eval_param

BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]  # ./src/api

# BASE_PATH = "."
CONFIG_PATH = os.path.join(BASE_PATH, 'config')
DATA_PATH = os.path.join(BASE_PATH, 'data')
# TEST_PATH = os.path.join(BASE_PATH, "tests")
DRIVERS_PATH = os.path.join(BASE_PATH, 'drivers')
LOG_PATH = os.path.join(BASE_PATH, 'log')
REPORT_PATH = os.path.join(BASE_PATH, 'reports')
# UTILS_PATH = os.path.join(BASE_PATH,'utils')
CONFIG_FILE = os.path.join(CONFIG_PATH, 'config.yml')

ROOT_PATH = os.path.split(os.path.dirname(BASE_PATH))[0]  # ./
TEST_PATH = os.path.join(ROOT_PATH, "tests")


class Config:
    """
    读取yaml配置文件的元素
    Config(): 默认读取 ${workspace}/config/config.yml
    Config('api_config.yml'): 读取 ${workspace}/config/api_config.yml
    Config('testAPI/interface/mod_2_video/test.yml'): 读取 ${workspace}/testAPI/interface/mod_2_video/test.yml
    Config('/usr/data/images'): 读取 /usr/data/images
    """

    def __init__(self, config='config.yml', index=0):
        if config.startswith("/"):
            self.abspath = config
        elif '/' in config:
            self.abspath = BASE_PATH
            for var in config.split('/'):
                self.abspath = os.path.join(self.abspath, var)
        else:
            self.abspath = os.path.join(CONFIG_PATH, config)

        try:
            self.config = self.get(index=index)
        except Exception as e:
            self.config = None

    def get(self, element=None, index=0):
        """
        get config element
        :param element: yaml element
        :param index: yaml is separated to lists by '---'
        :return:
        """
        try:
            self.config = YamlReader(self.abspath).data[index]
        except Exception as e:
            raise Exception("Yaml read error")

        if element:
            res = self.config.get(element)
        else:
            res = self.config
        return res

    def global_var(self, index=0):
        """
        Be careful! Transfer yaml key to global var name
        :return:
        """
        if index:
            self.config = YamlReader(self.abspath).data[index]

        for key in sorted(self.config.keys()):
            globals()[key] = self.config[key]

    def put(self, yaml_obj, abspath=None):
        """把yaml格式对象，写入一个新的yaml文件（覆盖重写）"""
        abspath = self.abspath if not abspath else abspath
        self.touch(abspath)
        YamlWriter(yaml_obj, abspath, overwrite=True)

    def update(self, yaml_obj, abspath=None):
        """把yaml格式对象，写入一个旧的yaml文件（更新追加）"""
        abspath = self.abspath if not abspath else abspath
        try:
            dest = YamlReader(abspath).data[0]
            if isinstance(dest, list) and isinstance(yaml_obj, list):
                YamlWriter(yaml_obj, abspath, overwrite=False)
            elif isinstance(dest, dict) and isinstance(yaml_obj, dict):
                dest.update(yaml_obj)
                YamlWriter(dest, abspath, overwrite=True)
            else:
                raise ValueError("试图写入不同类型的数据到YAML文件，请检查！ ")
        except FileNotFoundError:
            self.put(yaml_obj, abspath)

    def json_get(self):
        """从json文件读取json对象"""
        json_data = JsonReader(self.abspath).data
        return json_data

    def json_put(self, json_obj, abspath=None):
        """把json对象写为json文件"""
        abspath = self.abspath if not abspath else abspath
        self.touch(abspath)
        JsonWriter(json_obj, self.abspath)

    def json_update(self):
        pass

    def raw_get(self):
        raw_data = RawReader(self.abspath).data
        return raw_data

    def raw_put(self, raw_obj):
        RawWriter(raw_obj, self.abspath)

    def touch(self, abspath):
        """当写入文件时，需要保证路径和文件都是存在的"""
        dirname = os.path.dirname(abspath)
        os.makedirs(dirname, exist_ok=True)
        with open(abspath, 'a'):
            os.utime(abspath, None)


class YamlParam(Config):
    """
    Read and Format Input Param from config
    """

    @staticmethod
    def parse_by_case_type(original_data, type='valid'):
        # transfer `{a: {valid: []}, b: {valid: []}}` to `{a: [], b: []}`
        original_data = eval_param(original_data)
        param = {}
        param_list = []

        if isinstance(original_data, dict):
            type_value = original_data.get(type)
            if type_value:
                type_value = to_list(type_value)
                param_list = YamlParam.parse_by_case_type(type_value, type)
                return param_list
            else:
                for key in original_data.keys():
                    if key != 'valid' and key != 'invalid':
                        param[key] = YamlParam.parse_by_case_type(original_data.get(key), type)
                return param

        elif isinstance(original_data, list):
            for value in original_data:
                param = YamlParam.parse_by_case_type(value, type)
                param_list.append(param)
            return param_list
        else:
            return original_data

    @staticmethod
    def dict_value_to_list(src_dict: dict):
        """
        To transfer a dict to a permutation lists
        :param src_dict: {key1: [a1,a2], key2: [b1,b2,b3], key3:[c1]}
        :return: [[a1,b1,c1], [a2,b2,c1], [a2,b3,c1]]
        """
        res = []
        over_key = set()
        while len(over_key) < len(src_dict):
            lr = len(res)
            res_i = {}
            for key in src_dict.keys():
                # ensure the value list is this format: [value]
                if src_dict[key] and isinstance(src_dict[key], list):
                    value_list = src_dict[key]
                else:
                    value_list = [src_dict[key]]

                # combine valid params
                if lr < len(value_list) - 1:
                    res_i[key] = value_list[lr]
                else:
                    over_key.add(key)
                    res_i[key] = value_list[-1]

                # disable key if value is 'x'
                if res_i[key] == 'x':
                    res_i.pop(key)
            if res_i not in res:
                res.append(res_i)
        return res

    @staticmethod
    def replace_json_with_dict(src_dict: dict, json: dict) -> list:
        """
        To combine yml wrong params with the template
        :param src: {arg1: [1,2,3]}
        :param json: {arg1: 0, arg2:9}
        :return: [{arg1: 1, arg2:9},{arg1: 2, arg2:9},{arg1: 3, arg2:9}]
        """
        res = []
        for key in src_dict.keys():
            # ensure the value list is this format: [value]
            if src_dict[key] and isinstance(src_dict[key], list):
                value_list = src_dict[key]
            else:
                value_list = [src_dict[key]]

            for val in value_list:
                tmp = json.copy()
                tmp[key] = val

                # disable key if value is 'x'
                if val == 'x':
                    tmp.pop(key)

                if tmp not in res:
                    res.append(tmp)
        return res

    def valid_params(self, element):
        """
        获取组合后的·有效字段·数据列表
        """
        # ele_valid = self.get(element).get('valid')
        ele = self.get(element)
        ele_valid = self.parse_by_case_type(ele, type='valid')
        if ele_valid and isinstance(ele_valid, dict):
            ele_valid = self.dict_value_to_list(ele_valid)
        self.ele_valid = ele_valid
        return self.ele_valid

    def invalid_params(self, element, template_file=None):
        """
        获取组合后的·无效字段·数据列表
        """
        # ele_invalid = self.get(element).get('invalid')
        ele = self.get(element)
        ele_invalid = self.parse_by_case_type(ele, type='invalid')
        if ele_invalid and isinstance(ele_invalid, dict):
            try:
                if template_file:
                    template = Config(template_file).json_get()
                elif self.valid_params(element) and isinstance(self.ele_valid[0], dict):
                    template = self.ele_valid[0]
                ele_invalid = self.replace_json_with_dict(ele_invalid, template)
            except Exception as e:
                raise FileNotFoundError("need template json file")
        self.ele_invalid = ele_invalid
        return self.ele_invalid

    def combined_params(self):
        """
        组合该yml文件下所有param， 生成_combined_xx.yml文件
        并返回其字典格式数据
        """
        res = {}
        try:
            all_params = self.config
            for key in all_params.keys():
                if key.startswith("param"):
                    valid = self.valid_params(key)
                    invalid = self.invalid_params(key)
                    res.update({f"{key}_valid": valid, f"{key}_invalid": invalid})
            original_path = os.path.split(self.abspath)
            out_path = os.path.join(original_path[0], "_combined_" + original_path[1])
            self.put(res, out_path)
        except Exception as e:
            raise
        return res


def com_params(yaml_files_list):
    """
    根据yaml文件列表，返回一个输入参数字典
    """
    param_dict = {}
    for file in yaml_files_list:
        yp = YamlParam(file)
        combined = yp.combined_params()
        param_dict.update(combined)
    return param_dict


if __name__ == "__main__":
    c = Config()
    print(c.get('dl_admin_url'), BASE_PATH)
    c.global_var()

    p = YamlParam("data/input_loads/image_generate.yml")
    param_request_list_correct = [tuple(i) for i in p.valid_params("param_request_list")]
    print(param_request_list_correct)
    print(p.valid_params('param_inputset'))
    # print(Config('data/input_loads/image_stock/attribute.yml').get('param_add_attribute'))

    attribute_yml = 'data/input_loads/image_stock/attribute.yml'
    yp = YamlParam(attribute_yml)
    param_get_attributes_valid = [tuple(i) for i in yp.valid_params("param_get_attributes")]
    print(yp.valid_params("param_get_attributes"))
    print(yp.invalid_params("param_add_attribute"))

    #
    # param_name_correct = p.valid_params("param_name")
    # print(param_name_correct)
    # param_name_wrong = p.invalid_params("param_name")
    # print(param_name_wrong)
    #
    # param_inputset_correct = p.valid_params("param_inputset")
    # print(param_inputset_correct)
    # param_inputset_wrong = p.invalid_params("param_inputset", "image_gen_input.json")
    # print(param_inputset_wrong)

from tinydb import TinyDB, Query, where
from flask import Flask, abort, request
from pprint import pprint, pformat
from ad_set_gpu import set_gpu
import shutil
import os
import numpy as np
import copy
import random
import time
import json
import threading
import traceback
import ast
import requests
import logging
import heapq

Query, where = Query, where


def get_logger(path='log/logger.log', out_log=('ERROR', 'CRITICAL'), mode='w'):
    """
    获取可以写入文件的日志类, 需要包 logging, os
    :param path: str; 输出的日志路径文件, 会根据out_log重命名文件
    :param out_log: list or tuple; 包含哪几种类型的日志文件, 可以包括: DEBUG,INFO,WARNING,ERROR,CRITICAL
    :param mode: str; 日志写入的模式, w表示覆盖, a表示追加
    :return: logger
    """
    print(__file__)
    # 创建目录
    dir = os.path.split(path)[0]
    if dir and not os.path.exists(dir):
        os.makedirs(dir)
    # 创建日志类
    logger = logging.getLogger()
    logger.setLevel(logging.NOTSET)
    # 创建日志文件
    for name in out_log:
        fname, fextension = os.path.splitext(path)
        fh = logging.FileHandler(f'{fname}.{name.lower()}{fextension}', mode=mode)
        fh.setLevel(name)
        fh.setFormatter(logging.Formatter(
            # 输出例如: 2021-04-05 15:47:28,573 - shiyan3.py/<module>[line:28] - ERROR: 你好
            "%(asctime)s - %(filename)s/%(funcName)s[line:%(lineno)d] - %(levelname)s: %(message)s"
        ))
        logger.addHandler(fh)
    return logger


class TaskDB:
    def __init__(self, dir, new=False):
        """
        :param dir: str; 参数数据库的存储文件夹, 文件夹下还将存储其他main_path. 文件夹内其他数据可能会被清理数据(见close函数)
        :param new: bool; 是否覆盖该路径原有数据库. 注意: 如果为True, 哪怕正在使用中的数据库也会覆盖
        """
        # 不存在目录新建
        if not os.path.exists(dir):
            os.makedirs(dir)
        # 镜像主目录, 用于是否重新清理参数
        db_folder = f'{dir}/database'
        if not os.path.exists(db_folder):
            os.makedirs(db_folder)
        # 生成数据库
        path = f'{db_folder}.json'
        if new or not os.path.exists(path):
            db = TinyDB(path, encoding='utf8', access_mode='w+')
        else:
            db = TinyDB(path, encoding='utf8', access_mode='r+')
        self._db_tasks = db.table("tasks")
        self._db = db
        self._dir = dir.rstrip('/\\')
        self._db_folder = db_folder.rstrip('/\\')
        self.clean()

    @property
    def result(self):
        """
        子类需要在父类基础上重载
        一个任务-结果模版. 兼容TinyDB需要key只能是str类型, 且不能有set, vaule不能带有双引号, TinyDB不支持多线程(需要lock)
        :return:
        """
        result = {
            'no': '1617199720.1552498-0.17835507118070226',  # 任务唯一编号 - 构建任务的时间时间戳+随机数, 极低概率重复
            # add_task 时修改
            'paras': {'test': [1, 2], },  # run_task 需要的参数
            'filter': {},  # 用于结果过滤的相关参数, 不能有test123
            'priority': 1,  # 任务运行的优先级, 数值越小越优先, 并行时小数值任务未完考虑不运行后面任务. 防止任务之间的依赖
            # run_task 时修改
            'executed': False,  # 是否已执行得到结果
            'machine': {},  # 完成这个任务的机器信息, 可以使用 TaskDB.get_machine()
            'main_path': 'None',  # 数据生成的主目录, 和数据库文件目录同级, 不能叫databas(或者以__开头), 用于快捷手动重置任务(删除database中对应文件夹即可)
        }
        return result

    @property
    def db_dir(self):
        """
        数据库文件所在主目录
        :return:
        """
        return self._dir

    @property
    def tasks(self):
        """
        返回数据库中的所有任务, 没有深拷贝, 注意不要修改
        :return:
        """
        return self._db_tasks.all()

    @staticmethod
    def get_machine(name='default', is_gpu=None, **kwargs):
        """
        完成这个任务的机器信息
        :param name: str; 自定义名字
        :param is_gpu: bool; 是否使用gpu
        :param kwargs:
        :return:
        """
        ret = set_gpu(return_more=True)
        ret.update({
            'name': name,
            'is_gpu': is_gpu,
        })
        return ret

    @staticmethod
    def numpy_to_base(result, print_type=False):
        """
        递归将 result 中可能是numpy的结果转换python基本类型, 防止无法写入json数据库
        :param result:
        :param print_type: bool; 是否输出每个修改后的所有类型及变量的前30个字符, 用于调试
        :return:
        """
        if isinstance(result, dict):
            result_ = {}
            for k, v in result.items():
                result_[k] = TaskDB.numpy_to_base(v, print_type)
        elif isinstance(result, tuple) or isinstance(result, list):
            result_ = [TaskDB.numpy_to_base(v, print_type) for v in result]
        elif "'numpy." in str(type(result)):
            result_ = np.array(result).tolist()
        elif isinstance(result, set):
            raise NameError(f'tinydb数据库不能存入set类型: {result}')
        else:
            if isinstance(result, str) and '"' in result:
                raise NameError('不能带有双引号!', result)
            result_ = result
        if print_type:
            return print(type(result_), ':', str(result_)[:30], '...')
        return result_

    @staticmethod
    def _result_to_query(result: dict, root='Query()'):
        """
        将结果模版转换为 TinyDB 的查询形式, 然后用 eval(). 这是对存在参数完全相等的匹配
        list/tuple 匹配不考虑顺序
        如果 list/tuple 中有 list/tuple 那就要一摸一样才能匹配上
        如果 list/tuple 中的 list/tuple 有 tuple 则匹配不上
        :param result: 参考 一个任务-结果模版
        :return: str
        """
        q_L = []
        for k, v in result.items():
            root_ = f'{root}["{k}"]'
            q = ''
            if isinstance(v, dict):
                q = TaskDB._result_to_query(v, root_)
            elif isinstance(v, tuple) or isinstance(v, list):
                v_ = []
                for i in v:
                    if isinstance(i, dict):
                        i = TaskDB._result_to_query(i, 'Query()')
                        if i:
                            i = f'{root_}.any({i})'
                            q_L.append(i)  # list/tuple 中有 dist
                    else:
                        if isinstance(i, tuple):  # list/tuple 中有 tuple
                            i = list(i)
                        v_.append(i)
                if v_:
                    q = f'{root_}.all({v_})'
            else:
                if isinstance(v, str):  # str需要加双引号
                    v = f'"{v}"'
                q = f'({root_} == {v})'
            if q:
                q_L.append(q)
        return ' & '.join(q_L)

    def add_task(self, paras, filter=None, priority=1):
        """
        增加一个任务
        :param paras: dict; 运行任务需要的参数
        :param filter: None or dict; 结果过滤器
        :param priority: int; 任务运行的优先级, 数值越小越优先, 并行时小数值任务未完考虑不运行后面任务
        :return: the inserted document's ID
        """
        result = self.result
        result.update({
            'no': f'{time.time()}-{random.random()}',
            'paras': copy.deepcopy(paras),
            'filter': copy.deepcopy(filter),
            'priority': priority,
            'executed': False,
        })
        result = self.numpy_to_base(result)
        return self._db_tasks.insert(result)  # 返回 doc_id

    def add_tasks(self, info_L):
        """
        增加多个任务, 速度快
        :param info_L: [{'paras':dict,..},..]; 一个list, 每个元素是一个和 add_task 参数一样的 dict
            默认值会被填充
        :return: a list containing the inserted documents' IDs
        """
        result_L = []
        for info in info_L:
            try:
                paras = info['paras']
                filter = info.setdefault('filter', None)
                priority = info.setdefault('priority', 1)
            except:
                pprint('info:', info)
                raise
            result = self.result
            result.update({
                'no': f'{time.time()}-{random.random()}',
                'paras': copy.deepcopy(paras),
                'filter': copy.deepcopy(filter),
                'priority': priority,
                'executed': False,
            })
            result = self.numpy_to_base(result)
            result_L.append(result)
        return self._db_tasks.insert_multiple(result_L)  # 返回 [doc_id,..]

    def del_task(self, result):
        """
        删除一个结果, 输出的数据会被保留
        :param result: dict; 部分类似 result 的格式
        :return: a list containing the removed documents' ID
        """
        result = self.numpy_to_base(result)
        result = self._result_to_query(result)
        return self._db_tasks.remove(eval(result))

    def que_task(self, result):
        """
        查询一个结果
        :param result: dict; 部分类似 result 的格式
        :return: list of matching documents
        """
        result = self.numpy_to_base(result)
        result = self._result_to_query(result)
        return self._db_tasks.search(eval(result))

    def update_one(self, result, no):
        """
        更新一个结果, 如果已执行的话会生成完成标志的镜像文件夹, main_path没有提供会生成默认
        :param result: dict; 部分类似 result 的格式
        :param no: result['no']; 编号, 用于查找对应的结果
        :return: result
        """
        try:
            result = self.numpy_to_base(result)
            doc_ids = self._db_tasks.update(result, Query()['no'] == no)
            assert len(doc_ids) == 1, f'更新任务数量应等于1!, {doc_ids}'
            doc = self._db_tasks.get(doc_id=doc_ids[0])
            # 生成镜像文件夹
            if doc['executed']:
                db_path = f"{self._db_folder}/{doc['main_path']}"
                if not os.path.exists(db_path):
                    os.makedirs(db_path)
        except:  # 错误检查
            result = self.numpy_to_base(result, True)
            print('result:')
            pprint(result)
            self._db_tasks.update(result, Query()['no'] == no)
            raise
        return doc

    def update_multiple(self, info_L):
        """
        更新多个结果-加速, 如果已执行的话会生成完成标志的镜像文件夹, main_path没有提供会生成默认
        :param info_L: [{'result':dict,..},..]; 一个list, 每个元素是一个和 update_one 参数一样的 dict
        :return: list of result
        """
        results_L = []
        for info in info_L:
            try:
                result = self.numpy_to_base(info['result'])
                no = Query()['no'] == info['no']
            except:
                pprint('info:', info)
                raise
            results_L.append((result, no))
        try:
            doc_ids = self._db_tasks.update_multiple(results_L)
            assert len(doc_ids) == len(results_L), f'更新任务数量应等于要更新的数量!, {len(doc_ids)}!={len(results_L)}'
            doc_L = []
            for doc_id in doc_ids:
                doc = self._db_tasks.get(doc_id=doc_id)
                # 生成镜像文件夹
                if doc['executed']:
                    db_path = f"{self._db_folder}/{doc['main_path']}"
                    if not os.path.exists(db_path):
                        os.makedirs(db_path)
                doc_L.append(doc)
        except:  # 错误检查
            print('results_L:')
            pprint(results_L)
            raise
        return doc_L

    def output_table(self, path=None, cols_limit=100, col_front=('main_path', 'executed', 'priority'),
                     col_back=('no',)):
        """
        将整个数据库的内容全部用tab表格\t的形式输出, 第一行是展开的表头(排序), 行顺序是tasks默认顺序
        :param path: str or None; 表格输出的路径, None表示输出在数据库内
        :param cols_limit: int; 最多输出多少列
            多余的列会不输出(不断的展开最少数量的dict到不能展开,list会直接输出而不展开),只输出排序后的最后一列
            每个 self.result 的根参数都会输出来
        :param col_front: list or tuple; 手动放前面的键值, 剩下的顺序排序
            不在task中的属性会被忽略, 嵌入属性使用"分隔父子层次
        :param col_back: list or tuple; 手动放后面的键值, 剩下的顺序排序
            不在task中的属性会被忽略, 嵌入属性使用"分隔父子层次
        :return:
        """
        if not path:
            path = f'{self.db_dir}/all_task_table.txt'
        tasks = self.tasks

        # 先一层层展开, 用"连接起dict的命名, 得到值dict
        def extend_f(content, x=None, root=''):
            if x is None:
                x = {}
            if isinstance(content, dict):
                for k, v in content.items():
                    extend_f(v, x, root + f'"{k}')
            else:
                x[root[1:]] = str(content)
            return x  # {'列名':值,..}

        col_content_D = {}  # {'列名':[],..}
        for i, task in enumerate(tasks):
            x = extend_f(task)
            # 先填充col_content_D中有的, 保证每列对应
            for k, v in col_content_D.items():
                if k in x:
                    v.append(x.pop(k))
                else:
                    v.append('')  # 没有的话填空
            # 填充col_content_D中没有的
            for k, v in x.items():
                col_content_D[k] = [''] * int(i) + [v]

        # 依据值dict还原出嵌套字典
        nest_D = {}  # {'列名':{'列名':{..},..},..}

        def nest_f(s_L, d_D=None, root=''):
            if d_D is None:
                d_D = nest_D
            root += f'"{s_L[0]}'
            root_ = root[1:]  # 去除第一个 "
            if root_ not in d_D:
                d_D[root_] = {}
            if len(s_L) > 1:
                nest_f(s_L[1:], d_D[root_], root)

        for k in col_content_D.keys():
            nest_f(k.split('"'))

        # 依据嵌套字典控制展示数量, 层次遍历+排序
        partCol_content_D = nest_D.copy()  # {'partCol':{..},..}
        min_partCol_content = heapq.nlargest(1, partCol_content_D.items(), key=lambda t: -len(t[1]) if t[
            1] else -10 ** 100)[0]  # ('partCol',{..}), 最小非空值
        while len(partCol_content_D) + len(min_partCol_content[1]) - 1 <= cols_limit:
            # 如果最小值已经无法展开
            if len(min_partCol_content[1]) == 0:
                break
            partCol_content_D.pop(min_partCol_content[0])  # 出栈扩展最少数量那个
            partCol_content_D.update(min_partCol_content[1])  # 加入最少数量那个
            min_partCol_content = heapq.nlargest(1, partCol_content_D.items(), key=lambda t: -len(t[1]) if t[
                1] else -10 ** 100)[0]  # ('partCol',{..}), 最小非空值

        # col倒叙过滤
        partCol_S = set(partCol_content_D)
        colNew_content_D = {}  # 过滤后将要输出的, 和 col_content_D 格式一样
        for col, content_L in sorted(col_content_D.items(), reverse=True):
            col_L = col.split('"')
            c = None
            for i in range(len(col_L), 0, -1):  # 从长到短遍历
                c = '"'.join(col_L[0:i])
                if c in partCol_S:  # 可以输出
                    break
                else:
                    c = None
            if c:
                colNew_content_D[col] = content_L
                partCol_S.remove(c)
            if len(partCol_S) == 0:
                break
        colNew_L = list(set(colNew_content_D) - set(col_front) - set(col_back))  # ['col',..]
        colNew_L.sort()
        colNew_L = [i for i in col_front if i in colNew_content_D] + colNew_L + \
                   [i for i in col_back if i in colNew_content_D]

        # tab隔开col展示
        with open(path, 'w', encoding='utf8') as w:
            w.write('\t'.join(colNew_L) + '\n')
            for i in range(len(colNew_content_D[colNew_L[0]])):
                w.write(colNew_content_D[colNew_L[0]][i])
                for col in colNew_L[1:]:
                    w.write('\t' + colNew_content_D[col][i])
                w.write('\n')
        return path

    def get_uncomplete_tasks(self):
        """
        获取未完成的任务
        :return:
        """
        tasks = self._db_tasks.search(where('executed') == False)
        # 按照优先级排序
        tasks = sorted(tasks, key=lambda d: d['priority'])
        return tasks

    def run_task(self, **kwargs):
        """
        需要重载, 循环完成未完成的任务
        :return:
        """
        tasks = self.get_uncomplete_tasks()
        完成任务 = 0
        # 对于每个任务
        while len(tasks) != 0:
            if len(tasks) != 0:
                task = tasks.pop(0)
            paras = copy.deepcopy(task['paras'])  # 后续可能需要修改
            # 结果过滤
            result = {}
            filter = task['filter']
            if not filter:  # 防止无参数输入错误
                filter = {'test': None}
            while self.filtrate_result(result, **filter):
                # 运行得到结果
                time_start = time.time()
                result = {
                    'executed': True,
                    'main_path': str(len(tasks)),
                    'machine': self.get_machine(),
                    'time_start': time_start,
                }
            # 写入数据
            self.update_one(result, task['no'])
            完成任务 += 1
            print('=' * 20, '本次任务结果:')
            pprint(result)
            print('=' * 20, f'已完成第{完成任务}个任务, 剩余{len(tasks)}个.')
            print()

    def stat_result(self, out_tasked=False, **kwargs):
        """
        可以重载, 统计结果
        :param out_tasked: bool; 是否输出所有任务
        :return:
        """
        tasks = self._db_tasks.search(where('executed') == True)
        print('已完成任务数:', len(tasks), '; 未完成任务数:', len(self._db_tasks.all()) - len(tasks))
        if out_tasked:
            print('=' * 10, '所有已完成任务:')
            pprint(tasks)
            print('=' * 10, '所有未完成任务:')
            pprint(self._db_tasks.search(where('executed') == False))

    def filtrate_result(self, result, **kwargs):
        """
        需要重载, 对参数返回结果进行过滤, 如果结果不好就重新执行任务. 使用 api 建议用 no 寻找 filter
        :param result: dict;
        :param kwargs: 其他参数
        :return: bool; True 表示结果过滤掉
        """
        if not result:
            return True
        return False

    def clean(self):
        """
        清理主目录下非完成任务的文件夹, __开头不删除, 非文件夹不删除
        main_path 中有文件缺失的完成任务会被重制为未完成任务, 并清除原文件夹
        :return:
        """
        tasks = self._db_tasks.search(where('executed') == True)
        path_S = {f"{self._dir}/" + t['main_path'].rstrip('/\\') for t in tasks}  # 每个已执行参数的主目录
        path_S |= {self._db_folder}  # 镜像主目录不删除
        # 删除多余路径数据
        n = 1
        for i, p in enumerate(os.listdir(self._dir)):
            p_ = p
            p = f"{self._dir}/{p}"
            if os.path.isdir(p) and p not in path_S and p_[:2] != '__':
                shutil.rmtree(p)
                print(f'删除多余路径数据({n}):', p)
                n += 1
        # 删除缺失镜像文件夹数据并重置任务
        n = 1
        valid_path = set()  # 有效的 main_path 用于清理镜像主目录
        info_L = []
        for i, t in enumerate(tasks):
            main_path = t['main_path'].rstrip('/\\')
            p = f"{self._dir}/{main_path}"
            dp = f"{self._db_folder}/{main_path}"
            if not os.path.exists(dp):
                if os.path.isdir(p):
                    shutil.rmtree(p)  # 必须是目录
                print(f'删除缺失镜像文件夹数据({n}):', p)
                n += 1
                info_L.append({'result': {'executed': False}, 'no': t['no']})
            else:
                valid_path.add(dp)
        if info_L:
            print('重置缺失镜像文件夹任务...')
            print(len(self.update_multiple(info_L)), '个任务重置')
        # 删除多余镜像主目录中的文件夹
        n = 1
        for i, p in enumerate(os.listdir(self._db_folder)):
            p = f"{self._db_folder}/{p}"
            if os.path.isdir(p) and p not in valid_path:
                shutil.rmtree(p)
                print(f'删除多余镜像主目录中的文件夹({n}):', p)
                n += 1

    def close(self):
        """
        关闭数据库
        :return:
        """
        self.clean()
        self._db.close()

    @staticmethod
    def test(db):
        obj = TaskDB(db, new=True)
        n = 5
        for i in range(n - 3):
            print('增加任务:', obj.add_task(obj.result['paras'], priority=i))
        info_L = []
        for i in range(n - 3, n):
            info_L.append({
                'paras': obj.result['paras'],
                'priority': i,
            })
        print('增加任务s:', obj.add_tasks(info_L))
        print()
        print('查询任务:')
        q_L = obj.que_task({'paras': obj.result['paras']})
        print(q_L)
        # print(TaskDB._result_to_query({'paras': obj.result['paras']}))
        print()
        print('运行任务:')
        obj.run_task()
        print('更新任务:')
        print(obj.update_one({'executed': False}, q_L[0]['no']))
        info_L = [
            {'result': {'executed': False}, 'no': q_L[1]['no']},
            {'result': {'test': 123}, 'no': q_L[-1]['no']},
        ]
        print(obj.update_multiple(info_L))
        print()
        print('统计结果:')
        obj.stat_result(out_tasked=True)
        print()
        print('输出表格展示:')
        print(obj.output_table())
        print(obj.output_table(path=f'{db}/all_task_table_14.txt', cols_limit=14))
        print(obj.output_table(path=f'{db}/all_task_table_17.txt', cols_limit=17))
        print()
        print('关闭数据库:')
        obj.close()


class TaskDBapi:
    @staticmethod
    def app_run(db_dirs: list, port=19999, log_path=f'log/TaskDBapi.app_run.log'):
        """
        将数据库做成 http api 用于分布式机器任务分配
        :param db_dirs: [数据库目录1,..]
        :param port: int; 访问端口
        :param log_path: str; 日志输出地址
        :return:
        """
        if not db_dirs:
            return None
        db_obj_D = {d: TaskDB(d) for d in db_dirs}  # 所有数据库
        db_no_tasks_D = {}  # {dir:{no:task,..},..}; 所有数据库的未完成任务
        db_assigned_task_D = {d: [] for d in db_dirs}  # {dir:[no,..],..}; 所有已分配任务no序列
        db_unassigned_task_D = {d: [] for d in db_dirs}  # {dir:[no,..],..}; 所有未分配任务no序列
        for d in db_dirs:
            db_no_tasks_D[d] = {}  # {no:task,..}
            db_unassigned_task_D[d] = []  # [no,..]; 按这个顺序分配任务
            for task in db_obj_D[d].get_uncomplete_tasks():
                no = task['no']
                db_no_tasks_D[d][no] = task
                db_unassigned_task_D[d].append(no)
        all_assigned_no_L = []  # [no,..]; 所有分配过的编号记录, 回退的不会删除
        api_access_times = [0]  # api访问次数
        logger = get_logger(log_path)

        # 获取-回退任务方法
        def one_task(db, no=None):
            """
            获取/回退一个任务, 获取任务考虑优先级问题
            :param db: post_dict['db']
            :param no: None or str; 如果是None则获取任务, 否则回退任务
            :return:
            """
            task = {}
            if no:  # 回退任务
                if no not in db_assigned_task_D[db]:
                    describe = '回退失败-这不是已分配任务no: ' + no
                    status = 0
                else:
                    db_assigned_task_D[db].remove(no)  # 去除已分配
                    db_unassigned_task_D[db].insert(0, no)  # 变成未分配
                    task = db_no_tasks_D[db][no]
                    describe = '回退任务成功'
                    status = 1
            else:  # 获取任务
                if len(db_unassigned_task_D[db]) == 0:
                    describe = '所有任务已完成'
                    status = 2
                    if len(db_assigned_task_D[db]) != 0:
                        describe += ', 现将已分配的任务再分配!'
                        no = db_assigned_task_D[db][0]  # 获取任务编号
                        task = db_no_tasks_D[db][no]  # 获取任务
                        status = 3
                else:
                    no = db_unassigned_task_D[db][0]  # 获取任务编号
                    task = db_no_tasks_D[db][no]  # 获取任务
                    priority_S = {db_no_tasks_D[db][i]['priority'] for i in db_assigned_task_D[db]}
                    if len(priority_S) >= 1 and list(priority_S)[0] != task['priority']:
                        describe = f"高优先级任务还未全部完成: {list(priority_S)[0]}!={task['priority']}, " \
                                   f"最近一次分配过的编号: {all_assigned_no_L[-1]}, 现将已分配的任务再分配"
                        no = db_assigned_task_D[db][0]  # 获取任务编号
                        task = db_no_tasks_D[db][no]  # 获取任务
                        status = 4
                    else:
                        db_unassigned_task_D[db].pop(0)  # 去除未分配
                        db_assigned_task_D[db].append(no)  # 变成已分配
                        describe = '获取任务成功'
                        status = 5
            return no, task, describe, status  # 获取时task={}表示获取失败

        # 启动
        app = Flask(__name__)
        lock = threading.RLock()

        @app.route('/api', methods=['POST'])
        def api():
            """
            status 含义在代码中查看
            request_data: dict
                type: 必填, 3种请求模式 request/complete/failure
                    request: 请求任务
                    complete: 完成任务
                    failure: 任务不合适, 会重新放在队列前面
                db: 必填, 数据库名字(db_dir)
                no: complete, 完成任务的编号
                result: complete, 完成任务的结果
                filter: 是否过滤完成结果, 1表示过滤, 0表示不过滤
                brief_out: 是否简化输出, 1表示简化, 0表示不简化. 未实现功能
            :return:
            """
            start_queue = time.time()
            lock.acquire()  # 加锁
            start = time.time()
            api_access_times[0] += 1
            print()
            response = {'task': {}, 'type': 'normal', 'error': '', 'message': '', 'status': 0}
            out_request = None
            try:
                post_dict = dict(request.form)
                assert 'type' in post_dict, '缺少 type 请求类型(request/complete/failure)!'
                assert 'db' in post_dict, '缺少 db 数据库参数!'
                filter = int(post_dict.setdefault('filter', 1))
                brief_out = int(post_dict.setdefault('brief_out', 1))
                db = post_dict['db']
                # 请求任务
                if post_dict['type'] == 'request':
                    no, task, describe, status = one_task(db)[:4]
                    response['task'] = task
                    print(describe)
                    if task:
                        all_assigned_no_L.append(no)
                    response['message'] = describe
                    response['status'] = status
                # 完成任务
                elif post_dict['type'] == 'complete':
                    assert 'no' in post_dict, '缺少 no 任务编号!'
                    assert 'result' in post_dict, '缺少 result 任务结果!'
                    no = post_dict['no']
                    result = ast.literal_eval(post_dict['result'])  # str转类型
                    result['executed'] = True  # 表示执行完成
                    post_dict['result'] = result  # 为了pformat输出更好看
                    # 已分配还是未分配
                    if no in db_assigned_task_D[db]:
                        message = '已分配'
                        tasks = db_assigned_task_D[db]
                    elif no in db_unassigned_task_D[db]:
                        message = '未分配(会忽略优先级)'
                        tasks = db_unassigned_task_D[db]
                    else:
                        response['status'] = -1
                        raise NameError('完成任务失败-不是已分配/未分配的no')
                    # 过滤
                    if filter and db_obj_D[db].filtrate_result(result, no=no, api=True):
                        one_task(db, no=no)
                        response['status'] = 0
                        raise NameError(f'完成{message}任务失败-没有通过 filtrate_result 检测!')
                    # 更新任务
                    db_obj_D[db].update_one(result, no)
                    tasks.remove(no)  # 去除完成的任务
                    print(f'完成并写入一个{message}任务no:', no)
                    response['message'] = f'完成并写入一个{message}任务'
                    response['status'] = 1  # >=1 表示任务完成
                # 任务不合适
                elif post_dict['type'] == 'failure':
                    assert 'no' in post_dict, '缺少 no 任务编号!'
                    no, task, describe, status = one_task(db, no=post_dict['no'])[:4]  # 回退任务
                    response['task'] = task
                    print(describe)
                    response['message'] = describe
                    response['status'] = status
                # 错误参数
                else:
                    raise NameError('type 参数错误!')
                out_request = f'请求信息:\n' + pformat(post_dict) + \
                              f"\n数据库({db})启动api时的未完成任务: {len(db_no_tasks_D[db])}/{len(db_obj_D[db].tasks)}; " \
                              f"未分配: {len(db_unassigned_task_D[db])}; " \
                              f"已分配: {len(db_assigned_task_D[db])}"
                logger.critical(out_request + '\n')  # 日志
            except Exception as e:
                error = traceback.format_exc()
                print(error, end='')
                logger.critical('error\n' + error)
                response['type'] = 'error'
                response['message'] = 'error'
                e = str(e).replace("\n", " ")
                response['error'] = 'error'f'{type(e)}: {e}'
            out_response = f'返回信息:\n' + pformat(response) + \
                           f"\napi耗时: {round(time.time() - start, 4)}s; " \
                           f"排队耗时: {round(abs(start_queue - start), 4)}s; " \
                           f"api已访问次数: {api_access_times[0]}"
            print(out_response)
            logger.critical(out_response + '\n')  # 日志
            if out_request:  # 请求结果在前端输出放在后面, 方便查看
                print(out_request)
            lock.release()  # 去锁
            response = json.dumps(response, ensure_ascii=False, indent=2)
            return response

        print('接口可运行在:', f'http://{TaskDB.get_machine()["ip"]}:{port}/api')
        app.run(host='0.0.0.0', port=port, debug=False)

    @staticmethod
    def request_api(request_data: dict, url='http://127.0.0.1:19999', sleep=0.5, try_times=5, db_dir=None):
        """
        app_run.api() 对应的客户端
        :param request_data: dict; 与 app_run.api() 中的 request_data 一致, request/complete/failure
        :param url: str; 获取数据的api接口, 不需要router
        :param sleep: float or int; 访问间隔, 防止过于频繁, 单位秒
        :param try_times: int; 访问几次失败就返回失败
        :param db_dir: str or None; 用于将完成的文件移动到子文件夹, str且已完成才会移动
        :return:
        """
        url = '/'.join(url.split('/')[:3]) + '/api'
        response = {}
        for i in range(try_times):
            time.sleep(sleep)
            try:
                response = json.loads(requests.post(url, data=request_data).text)
                break
            except:
                print(f'request_api 失败{i + 1}次:')
                traceback.print_exc()
                time.sleep(sleep)
        # completed_move
        if db_dir and 'status' in response and response['status'] >= 1 and request_data['type'] == 'complete':
            result = ast.literal_eval(request_data['result'])
            assert 'main_path' in result, '请求完成结果中没有主目录 main_path !' + str(result)
            TaskDBapi.completed_move(db_dir, completed_path=result['main_path'])
        return response

    @staticmethod
    def completed_move(db_dir, completed_path):
        """
        用于将完成的 main_path 文件夹移动到 __completed, 防止因中断导致大量未完成文件夹的产生.
        __completed 中已经有 completed_path 的会被删除
        :param db_dir: str; 生成数据的主目录, 用于保存 main_path, 最后其子目录__completed中的内容需要剪切到api数据库的位置
        :param completed_path: str; main_path, 向 __completed 中移动已完成的子文件夹
        :return:
        """
        if not os.path.exists(f'{db_dir}/__completed'):
            os.makedirs(f'{db_dir}/__completed')
        src = f'{db_dir}/{completed_path}'
        dst = f'{db_dir}/__completed/{completed_path}'
        if os.path.exists(src):
            if os.path.exists(dst):
                shutil.rmtree(dst)
            shutil.move(src, dst)
            return True
        else:
            return False

    @staticmethod
    def test():
        """
        连续运行两次分别测试服务端和客户端
        :return:
        """
        db = 'test_TaskDB'
        port = 19998
        url = f'http://127.0.0.1:{port}'
        if not TaskDBapi.request_api({}, try_times=3, url=url):  # 是否有服务器存在
            TaskDB.test(db)  # 注意这里运行两次会覆盖TaskDB
            TaskDBapi.app_run(db_dirs=[db], port=port)
        else:
            response = TaskDBapi.request_api(request_data={'type': 'request', 'db': db}, url=url)
            response = TaskDBapi.request_api(request_data={'type': 'failure', 'db': db, 'no': response['task']['no']},
                                             url=url)
            response = TaskDBapi.request_api(request_data={'type': 'request', 'db': db}, url=url)
            while response['task']:
                response = TaskDBapi.request_api(
                    request_data={'type': 'complete', 'db': db, 'no': response['task']['no'],
                                  'result': "{'test': 123}"}, url=url)
                response = TaskDBapi.request_api(request_data={'type': 'request', 'db': db}, url=url)


if __name__ == '__main__':
    TaskDBapi.test()

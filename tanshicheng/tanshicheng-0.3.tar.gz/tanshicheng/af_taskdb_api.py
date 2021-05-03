from tinydb import TinyDB, Query, where
from flask import Flask, abort, request
import shutil
import os
import numpy as np
import copy
import random
import time
import json
import threading
import subprocess
import traceback
import socket
import ast
import requests
import logging
from pprint import pprint, pformat


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
        hostname = subprocess.getstatusoutput('hostname')[1]
        ip = socket.gethostbyname(hostname)
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('8.8.8.8', 80))
            ip = s.getsockname()[0]
        except:
            ...
        return {
            'name': name,
            'hostname': hostname,
            'ip': ip,
            'is_gpu': is_gpu,
        }

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
        for i, t in enumerate(tasks):
            main_path = t['main_path'].rstrip('/\\')
            p = f"{self._dir}/{main_path}"
            dp = f"{self._db_folder}/{main_path}"
            if not os.path.exists(dp):
                shutil.rmtree(p)  # 必须是目录
                print(f'删除缺失镜像文件夹数据并重置任务({n}):', p)
                n += 1
                self.update_one({'executed': False}, t['no'])
            else:
                valid_path.add(dp)
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
        for i in range(5):
            print('增加任务:', obj.add_task(obj.result['paras'], priority=i))
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
        print(obj.update_one({'executed': False}, q_L[1]['no']))
        print(obj.update_one({'test': 123}, q_L[-1]['no']))
        print()
        print('统计结果:')
        obj.stat_result(out_tasked=True)
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
    def request_api(request_data: dict, url='http://127.0.0.1:19999/api', sleep=0.5, try_times=5, db_dir=None):
        """
        app_run.api() 对应的客户端
        :param request_data: dict; 与 app_run.api() 中的 request_data 一致, request/complete/failure
        :param url: str; 获取数据的api接口
        :param sleep: float or int; 访问间隔, 防止过于频繁, 单位秒
        :param try_times: int; 访问几次失败就返回失败
        :param db_dir: str or None; 用于completed_check, None表示不使用completed_check
        :return:
        """
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
        # completed_check
        if db_dir and 'type' in request_data and 'db' in request_data:
            # 这些请求后清洗目录
            if request_data['type'] in {'request', 'failure'}:
                TaskDBapi.completed_check(db_dir)
            # 完成后生成镜像文件夹
            elif request_data['type'] == 'complete' and 'status' in response and response['status'] >= 1:
                result = ast.literal_eval(request_data['result'])
                assert 'main_path' in result, '请求完成结果中没有主目录 main_path !' + str(result)
                TaskDBapi.completed_check(db_dir, completed_path=result['main_path'])
        return response

    @staticmethod
    def completed_check(db_dir, completed_path=None):
        """
        用于清理客户端未完成 main_path 文件夹, 防止因中断导致大量未完成文件夹的产生.
        run_task 完成一次需要调用一次 completed_path 以记录, 开头和结尾一般也需要.
        :param db_dir: str; 生成数据的主目录, 用于保存 main_path, 最后其子目录需要剪切到api数据库的位置
            注意: 如果 completed_path==None, 删除 db_dir/__completed 中没有但是 db_dir 中有的子文件夹
        :param completed_path: None or str; main_path, 向 __completed 中增加已完成的子文件夹
        :return:
        """
        if not os.path.exists(f'{db_dir}/__completed'):
            os.makedirs(f'{db_dir}/__completed')
        if completed_path:
            os.makedirs(f'{db_dir}/__completed/{completed_path}')
        else:
            __completed_S = set(os.listdir(f'{db_dir}/__completed'))
            n = 1
            for i, p in enumerate(os.listdir(f'{db_dir}')):
                p_ = p
                p = f"{db_dir}/{p}"
                if os.path.isdir(p) and p_ not in __completed_S and p_ != '__completed':
                    shutil.rmtree(p)
                    print(f'删除未完成文件数据({n}):', p)
                    n += 1

    @staticmethod
    def test():
        """
        连续运行两次分别测试服务端和客户端
        :return:
        """
        db = 'test_TaskDB'
        if not TaskDBapi.request_api({}, try_times=3):  # 是否有服务器存在
            TaskDB.test(db)  # 注意这里运行两次会覆盖TaskDB
            TaskDBapi.app_run(db_dirs=[db])
        else:
            response = TaskDBapi.request_api(request_data={'type': 'request', 'db': db})
            response = TaskDBapi.request_api(request_data={'type': 'failure', 'db': db, 'no': response['task']['no']})
            response = TaskDBapi.request_api(request_data={'type': 'request', 'db': db})
            while response['task']:
                response = TaskDBapi.request_api(
                    request_data={'type': 'complete', 'db': db, 'no': response['task']['no'],
                                  'result': "{'test': 123}"})
                response = TaskDBapi.request_api(request_data={'type': 'request', 'db': db})


if __name__ == '__main__':
    TaskDBapi.test()

import json
import os
from random import sample

import networkx as nx
import yaml

from adb import list_packages, uninstall_pkg, install_pkg
from AddUserCase import AddUserCase
from dbsql import sql2key, sql2dict
from page import name2short, img_path, ope2num


def manual_case(add_case_list):
    mcase = dict()
    add_ks = AddUserCase()
    add_ks.add_case_db(add_case_list)
    add_ks.case2list()
    mcase['add_img_dict_'] = add_ks.add_img_dict
    mcase['show_json'] = add_ks.show_case_list
    mcase['sj'] = add_ks.show_img_list
    del add_ks
    return mcase


def leaves2tree(user_id, recom_num, op_values, po_values, object_values, page_values):
    pageKey_op = sql2key(op_values, 'page_id')
    objectKey_po = sql2key(po_values, 'object_id')
    pageKey = sql2dict(page_values)
    objectKey = sql2dict(object_values)

    goal_id_arr_ = list()

    for k, v in objectKey.items():
        if v['valid'] == 1:
            goal_id_arr_.append(k)

    # print('goal_id_arr_', goal_id_arr_)

    sample_arr = list(set(list(objectKey.keys())).difference(set(goal_id_arr_)))
    # print('sample_arr', sample_arr)
    print('recom_num', recom_num)
    print('sample_arr', sample_arr)

    goal_id_arr = sample(sample_arr, len(sample_arr) if recom_num > len(sample_arr) else recom_num)
    goal_id_arr_.extend(goal_id_arr)
    # print('goal_id_arr_', goal_id_arr_)

    object_dict_short = object_short_path2root(objectKey_po, pageKey_op, goal_id_arr_)
    return case_image2html(user_id, pageKey, objectKey, object_dict_short)


def leaf2tree(object_id, object_values, op_values, po_values, object_db_in_values, object_db_no_values):
    object_dict = sql2dict(object_values)
    pageKey_op = sql2key(op_values, 'page_id')
    objectKey_po = sql2key(po_values, 'object_id')

    goal_list = object_short_path2root(objectKey_po, pageKey_op, [object_id])
    print('goal_list', goal_list)

    result = case_imahtml(object_id, goal_list, object_dict, object_db_in_values, object_db_no_values)
    return result


def object_short_path2root(objectKey_po, pageKey_op, goal_id_arr_):
    object_dict_short = dict()

    def tree_root(object_id_list, object_list):
        if str(object_id_list[0]) in object_dict_short.keys() \
                and len(object_dict_short[str(object_id_list[0])]) <= len(object_list):
            return
        object_id = object_id_list[-1]
        page_father = objectKey_po[str(object_id)]
        # 获取页面列表
        for page_ in page_father:
            page_id = str(page_['page_id'])
            # 获取页面ID
            if [object_id, page_id] in object_list:
                return

            object_father = pageKey_op[page_id]
            # 获取进入页面的控件列表
            for k in object_father:
                object_list_copy = object_list.copy()
                object_list_copy.append([str(object_id), str(page_id)])
                # 控件,页面不在列表中，放入操作序列
                object_child_id = k['object_id']
                # 获取进入页面的控件ID
                # print('------', object_id, page_id, object_child_id, object_list_copy)
                if object_child_id in object_id_list:
                    # print('--------loop 2 long', object_id_list)
                    return
                if str(object_child_id) not in objectKey_po.keys():
                    # 进入页面的控件ID 不在页面的所有元素中,执行退出
                    # object_list_copy.append([str(object_child_id), str(0)])
                    if str(object_id_list[0]) not in object_dict_short.keys() \
                            or len(object_dict_short[str(object_id_list[0])]) > len(object_list_copy):
                        object_dict_short[str(object_id_list[0])] = object_list_copy
                    return

                object_id_list_copy = object_id_list.copy()
                object_id_list_copy.append(str(object_child_id))
                tree_root(object_id_list_copy, object_list_copy)

    print('goal_id_arr_', goal_id_arr_)

    for goal_id in goal_id_arr_:
        print('goal_id', goal_id)
        if '|' in str(goal_id):
            for goal_id_ in str(goal_id).split('|'):
                tree_root([goal_id_], object_list=list())

            short_key = None

            for k, v in object_dict_short.items():

                if short_key == None or len(object_dict_short[k]) < len(object_dict_short[short_key]):
                    short_key = k

            object_dict_short_ = dict()

            object_dict_short_[str(short_key)] = object_dict_short[str(short_key)]
            print('object_dict_short_', object_dict_short_)
            return object_dict_short_

        else:
            tree_root([goal_id], object_list=list())

    print('object_dict_short', object_dict_short)
    return object_dict_short


def case_imahtml(object_id, goal_list, object_dict, object_db_in_values, object_db_no_values):
    pdi = None
    id_ope = dict()
    object_list = ['<option value="">请选择操作步骤</option>']

    page_show_list = list()
    page_input_define_list = list()
    page_input_undefine_list = dict()

    result = dict()

    object_goal_list = list(goal_list.values())[0]

    object_goal_list.reverse()
    for obj_page in object_goal_list:
        print('obj_page', obj_page)
        object_gl = object_dict[str(obj_page[0])]
        page_show_list.append('<option >%s-->%s</option>' % (object_gl['os'], object_gl['ns']))
        page_input_define_list.append(-1)

    if object_db_in_values:
        page_list_in = [None] * len(object_db_in_values)
        for obj in object_db_in_values:
            page_input_define_list.append(obj['object_id'])
            id_ope[obj['object_id']] = obj['ope']
            run_input = '' if not obj['run_input'] else 'value="%s"' % (obj['run_input'])

            if 'EditText' in obj['clz']:
                pdi = obj['img_info']
                page_list_in[obj['run_index']] = '<option value="%s">【%s】-->输入</option>' % (
                    obj['object_id'], obj['ns'])
            else:
                page_list_in[obj['run_index']] = '<option value="%s">%s-->%s</option>' % (
                    obj['object_id'], obj['os'], obj['ns'])

            page_input_undefine_list[obj['object_id']] = run_input

        page_show_list.extend(page_list_in)

    print('page_input_define_list', page_input_define_list)

    if object_db_no_values:
        for obj in object_db_no_values:
            print('---', obj)
            id_ope[obj['object_id']] = obj['ope']
            run_input = '' if not obj['run_input'] else 'value="%s"' % (obj['run_input'])

            if 'EditText' in obj['clz']:
                pdi = obj['img_info']
                object_list.append('<option value="%s">【%s】-->输入</option>'
                                   % (obj['object_id'], obj['ns']))
            else:
                print(object_dict[obj['object_id']])
                object_list.append('<option value="%s">%s-->%s</option>'
                                   % (obj['object_id'], object_dict[obj['object_id']]['os'],
                                      object_dict[obj['object_id']]['ns']))
            page_input_undefine_list[obj['object_id']] = run_input

    print('page_input_undefine_list', page_input_undefine_list)

    if len(object_list) == 1:
        object_list.append('<option value="%s">提交重置操作步骤</option>' % (999))
        id_ope[999] = 1
        page_input_undefine_list[999] = ''

    print('object_list', object_list)
    print('page_input_define_list', page_input_define_list)
    print('page_input_undefine_list', page_input_undefine_list)
    print('id_ope', id_ope)
    print('page_show_list', page_show_list)
    print('object_list', object_list)

    result['pl'] = page_input_define_list
    result['ii'] = page_input_undefine_list
    result['io'] = id_ope
    result['o'] = object_list
    result['p'] = page_show_list
    result['d'] = pdi

    return result


def case_image2html(user_id, pageKey, objectKey, object_dict_short):
    object_case = dict()

    page_info_json = list()
    case_img_arr = list()
    recom_case_arr = list()

    for k, v in object_dict_short.items():
        # print(k, v)
        case_info = list()
        img_arr = list()
        recom_case = dict()
        case_info_ = list()

        for po_id in range(len(v)):
            # print('len(v)', len(v), po_id)

            po_run = v[len(v) - po_id - 1]
            # print('po_run', po_run)
            obj_id = po_run[0]
            page_id = po_run[1]
            # print(obj_id, page_id)
            obj = objectKey[obj_id]
            # print('obj', obj)

            page = pageKey[page_id]
            # print('page', page)

            if len(v) > po_id + 1:
                po_next = v[len(v) - po_id - 2]
                _n = objectKey[po_next[0]]
                exp = ['%s||%s||%s||%s' % (
                    _n['clz'], _n['bnz'], _n['text'], _n['rid'])]
            else:
                exp = None

            case_info.append({'os': obj['os']
                                 , 'ns': obj['ns']
                                 , 'exp': exp
                              })

            case_info_.append(name2short(obj))

            img_arr.append(img_path(page['rotation']
                                    , page['height']
                                    , page['width']
                                    , page['pageTime']
                                    , obj['bnz']
                                    , user_id))

            if len(v) == po_id + 1:
                recom_case['id'] = obj['id']
                recom_case['case_name'] = 'recom||%s||%s' % (obj['id'], obj['ns'])
                recom_case['case_info'] = json.dumps(case_info_)
                recom_case['user_parent_id'] = user_id
                recom_case['img_info'] = json.dumps(img_arr)
                case_info.insert(0, {'id': obj['id']
                    , 'case_title': obj['ns'],
                                     'valid': obj['valid']})

        recom_case_arr.append(recom_case)
        page_info_json.append(case_info)
        case_img_arr.append(img_arr)
    object_case['show_json'] = page_info_json
    object_case['sj'] = case_img_arr
    object_case['recom_case'] = recom_case_arr
    object_case['case_title'] = 'recommend'
    return object_case


def step_depth(user_id, page_objects_values, page_objects_select, objects_values, object2page_values):
    step_depth_ = list()

    objects_dict = sql2dict(objects_values)
    print('objects_dict', objects_dict)

    object2page_dict = sql2key(object2page_values, 'page_id')
    print('object2page_dict', object2page_dict)

    for po_run in page_objects_values:
        if po_run['page_id'] in page_objects_select:
            obj = objects_dict[str(po_run['object_id'])]
            parent_id_arr = list()
            for j in object2page_dict[str(po_run['page_id'])]:
                parent_id_arr.append(str(j['object_id']))
            obj_in = dict()

            obj_in['user_id'] = user_id
            obj_in['parent_id'] = '|'.join(parent_id_arr)
            obj_in['page_id'] = po_run['page_id']
            obj_in['object_id'] = po_run['object_id']
            obj_in['ope'] = ope2num(obj)
            obj_in['text'] = obj['text']
            obj_in['clz'] = obj['clz']
            obj_in['bnz'] = obj['bnz']
            obj_in['rid'] = obj['rid']
            obj_in['os'] = obj['os']
            obj_in['ns'] = obj['ns']

            step_depth_.append(obj_in)

    return step_depth_


def root_id_from_objects(object_values):
    if isinstance(object_values, list):
        root_id_list = list()
        for obj in object_values:
            if obj['ope'] == 'init' and obj['text'] == 'initArd':
                root_id_list.append(obj['id'])

        if len(root_id_list) == 1:
            return root_id_list[0]
        else:
            print('root_id_list', root_id_list)
    print('root_id_from_objects', object_values)


def yaml_w(fn, data):
    print('yaml_w', data)
    yamlPath = os.path.join('uiautomator', 'debug_info', fn + '.yaml')
    print('yamlPath', yamlPath)

    fw = open(yamlPath, 'w', encoding='utf-8')
    yaml.dump(data, fw)
    fw.close()


def yaml_r(fn):
    try:
        yamlPath = os.path.join('uiautomator', 'debug_info', fn + '.yaml')
        f = open(yamlPath, 'r', encoding='utf-8')
        cont = f.read()
        f.close()
        x = yaml.load(cont, Loader=yaml.FullLoader)
        return x
    except Exception as e:
        print('Exception::', __name__, 'yaml_r', fn, e)


def app_ks(project_id):
    app_ks_ = dict()

    try:
        apk_file = os.path.join('uiautomator', 'run_app_home', 'download_%s.apk' % (project_id))
        app_ks_['apk_file'] = apk_file

        if os.path.isfile(apk_file):

            pkg_unremove_name = list()
            pkg_uninstall_list = list_packages()

            remove_list = list()
            for pl in str(pkg_uninstall_list, encoding="utf-8").split('\n'):
                if 'package' in str(pl) \
                        and 'duokan' not in str(pl) \
                        and 'mfashiongallery' not in str(pl) \
                        and 'zt' not in str(pl):
                    pkg_name = pl.replace('package:', '')
                    print('卸载APP...', pkg_name)
                    uninstall_pkg(pkg_name)
                    remove_list.append(pkg_name)
            app_ks_['pkg_uninstall_list'] = remove_list

            pkg_list = list_packages()
            apk_list = list()
            for pl in str(pkg_list, encoding="utf-8").split('\n'):
                if 'package' in str(pl) and 'c.ez' not in str(pl):
                    pkg_name = pl.replace('package:', '')
                    print('当前已安装APP:', pkg_name)
                    pkg_unremove_name.append(pkg_name)
                    apk_list.append(pkg_name)
            app_ks_['apk_list'] = apk_list

            ri = install_pkg(apk_file)
            print('安装APP:', ri)

            pkg_install_list = list_packages()

            pkg_install_name = list()
            for pl in str(pkg_install_list, encoding="utf-8").split('\n'):
                if 'package' in str(pl) and 'c.ez' not in str(pl):
                    pkg_name = pl.replace('package:', '')
                    if pkg_name not in pkg_unremove_name:
                        print('安装后APP:', pkg_name)
                        pkg_install_name.append(pkg_name)

            app_ks_['pkg_install_name'] = pkg_install_name
    except Exception as e:
        print('Exception', e)
    return app_ks_


def ez_step(page_object, object_values, op_values, po_values):
    try:
        print('page_object', type(page_object), page_object)

        if type(page_object) is not list:
            print('[ERROR]page_object::', type(page_object), page_object)

        if type(op_values) is not list:
            print('[ERROR]o2p_db::', op_values)

        object_o2p_db = [i['object_id'] for i in op_values]
        print('存在页面 id', object_o2p_db)

        online_object_key = dict()

        test_case_key = dict()

        for obj in object_values:

            test_case_key[obj['id']] = obj

            if len(page_object) > len(online_object_key.keys()):

                rid_ = obj['rid']
                clz_ = obj['clz']
                bnz_ = obj['bnz']

                for object_show in page_object:

                    rid = object_show['rid']
                    clz = object_show['clz']
                    text = object_show['text']
                    bnz = object_show['bnz']
                    ope = object_show['ope']

                    if rid == rid_ and clz == clz_ and bnz == bnz_:
                        if obj['id'] in object_o2p_db:
                            online_object_key[obj['id']] = obj
                            continue
                        else:
                            obj_list_ = list()

                            object_rsp = dict()
                            object_rsp['rid'] = rid
                            object_rsp['clz'] = clz
                            object_rsp['ope'] = ope
                            object_rsp['text'] = text
                            object_rsp['bnz'] = bnz
                            object_rsp['father_id'] = obj['id']
                            object_rsp['editIn'] = None
                            object_rsp['result'] = 'success'

                            obj_list_.append(object_rsp)

                            ez_step_ = dict()
                            ez_step_['result'] = 'success'
                            ez_step_['obj_list'] = obj_list_

                            return ez_step_

        print('当前元素', online_object_key.keys())

        key_all_get = edges(op_values, po_values, online_object_key.keys())
        print('key_all_get', key_all_get)
        if key_all_get:
            obj_list = list()

            for k in key_all_get:
                obj = dict()
                ko = test_case_key[k]
                obj['rid'] = ko['rid']
                obj['clz'] = ko['clz']
                obj['ope'] = ko['ope']
                obj['text'] = ko['text']
                obj['bnz'] = ko['bnz']
                obj['father_id'] = k
                obj['editIn'] = None
                obj_list.append(obj)

            ez_step_ = dict()
            ez_step_['result'] = 'success'

            ez_step_['obj_list'] = obj_list
            print('ez_step::', ez_step_)
            return ez_step_
    except Exception as e:
        print('Exception', e)
        print('page_object::', page_object)

    return {'result': 'fail'}


def edges(op_values, po_values, father_keys):
    print('edges', father_keys)
    try:

        if len(father_keys) == 1:
            print('father_keys', father_keys)
            return [list(father_keys)[0]]

        edges_ = list()
        nodes = list()

        o2p_ol = list()

        for o2p in op_values:
            objectId = o2p['object_id']
            pageId = o2p['page_id']
            objectId_ = 'O' + str(objectId)
            pageId_ = 'P' + str(pageId)

            edges_.append((objectId_, pageId_))

            if objectId_ not in nodes:
                nodes.append(objectId_)
            if pageId_ not in nodes:
                nodes.append(pageId_)

            edges_.append((objectId_, pageId_))

            o2p_ol.append(objectId)

        o2p_ol_ = list(set(o2p_ol))

        opo_list = list()
        for p2o in po_values:
            objectId = p2o['object_id']
            pageId = p2o['page_id']

            objectId_ = 'O' + str(objectId)
            pageId_ = 'P' + str(pageId)

            if objectId not in opo_list and objectId not in o2p_ol_:
                opo_list.append(objectId)

            if objectId_ not in nodes:
                nodes.append(objectId_)
            if pageId_ not in nodes:
                nodes.append(pageId_)

            edges_.append((pageId_, objectId_))

        opo_list.sort()
        print('opo_list', opo_list)
        G = nx.Graph()

        for node in nodes:
            G.add_node(node)

        G.add_edges_from(edges_)

        for obj_id in opo_list:
            short_way = None
            for father_key in father_keys:
                shortest_way = nx.shortest_path(G, 'O' + str(father_key), 'O' + str(obj_id))
                print('shortest_way', obj_id, father_key, shortest_way, len(shortest_way))
                if len(shortest_way) > 1 and (short_way == None or len(short_way) > len(shortest_way)):
                    short_way = shortest_way

            if len(short_way) > 0:
                print('short_way', short_way)
                sw_list = list()
                for sw in short_way:
                    if str(sw).startswith('O'):
                        sw_list.append(int(sw[1:]))
                print('sw_list', sw_list)

                return sw_list

    except Exception as e:
        print('Exception', e)

    return None

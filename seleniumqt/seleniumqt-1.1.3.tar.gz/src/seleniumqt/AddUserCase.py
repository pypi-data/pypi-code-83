# -*- coding: utf-8 -*-
import json


class AddUserCase:
    add_case_dict = dict()
    add_img_dict = dict()

    show_case_list = list()
    show_img_list = list()

    app_case_list = list()

    def __init__(self):
        self.add_case_dict.clear()
        self.show_case_list.clear()

    def add_case_db(self, step_db):
        for step in step_db:
            if type(step) is dict and 'case_name' in step.keys():
                case_name = step['case_name']
                step_id = step['step_id']

                step_add = dict()
                if step['text'] == 'initArd':
                    step_add['id'] = step['id']
                    step_add['user_parent_id'] = step['user_parent_id']

                step_add['ns'] = step['ns']
                step_add['os'] = step['os']

                step_add['ope'] = step['ope']
                step_add['text'] = step['text']
                step_add['clz'] = step['clz']
                step_add['bnz'] = step['bnz']
                step_add['rid'] = step['rid']

                step_add['valid'] = 1
                step_add['exp'] = [step['exp']]
                step_add['exp_'] = [step['exp_text'], step['exp_bnz'], step['exp_rid'], step['exp_clz']]

                if case_name not in self.add_case_dict.keys():
                    self.add_case_dict[case_name] = dict()

                self.add_case_dict[case_name][step_id] = step_add

                img_add = list()
                img_add.append(int(step['rotation']))
                for i in step['bnz'].split('_'):
                    img_add.append(int(int(i) / 5))

                img_add.append('%s/%s' % (step['user_parent_id'], step['img_time']))

                if case_name not in self.add_img_dict.keys():
                    self.add_img_dict[case_name] = dict()
                self.add_img_dict[case_name][step_id] = img_add.copy()

    def case2list(self):

        for k in self.add_case_dict.keys():
            img_v = self.add_img_dict[k]
            case_v = self.add_case_dict[k]

            ks_title = dict()
            ks_cnt = list()

            for ks_stp in range(len(case_v.keys())):
                case_dict = case_v[ks_stp + 1]
                ks_dict = dict()
                ks_dict['ns'] = case_dict['ns']
                ks_dict['os'] = case_dict['os']
                ks_dict['valid'] = case_dict['valid']
                ks_dict['exp'] = case_dict['exp']
                ks_dict['exp_'] = case_dict['exp_']
                ks_cnt.append(ks_dict)
            ks_cnt = ks_cnt[1:]
            ks_title['id'] = case_v[1]['id']
            ks_title['case_title'] = k
            ks_title['valid'] = case_v[1]['valid']

            ks_cnt.insert(0, ks_title)
            self.show_case_list.append(ks_cnt)

            img_cnt = list()
            for img_stp in range(len(img_v.keys())):
                img_cnt.append(img_v[img_stp + 1])
            self.show_img_list.append(img_cnt[1:])

    def case2dictlist(self):
        for kd in self.add_case_dict.keys():
            img_v = self.add_img_dict[kd]
            case_v = self.add_case_dict[kd]

            ks = dict()
            ks['id'] = case_v[1]['id']
            ks['case_name'] = kd
            ks['valid'] = case_v[1]['valid']
            ks['user_parent_id'] = case_v[1]['user_parent_id']

            img_cnt = list()
            for img_stp in range(len(img_v.keys())):
                img_db = img_v[img_stp + 1]
                if img_db[0] == img_db[1] == img_db[2] == img_db[3] == img_db[4] == 0:
                    continue
                img_cnt.append(img_db)
            ks['img_info'] = json.dumps(img_cnt)

            ks_cnt = list()
            for ks_stp in range(len(case_v.keys())):
                step = case_v[ks_stp + 1]
                step_and = dict()

                if step['ope'] == 'init':
                    continue

                for k, v in step.items():
                    if 'ope' == k:
                        step_and['ope'] = v
                    elif 'clz' == k:
                        step_and['clz'] = v
                    elif 'bnz' == k:
                        step_and['bnz'] = v
                    elif 'rid' == k:
                        step_and['rid'] = v
                    else:
                        step_and[k] = v

                ks_cnt.append(step_and)
            ks['case_info'] = json.dumps(ks_cnt)
            self.app_case_list.append(ks)

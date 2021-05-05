import json
import traceback


def key_in(d, key):
    if key in d.keys():
        return d[key]


def case2android_step(cur_case_arr):
    android_cur_case_arr = list()
    for cur_case in cur_case_arr:
        try:
            print('cur_case', cur_case)
            case_info_db = dict()
            case_info_db['id'] = cur_case['id']

            case_info_db['case_name'] = cur_case['case_name']
            case_info_db['img_info'] = json.loads(cur_case['img_info'])
            case_info_db['user_parent_id'] = cur_case['user_parent_id']

            case_info_db['valid'] = key_in(cur_case, 'valid')
            case_info_db['run_client'] = key_in(cur_case, 'run_client')

            db_case_info = json.loads(cur_case['case_info'])

            case_db = list()
            for on_step in range(len(db_case_info)):
                on_step_ = db_case_info[on_step]
                print('on_step_', on_step_)
                step_db = dict()
                step_db['clz'] = on_step_['clz']
                step_db['bnz'] = on_step_['bnz']
                step_db['ope'] = on_step_['ope']
                step_db['text'] = on_step_['text']
                step_db['rid'] = on_step_['rid']
                step_db['ns'] = on_step_['ns']
                step_db['os'] = on_step_['os']

                if 'exp_' in on_step_.keys():
                    step_db['exp_'] = on_step_['exp_']
                else:
                    if on_step + 1 < len(db_case_info):
                        n_ = db_case_info[on_step + 1]
                        step_db['exp_'] = [n_['text'], n_['bnz'], n_['rid'], n_['clz']]
                    else:
                        step_db['exp_'] = None

                case_db.append(step_db)

            case_info_db['case_db'] = case_db
            print('db_case_info', db_case_info)
            print('case_info_db', case_info_db)
            android_cur_case_arr.append(case_info_db)
        except:
            traceback.format_exc()

    return android_cur_case_arr

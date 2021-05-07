import json

from seleniumqt.dbsql import sql2dict


def manual_rpt(resmanual_all, pjt_all):
    res_user = sql2dict(resmanual_all)
    pjt_user = sql2dict(pjt_all)

    pjt_rpt = dict()

    for k, v in res_user.items():
        t = v['ua_run_time']
        if t not in pjt_rpt.keys():
            pjt_rpt[t] = dict()

        if 'pjt_name' not in pjt_rpt[t].keys():
            pjt_rpt[t]['pjt_name'] = pjt_user[str(v['pjt_owner_id'])]['pjt_name']

        if 'v' not in pjt_rpt[t].keys():
            pjt_rpt[t]['v'] = 0

        if 'v_' not in pjt_rpt[t].keys():
            pjt_rpt[t]['v_'] = 0

        if v['valid'] == 1:
            pjt_rpt[t]['v'] = pjt_rpt[t]['v'] + 1
        else:
            pjt_rpt[t]['v_'] = pjt_rpt[t]['v_'] + 1

    d = list()
    for k, v in pjt_rpt.items():
        fname = '<a style="color:blueviolet" href="/report/fcsRpt/%s">%s_%s</a>' % (k, v['pjt_name'], k)
        rpt_dict = {'f': fname, 'e': v['v'], 'i': v['v_'], 't': "%.2f%%" % (v['v'] / (v['v'] + v['v_']) * 100)}
        d.append(rpt_dict)

    manual_report = dict()
    manual_report['table_title'] = ['报告名称', '通过', '未通过', '通过率']
    manual_report['d'] = d
    return manual_report


def report_function(manualCase, pjt_all):
    manual_case = sql2dict(manualCase)
    pjt_user = sql2dict(pjt_all)

    pjt_rpt = dict()
    for k, v in manual_case.items():
        t = v['ua_run_time']
        if t not in pjt_rpt.keys():
            pjt_rpt[t] = dict()
        if 'pjt_name' not in pjt_rpt[t].keys():
            pjt_rpt[t]['pjt_name'] = pjt_user[str(v['pjt_owner_id'])]['pjt_name']

        if 'case_info' not in pjt_rpt[t].keys():
            pjt_rpt[t]['case_info'] = list()

        case_info_ = json.loads(v['case_rpt'])
        case_info_add_title = case_info_
        case_info_add_title.insert(0, {'id': v['id'],
                                       'case_title': v['case_name'],
                                       'valid': v['valid']})

        pjt_rpt[t]['case_info'].append({k: case_info_add_title})

        if 'img_info' not in pjt_rpt[t].keys():
            pjt_rpt[t]['img_info'] = list()

        img_info_ = json.loads(v['img_info'])

        pjt_rpt[t]['img_info'].append({k: img_info_})

    max_run_time = max(pjt_rpt.keys())

    case_title = '[%s_%s]' % (pjt_rpt[max_run_time]['pjt_name'], max_run_time)
    case_show_json = list()
    case_image_list = list()

    case_info = pjt_rpt[max_run_time]['case_info']
    img_info = pjt_rpt[max_run_time]['img_info']
    for case_loop in case_info:
        for k, v in case_loop.items():
            case_show_json.append(v)
    for image_loop in img_info:
        for k, v in image_loop.items():
            case_image_list.append(v)

    report_func = dict()
    report_func['show_json'] = case_show_json
    report_func['sj'] = case_image_list
    report_func['case_title'] = case_title
    return report_func

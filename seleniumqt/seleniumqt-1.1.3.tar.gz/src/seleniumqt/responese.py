from seleniumqt.dbsql import sql2key, sql2dict


def truck2leaves(user_id, case_id, step_id, object_page, page_object, page_values, object_values):
    objectKey_op = sql2key(object_page, 'object_id')
    pageKey_po = sql2key(page_object, 'page_id')
    pageKey = sql2dict(page_values)
    objectKey = sql2dict(object_values)

    rsp = dict()
    si = int(step_id) + 1
    pr = list()
    pi = list()
    pr.append('<option value=""></option>')
    pi.append('<option value=-1,%s>请选择操作步骤</option>' % (si))
    rsp['si'] = si
    rsp['i'] = None
    rsp['h'] = 'height:100px;'
    rsp['t'] = ''

    op_case = objectKey_op[case_id]
    print('op_case', op_case)

    for op in op_case:
        page_children = pageKey[str(op['page_id'])]
        print('page_children', page_children)

        if page_children['rotation'] == 1:
            hw_l = (page_children['height'] - page_children['width']) * 50 / page_children['height']
            rsp['t'] = 'transform: translate(-%spx, %spx) rotate(90deg);' % (hw_l, hw_l)
            rsp['h'] = 'width:100px;'

        rsp['i'] = '%s/%s' % (user_id, page_children['pageTime'])

        page_children_object = pageKey_po[str(op['page_id'])]
        print('page_children_object', page_children_object)

        for po_ in page_children_object:
            object_children_object = objectKey[str(po_['object_id'])]
            print('object_children_object', object_children_object)
            object_children_id = str(object_children_object['id'])

            pr.append('<option value="%s">%s</option>'
                      % (object_children_id, object_children_object['ns']))

            if object_children_id != case_id and object_children_id in objectKey_op.keys():
                pi.append('<option value=%s,%s>%s-->%s</option>'
                          % (object_children_id, si, object_children_object['os'], object_children_object['ns']))
            else:
                print('[INFO::]case_id', case_id)
                print('[INFO::]objectKey_op', objectKey_op)

    rsp['o'] = ''.join(pi)
    rsp['r'] = ''.join(pr)
    return rsp

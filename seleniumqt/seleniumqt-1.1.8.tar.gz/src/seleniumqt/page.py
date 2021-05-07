def ope2num(obj):
    print('obj', obj)
    if 'EditText' in obj['clz']:
        ope = 3
    elif obj['ope'][0] == 'C':
        ope = 1
    elif obj['ope'][1] == 'S':
        ope = 2
    elif obj['rid'] == "android:id/content":
        ope = 0
    else:
        ope = -1
    return ope


def object_html(obj):
    clz = obj['clz']
    bnz = obj['bnz']
    ope_ = obj['ope']
    rid = obj['rid']

    ns = obj['text']
    if len(ns) > 16:
        ns = ns[: 16] + '...'

    if '_' == ns or ns == '' or 'EditText' in clz:
        ns = bnz + '@' + clz.split('.')[-1]

    os = '未知操作'

    if 'C' == ope_[0:1]:
        os = '点击'
    elif 'S' == ope_[1:2]:
        os = '滚动'
    elif 'E' == ope_[2:3]:
        os = '选中'
    elif ope_ == 'init':
        os = '初始化'
        print('------', obj)

    elif ope_ == 'cself' and obj['text'] == 'zt':
        os = '启动'
        ns = rid

    if ns[:5] == 'CHILD':
        ns = ns[5:]
    if ns[:3] == 'IMG':
        ns = ns[3:]

    return ns, os


def name2short(obj):
    key_word = dict()
    key_word['ope'] = 'ope'
    key_word['clz'] = 'clz'
    key_word['bnz'] = 'bnz'
    key_word['rid'] = 'rid'

    un_use = ['valid', 'flag', 'server_object']
    obj_short = dict()
    for k, v in obj.items():
        if k in key_word.keys():
            obj_short[key_word[k]] = v
        elif k in un_use:
            continue
        else:
            obj_short[k] = v

    return obj_short


def img_path(page_rotation, page_height, page_width, page_time, obj_bnz, user_id):
    img_path_ = list()

    try:
        img_path_.append(page_rotation)
        img_path_.append(int(int(page_height) / 5))
        img_path_.append(int(int(page_width) / 5))
        bnz = str(obj_bnz).split('_')
        img_path_.append(int(int(bnz[0]) / 5))
        img_path_.append(int(int(bnz[1]) / 5))
        img_path_.append(int(int(bnz[2]) / 5))
        img_path_.append(int(int(bnz[3]) / 5))

        step_image = '%s/%s' % (user_id, page_time)
        img_path_.append(step_image)
    except Exception as e:
        print('page_rotation', page_rotation)
        print('page_height', page_height)
        print('page_width', page_width)
        print('page_time', page_time)
        print('obj_bnz', obj_bnz)
        print('user_id', user_id)
        print('img_path_Exception', e)
    return img_path_

import os

import numpy as np
import pytesseract
from PIL import Image


def img_oss(user_id, time_on_show):
    if os.environ.get('DEBUG', 'on') == 'on':
        return '/uiautomator/ez_img/ez_%s_%s.jpg' % (user_id, time_on_show)

    return 'https://apk2ali.oss-cn-huhehaote.aliyuncs.com/dd_pjt_img/' \
           'ez_%s_%s.jpg' % (user_id, time_on_show)


def apk_oss(user_id, app_file):
    return 'https://apk2ali.oss-cn-huhehaote.aliyuncs.com/dd_apk/ez_test_%s_%s' % (user_id, app_file)


def img2string(img_path):
    return pytesseract.image_to_string(Image.open(img_path), lang='chi_sim')


def check_img_contains_chinese(check_str):
    for ch in check_str.decode('utf-8'):
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False


def check_img_object_is_black(img_in, i_po):
    try:
        print(i_po)
        r = i_po['bnz'].split('_')

        region = img_in.crop((int(r[0]), int(r[1]), int(r[2]), int(r[3])))
        img = np.array(region)
        shape = img.shape

        point_list = list()
        for x in range(shape[0]):
            for y in range(shape[1]):
                t = img[x, y]
                po_now = '%s_%s_%s' % (t[0], t[1], t[2])
                if po_now not in point_list:
                    point_list.append(po_now)
                if len(point_list) > 3:
                    print('image_load_OK', point_list)
                    return False
        print('point_list', len(point_list))
    except Exception as e:
        print('image_point_list', e)
    print('i_po', i_po)
    return True

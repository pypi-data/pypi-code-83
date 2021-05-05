# -*- coding: utf-8 -*-
import base64
import json
import os
import time
import datetime
import hmac
import traceback
from hashlib import sha1 as sha
import oss2


def get_iso_8601(expire):
    gmt = datetime.datetime.fromtimestamp(expire).isoformat()
    gmt += 'Z'
    return gmt


def get_token(access_key_id, access_key_secret, end_point, bucket_name, upload_dir):
    expire_syncpoint = int(time.time()) + 30
    expire = get_iso_8601(expire_syncpoint)

    policy_dict = {'expiration': expire}
    condition_array = []

    array_item = ['starts-with', '$key', upload_dir]
    condition_array.append(array_item)
    policy_dict['conditions'] = condition_array
    policy_json = json.dumps(policy_dict).strip()
    policy_json_bytes = bytes(policy_json, encoding='utf-8')
    policy_encode = base64.b64encode(policy_json_bytes)
    h = hmac.new(access_key_secret, policy_encode, sha)
    sign_result = base64.b64encode(h.digest()).strip()
    token_dict = {'accessid': access_key_id, 'host': 'http://%s.%s' % (bucket_name, end_point),
                  'policy': str(policy_encode, encoding='utf-8'), 'signature': str(sign_result, encoding='utf-8'),
                  'expire': expire_syncpoint, 'dir': upload_dir}
    result = json.dumps(token_dict)
    return result


def img2oss(access_key_id, access_key_secret, end_point, bucket_name, image_path, user_id, page_time):
    try:
        auth = oss2.Auth(access_key_id, access_key_secret)
        bucket = oss2.Bucket(auth, 'http://' + end_point, bucket_name)

        oss_file = 'dd_pjt_img/ez_%s_%s.jpg' % (user_id, page_time)
        ard_file = '%s/ez_%s_%s.jpg' % (image_path, user_id, page_time)

        print('oss_file', oss_file)
        print('ard_file', ard_file)

        debug_env = os.environ.get('DEBUG', 'on') != 'on'

        if not debug_env:
            exist = bucket.object_exists(oss_file)
            print('exist', exist, oss_file, ard_file)
            if not exist:
                bucket.put_object_from_file(oss_file, ard_file)
        print('debug_env', debug_env, oss_file, ard_file)

    except Exception as e:
        print(e)


def download_apk(access_key_id, access_key_secret, end_point, bucket_name, apk_path, project_id, app_file):
    download_apk_info = dict()
    try:
        obj_name = 'dd_apk/ez_test_%s_%s' % (project_id, app_file)
        local_file = '%sdownload_%s.apk' % (apk_path, project_id)

        download_apk_info['obj_name'] = obj_name

        if os.path.exists(local_file):
            download_apk_info['file_has_in'] = local_file
            print('[INFO:]download_apk 已存储', local_file)
            return download_apk_info

        print('[INFO:]download_apk 开始下载', local_file)
        download_apk_info['load_start'] = True

        auth = oss2.Auth(access_key_id, access_key_secret)
        bucket = oss2.Bucket(auth, end_point, bucket_name)
        bucket.get_object_to_file(obj_name, local_file)
        print('[INFO:]download_apk 下载完成', local_file)
        download_apk_info['load_ok'] = True

        return download_apk_info
    except:
        traceback.print_exc()

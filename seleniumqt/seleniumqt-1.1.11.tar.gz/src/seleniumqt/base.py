import json
import pytesseract
import traceback

from PIL import Image
from pylab import *


class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        else:
            return json.JSONEncoder.default(self, obj)


def date_format_json(format_dict):
    if isinstance(format_dict, dict):
        return json.dumps(format_dict, cls=DateEncoder)


def char_is_code(uchar):
    if u'\u4e00' <= uchar <= u'\u9fa5':
        return uchar
    elif u'\u0030' <= uchar <= u'\u0039':
        return uchar
    elif (u'\u0041' <= uchar <= u'\u005a') \
            or (u'\u0061' <= uchar <= u'\u007a'):
        return uchar
    return None


#
# def db_value2dict(op_, clm_name):
#     db_dict = dict()
#     try:
#         for i in op_:
#             clm_ = i[clm_name]
#             if clm_ not in db_dict.keys():
#                 db_dict[clm_] = [i]
#             else:
#                 db_dict[clm_].append(i)
#     except Exception as e:
#         print('Exception', e)
#     return db_dict
#

def cutImg(imgsrc, box):
    try:
        image = Image.open(imgsrc)
        region_ = image.crop(box)
        code = pytesseract.image_to_string(region_, lang="chi_sim", config="-psm 6")
        img_code = list()

        for uchar in code:
            img_code.append(char_is_code(uchar))

        img_code.append(None)
        img_code_ = list()
        for i in range(len(img_code)):
            if img_code[i]:
                if (i > 0 and img_code[i - 1]) \
                        or (i < len(img_code) - 1 and img_code[i + 1]):
                    img_code_.append(img_code[i])
            elif len(img_code_) > 1 and img_code_[-1] != '-':
                img_code_.append('-')

        if len(img_code_) > 0:
            if img_code_[-1] == '-':
                img_code_ = img_code_[0:-1]
            return ''.join(img_code_)
        return None
    except:
        traceback.print_exc()


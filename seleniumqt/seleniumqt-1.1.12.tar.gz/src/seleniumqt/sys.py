# -*- coding: utf-8 -*-
import traceback

from PIL import Image
import pytesseract
from pinyin import pinyin
from pylab import *


def time_cn(cn_fmt=None):
    if cn_fmt:
        return datetime.datetime.now().strftime(cn_fmt)
    else:
        datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        return '---'


def time_fmt(cn_fmt):
    return datetime.datetime.now().strftime(cn_fmt)


def cut_image(img_src, coordinate):
    try:
        image = Image.open(img_src)
        t = coordinate.split('_')
        x = int(t[0])
        y = int(t[1])
        x_w = int(t[2])
        y_h = int(t[3])

        t_point = (x, y, x_w, y_h)
        region_ = image.crop(t_point)
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
            print(t, img_code_)
            return ''.join(img_code_)
        return None
    except:
        traceback.print_exc()


def char_is_code(uchar):
    if u'\u4e00' <= uchar <= u'\u9fa5':
        return uchar
    elif u'\u0030' <= uchar <= u'\u0039':
        return uchar
    elif (u'\u0041' <= uchar <= u'\u005a') \
            or (u'\u0061' <= uchar <= u'\u007a'):
        return uchar
    return None


def is_rare_name(string):
    pattern = re.compile(u"[~!@#$%^&* ]")
    match = pattern.search(string)
    if match:
        return True
    try:
        string.encode("gb2312")
    except UnicodeEncodeError:
        return True

    return False


def text2pinyin(text):
    py = list()
    for i in text.split():
        py.append(pinyin.get(i, format='strip', delimiter=""))
    return py


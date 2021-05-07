# -*- coding: utf-8 -*-
"""
@Author: Ssfanli
@Time  : 2021/04/26 8:29 下午
@Desc  : 
"""
from enum import Enum


class PACKAGE(str, Enum):
    IOSQQ = 'com.tencent.mqq'
    IOSWX = 'com.tencent.xin'
    ANDWX = 'com.tencent.mm'
    ANDQQ = 'com.tencent.mobileqq'


class APP(str, Enum):
    WX = 'wx'
    QQ = 'qq'


class PLATFORM(str, Enum):
    IOS = 'ios'
    AND = 'android'


class ACTIVITY(str, Enum):
    QQSPLASH = 'com.tencent.mobileqq.activity.SplashActivity'
    QQLOGIN = 'com.tencent.mobileqq.activity.LoginActivity'
    QQNTF = 'com.tencent.mobileqq.activity.NotificationActivity'


class URL(str, Enum):
    # TODO: url maybe change
    ANDQQ = 'http://gdown.baidu.com/data/wisegame/98156ec27aeb4c78/d6fb98156ec27aeb4c782708ea7de953.apk'
    ANDWX = ''


class COMMON(tuple, Enum):
    PLATFORMS = (PLATFORM.IOS, PLATFORM.AND)
    APPS = (APP.WX, APP.QQ)
    WHITELIST = ('允许', '同意', '跳过', '想想', '关闭', '稍后', '取消')
    ACTIVITIES = (ACTIVITY.QQSPLASH, ACTIVITY.QQLOGIN, ACTIVITY.QQNTF)


class QQLoc:
    acc = {
        PLATFORM.AND: {'descriptionContains': '请输入QQ号码'},
        PLATFORM.IOS: {'name': '帐号', 'className': 'TextField'}
    }
    pwd = {
        PLATFORM.AND: {'resourceId': 'com.tencent.mobileqq:id/password'},
        PLATFORM.IOS: {'name': '密码', 'className': 'SecureTextField'}
    }
    login = {
        PLATFORM.AND: {'resourceId': 'com.tencent.mobileqq:id/login'},
        PLATFORM.IOS: {'name': '登录按钮', 'className': 'Button'}
    }
    login_fail = {
        PLATFORM.AND: {'text': '登录失败'},
        PLATFORM.IOS: {'label': '登录失败', 'className': 'StaticText'}
    }
    confirm_btn = {
        PLATFORM.AND: {'text': '确定'},
        PLATFORM.IOS: {'label': '确定', 'className': 'Button'}
    }
    qq_login_flag = {
        PLATFORM.AND: {'descriptionContains': '快捷入口'},
        PLATFORM.IOS: {'label': '快捷入口', 'className': 'Button'}
    }
    # first install
    privacy_title = {
        PLATFORM.AND: {'text': '服务协议和隐私政策'},
        PLATFORM.IOS: {'label': '服务协议和隐私政策', 'className': 'StaticText'}
    }
    agree_btn = {
        PLATFORM.AND: {'text': '同意'},
        PLATFORM.IOS: {'label': '同意', 'className': 'StaticText'}
    }
    first_login_btn = {
        PLATFORM.AND: {'text': '登录'},
        PLATFORM.IOS: {'name': '登录', 'className': 'Button'}
    }
    authority_title = {
        PLATFORM.AND: {'text': '权限申请'},
        PLATFORM.IOS: {'label': '权限申请', 'className': 'StaticText'}
    }
    authorize_btn = {
        PLATFORM.AND: {'text': '去授权'},
        PLATFORM.IOS: {'label': '去授权', 'className': 'StaticText'}
    }


if __name__ == '__main__':
    print(PACKAGE.IOSQQ == 'com.tencent.mqq')
    print('ios' in COMMON.PLATFORMS)




#!/usr/local/bin python3
# -*- coding: utf-8 -*-

"""
    created by iprobeyang@gmail.com 2021/5/4
"""
# import os
#
# from fast_tracker import config
# from fast_tracker.utils import functions
# os.environ['FastTracker_Enable'] = "True"
# os.environ['FastTracker_LogLevel'] = "41"
# os.environ['FastTracker_TenantCode'] = "4sss"
#
# env_dict = os.environ
#
# for key, val in env_dict.items():
#     if key.startswith("FastTracker_"):
#         config_name = functions.lower_case_name(key[12:])
#         setattr(config, config_name, val)
#
# print(config.enable)
# print(config.log_level)
# print(config.tenant_code)

a = "cus_user_code_reader".replace('_', '-')
print(a)
# -*- coding: utf-8 -*- 
# @Time : 2020-03-21 09:43 
# @Author : zhengjinlei 
# @File : utils.py
from custmenu.models import MinorAddress


def add_menu_to_app_list(app_dict: dict, address: MinorAddress):
    major = address.major
    menu_index = address.menu_index if address.menu_index else ord(address.name[:1])
    if major.app_label in app_dict.keys():
        model = {'name': address.name, 'object_name': address.object_name,
                 'perms': {'add': False, 'change': False, 'delete': False, 'view': True},
                 'admin_url': address.admin_url,
                 'add_url': '#',
                 'view_only': True,
                 'menu_index': menu_index
                 }
        app_dict[major.app_label]['models'].append(model)
    else:
        app_dict[major.app_label] = {'name': major.name, 'app_label': major.app_label, 'app_url': major.app_url,
                                     'has_module_perms': False,
                                     'models': [{
                                         'name': address.name,
                                         'object_name': address.object_name,
                                         'perms': {'add': False, 'change': False, 'delete': False,	'view': True},
                                         'admin_url': address.admin_url,
                                         'add_url': '#',
                                         'view_only': True,
                                         'menu_index': menu_index
                                     }]}

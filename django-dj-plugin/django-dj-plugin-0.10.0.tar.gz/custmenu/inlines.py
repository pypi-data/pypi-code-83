# -*- coding: utf-8 -*- 
# @Time : 2020-03-21 10:04 
# @Author : zhengjinlei 
# @File : inlines.py
from django.contrib import admin

from custmenu.models import MinorAddress


class MinorAddressInline(admin.TabularInline):
    model = MinorAddress
    extra = 0

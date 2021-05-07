# -*- coding: utf-8 -*-
import json
import datetime


def sql2dict(sql):
    sql_dict = dict()
    if isinstance(sql, list):
        for i in sql:
            sql_dict[str(i['id'])] = i
    return sql_dict


def sql2key(sql, k):
    sql_dict = dict()
    try:
        if isinstance(sql, list):
            for i in sql:
                t = list()
                if str(i[k]) in sql_dict.keys():
                    t.extend(sql_dict[str(i[k])])
                t.append(i)
                sql_dict[str(i[k])] = t
    except:
        print(__name__, sql)
        print(__name__, k)

    return sql_dict


class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        else:
            return json.JSONEncoder.default(self, obj)

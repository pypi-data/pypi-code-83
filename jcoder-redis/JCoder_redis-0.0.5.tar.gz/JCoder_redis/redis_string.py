#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2021/5/1 15:42   satan      1.0         None
"""
from JCoder_redis import Redis

class r_str(Redis):
    def __init__(self,host :str='localhost',port: int=6379,default_db :int=0,is_decode :bool =True):
        """
        初始化
        """
        super().__init__(host,port,default_db,is_decode)

    def __getitem__(self, item: str) -> str:
        """
        获取值
        :param item:
        :return:
        """
        return self._redis.get(item)

    def __setitem__(self, key: str, value: tuple) -> None:
        """
        设置值
        :param key:
        :param value:
        :return:
        """
        self._redis.set(key,value) if type(value)==str else self._redis.setex(name=key,value=value[0],ex=value[1])

    def __iadd__(self, other: tuple):
        """
        自增
        :param other:
        :return:
        """
        self._redis.set(other[0],self._redis.get(other[0])+other[1])
        return self

    def memset(self,args:dict):
        """

        :param args:
        :return:
        """
        self._redis.mset(args)

    def memget(self,names:list):
        """

        :param names:
        :return:
        """
        return self._redis.mget(names)

    def getrange(self,key,start,end):
        """

        :param key:
        :param start:
        :param end:
        :return:
        """
        return self._redis.getrange(key,start,end)

    def setrange(self,key,offset,val):
        """

        :param key:
        :param offset:
        :param val:
        :return:
        """
        self._redis.setrange(key,offset,val)

    def strlen(self,key):
        """

        :param key:
        :return:
        """
        return self._redis.strlen(key)
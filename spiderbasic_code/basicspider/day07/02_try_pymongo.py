#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 18-10-23  @Author:libo  @FileName: 01_try_pymongo.py
from pymongo import MongoClient
client = MongoClient()
collection = client["cli"]["t3"]

# # 插入数据
# list = [{"_id":i,"name":"py{}".format(i)} for i in range(1000)]
# print(list)
# collection.insert_many(list)

re_list = list(collection.find())

ret = [i["name"] for i in re_list if i["_id"]%100 == 0 and i["_id"]!=0 ]

print(ret)
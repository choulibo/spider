#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 18-10-23  @Author:libo  @FileName: 01_try_pymongo.py

from pymongo import MongoClient

# db = MongoClient().test18
# db.insert_many(i["name"]:)
client = MongoClient()
collections = client['test18']['t1']

# -----------------------------------------
# 插入一条数据
# client = MongoClient(host="127.0.0.1",port=27017)
#
# collection = client['test17']['t1']
# 创建一个db变量
# 通过.来获取数据库,方便在终端执行
# db = MongoClient().test17
# # 使用db变量.集合名.方法来操作数据库
# db.user.insert_many({"userbame": "zhangsan", "password": "zhansan123"})
# ret = db.user# for i in ret:
#     print(i)

# -----------------------------------------
# # 插入多条数据
# # db = MongoClient().test18
# # db.insert_many(i["name"]:)
# client = MongoClient()
# collections = client['test18']['t1']
# # temp_list = [{"_id":i,"py_{}".format(i)} for i in range(100)]
# temp_list = [{"name": "py{}".format(i)} for i in range(20)]
# ret = collections.insert_many(temp_list)
#
# t = collections.find_one({"name":"py17"})
# # # for r in ret:
# # print(ret)
# print(t)

# -----------------------------------------

# # 更新一条数据
# ret = collections.update_one({"name":"py17"},{"$set":{"name":"py170"}})
#
# t = collections.find_one({"name":"py170"})
# print(t)

# -----------------------------------------
# 更新多条数据
# ret = collections.update_many({"name": "py170"}, {"$set": {"name": "pyy170"}})
#
# t = collections.find()
# for ty in t:
#     print(ty)


# # 删除1条数据
# ret = collections.delete_one({"name": "pyy170"})
#
# t = collections.find()
# for ty in t:
#     print(ty)

# 删除多条数据
ret = collections.delete_many({"name": "py0"})

t = collections.find()
for ty in t:
    print(ty)
#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 18-10-19  @Author:libo  @FileName: x.py
# import requests
# r = requests.get('http://www.santostang.com/')
# print('文本编码:',r.encoding)
# print('响应状态码:',r.status_code)
# print('字符串方式的响应:',r.text)


import requests

url = "http://www.baidu.com"
response = requests.get(url)
print(type(response.cookies))

cookies = requests.utils.dict_from_cookiejar(response.cookies)
print(cookies)

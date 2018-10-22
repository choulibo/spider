#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 18-10-22  @Author:libo  @FileName: 07_netease_cloud_music.py
import requests
from lxml import etree

url = "http://music.163.com/discover/playlist"
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"}
resposne = requests.get(url,headers= headers)
html = etree.HTML(resposne.content.decode())
dl_list = html.xpath("//dl[@class='f-cb']")
print(dl_list)
ret = html.xpath("//dl[@class='f-cb']/dt//text()")
ret2 = html.xpath("//dl[@class='f-cb']/dd/a/text()")
print(ret)
print(ret2)


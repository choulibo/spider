#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 18-10-19  @Author:libo  @FileName: 001_100内的奇数.py

for i in range(1,101):
    if i%2 == 1:
        # print(i)
        with open('num.txt','a+',encoding='utf-8') as f:
            f.write(str(i))
            f.write('\n')

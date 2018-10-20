#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 18-10-19  @Author:libo  @FileName: 002_9*9乘法口诀表.py

for i in range(1,10):
    for j in range(1,i+1):
        # print("%d * %d = %d " %(j,i,i*j),end='')
        print("%d * %d = %d " %(j,i,i*j),end='')
    print('')

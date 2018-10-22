#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 18-10-19  @Author:libo  @FileName: x.py
while True:  # 防止主线程结束
    time.sleep(0.0001)  # 避免cpu空转，浪费资源
    if self.total_response_num >= self.total_requests_num:
        self.is_running = False
        break
self.pool.close()  # 关闭线程池，防止新的线程开启
# self.pool.join() #等待所有的子线程结束

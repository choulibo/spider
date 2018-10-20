#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 18-10-20  @Author:libo  @FileName: 02_qiubai.py
import requests
from lxml import etree
# from queue import Queue
# import threading
import time
from multiprocessing import Process
from multiprocessing import JoinableQueue as Queue


class QiuBai:
    """qiubaispider"""

    def __init__(self):
        self.url = 'https://www.qiushibaike.com/8hr/page/{}'
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"}
        self.url_queue = Queue()
        self.html_queue = Queue()
        self.content_list_queue = Queue()

    def get_url_list(self):
        """获取url_list"""
        # return [self.url.format(i) for i in range(1, 14)]
        for i in range(1,14):
            self.url_queue.put(self.url.format(i))

    def parse_url(self):
        """获取响应"""
        while True:
            # print(url)
            url = self.url_queue.get()
            response = requests.get(url, headers=self.headers)
            # return response.content.decode()
            print(response)
            if response.status_code != 200:
                self.url_queue.put(url)
            else:
                self.html_queue.put(response.content.decode())
            self.url_queue.task_done()


    def get_content_list(self):
        """提取数据"""
        while True:
            html_str = self.html_queue.get()
            html = etree.HTML(html_str)
            div_list = html.xpath("//div[@id='content-left']/div")
            content_list = []
            for div in div_list:
                item = {}
                item['user_name'] = div.xpath('.//h2/text()')[0].strip()
                item['content'] = [i.strip() for i in div.xpath('.//div[@class = "content"]/span/text()')]
                content_list.append(item)
            self.content_list_queue.put(content_list)
            self.html_queue.task_done()

    def save_content(self):
        """保存数据"""
        while True:
            content_list = self.content_list_queue.get()
            for content in content_list:
                # print(content)
                with open('process.txt','a+',encoding='utf-8') as f:
                    f.write(str(content))
            self.content_list_queue.task_done()

    def run(self):
        thread_list = []
        # 1.准备url列表
        t_url = Process(target=self.get_url_list)
        thread_list.append(t_url)
        # 2.发送请求,获取响应
        for i in range(3):
            t_parse = Process(target=self.parse_url)
            thread_list.append(t_parse)
        # 3.提取数据
        t_content = Process(target=self.get_content_list)
        thread_list.append(t_content)
        # 4.保存数据
        t_save = Process(target=self.save_content)
        thread_list.append(t_save)

        for process in thread_list:
            process.daemon = True # 把子线程设置为守护线程
            process.start()
        for q in [self.url_queue,self.html_queue,self.content_list_queue]:
            q.join()  # 让主线程堵塞,等待队列计数为0

if __name__ == '__main__':
    t1 = time.time()
    qiubai = QiuBai()
    qiubai.run()
    print("total_time:",time.time()-t1)
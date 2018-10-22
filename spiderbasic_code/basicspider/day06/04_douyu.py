#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 18-10-21  @Author:libo  @FileName: 04_douyu.py
import time

from selenium import webdriver


class DouYu:
    """爬取斗鱼直播的所有房间号"""

    def __init__(self):
        self.start_url = 'https://www.douyu.com/directory/all'
        self.driver = webdriver.Chrome()

    def get_content_list(self):
        """获取数据"""
        # li_list = self.driver.find_elements_by_xpath('//ul[@id="live-list-contentbox"/li')
        li_list = self.driver.find_elements_by_xpath("//ul[@id='live-list-contentbox']/li")
        # 对返回数据列表进行遍历
        content_list = []
        for li in li_list:
            item = {}
            item['title'] = li.find_element_by_xpath("./a").get_attribute('title')
            item['anchor'] = li.find_element_by_xpath(".//span[@class='dy-name ellipsis fl']").text
            item['watch_num'] = li.find_element_by_xpath('.//span[@class = "dy-num fr"]').text
            print(item)
            content_list.append(item)

        # 提取下一页
        next_url = self.driver.find_elements_by_xpath("//a[@class = 'shark-pager-next']")
        next_url = next_url[0] if len(next_url) > 0 else None
        return content_list, next_url

    def save_content_list(self, content_list):
        for content in content_list:
            with open('douyu.json','a+',encoding='utf-8') as f:
                f.write(str(content))

    def run(self):
        """运行主程序"""
        # 1.start_url
        # 2.发送请求,获取响应
        self.driver.get(self.start_url)

        # 3.提取数据
        content_list,next_url = self.get_content_list()
        # 4.保存数据
        self.save_content_list(content_list)

        # 5.下一页的提取
        while next_url is not None:
            next_url.click()
            time.sleep(3)
            content_list,next_url = self.get_content_list()
            self.save_content_list(content_list)

if __name__ == '__main__':
    douyu = DouYu()
    douyu.run()

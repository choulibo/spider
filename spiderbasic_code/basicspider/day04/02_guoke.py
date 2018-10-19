# -*- coding:utf-8 -*-
import json
import re

import requests


class Guoke:
    """获取果壳网"""

    def __init__(self):
        self.url = "https://www.guokr.com/ask/highlight/?page={}"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Mobile Safari/537.36"
        }

    def get_url_list(self):
        return [self.url.format(i) for i in range(1, 101)]

    def parse_url(self, url):
        '''获取响应'''
        resp = requests.get(url, headers=self.headers)
        html_str = resp.content.decode()
        return html_str

    def get_content_lsit(self, html_str):
        """提取数据"""
        content_list = re.findall(r"<h2><a target=\"_blank\" href=\"(.*?)\">(.*?)</a></h2>", html_str, re.S)
        return content_list

    def save_content(self, content_list):
        """保存数据"""
        with open('a.json', 'a', encoding='utf-8') as f:
            for content in content_list:
                # print(content)
                f.write(json.dumps(content, ensure_ascii=False))
                f.write('\n')
            print('OK')

    def run(self):
        '''运行主程序'''
        # 1.获取url
        url_list = self.get_url_list()
        # 2. 获取响应
        for url in url_list:
            html_str = self.parse_url(url)
            # 3.提取数据
            content_list = self.get_content_lsit(html_str)
            # 4.保存数据
            self.save_content(content_list)


if __name__ == '__main__':
    guoke = Guoke()
    guoke.run()

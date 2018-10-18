# coding=utf-8
import requests
import json
import sys


class Fanyi:
    def __init__(self, query_string):
        self.url = "http://fanyi.baidu.com/basetrans"
        self.query_string = query_string
        self.headers = {
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"}
        self.langdetect_url = "http://fanyi.baidu.com/langdetect"

    def get_post_data(self):  # 1.url，post_data
        # 1.url
        data = {"query": self.query_string}
        # 2.发送请求，获取响应
        json_str = self.parse_url(self.langdetect_url, data)
        # 3.提取数据
        lan = json.loads(json_str)["lan"]
        to = "en" if lan == "zh" else "zh"
        post_data = {"query": self.query_string,
                     "from": lan,
                     "to": to}
        return post_data

    def parse_url(self, url, data):  # 发送请求，获取响应
        resposne = requests.post(url, data=data, headers=self.headers)
        return resposne.content.decode()

    def get_ret(self, json_str):  # 3.提取数据
        temp_dict = json.loads(json_str)
        ret = temp_dict["trans"][0]["dst"]
        print("{} :{}".format(self.query_string, ret))

    def run(self):  # 实现主要逻辑
        # 1.url，post_data
        post_data = self.get_post_data()
        # 2.发送请求，获取响应
        json_str = self.parse_url(self.url, post_data)
        # 3.提取数据
        self.get_ret(json_str)


if __name__ == '__main__':
    # query_string = sys.argv[1]
    query_string = "hello"
    fanyi = Fanyi(query_string)
    fanyi.run()

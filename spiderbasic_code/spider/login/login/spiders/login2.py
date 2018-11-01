# -*- coding: utf-8 -*-
import re

import scrapy

# 模拟表单登录

class Login2Spider(scrapy.Spider):
    name = 'login2'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/login']

    def parse(self, response):
        # 准备post数据
        formdata = {
        "login":"choulibo",
        "password":"XXXXXXXXXX"
        }

        yield scrapy.FormRequest.from_response(
            response,
            formdata = formdata,
            callback = self.parse_login,
        )

    def parse_login(self,response):
        ret = re.findall("choulibo",response.body.decode(),re.I)
        print(ret)

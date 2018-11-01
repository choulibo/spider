# -*- coding: utf-8 -*-
import re

import scrapy

# 携带cookie模拟登录
class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren,com']
    start_urls = ['http://www.renren.com/587961229/profile']


    def start_requests(self):
        cookies_str = '''anonymid=jnrdt89zagvzbr; depovince=GW; _r01_=1; ick_login=cdde41c4-bc95-46b5-9613-03ba41aa4d26; JSESSIONID=abc2xQJb6w0Du6KJmA1Aw; jebecookies=04647eae-d7dc-4846-8960-f24480540009|||||; _ga=GA1.2.1087081991.1540641928; _gid=GA1.2.150754726.1540641928; fenqi_user_city=36; _de=5CD6565CF913905CE31AA8D93C1B4824; p=7f916a38f98f7f3072be13429c6531239; first_login_flag=1; ln_uact=13253670203; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=fd3b63a2a0b2b166d0b19bc5dd5671819; societyguester=fd3b63a2a0b2b166d0b19bc5dd5671819; id=587961229; xnsid=4a8ed9d3; loginfrom=syshome; jebe_key=b308384b-378a-4911-abd9-0bd9edbcb61c%7Caf6b34d8b0d318395be9226e5b5ccc6f%7C1540642385112%7C1%7C1540642388174; wp_fold=0; XNESSESSIONID=74a88a6d8d75; WebOnLineNotice_587961229=1'''
        # cookie是字典形式
        cookies_dict = {i.split('=')[0]:i.split('=')[1]  for i in cookies_str.split('; ')}
        for url in self.start_urls:
            yield scrapy.Request(
                url,
                callback= self.parse,
                cookies=cookies_dict
            )


    def parse(self, response):
        # 判断是否请求成功
        ret = re.findall('AHA',response.body.decode())
        print(ret)
        yield scrapy.Request(
            url = 'http://blog.renren.com/blog/587961229/myBlogs',
            callback=self.parse_next
        )

    def parse_next(self,response):
        # 判断是否请求成功
        ret = re.findall("AHA",response.body.decode())
        print(ret)
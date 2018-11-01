# -*- coding: utf-8 -*-
import scrapy


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):  # 处理start_url地址的响应

        # 先分组,在提取数据
        li_list = response.xpath('//div[@class="tea_con"]/div/ul/li')
        for li in li_list:
            item = {}
            item["name"] = li.xpath('.//h3/text()').extract_first()
            item["title"] = li.xpath('.//h4/text()').extract_first()
            # item["desc"] = li.xpath('.//p/text()').extract_first()
            print(item)

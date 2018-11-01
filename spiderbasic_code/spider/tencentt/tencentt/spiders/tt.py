# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

# 利用crawl进行腾讯招聘的爬虫
class TtSpider(CrawlSpider):
    name = 'tt'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['https://hr.tencent.com/position.php']

    rules = (
        # 提取列表页的URL地址
        Rule(LinkExtractor(allow=r'position\.php\?&start=\d+#a/'), follow=True),
        # 提取详情页的URL地址
        Rule(LinkExtractor(allow=r'position_detail.php\?id=\d+&keywords=&tid=0&lid=0'), callback='parse_item'),
    )

    def parse_item(self, response):
        i = {}
        # i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        # i['name'] = response.xpath('//div[@id="name"]').extract()
        # i['description'] = response.xpath('//div[@id="description"]').extract()
        item = {}
        item["title"] = response.xpath("//td[@id='sharetitle']/text()").extract_first()
        item["duty"] = response.xpath("//div[text()='工作职责：']/following-sibling::ul[1]/li/text()").extract()
        item["require"] = response.xpath("//div[text()='工作要求：']/following-sibling::ul[1]/li/text()").extract()
        print(item)

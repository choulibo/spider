# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_redis.spiders import RedisCrawlSpider
import re


class AmazonSpider(RedisCrawlSpider):
    name = 'amazon'
    allowed_domains = ['amazon.cn']
    # start_urls = ['http://amazon.cn/']
    redis_key = 'amazon'

    rules = (
        # 实现同时提取大小分类url地址
        Rule(LinkExtractor(restrict_xpaths=("//ul[contains(@class,'a-unordered-list a-nostyle a-vertical s-ref-indent-')]/div/li")), follow=True),
        # 实现提取图书详情页的url地址
        Rule(LinkExtractor(restrict_xpaths=("//div[@id='mainResults']/ul/li//h2/..",)), callback="parse_item"),

        # 实现列表页的翻页
        Rule(LinkExtractor(restrict_xpaths=("//div[@id='pagn']//a",)), follow = True),

    )

    def parse_item(self, response):
        item = {}
        item["book_name"] = response.xpath("//span[contains(@id,'roductTitle')]/text()").extract_first()
        item["book_author"] = response.xpath("//div[@id='bylineInfo']/span[@class='author notFaded']/a/text()").extract()
        item["book_press"] = response.xpath("//b[text()='出版社:']/../text()").extract_first()
        item["book_cate"] = response.xpath("//div[@id='wayfinding-breadcrumbs_feature_div']/ul/li[not(@class)]/span//a/text()").extract()
        # item["book_url"] = response.url
        item["book_desc"] = re.findall(r"\s+<noscript>(.*?)</noscript>\n  <div id=\"outer_postBodyPS\"",response.body.decode(),re.S)[0]
        # print(item)
        # yield item
        item["is_ebook"] = "kindle电子书" in response.xpath("//title/text()").extract_first()
        if item["is_ebook"]:
            item["ebook_price"] = response.xpath("//td[@class='a-color-price a-size-medium a-align-bottom a-text-bold']/text()").extract_first()
        else:
            item["book_price"] = response.xpath("//span[contains(@class,' price3P')]/text()").extract_first()
        print(item)
        print("+"*100)
        yield item
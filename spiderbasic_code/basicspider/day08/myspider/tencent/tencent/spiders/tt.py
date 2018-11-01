# -*- coding: utf-8 -*-
import scrapy


class TtSpider(scrapy.Spider):
    name = 'tt'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['https://hr.tencent.com/position.php?&start=0#a']

    def parse(self, response):
        # 提取当前页面的数据
        # 先分组,再提取数据
        tr_list = response.xpath('//table[@class="tablelist"]/tr')[1,-1]
        for tr in tr_list:
            item = {}
            item["position_name"] = tr.xpath('./td[1]/a/text()').extract_first()
            item["position_href"] = tr.xpath('./td[1]/a/@href').extract_first()
            item["position_cate"] = tr.xpath('./td[2]/text()').extract_first()
            item["position_num"] = tr.xpath('./td[3]/text()').extract_first()
            item["location"] = tr.xpath('./td[4]/text()').extract_first()
            item["publish_date"] = tr.xpath('./td[5]/text()').extract_first()
            yield item

        # 翻页
        next_url = response.xpath('//a[@id="next"]/@href').extract_first()
        # 最后一页的next的href不是一个url,是一个"javascript:;"
        if next_url != 'javascript:;':
            next_url = 'https://hr.tencent.com/' + next_url
            yield scrapy.Request(
                next_url,
                callback=self.parse
            )
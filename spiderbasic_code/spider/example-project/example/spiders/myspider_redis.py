from scrapy_redis.spiders import RedisSpider


class MySpider(RedisSpider):  #能够实现分布式爬虫
    """Spider that reads urls from redis queue (myspider:start_urls)."""
    name = 'myspider_redis'  # 爬虫名
    redis_key = 'myspider:start_urls'  # start_url在redis中的键

    def __init__(self, *args, **kwargs):
        # Dynamically define the allowed domains list.
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(MySpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        return {
            'name': response.css('title::text').extract_first(),
            'url': response.url,
        }

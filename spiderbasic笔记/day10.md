#### 1.crawlspider 类的使用

##### crawlspider 可以实现：

- 从response中提取满足所有规则 的url地址
- 自动构建自己的requests请求，发送给引擎

##### 创建crawlspider 爬虫

scrapy genspider -t scrawl 项目名 域名

 ```Python
# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class TtSpider(CrawlSpider):
    name = 'tt'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['https://hr.tencent.com/position.php']

    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
 ```

- rules 是一个元组或者列表，包含的是rule对象
- Rule 表示规则，包含LinkExtractor，callback和follow 
  - LinkExtractor :连接提取器，可以通过正则或者xpath来进行地址的匹配；
  - callback：表示**经过连接提取器出来的url地址响应**的回调函数，如果没有表示响应不会进行回调函数的处理
  - follow ：表示 **经过连接提取器出来的url地址响应**是否还会继续被rules中规则进行提取

![1540638125698](/home/libo/.config/Typora/typora-user-images/1540638125698.png)

##### 补充知识点

![1540638171769](/home/libo/.config/Typora/typora-user-images/1540638171769.png)

#### 2.下载中间件

- 编写Downloader MIddleware 和写一个pipeline一样，定义一个类，在setting中开启
- Downloader MIddleware 默认的方法：
  - process_request(self,request,spider):
    - 当每个request通过下载中间件时，该方法被调用
    - 存在三种情况
      1. 返回None，继续请求，被下载器执行
      2. 返回Requests对象，经过引擎返回给调度器
      3. 返回Response 对象，response直接返回给引擎交给爬虫
  - process_response(self,request,response,spider):
    - 当下载器完成http请求，传递响应给引擎的时候调用
    - 存在两种情况
      1. 返回response对象，通过引擎交给爬虫
      2. 返回request对象，通过引擎交给调度器

- 定义随机实现User-Agent下载中间件

  ```Python
  # -*- coding: utf-8 -*-
  import random
  # 定义方法
  def get_ua():
      first_num = random.randint(55, 62)
      third_num = random.randint(0, 3200)
      fourth_num = random.randint(0, 140)
      os_type = [
          '(Windows NT 6.1; WOW64)', '(Windows NT 10.0; WOW64)', '(X11; Linux x86_64)',
          '(Macintosh; Intel Mac OS X 10_12_6)'
      ]
      chrome_version = 'Chrome/{}.0.{}.{}'.format(first_num, third_num, fourth_num)
  
      ua = ' '.join(['Mozilla/5.0', random.choice(os_type), 'AppleWebKit/537.36',
                     '(KHTML, like Gecko)', chrome_version, 'Safari/537.36']
                    )
      return ua
  
  #  定义中间件
  class RandomUserAgentMid:
      def process_request(self,request,spider):
          request.headers["User-Agent"] = get_ua()
  # 定义检查ua
  class CheckUA:
      def process_response(self,request,response,spider):
          print(request.headers["User-Agent"],"*"*100)
          return response
  ```

- 定义实现使用代理的下载中间件

  ```Python
  # -*- coding: utf-8 -*-
  class ProxyMid:
      def process_request(self,request,spider):
          request.meta["proxy"] = "http://127.0.0.1:8000"
  ```


#### 3.使用scrapy 进行模拟登录

##### scrapy 携带cookie进行模拟登录

  ```Python
  #  cookie 字典传递给请求的cookies 参数
    yield scrapy.Request(
                  url,
                  callback=self.parse,
                  cookies=cookie_dict,
                  # headers = {"Cookie":cookies_str}
              )
  ```

  - 携带cookie进行登录的应用场景

    1. cookie过期时间很长，常见于一些不规范网站
    2. 能在cookie过期之前把搜到的数据拿到
    3. 配合其他程序使用，比如把selenium把登录之后的cookie获取到的保存到本地，scrapy 发送请求之前先读取到本地cookie

  - scrapy的start_request方法的学习

    scrapy中的start_url 是通过start_requests来进行处理

    ```Python
    # -*- coding: utf-8 -*-
     def start_requests(self):
         cls = self.__class__
         if method_is_overridden(cls, Spider, 'make_requests_from_url'):
             warnings.warn(
                 "Spider.make_requests_from_url method is deprecated; it "
                 "won't be called in future Scrapy releases. Please "
                 "override Spider.start_requests method instead (see %s.%s)." % (
                     cls.__module__, cls.__name__
                 ),
             )
             for url in self.start_urls:
                 yield self.make_requests_from_url(url)
         else:
             for url in self.start_urls:
                 yield Request(url, dont_filter=True)
    ```

    所以，如果start_url地址中的url是登录后才能访问url地址，则需要重写start_request方法并在其中手动添加cookie

  - 实现写到cookie登录人人网

    ```Python
    # -*- coding: utf-8 -*-
    import scrapy
    import re
    
    class RenrenSpider(scrapy.Spider):
        name = 'renren'
        allowed_domains = ['renren.com']
        start_urls = ['http://www.renren.com/941954027/profile']
    
        def start_requests(self):
            cookie_str = "cookie_str"
            cookie_dict = {i.split("=")[0]:i.split("=")[1] for i in cookie_str.split("; ")}
            yield scrapy.Request(
                self.start_urls[0],
                callback=self.parse,
                cookies=cookie_dict,
                # headers={"Cookie":cookie_str}
            )
    
        def parse(self, response):
            ret = re.findall("新用户287",response.text)
            print(ret)
            yield scrapy.Request(
                "http://www.renren.com/941954027/profile?v=info_timeline",
                callback=self.parse_detail
            )
    
        def parse_detail(self,response):
            ret = re.findall("新用户287",response.text)
            print(ret)
    ```

    在settings中开启cookie_debug

    在settings.py中通过设置`COOKIES_DEBUG=True `能够在终端看到cookie的传递传递过程

##### scrapy 发送post请求

  scrapy 中发送post请求的方法，通过scrapy.FormRequest 能够发送post请求，同时需要添加formdata 参数作为请求体

  思路分析

  1. 找到post的url地址

     点击登录按钮进行抓包，然后定位url地址为`https://github.com/session`

  2. 找到请求体的规律

     分析post请求的请求体，其中包含的参数均在前一次的响应中

  3. 验证是否登录成功

     通过请求个人主页，观察是否包含用户名

     代码实现如下：

  ```Python
  # -*- coding: utf-8 -*-
  yield scrapy.FormRequest(
               "https://github.com/session",
               formdata={  # 请求体
                   "authenticity_token":authenticity_token,
                   "utf8":utf8,
                   "commit":commit,
                   "login":"noobpythoner",
                   "password":"zhoudawei123"
               },
               callback=self.parse_login
           )
  ```

##### scrapy 模拟表单提交登录
方法介绍：

  scrapy中具有一个方法：`scrapy.Formrequest.from_response`能够自动的从响应中寻找form表单，然后把formdata中的数据提交到action对应的url地址中

  使用实例如下：

```Python
-*- coding: utf-8 -*-
  def parse(self, response):
      yield scrapy.FormRequest.from_response(
            response,#自动的从中寻找action对应的url地址
            formdata={
                "login":"noobpythoner",
                "password":"***"
            },
            callback = self.parse_login
        )
```



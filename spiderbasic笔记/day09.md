#### scrapy 的深入使用

#### scrapy 的debug信息

![1540547361598](/home/libo/.config/Typora/typora-user-images/1540547361598.png)​	

```python
# Scrapy的版本 和 爬虫项目名称
2018-09-08 14:55:57 [scrapy.utils.log] INFO: Scrapy 1.5.1 started (bot: yangguang)
# scrapy加载的第三方模块的版本信息 以及python的版本新
2018-09-08 14:55:57 [scrapy.utils.log] INFO: Versions: lxml 4.2.1.0, libxml2 2.9.5, cssselect 1.0.3, parsel 1.4.0, w3lib 1.19.0, Twisted 18.4.0, Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 17:00:18) [MSC v.1900 64 bit (AMD64)], pyOpenSSL 18.0.0 (OpenSSL 1.1.0i  14 Aug 2018), cryptography 2.3.1, Platform Windows-10-10.0.17134-SP0
# 配置文件的所有配置新
2018-09-08 14:55:57 [scrapy.crawler] INFO: Overridden settings: {'BOT_NAME': 'yangguang', 'NEWSPIDER_MODULE': 'yangguang.spiders', 'SPIDER_MODULES': ['yangguang.spiders'], 'USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
# 启用的扩展
2018-09-08 14:55:57 [scrapy.middleware] INFO: Enabled extensions:
['scrapy.extensions.corestats.CoreStats', # 内容统计
 'scrapy.extensions.telnet.TelnetConsole', # Telnet控制台
 'scrapy.extensions.logstats.LogStats'] # 日志统计
# 启用的下载器中间件
2018-09-08 14:55:57 [scrapy.middleware] INFO: Enabled downloader middlewares:
['scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware', # http验证
 'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware', # 下载器超时控制
 'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware', # 默认请求头
 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware', # UserAgent
 'scrapy.downloadermiddlewares.retry.RetryMiddleware', # 重试
 'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware', # Html meta标签中的refresh
 'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware', # http压缩
 'scrapy.downloadermiddlewares.redirect.RedirectMiddleware', # 页面跳转自动处理
 'scrapy.downloadermiddlewares.cookies.CookiesMiddleware', # 添加和处理cookie
 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware', # http代理
 'scrapy.downloadermiddlewares.stats.DownloaderStats'] # 下载器信息统计
# 启用的爬虫中间件
2018-09-08 14:55:57 [scrapy.middleware] INFO: Enabled spider middlewares:
['scrapy.spidermiddlewares.httperror.HttpErrorMiddleware', # 自动处理http错误
 'scrapy.spidermiddlewares.offsite.OffsiteMiddleware', # 站点域名过滤和处理
 'scrapy.spidermiddlewares.referer.RefererMiddleware', # Referer头部添加
 'scrapy.spidermiddlewares.urllength.UrlLengthMiddleware', # Url长度处理
 'scrapy.spidermiddlewares.depth.DepthMiddleware'] # 请求深度处理
# 启用的PIPELINE
2018-09-08 14:55:57 [scrapy.middleware] INFO: Enabled item pipelines:
['yangguang.pipelines.YangguangPipeline']
# 爬虫启动
2018-09-08 14:55:57 [scrapy.core.engine] INFO: Spider opened
# 统计信息
2018-09-08 14:55:57 [scrapy.extensions.logstats] INFO: Crawled 0 pages (at 0 pages/min), scraped 0 items (at 0 items/min)
# Telnet控制台信息
2018-09-08 14:55:57 [scrapy.extensions.telnet] DEBUG: Telnet console listening on 127.0.0.1:6023
# 按下了Ctrl+C Scrapy打印出来的信息
2018-09-08 14:55:57 [scrapy.crawler] INFO: Received SIGINT, shutting down gracefully. Send again to force
# 爬虫关闭
2018-09-08 14:55:57 [scrapy.core.engine] INFO: Closing spider (shutdown)
# 下载器请求url 打印的日志
2018-09-08 14:55:58 [scrapy.core.engine] DEBUG: Crawled (200) <GET http://wz.sun0769.com/index.php/question/questionType?type=4&page=0> (referer: None)
# Scrapy关闭前 打印出来的统计信息
2018-09-08 14:55:58 [scrapy.statscollectors] INFO: Dumping Scrapy stats:
{'downloader/request_bytes': 345, # 所有的请求发送了多少字节
 'downloader/request_count': 1, # 发送了多少个请求
 'downloader/request_method_count/GET': 1, # 发送get请求的数量
 'downloader/response_bytes': 29528, # 所有响应的总字节数
 'downloader/response_count': 1, # 响应的总数量
 'downloader/response_status_count/200': 1, # 响应状态吗为200的总数量
 'finish_reason': 'shutdown', # 完成原因
 'finish_time': datetime.datetime(2018, 9, 8, 6, 55, 58, 253924), # 完成时间
 'log_count/DEBUG': 2, # DEBUG级别的日志数量
 'log_count/INFO': 8, # INFO级别的日志数量
 'request_depth_max': 1, # 请求的最大深度
 'response_received_count': 1, # 响应接收数量
 'scheduler/dequeued': 1, # 调度器出队数量 (从调度器中取得了多少个request)
 'scheduler/dequeued/memory': 1, 
 'scheduler/enqueued': 32, # 调度器入队数量 (添加到调度器中的request数量)
 'scheduler/enqueued/memory': 32,
 'start_time': datetime.datetime(2018, 9, 8, 6, 55, 57, 484373)} # 爬虫启动时间
# 爬虫结束
2018-09-08 14:55:58 [scrapy.core.engine] INFO: Spider closed (shutdown)
```



程序启动时都会报下列信息，有时也可以从debug信息中找到报错信息，

#### scrapy shell 的使用

scrapy shell 是scrapy 提供的一个终端工具，可以查看scrapy 中对象的属性和方法

使用方法：scrapy shell "url地址"

用处：

- scrapy shell url 可以进交互式终端
- 查看scrapy 中模块的属性
- 测试xpath ，scrapy shell 可以请求指定的页面 只需要请求一次,然后可以反复使用response.xpath来测试xpath.例如有些页面会比较靠后 比如获取最后一个的下一页地址，如果在项目中直接print 会需要爬虫跑起来 跑到最后一页，可能需要很长时间 比如5分钟后请求到了最后一页，结果抛异常了 然后修改xpath 然后在运行爬虫，又过了5分钟 又抛异常了 在进行修改 在运行爬虫，反复几次半个小时过去了，使用scrapy shell 可以直接请求最后一页，反复测试xpath是否能够正常运行。实际中可以写玩部分代码，运行代码测试看是否获取到

常用的几种：

- response.url：当前响应的url地址
- response.request.url：当前响应对应的请求的url地址
- response.headers：响应头
- response.body：响应体，也就是html代码，默认是byte类型
- response.requests.headers：当前响应的请求头
- response.text 能够获取响应str字符串

#### scrapy 中的setting文件

- 在setting文件中存放一些公共变量，在后续项目中便于修改，变量名一般大写

- 导入即可使用：
  - import引入

    from guokr.settings import HOST
    from ..settings import HOST

  - 爬虫中

    self.settings["HOST"] # 键不存在会报错
    self.settings.get("HOST") # 键不存在返回None

  - Pipeline中

    spider.settings.get("HOST")

- setting中的重要字段和内涵
  - USER_AGENT  设置ua

  - ROBOTSTXT_OBEY  是否遵守robot协议，默认是遵守

  - CONCURRENT_REQUESTS  设置并发请求的数量，默认是16个

  - DOWNLOAD_DELAY  下载延迟

  - COOKIE_ENABLED  是否开启cookie 即每次请求带上前一次的cookie，默认是开启的

  - DEFAULT_REQUEST_HEADERS   设置默认请求头

  - SPIDER_MIDDLEWARES 爬虫中间件

  - DOWNLOADER_MIDDLEWARES  下载中间件

    ```python
    # 机器人名称
    BOT_NAME = 'yangguang'
    # 爬虫所在模块的名称
    SPIDER_MODULES = ['yangguang.spiders']
    # 新爬虫所在的名称
    NEWSPIDER_MODULE = 'yangguang.spiders'
    # 日志等级
    LOG_LEVEL = "WARNING"
    # 日志文件路径
    LOG_FILE = "./log.log"
    # User Agent
    USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
    # 是否遵守robots.txt文件
    ROBOTSTXT_OBEY = True
    # 爬虫的并发数量
    CONCURRENT_REQUESTS = 32
    # 每次请求延迟多少秒
    DOWNLOAD_DELAY = 3
    # 每个域名和每个IP的并发限制
    CONCURRENT_REQUESTS_PER_DOMAIN = 16
    CONCURRENT_REQUESTS_PER_IP = 16
    # 是否启动cookie 默认启用
    COOKIES_ENABLED = False
    # 默认请求头
    DEFAULT_REQUEST_HEADERS = {
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Language': 'en',
    }
    # 自定义爬虫中间件
    SPIDER_MIDDLEWARES = {
    	'yangguang.middlewares.YangguangSpiderMiddleware': 543,
    }
    # 自定义下载中间件
    DOWNLOADER_MIDDLEWARES = {
    	'yangguang.middlewares.YangguangDownloaderMiddleware': 543,
    }
    # 项目扩展
    EXTENSIONS = {
    	'scrapy.extensions.telnet.TelnetConsole': None,
    }
    # 自定义管道
    ITEM_PIPELINES = {
       'yangguang.pipelines.YangguangPipeline': 300,
    }
    ```


  #### 管道中的open_spider 和close_spider的方法

  管道中除了定义process_item外，还可以定义两个方法：

  - open_spider(spider) :能够在爬虫开启的时候执行一次

  - close_spider(spider) :在爬虫关闭的时候执行一次

    所以，上述方法常用于爬虫和数据库的交互，在爬虫开启时建立和数据库 的链接，在爬虫关闭的时候断开和数据库的链接；例如把保存到mongodb中的代码放进open_spider中


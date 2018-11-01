### scrapy基础概念和流程

scrapy是一个为了爬取网站数据,提取结构性数据而编写的应用框架,只需要实现少量的代码,就能够快速的抓取.Scrapy使用了Twist异步网络框架,可以加速我们的下载速度.

官方文档: <http://scrapy-chs.readthedocs.io/zh_CN/1.0/intro/overview.html>

#### 异步和非堵塞

- 异步:调用在发出之后,这个调用就直接返回,不管有无结果

- 非堵塞:关注的是程序在等待调用结果(消息,返回值)时的状态,指不能立刻得到结果之前,该调用不会阻塞当前的进程.

  ![1540464625646](/home/libo/.config/Typora/typora-user-images/1540464625646.png)



#### Sceapy流程

流程简述如下:

1. 调度器把requests对象交给--->引擎--->下载中间件--->下载器;
2. 下载器发送请求,获取响应--->返回给下载中间件--->交给引擎--->引擎识别对象--->交给爬虫中间件--->爬虫;
3. 爬虫接受响应根据识别的对象:
   1. 爬虫提取其中的url地址,组装成requests--->爬虫中间件--->引擎--->调度器;
   2. 爬虫提取其中的数据--->跳过爬虫中间件交给引擎---管道
4. 管道进行数据的处理和保存;

### Scrapy的使用

scrapy项目实现流程:

- 创建scrapy项目:scrapy startproject  **project_name**
- 生成一个爬虫: scrapy genspider  **spider_name**  "url_name"
- 提取数据: 完善spider ,使用xpath等方法
- 保存数据:pipeline 中保存数据
- 运行爬虫scrapy crawl spider_name

![1540434386971](/home/libo/.config/Typora/typora-user-images/1540434386971.png)

数据传到pipeline中,yield可以进行数据的传递,交给其他管道,不用return 是因为return 会阻止循环的继续执行

![1540434566284](/home/libo/.config/Typora/typora-user-images/1540434566284.png)

yield可以传递的对象是:BaseItem , Request , dict , None

#### scrapy 如何构造请求

- scrapy.Request(url,callback,meta,dont_filter)
  - url: 详情页，下一页 的url
  - callback:回调，url地址响应的处理函数
  - meta：在不同的函数中传递数据
  - dont_filer :默认值false,过滤请求，请求过的不会在被请求，为True，表示还会被继续请求

- yield scrapy.Request(url,calback,meta,dont_filter)

#### item 的使用

```python
# 定义
class Item(scrapy.Item):
    name = scrapy.Field()
    
  # 导入使用字典
导入，使用name字典
```

scrapy 中的parse函数是什么

- 处理start_url 地址的响应
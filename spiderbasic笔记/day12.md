### scrapy_redis实现分布式爬虫

- 继承自RedisSpider

- 增加了一个redis_key的键，没有start_url,因为是分布式，如果每台电脑都请求一次start_url就会重复

  ![1540888407469](/home/libo/.config/Typora/typora-user-images/1540888407469.png)

#### Redisspider的爬虫和scrapy.spider的区别

- 区别
  - redisspider继承的父类scrapyspider
  - redisspider没有start_url，有redis_key
    - redis_key表示redis中存放start_url地址的键
- 创建爬虫
  - scrapy genspider 爬虫名 允许爬取的范围
  - 修改父类
  - 添加 redis_key
- 启动爬虫
  - scrapy crawl 爬虫，让爬虫就绪
  - lpush redis_key url 爬虫会启动

### RedisCrawlSpider

- 和scrapy的crawlspider的区别在于，继承的父类不相同，需要添加redis_key

  ![1540888563194](/home/libo/.config/Typora/typora-user-images/1540888563194.png)

#### rediscrawlspider 的爬虫和crawlspider的区别

- 区别
  - rediscrawlspider 继承的父类是RedisCrawlSpider
  - Rediscrawlspider没有start_url ，有redis_key
    - redis_key表示存放start_url地址的键
- 创建爬虫
  - scrapy genspider -t crawl 爬虫名 允许爬取的范围
  - 修改父类
  - 添加redis_key

- 启动爬虫
  - scrapy crawl 爬虫 ，让爬虫就绪
  - lpush redis_key url 

### 爬虫定时启动

#### 启动和安装

![1540891701933](/home/libo/.config/Typora/typora-user-images/1540891701933.png)

#### 使用流程

1. 把爬虫启动命令加入到.sh文件

   其中`>>`表示重定向，把print等信息导入log中

   `2>&1`表示把标准错误作为标准输出，输入用0表示，标准输出用1表示，标准错误用2标识，通过该命令能够把错误一起输出到log中

   ```sh
    cd `dirname $0` || exit 1
    python ./main.py >> run.log 2>&1
   ```

2. 给.sh文件添加执行权限

   ```python
   sudo chmod +x myspder.sh
   ```

3. 写入corntab中

   sh脚本文件也可能会报错，对应的可以把其输出和错误重定向到run2.log中(***注意是绝对路径***)

   ```python
   0 6 * * * /home/ubuntu/..../myspider.sh >> /home/ubuntu/.../run2.log 2>&1
   ```

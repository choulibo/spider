#### 百度贴吧 内容页优化

当我写这段代码的时候，只有老天和我自己知道我在做什么。
现在，只剩老天知道了。

```python
def get_img_list(self,detail_url):
    img_list = []
    
    next_url = detail_url
    while next_url is not None:
        #1. 发送请求，获取响应
        detail_html_str = self.parse_url(next_url)

        #2. 提取数据
        detail_html = etree.HTML(detail_html_str)
        img_list += detail_html.xpath("//img[@class='BDE_Image']/@src")

        #详情页下一页的url地址
        next_url = detail_html.xpath("//a[text()='下一页']/@href")
        next_url =self.part_url+ next_url[0] if len(next_url)>0 else None

    return img_list
```

#### 多线程的方法使用

在python3中主线程主进程结束,子线程,子进程不会结束

为了能够让主线程回收子线程，可以把子线程设置为守护线程,即该线程不重要，主线程结束，子线程结束

```python
t1 = threading.Thread(targe=func,args=(,))
t1.setDaemon(True)
t1.start()   #此时线程才会启动
```

#### 队列Queue

内部有连个数字(两个重要指标)

- 队列中有多少个任务
- 队列中有多少的未完成的任务

```python
#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 18-10-19  @Author:libo  @FileName: x.py
from queue import Queue

q = Queue(maxsize=100)
item = {}
q.put_nowait(item)  # 不等待直接放，队列满的时候会报错
q.put(item)  # 放入数据，队列满的时候回等待
q.get_nowait()  # 不等待直接取，队列空的时候会报错
q.get()  # 取出数据，队列为空的时候会等待
q.qsize()  # 获取队列中现存数据的个数 
q.join()  # 队列中维持了一个计数，计数不为0时候让主线程阻塞等待，队列计数为0的时候才会继续往后执行
q.task_done()
# put的时候计数+1，get不会-1，get需要和task_done 一起使用才会-1
```

q.put(item) 队列中有多少个任务加1 队列中有多少的未完成的任务加1
q.get() 队列中有多少个任务减一
q.task_done() 队列中有多少的未完成的任务减一
q.join() 队列中有多少的未完成的任务是否为零

#### 多进程实现

```
多进程中使用普通的队列模块会发生阻塞，对应的需要使用multiprocessing提供的JoinableQueue模块，
其使用过程和在线程中使用的queue方法相同
```

#### 线程池是实现更快的爬虫

1. 实例化线程池对象

   ```Python
    from multiprocessing.dummy import Pool
    pool = Pool(process=5) #默认大小是cup的个数
   ```

2. 把从发送请求，提取数据，到保存合并成一个函数，交给线程池异步执行,使用方法`pool.apply_async(func)`

   ```python
    def exetute_requests_item_save(self):
        url = self.queue.get()
        html_str = self.parse_url(url)
        content_list = self.get_content_list(html_str)
        self.save_content_list(content_list)
        self.total_response_num +=1
   
    pool.apply_async(self.exetute_requests_item_save)
   ```

3. 通过`apply_async`的方法能够让函数异步执行，但是只能够执行一次,为了让其能够被反复执行，通过添加回调函数的方式能够让_callback 递归的调用自己,同时需要指定递归退出的条件

   ```python
    def _callback(self,temp):
        if self.is_running:
             pool.apply_async(self.exetute_requests_item_save,callback=self._callback)
   
    pool.apply_async(self.exetute_requests_item_save,callback=self._callback)
   ```

4. 确定程序结束的条件 程序在获取的响应和url数量相同的时候可以结束

   ```python
   while True:  # 防止主线程结束
       time.sleep(0.0001)  # 避免cpu空转，浪费资源
       if self.total_response_num >= self.total_requests_num:
           self.is_running = False
           break
   self.pool.close()  # 关闭线程池，防止新的线程开启
   # self.pool.join() #等待所有的子线程结束
   ```

   ****具体代码实现

   ```python
   #!/usr/bin/python3
   # -*- coding: utf-8 -*-
   # @Time : 18-10-20  @Author:libo  @FileName: 02_qiubai.py
   import requests
   from lxml import etree
   from multiprocessing.dummy import Pool
   from queue import  Queue
   import time
   
   class QiuBai:
       """qiubaispider"""
   
       def __init__(self):
           self.url = 'https://www.qiushibaike.com/8hr/page/{}'
           self.headers = {
               "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"}
           self.queue = Queue()
           self.pool = Pool(5)
           self.is_running = True
           self.total_response_num = 0
           self.total_request_num = 0
   
       def get_url_list(self):
           """获取url_list"""
           # return [self.url.format(i) for i in range(1, 14)]
           for i in range(1,14):
               self.queue.put(self.url.format(i))
               self.total_request_num += 1
   
       def parse_url(self, url):
           """获取响应"""
           # print(url)
           response = requests.get(url, headers=self.headers)
           print(response)
           return response.content.decode()
   
       def get_content_list(self, html_str):
           """提取数据"""
           html = etree.HTML(html_str)
           div_list = html.xpath("//div[@id='content-left']/div")
           content_list = []
           for div in div_list:
               item = {}
               item['user_name'] = div.xpath('.//h2/text()')[0].strip()
               item['content'] = [i.strip() for i in div.xpath('.//div[@class = "content"]/span/text()')]
               content_list.append(item)
           return content_list
   
       def save_content(self, content_list):
           """保存数据"""
           for content in content_list:
               # print(content)
               with open('processing_pool.txt','a+',encoding='utf-8') as f:
                   f.write(str(content))
   
       def _execete_request_content_save(self):
           url = self.queue.get()
           # 2.发送请求,获取响应
           html_str = self.parse_url(url)
           # 3.提取数据
           content_list = self.get_content_list(html_str)
           # 4.保存数据
           self.save_content(content_list)
           self.total_response_num += 1
       def _callback(self,temp):
           if self.is_running:
               self.pool.apply_async(self._execete_request_content_save,callback=self._callback)
   
       def run(self):
           # 1.准备url列表
           self.get_url_list()
           # 2.发送请求,获取响应
           for i in range(13):  # 设置并发数为3
               self.pool.apply_async(self._execete_request_content_save,callback=self._callback)
           while True:
               time.sleep(0.0001)
               if self.total_response_num >= self.total_request_num:
                   self.is_running = False
                   break
   
   if __name__ == '__main__':
       t1 = time.time()
       qiubai = QiuBai()
       qiubai.run()
       print('total_cost:',time.time()-t1)
   ```

   #### 协程池具体代码实现

   ```python
   #!/usr/bin/python3
   # -*- coding: utf-8 -*-
   # @Time : 18-10-20  @Author:libo  @FileName: 02_qiubai.py
   
   import gevent.monkey
   gevent.monkey.patch_all()
   
   from gevent.pool import  Pool
   import requests
   from lxml import etree
   import time
   from queue import Queue
   
   class QiuBai:
       """qiubaispider"""
   
       def __init__(self):
           self.url = 'https://www.qiushibaike.com/8hr/page/{}'
           self.headers = {
               "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"}
           self.queue = Queue()
           self.pool = Pool(5)
           self.is_running = True
           self.total_response_num = 0
           self.total_request_num = 0
   
       def get_url_list(self):
           """获取url_list"""
           # return [self.url.format(i) for i in range(1, 14)]
           for i in range(1,14):
               self.queue.put(self.url.format(i))
               self.total_request_num += 1
   
       def parse_url(self, url):
           """获取响应"""
           # print(url)
           response = requests.get(url, headers=self.headers)
           print(response)
           return response.content.decode()
   
       def get_content_list(self, html_str):
           """提取数据"""
           html = etree.HTML(html_str)
           div_list = html.xpath("//div[@id='content-left']/div")
           content_list = []
           for div in div_list:
               item = {}
               item['user_name'] = div.xpath('.//h2/text()')[0].strip()
               item['content'] = [i.strip() for i in div.xpath('.//div[@class = "content"]/span/text()')]
               content_list.append(item)
           return content_list
   
       def save_content(self, content_list):
           """保存数据"""
           for content in content_list:
               # print(content)
               with open('gevent.txt','a+',encoding='utf-8') as f:
                   f.write(str(content))
   
       def _execete_request_content_save(self):
           url = self.queue.get()
           # 2.发送请求,获取响应
           html_str = self.parse_url(url)
           # 3.提取数据
           content_list = self.get_content_list(html_str)
           # 4.保存数据
           self.save_content(content_list)
           self.total_response_num += 1
       def _callback(self,temp):
           if self.is_running:
               self.pool.apply_async(self._execete_request_content_save,callback=self._callback)
   
       def run(self):
           # 1.准备url列表
           self.get_url_list()
           # 2.发送请求,获取响应
           for i in range(13):  # 设置并发数为3
               self.pool.apply_async(self._execete_request_content_save,callback=self._callback)
           while True:
               time.sleep(0.0001)
               if self.total_response_num >= self.total_request_num:
                   self.is_running = False
                   break
   
   if __name__ == '__main__':
       t1 = time.time()
       qiubai = QiuBai()
       qiubai.run()
       print('total_cost:',time.time()-t1)
   ```



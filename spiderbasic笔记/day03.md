#### python三元运算符的使用
a = 10 if  3<2 else 100

#### python中字典推导式的使用
{i:i+10 for i in range(10) if i%3==0}

```python
{0: 10, 9: 19, 3: 13, 6: 16}
```

#### requests模拟登陆的***三种方法***(使用requests处理cookie相关的请求)

##### cookiee和session区别

1. cookie数据存放在客户的浏览器中,session数据放在服务器上
2. cookie不是很安全,可以分析存放在本地的cookie进行cookie欺骗
3. session会在一定时间内保存在服务器上.当访问增多时,会比较占用你服务器的性能
4. 单个cookie保存的数据不能超过4k,很多浏览器都限制一个站点最多保存20个cookie.

- **session**

  - 实例化对象(requests提供了一个叫session类,来实现客户端和服务器的会话保持<1.保存cookie 2.实现和服务器端的长连接>)

  - ```python 
    session = requests.Session()
    session.get(url,headers = headers ) #cookie保存在session中
    ```

  - session.get(url) #带上保存在session中cookie

- **cookie方法headers中**

  ```PYTHON
  url = "http://www.renren.com/941954027/profile"
  headers = {
  	"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
      
  	"Cookie":" Pycharm-26c2d973=dbb9b300-2483-478f-9f5a-16ca4580177e; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1512607763; Pycharm-26c2d974=f645329f-338e-486c-82c2-29e2a0205c74; _xsrf=2|d1a3d8ea|c5b07851cbce048bd5453846445de19d|1522379036"}
  
  requests.get(url,headers=headers)
  ```

- **cookie传递给cookies参数**

  - cookie = {"cookie 的name的值":"cookie 的value对应的值"}  以登录人人网为例

    ```python
    url = "http://www.renren.com/941954027/profile"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36",
    }
    cookie="anonymid=jghfvoma-b8wgqk; depovince=GW; _r01_=1; JSESSIONID=abc8mwsUgbA-Xh0-5sfmw; ick_login=7123f1e3-d552-4d9a-aa75-e814c81632ca; first_login_flag=1; ln_uact=13146128763; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; loginfrom=syshome; ch_id=10016; _de=7A7A02E9254501DA6278B9C75EAEEB7A; _ga=GA1.2.1446821673.1524880234; _gid=GA1.2.1139412765.1524880234; jebecookies=f6abe0fa-49cf-49d6-ae31-74f4ce2373d5|||||; p=a0ba88dabb32cd73523d10e0d4b9b47a7; t=302f3cb26710699907148a1128ffe04a7; societyguester=302f3cb26710699907148a1128ffe04a7; id=941954027; xnsid=f4f89f0f; wp_fold=0"
    ```


#### js分析的流程
- 确定js的位置
  - 从event listener中寻找

  - search all file中寻找关键字

    ![searchallfile搜索关键字](/media/libo/work/uTorrent接收文件/07 爬虫/searchallfile搜索关键字.png)

- 添加断点的方式，观察执行过程![添加断点](/media/libo/work/uTorrent接收文件/07 爬虫/添加断点.png)

- 执行js

#### requests模块获取cookie

requests.utils.dict_from_cookiejar: 把cookiejar 对象转化成字典

```Python
import requests

url = "http://www.baidu.com"
response = requests.get(url)
print(type(response.cookies))

cookies = requests.utils.dict_from_cookiejar(response.cookies)
print(cookies)


# 输出为
<class 'requests.cookies.RequestsCookieJar'>
{'BDORZ': '27315'}
```

#### requests中超时参数的使用

- requests.get(url,timeout=3)  timeout 参数,能够保证在三秒内返回响应,否则报错,这个方法还能够拿来检测代理ip的质量，如果一个代理ip在很长时间没有响应，那么添加超时之后也会报错，对应的这个ip就可以从代理ip池中删除.
#### retrying模块的使用

在浏览网页的时候,速度很慢,在代码中刷新请求

- retrying模块的地址：<https://pypi.org/project/retrying/>
- retrying 模块的使用
  - 使用retrying模块提供的retry模块
  - 通过装饰器的方式使用，让被装饰的函数反复执行
  - retry中可以传入参数**`stop_max_attempt_number`,**让函数报错后继续重新执行，达到最大执行次数的上限，如果每次都报错，整个函数报错，如果中间有一个成功，程序继续往后执行

```python
# coding=utf-8
import requests
from retrying import retry

headers = {}


@retry(stop_max_attempt_number=3)  # 最大重试3次，3次全部报错，才会报错
def _parse_url(url)    # _xxx 外部不能调用
    response = requests.get(url, headers=headers, timeout=3)  # 超时的时候回报错并重试
    assert response.status_code == 200  # 状态码不是200，也会报错并充实
    return response


def parse_url(url)
    try:  # 进行异常捕获
        response = _parse_url(url)
    except Exception as e:
        print(e)
        response = None
    return response

```

### 数据提取

#### 概念

数据提取就是从响应中获取我们想要的数据的过程

#### 爬虫中数据的分类

- 结构化数据: **json,xm**l
  - 使用模块转化为python类型
- 非结构化数据: **html**
  - re,xpaht

#### json是什么，json模块如何使用
***具有`read`() 和`write`()方法的对象就是类文件对象***

```Python
# coding=utf-8
import json
# json.dumps 实现python类型转化为json字符串
# indent实现换行和空格
# ensure_ascii=False实现让中文写入的时候保持为中文
json_str = json.dumps(my_dict, indent=2, ensure_ascii=False)

# json.loads 实现json字符串转化为python类型
my_dict = json.loads(json_str)

# json.dump 实现把python类型写入类文件对象
with open("temp.txt", "w") as f:
    json.dump(my_dict, f, ensure_ascii=False, indent=2)

# json.load 实现类文件对象中的json字符串转化为python类型
with open("temp.txt", "r") as f:
    my_dict = json.load(f)

```



![img](file:///media/libo/work/uTorrent%E6%8E%A5%E6%94%B6%E6%96%87%E4%BB%B6/07%20%E7%88%AC%E8%99%AB/%E8%AE%B2%E4%B9%89(%E6%9B%B4%E6%96%B0%E4%B9%8B%E5%90%8E%E7%9A%84)/_book/%E7%88%AC%E8%99%AB%E5%85%A5%E9%97%A8/images/json%E7%9A%84%E6%96%B9%E6%B3%95.png)
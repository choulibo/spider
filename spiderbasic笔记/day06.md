### 1.常见反爬手段

思路:尽可能去模拟浏览器,浏览器如何操作,代码就如何实现.浏览器先请求了地址url1，保留了cookie在本地，之后请求地址url2，带上了之前的cookie，代码中也可以这样去实现。

1. 通过headers中的User-Agent字段来反爬,通过User-Agent字段反爬的话

   只需要给他在请求之前添加User-Agent即可，更好的方式是使用User-Agent池来解决,我们可以考虑收集一堆User-Agent的方式，或者是随机生成User-Agent

   ```python
   import random
   
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
   ```

2. 通过referer字段或者是其他字段来反爬

3. 通过js来反爬

   1. ###### 通过js实现跳转来反爬

   2. ###### 通过js生成了请求参

   3. 通过js实现了数据的加密

4. ###### 通过验证码来反爬

5. 通过ip地址来反爬

6. 其他的反爬方式

   1. 通过自定义字体来反爬
   2. 通过css来反爬(计算css的偏移)

### 2.selenium的使用

#### PhantomJS

PhantomJS无界面的浏览器 因为服务器是没有界面的 所以只能使用PhantomJS

#### ChromeDriver

一Chromedriver 也是一个能够被selenium驱动的浏览器

#### selenium 入门使用

   ```python
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("url")
driver.quit()
   ```

##### 基础属性和方法

```python
driver.page_source()  # 获取网页源码
driver.save_screenshot('path')  # 截屏,验证码时有用
driver.get_cookies()  # 获取所有的cookies
driver.maximize_window()  # 最大化
driver.set_window_size() # 设置浏览器的宽高
driver.current_url  # 当前的url
```

##### 定位元素

```python
driver.find_element_by_id()    # (返回一个元素)
driver.find_elements_by_xpath()   #（返回一个包含元素的列表）
driver.find_elements_by_link_text()   #（根据连接文本获取元素列表）
driver.find_elements_by_partial_link_text()  #（根据连接包含的文本获取元素列表）
driver.find_elements_by_tag_name()   # (根据标签名获取元素列表)
driver.find_elements_by_class_name()  #（根据类名获取元素列表）
```

##### 获取文本和属性

```python
element.text   # 获取文本
element.get_attribute("href")   # 获取属性值
```
##### 数据提取优化

使用driver.page_source获取网页当前源代码 然后使用lxml模块的etree去提取数据

##### 获取cookie

使用selenium登录 登录完成后使用driver.get_cookies()获取cookie 
然后使用requests模块进行之后的数据爬取

```python
# 把cookie转化为字典
{cookie[‘name’]: cookie[‘value’] for cookie in driver.get_cookies()}

#删除一条cookie
driver.delete_cookie("CookieName")
# 删除所有的cookie
driver.delete_all_cookies()
```

##### id属性获取可能失败

 因为只有find_element_by_id方法 没有find_elements方法

```python
ret6 = driver.find_elements_by_xpath("//*[@id='product_123456']")
if len(ret6) > 0:
	xxxx # 进一步处理
```

##### 页面等待

如果网站采用了动态html技术，那么页面上的部分元素出现时间便不能确定，这个时候就可以设置一个等待时间，强制要求在时间内出现，否则报错 next_url.click()是否不需要time.sleep(3)

```html
<script type="text/javascript">
	$(".next").click(function(){
		$.ajax({
			url: "xxx",
			success:function(resp){
				for (var i = 0; i < resp.data.length; i++) {
					$("#content_list").append(resp.data[i] // 添加到页面上
				}
			}
		});

		return false; 
		// click事件运行到这里就结束了,python代码就继续往下执行了,
		// 但是ajax回到还没有回来,数据还没有添加到页面上,导致获取失败
	});
</script>
```

##### 不同类型的验证码的处理

1. url地址不变，验证码不变
   - 请求验证码的地址，获取响应，进行识别
2. url地址不变，验证码变化
   - 请求验证码，发送登录请求，需要带上统一套cookie，才能够都能路成功，对应可以使用requests.Session()来实现
3. selenium处理验证码
   - 带上selenium的driver中的cookie来请求验证码
   - selenium截屏，获取验证

```python
#获取验证码的地址
img_url = driver.find_element_by_id("captcha_image").get_attribute("src")
cookies = {i["name"]:i["value"] for i in driver.get_cookies()}
response = requests.get(img_url, cookies=cookies)  #请求验证码的地址
ret = indetify(response.content)  #验证码识别
```

##### 使用selenium切换frame

frame是html中常用的一种技术，即一个页面中嵌套了另一个网页，selenium默认是访问不了frame中的内容的，对应的解决思路是 `driver.switch_to.frame()`

### 3.MongoDB

#### mongodb(非关系型数据库NoSQL)的优势

- 易扩展,共同的特点是去掉关系型数据库的关系型特性,数据之间并无关系,容易扩展
- 大数据量,高性能,非常高的读写能力,尤其在大数据量下
- 灵活的数据模型,NoSQL⽆需事先为要存储的数据建⽴字段， 随时可以存储⾃定义的数据格式。 ⽽在关系数据库⾥， 增删字段是⼀件⾮常麻烦的事情。 如果是⾮常⼤数据量的表， 增加字段简直就是⼀个噩梦

##### 安装

​    **sudo apt-get install -y mongodb**

- 启动	  sudo service mongod start 
- **mongo**

#### mongodb 中数据库和集合的命令

​	**数据库**

- 数据库不需要提前创建,插入数据的时候自动创建

- show dbs/databases # 查看所有的数据库

- db # 显示当前的数据库名

- use 数据库名  # 使用数据库

- 数据库名.dropDatabase()  # 删除数据库

  ​	**集合**

- 数据库不需要提前创建,插入数据的时候自动创建

- show collections  # 显示所有的集合

- db.集合名.drop()  #  删除集合                                                   

- db.集合名.find()  # 集合的使用

#### mongodb 中的常见的数据类型

- Object ID： ⽂档ID
- String： 字符串， 最常⽤， 必须是有效的UTF-8
- Boolean： 存储⼀个布尔值， true或false
- Integer： 整数可以是32位或64位， 这取决于服务器
- Double： 存储浮点值
- Arrays： 数组或列表， 多个值存储到⼀个键
- Object： ⽤于嵌⼊式的⽂档， 即⼀个值为⼀个⽂档
- Null： 存储Null值
- Timestamp： 时间戳， 表示从1970-1-1到现在的总秒数
- Date： 存储当前⽇期或时间的UNIX时间格式

##### 注意点

创建⽇期语句如下 ：参数的格式为YYYY-MM-DD new Date('2017-12-20')

- 每个⽂档都有⼀个属性， 为_id， 保证每个⽂档的唯⼀性,可以⾃⼰去设置_id插⼊⽂档，如果没有提供， 那么MongoDB为每个⽂档提供了⼀个独特的_id， 类型为objectID
- objectID是⼀个12字节的⼗六进制数,每个字节两位，一共是24 位的字符串： 前4个字节为当前时间戳 接下来3个字节的机器ID 接下来的2个字节中MongoDB的服务进程id 最后3个字节是简单的增量值

#### mongodb 的增删改查

- 增(insert)

  ```python
    db.stu.insert({_id:"20170101",name:'gj',gender:1})
  ```

  插入文档时,如果不指定_id参数,mongodb会为文档分配一个唯一 的ObjectId

- 保存(save)

  `db.集合名称.save(document)` 如果⽂档的_id已经存在则修改，不会报错, 如果⽂档的_id不存在则添加

- insert 和save的区别

  - `insert插入，_id重复会报错`
  - `save 保存，_id存在会更新，不存在会插入`

- 改(update)

  ```python
  db.集合名称.update(<query> ,<update>,{multi: <boolean>})
  ```

  - 参数query:查询条件
  - 参数update:更新操作符
  - 参数multi:可选， 默认是false，表示只更新找到的第⼀条记录， 值为true表示把满⾜条件的⽂档全部更新,**multi 只对$set有效**

  ```python
  db.col_name.update({条件},{name:1})   # 会把满足条件的数据的第一条更新为{name:1},其他的字段会删除
  db.col_name.update({条件},{$set:{name:1}})   # 把满足条件的第一条的name值更新成1
  db.col_name.update({条件},{$set:{name:1}},{multi:true})   # 只把name字段更新,全部记录更新
  db.stu.update({name:"zhangsan"}, {$inc:{age:-1}})  # 更新改变值
  ```

- 删(remove)

  ```python
  db.集合名称.remove(<query>,{justOne: <boolean>})
  ```

  - 参数query:必选，删除的⽂档的条件
  - 参数justOne:可选， 如果设为true或1， 则只删除⼀条， 默认false， 表示删除多条



- 查(find)

  ```python
  db.集合名.find()  # 集合的使用
  ```

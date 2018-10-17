## 发送带headers的请求

headers = {"User-Agent":"从浏览器中复制"}
requests.get(url,headers=headers)

## 发送带参数的请求

params = {"":""}
url_temp = "不完整的URL地址"
requests.get(url_temp,params=params)

## 列表推导式

```python
In [41]: [i for i in range(10)]
Out[41]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

In [42]: [i/2 for i in range(10)]
Out[42]: [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5]

In [43]: [i/2 for i in range(10) if i%2==0]
```

## 面向对象

- 对象
  - 生活中的客观事物
- 类
  - 对事物的抽象，在代码中实现class类型
- 实例
  - 使用之前对类的实例化之后的记过

## 发送post请求

data = {"从浏览器中formdata的位置寻找"}
requests.post(url,data=data)

## requests中如何使用代理，使用代理的目的，代理的分类

- proxies = {协议：协议+ip+端口}
- requests.get(url,proxies=proxies)
  目的：
  - 反反爬  (让服务器以为不是同一个客户端请求)
  - 隐藏真实ip(防止我们的真实地址被泄露防止被追究)

代理的分类

​	**正向代理**:对于浏览器知道服务器的真实地址,  例如**VPN**

​	**反向代理**: 浏览器不知道服务器的真实地址,  例如**nginx**

- **高匿名**：不知道在使用代理
- **混淆**:知道你在使用代理,会得到一个假的ip地址,伪装的更逼真
- **匿名**：知道在使用代理，但是不知道真实ip
- **透明**：对方知道真实的ip

oxies)

## session的使用

- session = requests.Session()
- session.post(url,data)    #cookie会存在session中
- session.get(url)  #会带上之前的cookie

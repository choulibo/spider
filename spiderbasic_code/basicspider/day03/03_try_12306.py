# coding=utf-8
import requests
url = "https://www.12306.cn/mormhweb/"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36",
}

resp = requests.get(url,headers = headers,verify = False)
print(resp.status_code)
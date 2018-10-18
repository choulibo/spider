# coding=utf-8
import json

import requests

url = "https://m.douban.com/rexxar/api/v2/subject_collection/movie_showing/items?start=0&count=18&loc_id=108288"

headers = {
    "Referer": "https://m.douban.com/movie/nowintheater?loc_id=108288",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"
}

response = requests.get(url, headers=headers)
# print(type(response))

json_str = response.content.decode()
ret1 = json.loads(json_str)  # python 类型
# print(type(ret1))

# json.dumps 实现python类型数据转换成json字符串
# with open('a.json','w',encoding='utf-8') as f:
#     f.write(json.dumps(ret1,ensure_ascii=False,indent=4))
#


# json.loads 实现json字符串转换成python类型
# json.load 实现json类文件对象转换成python类型

# with open('a.txt', 'r', encoding='utf-8') as f:
#     ret2 = json.load(f.read())
#     # print(ret2)
#     print(type(ret2))


with open('b.txt', 'w', encoding='utf-8') as f:
    json.dump(ret1,f, ensure_ascii=False, indent=2)

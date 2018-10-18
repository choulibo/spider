# coding=utf-8

import requests

url = 'http://www.renren.com/941954027/profile'

headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Mobile Safari/537.36",
    "Cookie": "anonymid=jghfvoma-b8wgqk; depovince=GW; _r01_=1; JSESSIONID=abc8mwsUgbA-Xh0-5sfmw; ick_login=7123f1e3-d552-4d9a-aa75-e814c81632ca; first_login_flag=1; ln_uact=13146128763; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; loginfrom=syshome; ch_id=10016; _de=7A7A02E9254501DA6278B9C75EAEEB7A; _ga=GA1.2.1446821673.1524880234; _gid=GA1.2.1139412765.1524880234; jebecookies=f6abe0fa-49cf-49d6-ae31-74f4ce2373d5|||||; p=a0ba88dabb32cd73523d10e0d4b9b47a7; t=302f3cb26710699907148a1128ffe04a7; societyguester=302f3cb26710699907148a1128ffe04a7; id=941954027; xnsid=f4f89f0f; wp_fold=0"
}
response = requests.get(url,headers = headers)

with open('renren.html','w',encoding='utf-8') as f:
    f.write(response.content.decode())
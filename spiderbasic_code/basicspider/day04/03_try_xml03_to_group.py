# -*- coding:utf-8 -*-
from lxml import etree

text = ''' <div> <ul> 
        <li class="item-1"><a href="link1.html">first item</a></li> 
        <li class="item-1"><a href="link2.html">second item</a></li> 
        <li class="item-inactive"><a href="link3.html">third item</a></li> 
        <li class="item-1"><a href="link4.html">fourth item</a></li> 
        <li class="item-0"><a href="link5.html">fifth item</a> 
        </ul> </div> '''

html = etree.HTML(text)

# print(type(html))  # 输出一个element对象
# print(html)  # 输出一个element对象
#
#
# html_str = etree.tostring(html).decode()  # 自动添加li标签
# print(html_str)

# # 获取href列表和title列表
#
# href_list = html.xpath('//li[@class="item-1"]/a/@href')
# title_list = html.xpath('//li[@class="item-1"]/a/text()')
#
# # print(href_list)
# # print(title_list)
# # 上述返回值是列表
#
# # 对上述列表进行遍历,组成字典
#
# for href in href_list:
#     item = {}
#
#     item['href'] = href
#     item['title'] = title_list[href_list.index(href)]
#     print(item)


# 对每一组中继续进行数据的提取
li_list = html.xpath("//li[@class = 'item-1']")

for li in li_list:
    item = {}
    item['href'] = li.xpath("./a/@href")[0] if len(li.xpath("./a/@href")) >0 else None
    item['title'] = li.xpath("./a/text()")[0] if len(li.xpath("./a/@text()")) >0 else None
    print(item)









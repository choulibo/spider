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

print(type(html))  # 输出一个element对象
print(html)  # 输出一个element对象


html_str = etree.tostring(html).decode()  # 自动添加li标签
print(html_str)
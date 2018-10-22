#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 18-10-21  @Author:libo  @FileName: 06_login_douban.py
import time

import requests
from selenium import webdriver

from yundama import indetify


driver = webdriver.Chrome()
driver.get('http://www.baidu.com')

# 输入用户名
driver.find_element_by_id('form_email').send_keys('18103849049')

# 输入密码
driver.find_element_by_id('form_password').send_keys('XXXXXXXXXXXX')
# 获取验证码的地址
img_url = driver.find_element_by_id('captcha_image').get_attribute('src')
response = requests.get(img_url)
ret = indetify(response.content) # 验证码识别

driver.find_element_by_id('captcha_field').send_keys(ret)

time.sleep(5)
driver.find_element_by_class_name('bn-submit').click()

time.sleep(8)
print(driver.get_cookies())
driver.quit()
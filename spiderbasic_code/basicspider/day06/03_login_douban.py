#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 18-10-21  @Author:libo  @FileName: 02_try_PhantomJS.py
import time

from selenium import webdriver

driver = webdriver.Chrome()  # 实例化driver

driver.get("https://www.douban.com/")

# 输入用户名
driver.find_element_by_id('form_email').send_keys('18103849049')

# 输入密码
driver.find_element_by_id('form_password').send_keys('XXXXXXXXXXX')
time.sleep(3)
# 点击登录
driver.find_element_by_class_name('bn-submit').click()

time.sleep(5)

driver.quit()

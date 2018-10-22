#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 18-10-22  @Author:libo  @FileName: 05_qq_mail.py

# selenium 的frame实现
import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://mail.qq.com/")
driver.switch_to.frame('login_frame')
driver.find_element_by_id('u').send_keys('1801085785@qq.com')
driver.find_element_by_id('p').send_keys('XXXXXXXXXXX')
driver.find_element_by_class_name('btn').click()
time.sleep(5)
driver.quit()

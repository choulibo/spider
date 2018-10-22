#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 18-10-21  @Author:libo  @FileName: 01_try_selenium.py
from selenium import webdriver

driver = webdriver.Chrome()  # 实例化driver
# driver.maximize_window()

driver.get('http://www.baidu.com')
# driver.save_screenshot('./baidu1.png')
driver.find_element_by_id('kw').send_keys('nba')
driver.find_element_by_id('su').click()
import time

time.sleep(3)
driver.quit()
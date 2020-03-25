#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @author:sisul
# @time:2020/3/23:14:21

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('http://djztec.f3322.net:81/manager/#/login')
time.sleep(1)
driver.find_element_by_class_name('el-input__inner').send_keys('aaaa')
time.sleep(1)
driver.quit()

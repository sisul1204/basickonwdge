# * coding:utf-8 *
# Author:sisul
#创建时间：2020/3/22 8:36

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('http://www.lemfix.com/')
time.sleep(1)
driver.close()
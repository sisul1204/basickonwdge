# * coding:utf-8 *
# Author:sisul
#创建时间：2020/3/22 17:50

from selenium import webdriver
import time
#1.创建webdriver对象

driver = webdriver.Chrome()

#2.发起请求
driver.get('http://www.baidu.com')

#3.定位元素
input_element = driver.find_element_by_xpath("//input[@id='kw']")
input_element.send_keys('柠檬班')

time.sleep(2)

#4.关闭会话
driver.close()
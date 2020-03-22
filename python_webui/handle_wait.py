# * coding:utf-8 *
# Author:sisul
#创建时间：2020/3/22 19:06


from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#1.创建webdriver对象

driver = webdriver.Chrome()

#2.发起请求
driver.get('http://www.baidu.com')

#3.定位元素
#方法一：最笨的方法，死等
# time.sleep(2)

#方法二，显示等待
wait = WebDriverWait(driver, 10)
input_element = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@id="kw"]')))


#方法三，隐式等待
driver.implicitly_wait(10)              #在使用find_element..定位元素时，会等待10s

# input_element = driver.find_element_by_xpath("//input[@id='kw']")
input_element.send_keys('柠檬班')



#4.关闭会话
driver.close()
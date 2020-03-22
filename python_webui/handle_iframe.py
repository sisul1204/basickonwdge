# * coding:utf-8 *
# Author:sisul
#创建时间：2020/3/22 21:15


#iframe标签下面的子页面，是无法定位的
#先切换到iframe中之后，才能定位

from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
#1.创建webdriver对象

driver = webdriver.Chrome()

#2.发起请求
driver.get('https://ke.qq.com')
driver.maximize_window()
time.sleep(2)
wait = WebDriverWait(driver, 5)


#3.定位元素
#点击登录
time.sleep(5)
wait.until(EC.presence_of_element_located((By.ID, 'js-login'))).click()

#点击QQ登录
wait.until(EC.presence_of_element_located((By.XPATH, '//a[contains(@class, "btns-enter-qq")]'))).click()

#切换到iframe中，然后再定位
#方法一：
#根据iframe标签name属性名来指定
driver.switch_to.frame('login_frame_qq')

#点击账号密码登录
wait.until(EC.presence_of_element_located((
    By.ID, 'switcher_plogin'))).click()

#4.关闭会话
driver.close()
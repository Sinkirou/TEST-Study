"""
浏览器操作方法: Part2
"""
# 1. 导入模块
from time import sleep

from selenium import webdriver

# 2. 实例化浏览器对象
driver = webdriver.Chrome()
# 3. 打开页面
driver.get('http://www.baidu.com')

# 定位搜索框输入内容
driver.find_element_by_id('kw').send_keys('黑马马')
# 点击搜索按钮
driver.find_element_by_id('su').click()
sleep(2)

# 后退: 浏览器对象.back()
driver.back()
sleep(2)

# 前进: 浏览器对象.forward()
driver.forward()
sleep(2)

# 刷新[重点]: refresh()
# 说明: 刷新动作是重新向服务器发起当前页面的请求!
driver.refresh()

# 4. 展示效果
sleep(3)
# 5. 退出浏览器
driver.quit()

"""
CSS 策略: 前四种
"""
# 1. 导入模块
from time import sleep

from selenium import webdriver

# 2. 实例化浏览器对象
driver = webdriver.Chrome()
# 3. 打开页面
driver.get('file:///Users/comesoon/Desktop/page/%E6%B3%A8%E5%86%8CA.html')

# 需求：打开注册A.html页面，完成以下操作
# 1).使用CSS定位方式中id选择器定位用户名输入框，并输入：admin
# 语法: #id属性值
driver.find_element_by_css_selector('#userA').send_keys('admin')

# 2).使用CSS定位方式中属性选择器定位密码输入框，并输入：123456
# 语法 1: [属性名="属性值"]
# 语法 2: 标签名[属性名="属性值"]
# driver.find_element_by_css_selector('input[placeholder="请输入密码"]').send_keys('123456')
driver.find_element_by_css_selector('[placeholder="请输入密码"]').send_keys('123456')

# 3).使用CSS定位方式中class选择器定位电话号码输入框，并输入：18600000000
# 语法: .class属性值
driver.find_element_by_css_selector('.telA').send_keys('18600000000')
sleep(2)

# 4).使用CSS定位方式中元素选择器定位注册按钮，并点击
# 说明: 元素选择器又名标签选择器
# 语法: 标签名
driver.find_element_by_css_selector('button').click()

# 4. 展示效果
sleep(3)
# 5. 退出浏览器
driver.quit()

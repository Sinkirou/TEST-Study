"""
账号不存在测试用例
"""
from time import sleep
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://127.0.0.1/')
driver.maximize_window()  # 窗口最大化
driver.implicitly_wait(10)  # 隐式等待

# 1. 点击首页的‘登录’链接，进入登录页面
driver.find_element_by_link_text('登录').click()

# 2. 输入一个不存在的用户名
driver.find_element_by_id('username').send_keys('13811110001')
# 3. 输入密码
driver.find_element_by_id('password').send_keys('123456')
# 4. 输入验证码
driver.find_element_by_id('verify_code').send_keys('8888')
# 5. 点击登录按钮
driver.find_element_by_name('sbtbutton').click()

# 6. 获取错误提示信息
# 获取元素文本值: 元素对象.text
msg = driver.find_element_by_class_name('layui-layer-content').text
print('错误信息为:', msg)

sleep(3)
driver.quit()

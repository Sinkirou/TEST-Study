"""
多窗口操作
"""
# 1. 导入模块
from time import sleep

from selenium import webdriver

# 2. 实例化浏览器对象
driver = webdriver.Chrome()
# 3. 打开页面
driver.get('file:///Users/comesoon/Desktop/page/%E6%B3%A8%E5%86%8C%E5%AE%9E%E4%BE%8B.html')

# 需求：打开‘注册实例.html’页面，完成以下操作
# 1). 点击‘注册A页面’链接
driver.find_element_by_id('ZCA').click()

# 查看当前窗口的句柄值
# 说明: 在浏览器的一个生命周期内(开启到关闭),
# 任意一个窗口都有唯一的一个句柄值, 可以通过句柄值完成窗口切换操作
print('当前句柄值为:', driver.current_window_handle)

# 切换窗口操作
# 1> 获取所含有窗口句柄(包含新窗口)
handles = driver.window_handles
# print(handles)
# print(type(handles))

# 2> 切换窗口: 列表的 -1 索引对应的值, 始终是最新窗口的句柄值
driver.switch_to.window(handles[-1])

# 2). 在打开的页面中，填写注册信息
driver.find_element_by_id('userA').send_keys('admin')
driver.find_element_by_id('passwordA').send_keys('123456')

# 4. 展示效果
sleep(3)
# 5. 退出浏览器
driver.quit()

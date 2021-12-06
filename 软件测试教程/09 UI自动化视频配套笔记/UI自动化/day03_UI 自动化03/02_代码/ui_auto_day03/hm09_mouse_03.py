"""
鼠标操作: 拖拽操作
"""
# 1. 导入模块
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains

# 2. 实例化浏览器对象
driver = webdriver.Chrome()
# 3. 打开页面
driver.get('file:///Users/comesoon/Desktop/page/drag.html')

# 需求：打开‘drag.html’页面，把红色方框拖拽到蓝色方框上
red = driver.find_element_by_id('div1')
blue = driver.find_element_by_id('div2')

# 1> 实例化鼠标对象(关联浏览器对象)
action = ActionChains(driver)
# 2> 调用方法(传入目标元素)
action.drag_and_drop(red, blue)
# 3> 执行方法
action.perform()

# 4. 展示效果
sleep(3)
# 5. 退出浏览器
driver.quit()

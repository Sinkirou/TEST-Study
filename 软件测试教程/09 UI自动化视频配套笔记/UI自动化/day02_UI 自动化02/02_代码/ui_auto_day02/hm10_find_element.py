# 1. 导入模块
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

# 2. 实例化浏览器对象
driver = webdriver.Chrome()
# 3. 打开页面
driver.get('file:///Users/comesoon/Desktop/page/%E6%B3%A8%E5%86%8CA.html')

# 说明: 在 Selenium 框架中, 元素定位方法的另一种写法
driver.find_element(By.ID, 'userA').send_keys('admin')
# 注意: By 和 by 方法可以同时使用!
driver.find_element_by_id('passwordA').send_keys('123456')

# 注释: 说法 1: by 方法是 By 方法的封装; 说法 2: By 方法是 by 方法的底层实现(原理)
# 查看原始代码方法: 按住 Ctrl 使用鼠标左键点击 by 方法即可

# 应用场景: 使用 PO 设计模式封装代码结构时需要使用 By 方法

# 4. 展示效果
sleep(3)
# 5. 退出浏览器
driver.quit()

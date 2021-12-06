"""
元素等待: 隐式等待
"""
# 1. 导入模块
from time import sleep

from selenium import webdriver

# 2. 实例化浏览器对象
driver = webdriver.Chrome()
# 3. 打开页面
driver.get('file:///Users/comesoon/Desktop/page/%E6%B3%A8%E5%86%8CA%E7%AD%89%E5%BE%85.html')

# 设置隐式等待
driver.implicitly_wait(10)

# 定位元素并输入
driver.find_element_by_id('userA').send_keys('admin')

# 注意:
# 1. 隐式等待是全局有效, 只需要设置一次即可
# 2. 当隐式等待被激活时, 虽然目标元素已经出现了,
# 但是还是会由于当前页面内的其他元素的未加载完成, 而继续等待, 进而增加代码的执行时长

# 4. 展示效果
sleep(3)
# 5. 退出浏览器
driver.quit()

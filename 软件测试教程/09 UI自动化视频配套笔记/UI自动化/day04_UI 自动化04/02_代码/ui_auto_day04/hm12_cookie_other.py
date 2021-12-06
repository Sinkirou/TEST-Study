"""
cookie: 其他方法
"""
# 1. 导入模块
from time import sleep

from selenium import webdriver

# 2. 实例化浏览器对象
driver = webdriver.Chrome()
# 3. 打开页面
driver.get('http://www.baidu.com')
driver.maximize_window()  # 窗口最大化

# 获取所有 cookie 信息
print(driver.get_cookies())

# 获取特定 cookie 信息: 需要传入 cookie 名
print(driver.get_cookie('BDUSS'))

# 4. 展示效果
sleep(3)
# 5. 退出浏览器
driver.quit()

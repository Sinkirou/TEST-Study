"""
元素等待: 显式等待
"""
# 1. 导入模块
from time import sleep

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

# 2. 实例化浏览器对象
driver = webdriver.Chrome()
# 3. 打开页面
driver.get('file:///Users/comesoon/Desktop/page/%E6%B3%A8%E5%86%8CA%E7%AD%89%E5%BE%85.html')

# 需求：打开注册A页面，完成以下操作
# 1).使用显式等待定位用户名输入框，如果元素存在，就输入admin
# driver.find_element_by_id('userA').send_keys('admin')

# 设置显式等待: 按住 Ctrl, 鼠标左键点击类名, 拷贝示例代码, 根据实际需求修改对应参数即可
"""
driver: 浏览器对象
timeout: 超时时长
poll_frequency: 定位方法执行间隔时长(默认 0.5 秒)
"""
element = WebDriverWait(driver, 10, 1).until(lambda x: x.find_element_by_id('userA'))
# 说明: 元素操作方法没有代码提示, 需要手写
element.send_keys('admin')

# 4. 展示效果
sleep(3)
# 5. 退出浏览器
driver.quit()

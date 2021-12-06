"""
鼠标操作: 左键双击
"""
# 1. 导入模块
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains

# 2. 实例化浏览器对象
driver = webdriver.Chrome()
# 3. 打开页面
driver.get('file:///Users/comesoon/Desktop/page/%E6%B3%A8%E5%86%8CA.html')

# 需求：打开注册页面A，输入用户名admin，暂停3秒钟后，双击鼠标左键，选中admin
username = driver.find_element_by_id('userA')
username.send_keys('admin')
sleep(3)

# 说明: 使用键盘快捷键 Ctrl + A, 也能实现全选
# 1> 实例化鼠标对象(关联浏览器对象)
action = ActionChains(driver)
# 2> 调用鼠标动作(传入目标元素)
action.double_click(username)
# 3> 执行方法
action.perform()

# 4. 展示效果
sleep(3)
# 5. 退出浏览器
driver.quit()

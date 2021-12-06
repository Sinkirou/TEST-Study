"""
鼠标操作: 鼠标右键
"""
# 1. 导入模块
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains

# 2. 实例化浏览器对象
driver = webdriver.Chrome()
# 3. 打开页面
driver.get('file:///Users/comesoon/Desktop/page/%E6%B3%A8%E5%86%8CA.html')

# 需求：打开注册页面A，在用户名文本框上点击鼠标右键
# 0> 定位目标元素
username = driver.find_element_by_id('userA')
# 1> 实例化鼠标对象(关联浏览器对象)
action = ActionChains(driver)
# 2> 调用鼠标方法
# 说明: 鼠标右键只能展示右键菜单内容, 而菜单中的元素无法操作!
action.context_click(username)
# 3> 执行方法: 该方法必须调用, 否则上述代码无效!!!!!!
action.perform()

# 4. 展示效果
sleep(3)
# 5. 退出浏览器
driver.quit()

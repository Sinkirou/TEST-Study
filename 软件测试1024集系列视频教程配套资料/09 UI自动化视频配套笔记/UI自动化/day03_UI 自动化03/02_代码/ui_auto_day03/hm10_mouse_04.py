"""
鼠标操作: 悬停操作
"""
# 1. 导入模块
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains

# 2. 实例化浏览器对象
driver = webdriver.Chrome()
# 3. 打开页面
driver.get('file:///Users/comesoon/Desktop/page/%E6%B3%A8%E5%86%8CA.html')

# 定位目标元素
btn = driver.find_element_by_tag_name('button')

# 实例化鼠标对象
action = ActionChains(driver)
# 调用鼠标方法
# 说明: 该方法在实际应用中, 处理悬停鼠标才会出现的菜单时使用
# 注意: 该方法执行时, 不要动鼠标!!!!!!
action.move_to_element(btn)
# 执行方法
action.perform()

# 另一种鼠标操作的写法:(在其他编程语言中称为链式编程)
# ActionChains(driver).move_to_element(btn).perform()

# 4. 展示效果
sleep(3)
# 5. 退出浏览器
driver.quit()

# 1. 导入模块
from time import sleep

from selenium import webdriver

# 2. 实例化浏览器对象
driver = webdriver.Chrome()
# 3. 打开页面
driver.get('file:///Users/comesoon/Desktop/page/%E6%B3%A8%E5%86%8CA.html')

# 没有 s 和带有 s 的定位方法的相互依据
# 说明 1: 如果调用完元素定位方法后, 再点语法, 提示的均为列表方法, 则方法带 s
driver.find_elements_by_name('AAA').send_keys('admin')  # 错误样例
#  说明 2: 如果调用完元素定位方法后, 再点语法, 提示的均为元素方法, 则方法不带 s
driver.find_element_by_name('AAA')[1]  # 错误样例

# 4. 展示效果
sleep(3)
# 5. 退出浏览器
driver.quit()

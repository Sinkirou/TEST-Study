"""
XPath 策略:层级与属性结合
"""
# 1. 导入模块
from time import sleep

from selenium import webdriver

# 2. 实例化浏览器对象
driver = webdriver.Chrome()
# 3. 打开页面
driver.get('file:///Users/comesoon/Desktop/page/%E6%B3%A8%E5%86%8CA.html')

# 层级与属性结合: 目标元素无法直接定位, 可以考虑先定位其父层级或祖辈层级, 再获取目标元素
# 语法: 父层级定位策略/目标元素定位策略

# 需求：打开注册A.html页面，完成以下操作
# 1).使用层级与属性结合定位策略，在test1对应的输入框里输入：admin
driver.find_element_by_xpath('//*[@id="p1"]/input').send_keys('admin')

# 4. 展示效果
sleep(3)
# 5. 退出浏览器
driver.quit()

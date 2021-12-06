"""
XPath:利用元素属性策略
"""
# 1. 导入模块
from time import sleep

from selenium import webdriver

# 2. 实例化浏览器对象
driver = webdriver.Chrome()
# 3. 打开页面
driver.get('file:///Users/comesoon/Desktop/page/%E6%B3%A8%E5%86%8CA.html')

# 利用元素属性策略: 该方法可以使用目标元素的任意一个属性和属性值(需要保证唯一性)
# 语法1: //标签名[@属性名='属性值']
# 语法2: //*[@属性名='属性值']

# 需求：打开注册A.html页面，完成以下操作
# 1).利用元素的属性信息精确定位用户名输入框，并输入：admin
# 注意: 使用 XPath 策略, 需要在浏览器工具中根据策略语法, 组装策略值, 验证后再放入代码中使用
# driver.find_element_by_xpath('//input[@placeholder="请输入用户名"]').send_keys('admin')
driver.find_element_by_xpath('//*[@placeholder="请输入用户名"]').send_keys('admin')

# 4. 展示效果
sleep(3)
# 5. 退出浏览器
driver.quit()

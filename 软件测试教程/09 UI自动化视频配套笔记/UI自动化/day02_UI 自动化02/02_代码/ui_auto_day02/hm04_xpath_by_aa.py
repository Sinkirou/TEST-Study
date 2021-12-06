"""
XPath: 属性和逻辑结合
"""
# 1. 导入模块
from time import sleep

from selenium import webdriver

# 2. 实例化浏览器对象
driver = webdriver.Chrome()
# 3. 打开页面
driver.get('file:///Users/comesoon/Desktop/page/%E6%B3%A8%E5%86%8CA.html')

# 属性和逻辑集合: 解决目标元素单个属性和属性值无法定位为一个元素的问题时使用
# 语法: //*[@属性1="属性值1" and @属性2="属性值2"]
# 注意: 多个属性值由 and 连接, 每一个属性都要由@开头, 可以根据需求使用更多属性值

# 需求：打开注册A.html页面，完成以下操作
# 1).使用属性与逻辑结合定位策略，在test1对应的输入框里输入：admin
driver.find_element_by_xpath('//*[@name="user" and @class="login"]').send_keys('admin')

# 4. 展示效果
sleep(3)
# 5. 退出浏览器
driver.quit()

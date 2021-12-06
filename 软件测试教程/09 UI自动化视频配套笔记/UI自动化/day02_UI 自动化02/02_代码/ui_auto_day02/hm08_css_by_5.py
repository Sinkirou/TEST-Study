"""
CSS 策略:层级选择器
"""
# 1. 导入模块
from time import sleep

from selenium import webdriver

# 2. 实例化浏览器对象
driver = webdriver.Chrome()
# 3. 打开页面
driver.get('file:///Users/comesoon/Desktop/page/%E6%B3%A8%E5%86%8CA.html')

# 需求：打开注册A.html页面，完成以下操作
# 1).使用CSS定位方式中的层级选择器定位用户名输入框，并输入：admin

# 层级选择器
# 父子层级关系: 父层级策略>子层级策略
driver.find_element_by_css_selector('#pa>input').send_keys('admin')
# 祖辈后代层级关系: 祖辈策略 后代策略
driver.find_element_by_css_selector('form [placeholder="请输入用户名"]').send_keys('admin')

# 注意: 父子层级关系中也可以使用空格连接上下层级策略

# 扩展: XPath 祖辈和后代关系: 只需要使用//连接祖辈和后代元素即可
driver.find_element_by_xpath('//form//*[@id="userA"]').send_keys('admin')

# 4. 展示效果
sleep(3)
# 5. 退出浏览器
driver.quit()

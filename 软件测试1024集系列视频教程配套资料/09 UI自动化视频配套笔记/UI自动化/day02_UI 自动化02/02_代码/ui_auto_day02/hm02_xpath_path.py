"""
XPath:路径策略
"""
# 1. 导入模块
from time import sleep

from selenium import webdriver

# 2. 实例化浏览器对象
driver = webdriver.Chrome()
# 3. 打开页面
driver.get('file:///Users/comesoon/Desktop/page/%E6%B3%A8%E5%86%8CA.html')

# 需求：打开注册A.html页面，完成以下操作
# 1).使用绝对路径定位用户名输入框，并输入：admin
driver.find_element_by_xpath('/html/body/div/fieldset/form/p[1]/input').send_keys('admin')
# 2).暂停2秒
sleep(2)
# 3).使用相对路径定位密码输入框，并输入：123
# 注意: 使用相对路径时, 需要注意方法参数的内外引号嵌套问题
driver.find_element_by_xpath('//*[@id="passwordA"]').send_keys('123')

# 4. 展示效果
sleep(3)
# 5. 退出浏览器
driver.quit()

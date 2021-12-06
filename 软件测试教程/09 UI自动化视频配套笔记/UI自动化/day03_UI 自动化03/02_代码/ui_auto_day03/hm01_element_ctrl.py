"""
元素操作方法
"""
# 1. 导入模块
from time import sleep

from selenium import webdriver

# 2. 实例化浏览器对象
driver = webdriver.Chrome()
# 3. 打开页面
driver.get('file:///Users/comesoon/Desktop/page/%E6%B3%A8%E5%86%8CA.html')

# 需求：打开注册A页面，完成以下操作
# 1).通过脚本执行输入用户名：admin；密码：123456；电话号码：18611111111；电子邮件：123@qq.com
driver.find_element_by_id('userA').send_keys('admin')
driver.find_element_by_id('passwordA').send_keys('123456')
# tel = driver.find_element_by_id('telA').send_keys('18611111111') # 错误样例, 不能接收元素操作结果
tel = driver.find_element_by_id('telA')
tel.send_keys('18611111111')
driver.find_element_by_name('emailA').send_keys('123@qq.com')

# 2).间隔3秒，修改电话号码为：18600000000
# 注意: 在使用操作中, 一般对于输入框元素, 都要先执行清空, 再执行输入, 避免操作错误
# 清空操作: 元素对象.clear()
sleep(3)
tel.clear()
tel.send_keys('18600000000')

# 3).间隔3秒，点击‘注册’按钮
sleep(3)
driver.find_element_by_css_selector('button').click()

# 4).间隔3秒，关闭浏览器
# 5).元素定位方法不限

# 4. 展示效果
sleep(3)
# 5. 退出浏览器
driver.quit()

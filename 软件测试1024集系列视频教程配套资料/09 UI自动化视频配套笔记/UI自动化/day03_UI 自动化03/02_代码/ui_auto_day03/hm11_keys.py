"""
键盘操作
"""
# 1. 导入模块
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 2. 实例化浏览器对象
driver = webdriver.Chrome()
# 3. 打开页面
driver.get('file:///Users/comesoon/Desktop/page/%E6%B3%A8%E5%86%8CA.html')

# 需求：打开注册A页面，完成以下操作
# 1). 输入用户名：admin1，暂停2秒，删除1
username = driver.find_element_by_id('userA')
username.send_keys('admin1')
sleep(2)
# 删除: BACK_SPACE 等价于 BACKSPACE
username.send_keys(Keys.BACK_SPACE)

# 2). 全选用户名：admin，暂停2秒
# 说明: macOS 系统需要使用 Command + a
username.send_keys(Keys.CONTROL, 'a')  # Windows 系统
# username.send_keys(Keys.COMMAND, 'a')  # macOS 系统
sleep(2)

# 3). 复制用户名：admin，暂停2秒
username.send_keys(Keys.CONTROL, 'c')  # Windows 系统
# username.send_keys(Keys.COMMAND, 'c')  # macOS 系统
sleep(2)

# 4). 粘贴到密码框
# 说明: 之所以能够复制完内容后, 在任意位置处可以进行粘贴, 是通过系统的剪切板实现的
password = driver.find_element_by_id('passwordA')
password.send_keys(Keys.CONTROL, 'v')  # Windows 系统
# password.send_keys(Keys.COMMAND, 'v')  # macOS 系统

# 4. 展示效果
sleep(3)
# 5. 退出浏览器
driver.quit()

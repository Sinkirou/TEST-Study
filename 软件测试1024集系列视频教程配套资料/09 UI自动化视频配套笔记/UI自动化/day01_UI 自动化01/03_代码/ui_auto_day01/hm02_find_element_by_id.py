# 1. 导入模块
from time import sleep

from selenium import webdriver

# 2. 实例化浏览器对象
driver = webdriver.Chrome()

# 3. 打开网页
driver.get('file:///Users/comesoon/Desktop/page/%E6%B3%A8%E5%86%8CA.html')

# 实现需求
# 需求：打开注册A.html页面，完成以下操作
# id 方法: 通过目标元素的 id 属性值定位, 由于 id 值一般是唯一的,
# 因此当元素存在 id 属性值时, 优先使用 id 方法定位元素
# 1).使用id定位，输入用户名：admin
username = driver.find_element_by_id('userA')
# 输入方法: 元素对象.send_keys('内容')
username.send_keys('admin')

# 2).使用id定位，输入密码：123456
password = driver.find_element_by_id('passwordA')
password.send_keys('123456')

# 3).3秒后关闭浏览器窗口

# 4. 展示效果
sleep(3)

# 5. 关闭页面
driver.quit()

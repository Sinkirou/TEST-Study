"""
Web 自动化基本代码
"""
# 1. 导入模块
from time import sleep

from selenium import webdriver

# 2. 实例化浏览器对象: 类名()
driver = webdriver.Chrome()  # 谷歌浏览器

# 3. 打开网页: 必须包含协议头
driver.get('file:///Users/comesoon/Desktop/page/%E6%B3%A8%E5%86%8CA.html')

# 实现需求
# 需求：打开注册A.html页面，完成以下操作
# name 方法：由于元素的 name 属性值可能存在重复, 必须确定其能够代表目标元素唯一性之后, 方可使用
# 注意: 当页面内有多个元素的特征值是相同的时候, 定位元素的方法执行时,
# 默认只会获取第一个符合要求的特征对应的元素
# 因此, 定位元素时需要尽量保证使用的特征值能够代表目标元素在当前页面内的唯一性!

# 1).使用name定位用户名，输入：admin
username = driver.find_element_by_name('AAA')
username.send_keys('admin')

# 2).使用name定位密码，输入：123456
password = driver.find_element_by_name('AAA')
password.send_keys('123456')

# 3).3秒后关闭浏览器窗口

# 4. 观察效果
sleep(3)

# 5. 关闭页面
driver.quit()

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
# tag_name 方法: 由于页面内可能存在大量重复的标签名, 因此必须确定其能够代表目标元素唯一性之后, 方可使用
# 注意: 由于标签名的重复性过高, 一般做精确定位时, 都不会选择 tag_name 方法
# 1).使用tag_name定位用户名输入框，并输入：admin
# username = driver.find_element_by_tag_name('input')
# username.send_keys('admin')
# 说明: 如果目标元素对象在后续的代码中只使用一次, 也可以直接在定位元素结束后, 直接调用输入方法实现操作
driver.find_element_by_tag_name('input').send_keys('admin')
# 以下为错误样例: 不能使用对象变量接收元素操作方法的结果!!!!!!
element = driver.find_element_by_tag_name('input').send_keys('admin')
print(element)

# 2).3秒后关闭浏览器窗口

# 4. 观察效果
sleep(3)

# 5. 关闭页面
driver.quit()

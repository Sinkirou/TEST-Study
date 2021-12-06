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
# class_name 方法: 由于元素的 class 属性值可能存在重复, 必须确定其能够代表目标元素唯一性之后, 方可使用
# 注意
# 1. 方法名是 class_name, 但要找元素的 class 属性值
# 2. 如果元素的 class 属性值存在多个值, 在 class_name 方法使用时, 只能使用其中的任意一个
# 1).通过class_name定位电话号码A，并输入：18611111111
tel = driver.find_element_by_class_name('telA')
tel.send_keys('18611111111')

# 2).通过class_name定位电子邮箱A，并输入：123@qq.com
# mail = driver.find_element_by_class_name('emailA dzyxA')  # 错误样例
# mail = driver.find_element_by_class_name('emailA')  # 正确样例
mail = driver.find_element_by_class_name('dzyxA')  # 正确样例
mail.send_keys('123@qq.com')

# 3).3秒后关闭浏览器窗口

# 4. 观察效果
sleep(3)

# 5. 关闭页面
driver.quit()

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
# 1).使用link_text定位(访问 新浪 网站)超链接，并点击
# link_text 方法: 该方法只针对超链接元素(a 标签), 并且需要输入超链接的全部文本信息
# 点击方法: 元素对象.click()
# driver.find_element_by_link_text('访问 新浪 网站').click()

# partial_link_text 方法: 该方法只针对超链接元素(a 标签), 并且只需要输入超链接的部分文本信息
# driver.find_element_by_partial_link_text('访问').click()
# 注意: 虽然是只传入部分文本信息, 但是需要确定其唯一性, 方可以使用
driver.find_element_by_partial_link_text('新浪').click()

# 2).3秒后关闭浏览器窗口

# 4. 观察效果
sleep(3)

# 5. 关闭页面
driver.quit()

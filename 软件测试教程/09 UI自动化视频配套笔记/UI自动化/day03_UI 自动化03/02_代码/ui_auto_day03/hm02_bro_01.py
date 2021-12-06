"""
浏览器操作方法 Pat1:
"""
# 1. 导入模块
from time import sleep

from selenium import webdriver

# 2. 实例化浏览器对象
driver = webdriver.Chrome()
# 3. 打开页面
driver.get('file:///Users/comesoon/Desktop/page/%E6%B3%A8%E5%86%8CA.html')

# 1. maximize_window() [重点]最大化浏览器窗口 --> 模拟浏览器最大化按钮
# 说明: 如果能够在打开页面时, 全屏显示页面, 就能尽最大可能加载更多的页面元素, 提高可定位性
driver.maximize_window()

# 2. set_window_size(width, height) [了解]设置浏览器窗口大小 --> 设置浏览器宽、高(像素点)
# 场景: 查看页面是否可以自适应(Web 和 APP 端切换)时使用
driver.set_window_size(300, 300)

# 3. set_window_position(x, y) [了解]设置浏览器窗口位置 --> 设置浏览器位置
driver.set_window_position(300, 300)

# 4. 展示效果
sleep(3)
# 5. 退出浏览器
driver.quit()

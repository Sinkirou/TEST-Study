"""
浏览器操作方法: Part3
"""
# 1. 导入模块
from time import sleep

from selenium import webdriver

# 2. 实例化浏览器对象
driver = webdriver.Chrome()
# 3. 打开页面
driver.get('file:///Users/comesoon/Desktop/page/%E6%B3%A8%E5%86%8CA.html')

# 点击新开新浪网页
driver.find_element_by_partial_link_text('访问').click()
sleep(2)

# 7. close() 关闭当前窗口 --> 模拟点击浏览器关闭按钮
# 8. quit() 关闭浏览器驱动对象 --> 关闭所有程序启动的窗口
# 9. title 获取页面title
# 10. current_url 获取当前页面URL

# 场景: 浏览器的标题和 URL 地址属性, 可以用来做断言使用
print('关闭前页面标题:', driver.title)
print('关闭前页面地址:', driver.current_url)

# 说明: 在没有实现浏览器页面切换操作前, close() 方法关闭的是原始页面!
# 场景: 关闭单个页面时使用
driver.close()

# 4. 展示效果
sleep(3)
# 5. 退出浏览器
# 说明: 关闭所有页面
driver.quit()

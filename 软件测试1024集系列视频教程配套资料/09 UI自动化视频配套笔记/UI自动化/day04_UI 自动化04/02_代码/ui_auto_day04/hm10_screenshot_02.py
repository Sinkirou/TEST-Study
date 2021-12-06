"""
截图操作
"""
# 1. 导入模块
from time import sleep, strftime

from selenium import webdriver

# 2. 实例化浏览器对象
driver = webdriver.Chrome()
# 3. 打开页面
driver.get('file:///Users/comesoon/Desktop/page/%E6%B3%A8%E5%86%8CA.html')

# 需求：打开‘注册A.html’页面，完成以下操作
# 1). 填写注册信息
driver.find_element_by_id('userA').send_keys('admin')
driver.find_element_by_id('passwordA').send_keys('123456')

# 扩展: 使用时间戳防止文件重名被覆盖
# 说明: Windows 系统文件名不支持特殊符号, 尽量只使用下划线, 否则可能无法生存截图文件
now_time = strftime('%Y%m%d_%H%M%S')  # %Y年%m月%d日%H时%M分%S秒
driver.get_screenshot_as_file('./info_{}.png'.format(now_time))

# 扩展: 给元素截图
btn = driver.find_element_by_tag_name('button')
btn.screenshot('./btn.png')

# 4. 展示效果
sleep(3)
# 5. 退出浏览器
driver.quit()

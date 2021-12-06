"""
截图操作
"""
# 1. 导入模块
from time import sleep

from selenium import webdriver

# 2. 实例化浏览器对象
driver = webdriver.Chrome()
# 3. 打开页面
driver.get('file:///Users/comesoon/Desktop/page/%E6%B3%A8%E5%86%8CA.html')

# 需求：打开‘注册A.html’页面，完成以下操作
# 1). 填写注册信息
driver.find_element_by_id('userA').send_keys('admin')
driver.find_element_by_id('passwordA').send_keys('123456')

# 2). 截图保存: 默认推荐使用 .png 格式
# driver.get_screenshot_as_file('./info.png')
# 说明: .jpg 虽然可以使用, 但是会有使用警告
# driver.get_screenshot_as_file('./info.jpg')
# 扩展: 指定图片文件存放路径: 需要先手动创建文件夹!!!!!!
driver.get_screenshot_as_file('./image/info.png')

# 4. 展示效果
sleep(3)
# 5. 退出浏览器
driver.quit()

"""
弹出框处理: 系统弹窗处理
"""
# 1. 导入模块
from time import sleep

from selenium import webdriver

# 2. 实例化浏览器对象
driver = webdriver.Chrome()
# 3. 打开页面
driver.get('file:///Users/comesoon/Desktop/page/%E6%B3%A8%E5%86%8CA.html')

# 需求：打开注册A.html页面，完成以下操作：
# 1).点击 alert 按钮
# 注意: 凡是通过 JS 实现的系统弹窗, 无法通过鼠标右键检查选项获取元素信息!!!!!!
# driver.find_element_by_id('alerta').click()  # 警告框
# driver.find_element_by_id('confirma').click()  # 确认框
driver.find_element_by_id('prompta').click()  # 提示框

# 2).关闭警告框
# 1> 切换到弹窗: 只要是系统弹窗, 无论哪一种, 处理方法都是以下的步骤!!!!!!
alert = driver.switch_to.alert
# driver.switch_to_alert()  # 调用的方法上如果存在黑线, 意为该方法已经过期, 将来会被移除, 不推荐使用
# 2> 获取弹窗信息(可选): 获取弹窗信息必须在处理弹窗操作之前!
print('弹窗信息是:', alert.text)
sleep(2)
# 3> 去除弹窗(同意/移除)
alert.accept()  # 同意
# alert.dismiss()  # 移除

# 3).输入用户名：admin
driver.find_element_by_id('userA').send_keys('admin')

# 4. 展示效果
sleep(3)
# 5. 退出浏览器
driver.quit()

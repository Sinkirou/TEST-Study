"""
XPath 策略: 延伸方法
"""
# 1. 导入模块
from time import sleep

from selenium import webdriver

# 2. 实例化浏览器对象
driver = webdriver.Chrome()
# 3. 打开页面
driver.get('file:///Users/comesoon/Desktop/page/%E6%B3%A8%E5%86%8CA.html')


# //*[contains(@属性名,'属性值的部分内容')] : 通过给定属性值的任意部分内容进行元素定位
driver.find_element_by_xpath('//*[contains(@id,"ss")]').send_keys('123456')

# //*[starts-with(@属性名,'属性值的开头部分内容')] : 通过给定属性值的开头部分内容进行元素定位
driver.find_element_by_xpath('//*[starts-with(@id,"te")]').send_keys('13800001111')

# //*[text()="文本信息"] : 通过文本信息定位目标元素(要求全部文本内容)
driver.find_element_by_xpath('//*[text()="访问 新浪 网站"]').click()

# 4. 展示效果
sleep(3)
# 5. 退出浏览器
driver.quit()

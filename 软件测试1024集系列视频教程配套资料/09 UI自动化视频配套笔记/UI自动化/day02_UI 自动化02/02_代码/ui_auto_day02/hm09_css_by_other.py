"""
CSS 策略:延伸方法
"""
# 1. 导入模块
from time import sleep

from selenium import webdriver

# 2. 实例化浏览器对象
driver = webdriver.Chrome()
# 3. 打开页面
driver.get('file:///Users/comesoon/Desktop/page/%E6%B3%A8%E5%86%8CA.html')

# 标签名[属性名^="属性值开头部分内容"] : 根据给出的属性值开头部分内容定位元素
driver.find_element_by_css_selector('[id^="pas"]').send_keys('123')

# 标签名[属性名$="属性值结尾部分内容"] : 根据给出的属性值结尾部分内容定位元素
driver.find_element_by_css_selector('[id$="rdA"]').send_keys('123')

# 标签名[属性名*="属性值任意部分内容"] : 根据给出的属性值任意部分内容定位元素
driver.find_element_by_css_selector('[id*="ss"]').send_keys('123')

# 注意: 标签名可以省略!

# 4. 展示效果
sleep(3)
# 5. 退出浏览器
driver.quit()

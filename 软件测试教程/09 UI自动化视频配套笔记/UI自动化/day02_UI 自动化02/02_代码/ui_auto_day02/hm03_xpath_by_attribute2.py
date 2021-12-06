"""
XPath:利用元素属性策略注意事项
"""
# 1. 导入模块
from time import sleep

from selenium import webdriver

# 2. 实例化浏览器对象
driver = webdriver.Chrome()
# 3. 打开页面
driver.get('file:///Users/comesoon/Desktop/page/%E6%B3%A8%E5%86%8CA.html')


# //*[@属性名='属性值']
# 说明: // 任意层级 * 任意标签名

# 注意: 目标元素的有些属性和属性值, 可能存在多个相同特征的元素, 需要注意唯一性.
driver.find_element_by_xpath('//*[@type="text"]').send_keys('admin')

# 注意: 与 class_name 方法不同的是, 如果使用具有多个值的 class 属性, 则需要传入全部的属性值!
driver.find_element_by_xpath('//*[@class="emailA dzyxA"]').send_keys('123@qq.com')

# 4. 展示效果
sleep(3)
# 5. 退出浏览器
driver.quit()

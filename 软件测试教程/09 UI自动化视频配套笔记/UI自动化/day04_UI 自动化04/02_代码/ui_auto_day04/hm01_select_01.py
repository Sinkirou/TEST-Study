"""
下拉框处理: 传统方案
"""
# 1. 导入模块
from time import sleep

from selenium import webdriver

# 2. 实例化浏览器对象
driver = webdriver.Chrome()
# 3. 打开页面
driver.get('file:///Users/comesoon/Desktop/page/%E6%B3%A8%E5%86%8CA.html')

# 需求：使用‘注册A.html’页面，完成对城市的下拉框的操作
# 1).选择‘广州’
driver.find_element_by_css_selector('[value="gz"]').click()
sleep(2)
# 2).暂停2秒，选择‘上海’
driver.find_element_by_css_selector('[value="sh"]').click()
sleep(2)
# 3).暂停2秒，选择‘北京’
driver.find_element_by_css_selector('[value="bj"]').click()

# 结论: 可以通过直接定位下拉框中的内容对应的元素, 完成对下拉框元素的处理!

# 4. 展示效果
sleep(3)
# 5. 退出浏览器
driver.quit()

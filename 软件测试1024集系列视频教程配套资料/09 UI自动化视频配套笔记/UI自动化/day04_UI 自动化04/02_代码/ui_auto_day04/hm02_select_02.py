"""
下拉框操作: Select 类的使用
"""
# 1. 导入模块
from time import sleep

from selenium import webdriver
from selenium.webdriver.support.select import Select

# 2. 实例化浏览器对象
driver = webdriver.Chrome()
# 3. 打开页面
driver.get('file:///Users/comesoon/Desktop/page/%E6%B3%A8%E5%86%8CA.html')

# 需求：使用‘注册A.html’页面，完成对城市的下拉框的操作
# 0> 定位下拉框元素
sel = driver.find_element_by_id('selectA')
# 1> 实例化下拉框选择对象
se = Select(sel)
# 1).选择‘广州’
# 2> 通过索引选择目标元素(索引从 0 开始)
se.select_by_index(2)
sleep(2)
# 2).暂停2秒，选择‘上海’
# 2> 通过 value 属性值选择目标元素
se.select_by_value('sh')
sleep(2)
# 3).暂停2秒，选择‘北京’
# 2> 通过可见文本信息选择目标元素
se.select_by_visible_text('A北京')

# 注意:
# 1. 如果页面内需要操作的下拉框元素有多个, 需要根据目标下拉框, 依次实例化下拉框选择对象
# 2. 根据具体需求, 三种下拉框内容元素选择方法, 任选其一使用即可!!!!!!

# 4. 展示效果
sleep(3)
# 5. 退出浏览器
driver.quit()

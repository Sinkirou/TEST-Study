"""
获取元素信息方法: Part1
"""
# 1. 导入模块
from time import sleep

from selenium import webdriver

# 2. 实例化浏览器对象
driver = webdriver.Chrome()
# 3. 打开页面
driver.get('file:///Users/comesoon/Desktop/page/%E6%B3%A8%E5%86%8CA.html')

# 1. size 返回元素大小
# 场景: 用于判断页面元素布局尺寸是否合理时使用
username = driver.find_element_by_id('userA')
print('目标元素的尺寸为:', username.size)

# 2. text 获取元素的文本
# 场景: 用于切换页面后, 对页面内容特定元素的文本信息的获取(用作断言使用)
btn = driver.find_element_by_tag_name('button')
print('目标元素的文本为:', btn.text)

# 3. get_attribute("xxx") 获取属性值，传递的参数为元素的属性名
# 场景: 有些情况下, 需要获取目标元素的特定属性值作为判断依据或数据
# 语法: 元素对象.get_attribute("属性名")
link = driver.find_element_by_link_text('新浪')
print('目标元素的地址为:', link.get_attribute('href'))

# 4. 展示效果
sleep(3)
# 5. 退出浏览器
driver.quit()

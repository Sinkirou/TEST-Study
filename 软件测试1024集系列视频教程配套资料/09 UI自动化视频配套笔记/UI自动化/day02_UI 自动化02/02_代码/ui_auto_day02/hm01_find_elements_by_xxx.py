# 1. 导入模块
from time import sleep

from selenium import webdriver

# 2. 实例化浏览器对象
driver = webdriver.Chrome()
# 3. 打开页面
driver.get('file:///Users/comesoon/Desktop/page/%E6%B3%A8%E5%86%8CA.html')

# 通过 name 属性值定位用户名和密码完成操作
driver.find_element_by_name('AAA').send_keys('admin')
# driver.find_element_by_name('AAA').send_keys('123456')
elements = driver.find_elements_by_name('AAA')
print(elements)
# 注意: 元素定位方法如果带有 s, 则执行结果返回的是列表类型数据, 里面的数据是多个元素对象
print(type(elements))
# 说明: 可以通过列表的下标(索引)获取对应的目标元素对象, 再执行操作
elements[1].send_keys('123456')

# 其他定位方法也可以实行定义一组元素:
# 使用标签名方法定位电话和邮箱并完成操作
new_els = driver.find_elements_by_tag_name('input')
new_els[2].send_keys('13800001111')
new_els[3].send_keys('123@qq.com')

# 4. 展示效果
sleep(3)
# 5. 退出浏览器
driver.quit()

"""
滚动条处理
"""
# 1. 导入模块
from time import sleep

from selenium import webdriver

# 2. 实例化浏览器对象
driver = webdriver.Chrome()
# 3. 打开页面
driver.get('file:///Users/comesoon/Desktop/page/%E6%B3%A8%E5%86%8CA.html')

# 需求：打开注册页面A，暂停2秒后，滚动条拉到最底层, 暂停 2 秒后, 恢复原位置
# 注意: Selenium 框架中没有专门处理滚动条的方法, 需要通过调用 JS 代码实现操作
sleep(2)
# 1> 准备 JS 代码: 1000 只是一个尽可能大的值, 不是准确值
js_down = "window.scrollTo(0,1000)"
# 2> 执行 JS 代码
driver.execute_script(js_down)
sleep(2)
# 向上: 反向只需要将坐标归零即可
js_up = "window.scrollTo(0,0)"
driver.execute_script(js_up)

# 4. 展示效果
sleep(3)
# 5. 退出浏览器
driver.quit()

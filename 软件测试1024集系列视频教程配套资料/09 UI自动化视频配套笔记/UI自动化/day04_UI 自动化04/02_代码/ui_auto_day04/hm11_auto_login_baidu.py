"""
cookie: 绕过登录操作
"""
# 1. 导入模块
from time import sleep

from selenium import webdriver

# 2. 实例化浏览器对象
driver = webdriver.Chrome()
# 3. 打开页面
driver.get('http://www.baidu.com')
driver.maximize_window()  # 窗口最大化

# cookie 绕过登录
# 1> 整理关键 cookie 信息为字典数据
# 注意: 字典数据的 key 必须是 name 和 value!!!!!!
cookie_value = {'name': 'BDUSS',
                'value': 'pXRTFVYUxZQTE0dVNqZlpnQTd2LUI5dC05M01PRlR2cWRVVWh6NGxRQXpQZGhnRVFBQUFBJCQAAAAAAAAAAAEAAABUjkMxUnl1dW1laTAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADOws'}

# 2> 调用方法添加 cookie 信息
driver.add_cookie(cookie_value)

# 3> 刷新页面 -> 发送 cookie 信息给服务器进行验证!!!!!!
driver.refresh()

# 注意:
# 1. 本地浏览器中登录的账号, 不能退出, 否则 cookie 信息过期, 需要重新获取
# 2. 不同项目的能够进行登录功能绕过的 cookie 字段信息都不相同, 具体需要询问开发
# 3. 利用 cookie 绕过登录, 则不能对登录功能本身进行测试
# 4. 个别项目如果想要绕过登录, 有可能需要添加多个 cookie 字段

# 4. 展示效果
sleep(3)
# 5. 退出浏览器
driver.quit()

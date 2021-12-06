"""
整合多个脚本至同一个测试用例中
"""
import pytest
from time import sleep
from selenium import webdriver


class TestLogin(object):
    """登录测试类"""

    def test_account_does_not_exist(self):
        """账号不存在测试方法"""
        driver = webdriver.Chrome()
        driver.get('http://127.0.0.1/')
        driver.maximize_window()  # 窗口最大化
        driver.implicitly_wait(10)  # 隐式等待

        # 1. 点击首页的‘登录’链接，进入登录页面
        driver.find_element_by_link_text('登录').click()

        # 2. 输入一个不存在的用户名
        driver.find_element_by_id('username').send_keys('13811110001')
        # 3. 输入密码
        driver.find_element_by_id('password').send_keys('123456')
        # 4. 输入验证码
        driver.find_element_by_id('verify_code').send_keys('8888')
        # 5. 点击登录按钮
        driver.find_element_by_name('sbtbutton').click()

        # 6. 获取错误提示信息
        # 获取元素文本值: 元素对象.text
        msg = driver.find_element_by_class_name('layui-layer-content').text
        print('错误信息为:', msg)

        sleep(3)
        driver.quit()

    def test_wrong_password(self):
        """密码错误测试方法"""
        driver = webdriver.Chrome()
        driver.get('http://127.0.0.1/')
        driver.maximize_window()  # 窗口最大化
        driver.implicitly_wait(10)  # 隐式等待

        # 1. 点击首页的‘登录’链接，进入登录页面
        driver.find_element_by_link_text('登录').click()

        # 2. 输入用户名
        driver.find_element_by_id('username').send_keys('13800001111')
        # 3. 输入错误密码
        driver.find_element_by_id('password').send_keys('error')
        # 4. 输入验证码
        driver.find_element_by_id('verify_code').send_keys('8888')
        # 5. 点击登录按钮
        driver.find_element_by_name('sbtbutton').click()

        # 6. 获取错误提示信息
        # 获取元素文本值: 元素对象.text
        msg = driver.find_element_by_class_name('layui-layer-content').text
        print('错误信息为:', msg)

        sleep(3)
        driver.quit()


if __name__ == '__main__':
    pytest.main(['-s', 'tpshop_login_1.py'])

"""
整合多个脚本至同一个测试用例中
"""
import pytest
from utils import DriverUtil, get_alert_msg
from v4.index_page import IndexTask
from v4.login_page import LoginTask


class TestLogin(object):
    """登录测试类"""

    def setup_class(self):
        self.driver = DriverUtil.get_driver()  # 获取浏览器对象
        self.index_task = IndexTask()  # 实例化首页业务层对象
        self.login_task = LoginTask()  # 实例化登录页面业务层对象

    def teardown_class(self):
        DriverUtil.quit_driver()  # 退出浏览器对象

    def setup(self):
        # 打开首页
        self.driver.get('http://127.0.0.1/')
        # 点击登录
        # self.driver.find_element_by_link_text('登录').click()
        self.index_task.go_to_login()  # 跳转登录

    def teardown(self):
        pass

    def test_account_does_not_exist(self):
        """账号不存在测试方法"""

        # # 2. 输入一个不存在的用户名
        # self.driver.find_element_by_id('username').send_keys('13811110001')
        # # 3. 输入密码
        # self.driver.find_element_by_id('password').send_keys('123456')
        # # 4. 输入验证码
        # self.driver.find_element_by_id('verify_code').send_keys('8888')
        # # 5. 点击登录按钮
        # self.driver.find_element_by_name('sbtbutton').click()
        self.login_task.login_method('13811110001', '123456', '8888')

        # 6. 获取错误提示信息
        msg = get_alert_msg()  # 获取弹窗信息
        print('错误信息为:', msg)

    def test_wrong_password(self):
        """密码错误测试方法"""

        # # 2. 输入用户名
        # self.driver.find_element_by_id('username').send_keys('13800001111')
        # # 3. 输入错误密码
        # self.driver.find_element_by_id('password').send_keys('error')
        # # 4. 输入验证码
        # self.driver.find_element_by_id('verify_code').send_keys('8888')
        # # 5. 点击登录按钮
        # self.driver.find_element_by_name('sbtbutton').click()
        self.login_task.login_method('13800001111', 'error', '8888')

        # 6. 获取错误提示信息
        msg = get_alert_msg()  # 获取弹窗信息
        print('错误信息为:', msg)


if __name__ == '__main__':
    pytest.main(['-s', 'tpshop_login.py'])

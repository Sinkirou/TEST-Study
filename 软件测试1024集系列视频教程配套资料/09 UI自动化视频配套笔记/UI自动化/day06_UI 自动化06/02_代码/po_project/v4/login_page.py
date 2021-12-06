"""
登录页面
"""
from utils import DriverUtil


class LoginPage(object):
    """登录对象层"""

    def __init__(self):
        self.driver = DriverUtil.get_driver()  # 获取浏览器对象

    def find_username(self):
        """定位用户名方法"""
        return self.driver.find_element_by_id('username')

    def find_password(self):
        """定位密码方法"""
        return self.driver.find_element_by_id('password')

    def find_verify_code(self):
        """定位验证码方法"""
        return self.driver.find_element_by_id('verify_code')

    def find_login_btn(self):
        """定位登录按钮方法"""
        return self.driver.find_element_by_name('sbtbutton')


class LoginHandle(object):
    """登录操作层"""

    def __init__(self):
        self.login_page = LoginPage()  # 获取对象层对象

    def input_username(self, name):
        """输入用户名方法"""
        self.login_page.find_username().send_keys(name)

    def input_password(self, pwd):
        """输入密码方法"""
        self.login_page.find_password().send_keys(pwd)

    def input_verify_code(self, code):
        """输入验证码方法"""
        self.login_page.find_verify_code().send_keys(code)

    def click_login_btn(self):
        """点击登录按钮方法"""
        self.login_page.find_login_btn().click()


class LoginTask(object):
    """登录业务层"""

    def __init__(self):
        self.login_handle = LoginHandle()  # 获取操作层对象

    def login_method(self, name, pwd, code):
        """登录方法"""
        self.login_handle.input_username(name)  # 输入用户名
        self.login_handle.input_password(pwd)  # 输入密码
        self.login_handle.input_verify_code(code)  # 输入验证码
        self.login_handle.click_login_btn()  # 点击登录按钮

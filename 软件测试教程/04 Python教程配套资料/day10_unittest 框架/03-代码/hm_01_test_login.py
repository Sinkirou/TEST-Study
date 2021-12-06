import unittest

from tools import login


class TestLogin(unittest.TestCase):
    def test_username_password_ok(self):
        """正确的用户名和密码: admin, 123456, 登录成功"""
        if login('admin', '123456') == '登录成功':
            print('pass')
        else:
            print('fail')

    def test_username_error(self):
        """错误的用户名: root, 123456, 登录失败"""
        if login('root', '123456') == '登录失败':
            print('pass')
        else:
            print('fail')

    def test_password_error(self):
        """错误的密码: admin, 123123, 登录失败"""
        if login('admin', '123123') == '登录失败':
            print('pass')
        else:
            print('fail')

    def test_username_password_error(self):
        """错误的用户名和错误的密码: aaa, 123123, 登录失败"""
        if login('aaa', '123123') == '登录失败':
            print('pass')
        else:
            print('fail')

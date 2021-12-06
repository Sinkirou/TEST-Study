# 1. 导包 unittest/ pa
import unittest
from parameterized import parameterized
from tools import login

# 组织测试数据  [(), (), ()] or [[], [], []]
data = [
    ('admin', '123456', '登录成功'),
    ('root', '123456', '登录失败'),
    ('admin', '123123', '登录失败')
]


# 2. 定义测试类
class TestLogin(unittest.TestCase):
    # 3. 书写测试方法(用到的测试数据使用变量代替)
    @parameterized.expand(data)
    def test_login(self, username, password, expect):
        self.assertEqual(expect, login(username, password))

# 4. 组织测试数据并传参(装饰器 @)


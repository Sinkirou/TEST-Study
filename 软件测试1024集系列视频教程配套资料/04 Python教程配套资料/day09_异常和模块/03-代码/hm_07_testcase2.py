"""
代码的目的: 学习 TestCase(测试用例)模块的书写方法
"""
# 1, 导包
import unittest


# 2, 自定义测试类, 需要继承 unittest 模块中的 TestCase 类即可
class TestDemo2(unittest.TestCase):
    # 3, 书写测试方法, 即 用例代码. 目前没有真正的用例代码, 使用 print 代替
    # 书写要求, 测试方法 必须以 test_ 开头(本质是以 test 开头)
    def test_method1(self):
        print('测试方法 2-1')

    def test_method2(self):
        print('测试方法 2-2')


# 4, 执行用例(方法)
# 4.1 将光标放在 类名的后边 运行, 会执行类中的所有的测试方法
# 4.2 将光标放在 方法名的后边 运行, 只执行当前的方法


"""
TestCase
"""
import unittest


class TestDemo(unittest.TestCase):
    """自定义测试类"""

    def test_method1(self):
        """自定义测试方法"""
        print('测试方法1')

    def test_method2(self):
        """自定义测试方法"""
        print('测试方法2')


if __name__ == '__main__':
    unittest.main()

"""案例练习"""
# 1,导包
import unittest
from tools import add

# 2, 自定义测试类


class TestAdd(unittest.TestCase):
    # 3. 书写测试方法, 就是测试用例代码
    def test_method1(self):
        # 1, 2, 3 判断实际结果和预期结果是否相符
        if add(1, 2) == 3:
            print('测试通过')
        else:
            print('测试不通过')

    def test_method2(self):
        if add(10, 20) == 30:
            print('测试通过')
        else:
            print('测试不通过')

    def test_method3(self):
        # 1, 2, 3 判断实际结果和预期结果是否相符
        if add(2, 3) == 5:
            print('测试通过')
        else:
            print('测试不通过')




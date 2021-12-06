# 测试类形式
import pytest


class TestDemo2(object):  # 正常定义类, 但是测试类名必须以 Test 开头
    """测试示例类"""

    def test_method1(self):  # 正常定义方法, 但是测试方法名必须以 test 开头
        """测试方法1"""
        print('测试方法2-1')

    def test_method2(self):
        """测试方法2"""
        print('测试方法2-2')


if __name__ == '__main__':
    # 语法: pytest.main(['-s', '文件名.py'])
    pytest.main(['-s', 'hm04_pytest_basic_04.py'])

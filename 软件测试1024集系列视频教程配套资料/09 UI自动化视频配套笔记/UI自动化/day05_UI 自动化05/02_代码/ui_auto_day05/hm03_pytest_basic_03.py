# 测试函数形式
import pytest


def test_func():  # 要求函数名以 test 开头
    """测试函数"""
    print('我是测试函数')


if __name__ == '__main__':
    # 语法: pytest.main(['-s', '文件名.py'])
    pytest.main(['-s', 'hm03_pytest_basic_03.py'])

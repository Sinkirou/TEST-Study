"""
pytest 参数化: 通过方法引入数据
"""
import pytest


def build_test_data():
    """构造测试数据函数"""
    # 中间代码略
    return [('admin', 123456), ('test', 654321), ('xxx', 'yyy')]


class TestDemo(object):
    """示例测试类"""

    # @pytest.mark.parametrize('name, pwd', build_test_data)  # 错误样例: 通过方法引入数据, 必须带小括号!!!!!!
    @pytest.mark.parametrize('name, pwd', build_test_data())  # 正确样例
    def test_method(self, name, pwd):
        """测试方法"""
        print('账号:{} 密码:{}'.format(name, pwd))


if __name__ == '__main__':
    pytest.main(['-s', 'hm13_pytest_para3.py'])

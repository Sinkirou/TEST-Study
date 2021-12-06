"""
pytest 参数化: 多个参数
"""
import pytest


class TestDemo(object):
    """示例测试类"""

    # 语法: @pytest.mark.parametrize('参数1, 参数n', [(数据1-1, 数据1-2), (数据2-1, 数据2-2), ...])
    # 注意:
    # 1. 多个参数必须置于同一个字符串内!
    # 2. 数据格式必须是: [(), ()] 或者 [[], []]
    # 扩展: 另一种写法
    # @pytest.mark.parametrize(('name', 'pwd'), [('admin', 123456), ('test', 654321), ('xxx', 'yyy')])
    @pytest.mark.parametrize('name, pwd', [('admin', 123456), ('test', 654321), ('xxx', 'yyy')])
    def test_method(self, name, pwd):
        """测试方法"""
        print('账号:{} 密码:{}'.format(name, pwd))


if __name__ == '__main__':
    pytest.main(['-s', 'hm12_pytest_para2.py'])

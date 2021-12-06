"""
pytest 控制方法执行顺序插件
"""
import pytest


@pytest.mark.run(order=2)
class TestDemo(object):
    """示例测试类"""

    # 语法: @pytest.mark.run(order=序号)
    # 注意: run(order=序号) 没有代码提示, 需要手写!

    # @pytest.mark.run(order=-3)
    def test_method1(self):
        """测试方法1"""
        print('测试方法1')

    # @pytest.mark.run(order=1)
    def test_method2(self):
        """测试方法2"""
        print('测试方法2')

    # @pytest.mark.run(order=2)
    def test_method3(self):
        """测试方法3"""
        print('测试方法3')

    # 扩展: 序号支持正数和负数, 以及正负混合
    # 1. 纯正数: 数越小, 优先级越高[掌握]
    # 2. 纯负数: 数越小, 优先级越高[了解]
    # 3. 正负混合: 正数先按照顺序执行, 负数最后执行[了解]


# 注意: 控制方法执行顺序对测试类同样有效!
@pytest.mark.run(order=1)
class TestDemo2(object):
    """测试类2"""

    def test_method(self):
        print('测试类2 -> 测试方法')

import unittest

# 实例化套件对象
from hm_08_test import TestAdd

suite = unittest.TestSuite()
# 添加测试方法
suite.addTest(unittest.makeSuite(TestAdd))
# 实例化执行对象
runner = unittest.TextTestRunner()
runner.run(suite)




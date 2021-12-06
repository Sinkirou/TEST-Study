"""TestLoader 的使用"""
# 1, 导包
import unittest

# 2, 使用默认的加载对象并加载用例
suite = unittest.defaultTestLoader.discover('case', 'hm_*.py')

# 可以将 3 4 步 变为一步
unittest.TextTestRunner().run(suite)


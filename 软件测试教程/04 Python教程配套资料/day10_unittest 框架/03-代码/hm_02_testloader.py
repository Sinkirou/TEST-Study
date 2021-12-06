"""TestLoader 的使用"""
# 1, 导包
import unittest

# 2, 实例化加载对象并添加用例
# unittest.TestLoader().discover('用例所在的路径', '用例的代码文件名')
# 用例所在的路径,建议使用相对路径, 用例的代码文件名可以使用 *(任意多个任意字符) 通配符
# suite = unittest.TestLoader().discover('./case', 'hm*.py')
# suite = unittest.TestLoader().discover('./case', '*test*.py')
# suite = unittest.TestLoader().discover('./case', '*test*')
suite = unittest.TestLoader().discover('./case', '*case1.py')

# 3, 实例化运行对象
# runner = unittest.TextTestRunner()
# # 4, 执行
# runner.run(suite)

# 可以将 3 4 步 变为一步
unittest.TextTestRunner().run(suite)


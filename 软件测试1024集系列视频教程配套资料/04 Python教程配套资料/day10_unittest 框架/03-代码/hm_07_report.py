# 1. 获取第三方的 测试运行类模块 , 将其放在代码的目录中
# 2. 导包 unittest
import unittest
from HTMLTestRunner import HTMLTestRunner

# 3. 使用  套件对象, 加载对象 去添加用例方法
suite = unittest.defaultTestLoader.discover('.', 'hm_05_pa1.py')
# 4. 实例化 第三方的运行对象 并运行 套件对象
# HTMLTestRunner()
# stream=sys.stdout, 必填,测试报告的文件对象(open ), 注意点,要使用 wb 打开
# verbosity=1, 可选, 报告的详细程度,默认 1 简略, 2 详细
# title=None, 可选, 测试报告的标题
# description=None 可选, 描述信息, Python 的版本, pycharm 版本

# file = 'report.html'   # 报告的后缀是.html
file = 'report1.html'   # 报告的后缀是.html
with open(file, 'wb') as f:
    # runner = HTMLTestRunner(f)  # 运行对象
    runner = HTMLTestRunner(f, 2, '测试报告', 'python 3.6.8 ')  # 运行对象

    # 运行对象执行套件, 要写在 with 的缩进中
    runner.run(suite)

import unittest
from HTMLTestRunnerCN import HTMLTestReportCN

# 组装用例方法
suite = unittest.defaultTestLoader.discover('.', '*pa1.py')

# 实例化运行对象
with open('report_cn.html', 'wb') as f:
    runner = HTMLTestReportCN(f)
    runner.run(suite)

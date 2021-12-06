# 方式一
import random

print(random.randint(1, 20))

# 方式二
# from random import randint
# from random import randint
#
# print(randint(1, 20))

# 方式三, 问题: 可能存在多个模块中有相同的名字的工具, 会产生冲突
# from random import *
#
# print(randint(1, 20))

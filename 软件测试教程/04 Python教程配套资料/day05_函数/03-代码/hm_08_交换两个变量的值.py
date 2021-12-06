a = 10
b = 20
# 方法一: 常规方法  引入第三个变量
# c = a  # 将 变量 a 中的值先保存起来 10
# a = b  # 将变量 b 中的值 给 a
# b = c  # 将变量 c中的值(即最开始 a 的值) 10 给 b
# print(a, b)

# 方法二, 不使用第三个变量, 使用数学中的方法
# a = a + b  # a 的值 30
# b = a - b  # 30 - 20 ===> 10
# a = a - b  # 30 - 10 ===> 20
# print(a, b)

# 方法三, 重点掌握, Python 特有
a, b = b, a
print(a, b)

# 组包
c = b, a  # 组包
print(type(c), c)  # <class 'tuple'> (10, 20)

# 拆包
a, b = c
print(a, b)

x, y, z = [1, 2, 3]
print(x, y, z)
str1 = "hello world and itcast and itheima and Python"

# 1. 将 str1 按照 and 字符进行拆分
result1 = str1.split('and')
print(result1)  # ['hello world ', ' itcast ', ' itheima ', ' Python']

# 2, 将 str1 按照 and 字符进行拆分, 拆分一次
result2 = str1.split('and', 1)
print(result2)  # ['hello world ', ' itcast and itheima and Python']

# 3. 按照空白字符进行切割
result3 = str1.split()
print(result3)  # ['hello', 'world', 'and', 'itcast', 'and', 'itheima', 'and', 'Python']

# 4. 按照空白字符进行切割, 拆分一次
result4 = str1.split(maxsplit=1)
print(result4)

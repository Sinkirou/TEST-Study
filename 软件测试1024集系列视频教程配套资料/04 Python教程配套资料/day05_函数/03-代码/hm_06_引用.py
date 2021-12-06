a = 1  # 将 数据 1 的地址 存到 a 对应的内存中
print('a:', id(a))

b = a  # 将 变量 a 中的引用 保存到变量 b
print('b:', id(b))

a = 10  # 将 数据 10 的地址 保存到 a 对应的地址, 即 a 的引用变了
print('a:', id(a))

print('b:', id(b))

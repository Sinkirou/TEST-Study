# 1, 类实例化的方式
# 1.1 定义空元祖(不会使用的)
my_tuple1 = tuple()
print(type(my_tuple1), my_tuple1)  # <class 'tuple'> ()
# 1.2 类型转换
# 可以将列表转换为元组, 只需要将 [], 变为 (), 同时 可以将元组转换列表 , 将() 变为 []
my_tuple2 = tuple([1, 2, 3])
print(my_tuple2)  # (1, 2, 3)
# 转换字符串, 和列表中一样,只是将列表的[] 变为()
my_tuple3 = tuple('hello')
print(my_tuple3)  # ('h', 'e', 'l', 'l', 'o')

# 2. 直接使用 () 定义
my_tuple4 = (1, "小王", 3.14, False)
print(my_tuple4)

# 3. 特殊点, 定义只有一个数据的元组时, 数据后边必须有一个逗号
my_tuple5 = (1,)
print(my_tuple5)  # (1,)

print(my_tuple4[1])  # 小王


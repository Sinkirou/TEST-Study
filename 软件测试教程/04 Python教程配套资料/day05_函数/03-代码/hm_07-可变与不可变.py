my_list = [1, 2, 3]
my_list1 = [1, 2, 3]

print('my_list :', id(my_list), id(my_list[1]))
print('my_list1:', id(my_list1))
my_list[1] = 10
print(my_list)
print('my_list :', id(my_list), id(my_list[1]))

my_tuple = (1, 2, [3, 4])  # 元组中存储的是 1 的地址, 2 的地址, 和 列表的地址
# 元组中的数据不能改变,是值 这个三个地址不能改变
print(my_tuple, id(my_tuple[-1]))
my_tuple[-1][0] = 10  # 修改的是列表中下标为 0 的位置的引用地址, 列表的地址没变, 元组中的内容没有变化
print(my_tuple, id(my_tuple[-1]))


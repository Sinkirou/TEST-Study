my_list = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]

# 1. 删除最后一个位置的数据
num = my_list.pop()
print('删除的数据为:', num)
print(my_list)  # [1, 3, 5, 7, 9, 2, 4, 6, 8]

# 2. 删除下标为 1 的数据 3
my_list.pop(1)
print(my_list)  # [1, 5, 7, 9, 2, 4, 6, 8]

# 3. 删除数据为 7 的数据
my_list.remove(7)  # 注意, 如果列表中有多个 7, 只能删除第一个, 如果数据不存在,会报错的
print(my_list)  # [1, 5, 9, 2, 4, 6, 8]

# my_list.remove(7)  # 会报错的

# 清空
my_list.clear()
print(my_list)  # []


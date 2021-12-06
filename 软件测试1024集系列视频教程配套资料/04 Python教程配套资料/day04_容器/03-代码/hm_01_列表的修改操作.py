# 定义列表
my_list = [1, 3, 5, 7]

# 1. 想要将下标为 1 的数据修改为 22
my_list[1] = 22
print(my_list)  # [1, 22, 5, 7]

# 修改最后一个位置的数据, 改为 'hello'
my_list[-1] = 'hello'
print(my_list)  # [1, 22, 5, 'hello']

# 2. 如果指定的下标不存在, 会报错的
# my_list[10] = 10  # 代码会报错


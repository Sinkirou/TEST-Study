my_list = [1, 3, 5, 7, 2, 3]

# 找 数据 3 出现的下标
num = my_list.index(3)
print(num)  # 1

# 找 数据 4 出现的下标
# num1 = my_list.index(4)  #  代码会报错
if 4 in my_list:
    num1 = my_list.index(4)
    print(num1)
else:
    print('不存在数据 4')

# my_list.count(4) 统计 数据 4 出现的次数
if my_list.count(4) > 0:
    num1 = my_list.index(4)
    print(num1)
else:
    print('不存在数据 4')

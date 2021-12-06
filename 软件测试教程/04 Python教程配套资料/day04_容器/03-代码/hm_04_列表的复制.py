my_list = [1, 2, 3]

my_list1 = my_list[:]
print('my_list :', my_list)
print('my_list1:', my_list1)
my_list1[1] = 22
print('my_list :', my_list)
print('my_list1:', my_list1)
print('-' * 30)

my_list2 = my_list.copy()
print('my_list :', my_list)
print('my_list2:', my_list2)
my_list2[2] = 33
print('my_list :', my_list)
print('my_list2:', my_list2)

print('=' * 30)
my_list3 = my_list  # 这是同一个列表,多了一个名字, 引用
print('my_list :', my_list)
print('my_list3:', my_list3)
my_list3[0] = 11
print('my_list :', my_list)
print('my_list3:', my_list3)
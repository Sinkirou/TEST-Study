my_list = []
print(my_list)  # []

# 1. 想列表中添加数据  郭德纲
my_list.append('郭德纲')
print(my_list)  # ['郭德纲']

# 2. 向列表的尾部添加 郭麒麟
my_list.append('郭麒麟')
print(my_list)  # ['郭德纲', '郭麒麟']

# 3. 在下标位置为 1 的位置添加数据 '岳岳
my_list.insert(1, '岳岳')
print(my_list)  # ['郭德纲', '岳岳', '郭麒麟']

# 4. 在下标位置为 1 的位置添加数据 于谦
my_list.insert(1, '于谦')
print(my_list)  # ['郭德纲', '于谦', '岳岳', '郭麒麟']

# 5. 定义新的列表 list1
list1 = ['孙越', '烧饼']
# 将 list1 中数据逐个添加到 my_list 中
my_list.extend(list1)
print(my_list)  # ['郭德纲', '于谦', '岳岳', '郭麒麟', '孙越', '烧饼']

# 将 list1 作为一个整体添加到 my_list
my_list.append(list1)
print(my_list)  # ['郭德纲', '于谦', '岳岳', '郭麒麟', '孙越', '烧饼', ['孙越', '烧饼']]


my_dict = {'name': '小明', 'age': 19, 'like': ['抽烟', '喝酒', '烫头', '学习']}

# 1. 获取 名字
print(my_dict['name'])  # 小明
print(my_dict.get('name'))  # 小明
print(my_dict.get('name', 'zzz'))  # 小明

# 2. 获取 sex 性别
# print(my_dict['sex'])   # 代码会报错, 原因 key 不存在

print(my_dict.get('sex'))  # None
print(my_dict.get('sex', '保密'))  # 保密

# 3. 获取 第二个爱好
print(my_dict['like'][1])  # 喝酒
print(my_dict.get('like')[1])  # 喝酒

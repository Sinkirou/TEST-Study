# 定义字典
my_dict = {'name': '小明', 'age': 18, 'sex': '男'}

# 1. 遍历字典的键
for k in my_dict:
    print(k)

for k in my_dict.keys():
    print(k)

print('-' * 30)

# 2. 遍历字典的值
for v in my_dict.values():
    print(v)

print('*' * 30)

# 3. 遍历键值
for k, v in my_dict.items():
    print(k, v)


# 定义字典  小明 18 爱好

my_dict = {"name": "小明", "age": 18, "like": ['抽烟', '喝酒', '烫头']}

print(my_dict)  # {'name': '小明', 'age': 18, 'like': ['抽烟', '喝酒', '烫头']}
# 1. 添加性别信息 sex
my_dict['sex'] = '男'
print(my_dict)  # {'name': '小明', 'age': 18, 'like': ['抽烟', '喝酒', '烫头'], 'sex': '男'}

# 2. 修改年龄为 19
my_dict['age'] = 19
print(my_dict)  # {'name': '小明', 'age': 19, 'like': ['抽烟', '喝酒', '烫头'], 'sex': '男'}

# 3. 添加一个爱好, 学习--> 本质是向列表中添加一个数据
my_dict['like'].append('学习')
print(my_dict)  # {'name': '小明', 'age': 19, 'like': ['抽烟', '喝酒', '烫头', '学习'], 'sex': '男'}

# 1. 使用 类实例化的方法
my_dict = dict()
print(type(my_dict), my_dict)  # <class 'dict'> {}

# dict() 不能转列表和元组,字符串

# 2. 直接使用{} 定义
# 2.1 空字典
my_dict1 = {}
print(type(my_dict1), my_dict1)  # <class 'dict'> {}

# 2.2 非空字典, 小明('name') 18('age') 1.71('height') True(is_men)  抽烟 喝酒 烫头('like')
my_dict2 = {"name": "小明", "age": 18, "height": 1.71, "is_men": True, "like": ["抽烟", "喝酒", "烫头"]}

print(my_dict2)
print(len(my_dict2))  # 5

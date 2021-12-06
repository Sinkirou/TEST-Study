person_info = [["张三", "18", "功能测试"], ["李四", "20", "自动化测试"]]

print(len(person_info))  # 2
print(person_info[0])  # ['张三', '18', '功能测试']

print(person_info[0][0])  # '张三'

print(person_info[0][0][0])  # 张

# 将 18 改为 19
person_info[0][1] = '19'
print(person_info)  # [['张三', '19', '功能测试'], ['李四', '20', '自动化测试']]

# 给 李四 所在的列表添加一个性别 信息
person_info[1].append('男')
print(person_info)  # [['张三', '19', '功能测试'], ['李四', '20', '自动化测试', '男']]

# 将张三的年龄信息删除
# person_info[0].pop(1)
person_info[0].remove('19')
print(person_info)  # [['张三', '功能测试'], ['李四', '20', '自动化测试', '男']]

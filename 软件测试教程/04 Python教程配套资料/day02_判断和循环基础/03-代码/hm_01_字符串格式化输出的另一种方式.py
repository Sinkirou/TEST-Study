# 定义变量 姓名  年龄  身高
name = '小明'  # 可以使用 input 输入
age = 18   # 可以使用 input 输入
height = 1.71  # 可以使用 input 输入
stu_num = 1  # 学号
num = 90  # 及格率

# print('我的名字是 xx, 年龄是 xx, 身高是 xx m, 学号 xx, 本次考试的及格率为 xx%')
print(f'我的名字是 {name}, 年龄是 {age}, 身高是 {height} m, 学号 {stu_num}, 本次考试的及格率为 {num}%')
# 一般不会有这样的需求
print(f'我的名字是 {name}, 年龄是 {age}, 身高是 {height:.3f} m, 学号 {stu_num:06d}, 本次考试的及格率为 {num}%')

# 字符串.format()
print('我的名字是 {}, 年龄是 {}, 身高是 {} m, 学号 {}, 本次考试的及格率为 {}%'.format(name, age, height, stu_num, num))
print('我的名字是 {}, 年龄是 {}, 身高是 {:.3f} m, 学号 {:06d}, 本次考试的及格率为 {}%'.format(name, age, height, stu_num, num))

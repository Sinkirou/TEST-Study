# 定义变量 姓名  年龄  身高
name = '小明'  # 可以使用 input 输入
age = 18   # 可以使用 input 输入
height = 1.71  # 可以使用 input 输入

# 要求按照以下个数输出个人信息
# 我的名字是 xx, 年龄是 xx, 身高是 xx m
# 使用格式化输出实现
# print('我的名字是 name, 年龄是 age, 身高是 height m')
print('我的名字是 %s, 年龄是 %d, 身高是 %f m' % (name, age, height))
# 小数默认显示 6 位, 如果想要指定显示小数点后几位,  %.nf , n 需要换成具体的整数数字,即保留小数的位置
print('我的名字是 %s, 年龄是 %d, 身高是 %.2f m' % (name, age, height))  # 两位小数
print('我的名字是 %s, 年龄是 %d, 身高是 %.1f m' % (name, age, height))  # 一位小数

# 补充
stu_num = 1   # 学号
# 我的学号是 000001
print('我的学号是%d' % stu_num)
# %0nd n 需要换成具体的整数数字, 表示整数一共占几位
print('我的学号是%06d' % stu_num)

num = 90  # 考试的及格率
# 某次考试的及格率为 90%, 如果在 格式化中需要显示%, 在书写的使用 需要使用 两个 %% 才可以
print('某次考试的及格率为 %d%%' % num)


# 1. 使用 input 获取用户的年龄, 类型是 str
age = input('请输入你的年龄:')
# 2. 判断年龄是否满足 18 岁
if int(age) >= 18:  # 字符串和 int 类型不能比大小, 先类型转换,再比大小
    # 3. 如果年龄大于等于(满足)18 岁, 输出 '满 18 岁了,可以进入网吧为所欲为了'
    print('满 18 岁了,可以进入网吧为所欲为了')
# 4. 如果不满足, 输出 '不满 18 岁,回去写作业吧'
else:
    print('不满 18 岁,回去写作业吧')

# 1. 定义 score 变量记录考试分数
score = int(input('请输入你的分数'))  # int  float
# 2. 如果分数是大于等于90分应该显示优
if score >= 90:
    print('优')
# 3. 如果分数是大于等于80分并且小于90分应该显示良
elif (score >= 80) and score < 90:
    print('良')
# 4. 如果分数是大于等于70分并且小于80分应该显示中
# and score < 80 可以不写的, 原因只有上边一个判断条件不成立(一定满足 score<80),才会执行这个
elif score >= 70:
    print('中')
# 5. 如果分数是大于等于60分并且小于70分应该显示差
elif score >= 60:
    print('差')
# 6. 其它分数显示不及格
else:
    print('不及格')

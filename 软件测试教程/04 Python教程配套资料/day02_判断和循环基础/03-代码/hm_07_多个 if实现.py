# 1. 定义 score 变量记录考试分数
score = int(input('请输入你的分数'))  # int  float
# 2. 如果分数是大于等于90分应该显示优
if score >= 90:
    print('优')
# 3. 如果分数是大于等于80分并且小于90分应该显示良
if (score >= 80) and score < 90:
    print('良')
# 4. 如果分数是大于等于70分并且小于80分应该显示中
if (score >= 70) and score < 80:
    print('中')
# 5. 如果分数是大于等于60分并且小于70分应该显示差
if (score >= 60) and score < 70:
    print('差')
# 6. 其它分数显示不及格
if score < 60:
    print('不及格')

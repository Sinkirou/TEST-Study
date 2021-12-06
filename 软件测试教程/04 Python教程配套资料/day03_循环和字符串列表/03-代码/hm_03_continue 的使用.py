# 1. 获取你输入的字符串
result = input('请输入一个字符串:')
# 2. 遍历打印这个字符串
for i in result:
    # 3. 在遍历的时候,如果这个字符是 e, 不打印(即后续的代码不执行)
    if i == 'e':
        continue  # 本次循环后续的代码不执行,执行下一次循环
    print(i)

print('-' * 30)

for i in result:
    # 3. 在遍历的时候,如果这个字符是 e, 不打印(即后续的代码不执行)
    # 如果这个字符不是 e, 打印
    if i != 'e':
        print(i)
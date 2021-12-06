num = 0

i = 1
while i <= 100:
    # 判断该数字是不是偶数,如果是偶数再求和
    if i % 2 == 0:
        # print(i)
        num += i

    # 改变计数器
    i += 1

print('求和的结果是:', num)

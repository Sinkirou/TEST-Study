try:
    # 1. 获取用户从键盘输入的数据
    num = input('请输入数字:')
    # 2. 转换数据类型为整数
    num = int(num)
    # 3. 输出转换之后的数据内容
    print(num)
    a = 10 / num   # 10 / 0
    print(f'a: {a}')

except Exception as e:
    print(f"错误信息为: {e}")
else:
    print('没有发生异常我会执行')
finally:
    print('不管有没有发生异常,我都会执行')
# print('不管有没有发生异常,我都会执行')
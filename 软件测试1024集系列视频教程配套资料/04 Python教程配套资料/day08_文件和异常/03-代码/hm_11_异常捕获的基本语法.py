# try:
#     # 1. 获取用户从键盘输入的数据
#     num = input('请输入数字:')
#     # 2. 转换数据类型为整数
#     num = int(num)
#     # 3. 输出转换之后的数据内容
#     print(num)
# except:
#     print('请输入正确的数字')
#
# print('后续其他的代码,可以继续执行')

try:
    # 1. 获取用户从键盘输入的数据
    num = input('请输入数字:')
    # 2. 转换数据类型为整数
    num = int(num)
    # 3. 输出转换之后的数据内容
    print(num)
    a = 10 / num   # 10 / 0
    print(f'a: {a}')

except ValueError:  # 只能捕获 ValueError 类型及其子类的异常
    print('发生了异常, 请输入正确的数字...')
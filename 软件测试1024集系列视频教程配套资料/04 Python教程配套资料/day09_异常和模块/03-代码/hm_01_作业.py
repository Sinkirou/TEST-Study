def func1():
    # 1. 获取用户输入的数字
    num = input('请输入数字:')
    # 2. 判断获取的数字是否整数
    try:
        num = int(num)
    # 3. 如果不是整数, 提示输入错误
    except Exception as e:
        print("输入错误", e)
    # 4. 如果是整数, 则进一步判断是奇数还是偶数
    else:
        if num % 2 == 0:
            print('偶数')
        else:
            print('奇数')
    # 5. 最终提示: 程序运行结束
    finally:
        print('程序运行结束')


def func2():
    # 1. 获取用户输入的数字
    num = input('请输入数字:')
    # 2. 判断获取的数字是否整数
    if num.isdigit():
        # 类型转换
        num = int(num)
        # 4. 如果是整数, 则进一步判断是奇数还是偶数
        if num % 2 == 0:
            print('偶数')
        else:
            print('奇数')
    # 3. 如果不是整数, 提示输入错误
    else:
        print("输入错误")
    # 5. 最终提示: 程序运行结束
    print('程序运行结束')

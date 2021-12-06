g_num = 10  # 全局变量


def func1():
    print(f'func1 中 {g_num}')  # 在函数中可以读取全局变量的值


def func2():
    g_num = 20  # 定义局部变量, 不会影响全局变量
    print(f'func2 中 {g_num}')


def func3():
    global g_num  # 这个函数中使用的 g_num  都是全局变量, 写在函数的第一行
    g_num = 30  # 修改了全局变量
    print(f'func3 中 {g_num}')


# func1()  # 10
# func2()  # 20
# func1()  # 10
# func3()  # 30
# func1()  # 30
print(g_num)

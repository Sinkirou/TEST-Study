def func1():
    num = 10  # num 就是局部变量
    print(f"func1 函数中 {num}")


def func2():
    num = 100  # 可以在不同函数中定义名字相同的局部变量,没有影响
    print(f"func2 函数中 {num}")


func1()  # 10
func2()  # 100
func1()  # 10


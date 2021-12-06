# 1. 无参无返回值
def func1():
    print('hello world')


func1()
# lambda : print('hello lambda')  # 匿名函数的定义
func11 = lambda: print('hello lambda')
func11()


# 2. 无参有返回值
def func2():
    return 10


print(func2())
func22 = lambda: 10
print(func22())


# 3. 有参无返回值
def my_sum(a, b):
    print(a + b)


my_sum(1, 2)
my_sum11 = lambda a, b: print(a+b)
my_sum11(10, 20)


# 4. 有参有返回值
def func4(a, b):
    return a + b


print(func4(1, 2))   # num = func4(1, 2)  print(num)
func44 = lambda a, b: a+b

print(func44(10, 20))





# 1. 定义一个匿名函数可以求两个数的乘积 (参数需要两个, )
func1 = lambda a, b: a * b

# 2. 定义一个匿名函数, 参数为字典,返回字典中键为 age 的值
# 参数只是一个占位的作用,定义的时候没有具体的数据值, 形参的值是在调用的时候进行传递,此时,形参才有数据值
# 形参的类型就是由实参来决定的, 在函数定义的时候,参数只是一个符号,写什么都可以, 想让其是字典类型,只需要保证
# 实参是字典即可
func2 = lambda x: x.get('age')
func3 = lambda x: x['age']


print(func1(1, 2))
print(func1(3, 2))
my_dict = {'name': '张三', 'age': 18}
print(func2(my_dict))
print(func3(my_dict))


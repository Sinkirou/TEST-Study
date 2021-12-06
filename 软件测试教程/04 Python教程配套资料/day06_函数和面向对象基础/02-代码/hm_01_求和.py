def my_sum(*args, **kwargs):
    num = 0  # 定义变量,保存求和的结果
    for i in args:
        num += i

    for j in kwargs.values():
        num += j

    print(num)


# 需求, my_list = [1, 2, 3, 4]  字典 my_dict =  {'a': 1, 'b': 2, 'c': 3, 'd': 4}
my_list = [1, 2, 3, 4]
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# 将字典和列表中的数据使用 my_sum 函数进行求和, 改如何传参的问题
# my_sum(1, 2, 3, 4)
# my_sum(a=1, b=2, c=3, d=4)
# 想要将列表(元组)中的数据 分别作为位置参数,进行传参,需要对列表进行拆包操作
# my_sum(*my_list)  # my_sum(1, 2, 3, 4)
# 想要将字典中的数据, 作为关键字传参,, 需要使用 使用 ** 对字典进行拆包
my_sum(**my_dict)  # my_sum(a=1, b=2, c=3, d=4)



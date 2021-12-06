def func(*args, **kwargs):
    print(type(args), args)
    print(type(kwargs), kwargs)
    print('-' * 30)


func()
func(1, 2, 3)  # 位置传参, 数据都给 args
func(a=1, b=2, c=3)  # 关键字传参, 数据都给 kwargs
func(1, 2, 3, a=4, b=5, c=6)

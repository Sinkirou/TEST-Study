def func(a, b, c):
    print(f'a: {a}, b: {b}, c: {c}')


# 位置传参
func(1, 2, 3)

# 关键字传参
func(a=2, b=3, c=1)

# 混合使用
func(1, 3, c=5)



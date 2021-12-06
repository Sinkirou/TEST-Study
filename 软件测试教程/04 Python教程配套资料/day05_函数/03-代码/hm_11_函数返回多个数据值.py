def calc(a, b):
    num = a + b
    num1 = a - b
    return num, num1


# 写法一
result = calc(10, 5)
print(result, result[0], result[1])

# 写法二, 直接拆包
x, y = calc(20, 10)
print(x, y)

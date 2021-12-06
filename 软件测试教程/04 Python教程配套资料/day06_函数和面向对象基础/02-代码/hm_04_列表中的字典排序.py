user_list = [
    {"name": "zhangsan", "age": 18},
    {"name": "lisi", "age": 19},
    {"name": "wangwu", "age": 17}
]

# user_list.sort()
# 列表的排序, 默认是对列表中的数据进行比大小的, 可以对 数字类型和字符串进行比大小,
# 但是对于字典来说,就不知道该怎么比大小, 此时,我们需要使用 sort 函数中的 key 这个参数, 来指定字典比大小的方法
# key 这个参数, 需要传递一个函数,一般是匿名函数, 字典的排序,其实要指定根据字典的什么 键进行排序, 我们只需要使用
# 匿名函数返回字典的这个键对应的值即可
# 列表.sort(key=lambda x: x['键'])
# 根据年龄排序
# user_list.sort(key=lambda x: x['age'])
user_list.sort(key=lambda x: x['age'], reverse=True)
print(user_list)

# user_list.sort(key=lambda x: x['age'])
# 说明: 匿名函数中的参数是 列表中的数据, 在 sort 函数内部,会调用 key 这个函数(将列表中每个数据作为实参传递给形参),
# 从列表中的获取函数的返回值, 对返回值进行比大小操作(<)


def get_value(x):
    return x['age']


user_list.sort(key=get_value)

print(user_list)
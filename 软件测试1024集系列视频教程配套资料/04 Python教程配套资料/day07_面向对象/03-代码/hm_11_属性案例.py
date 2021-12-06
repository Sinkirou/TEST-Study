class Dog:
    # 定义类属性
    count = 0

    # 定义实例属性, init 方法中
    def __init__(self, name):
        self.name = name   # 实例属性
        # 因为每创建一个对象,就会调用 init 方法, 就将个数加 1 的操作,写在 init 方法中
        Dog.count += 1


# 在类外部
# 打印输出目前创建几个对象
print(Dog.count)  # 0
# 创建一个对象
dog1 = Dog('小花')
# 打印输出目前创建几个对象
print(Dog.count)  # 1
dog2 = Dog   # 不是创建对象, 个数不变的
dog3 = dog1  # 不是创建对象, 个数不变的
print(Dog.count)  # 1

dog4 = Dog('大黄')  # 创建一个对象 , 个数 + 1
print(Dog.count)  # 2
dog5 = Dog('小白')
print(Dog.count)  # 3

# 补充, 可以使用 实例对象.类属性名 来获取类属性的值  (原因, 实例对象属性的查找顺序, 先在实例属性中找,找到直接使用
# 没有找到会去类属性中 找, 找到了可以使用, 没有找到 报错)
print(dog1.count)  # 3
print(dog4.count)  # 3
print(dog5.count)  # 3

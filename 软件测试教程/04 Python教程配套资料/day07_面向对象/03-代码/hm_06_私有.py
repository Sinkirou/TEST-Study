class Person:
    def __init__(self, name, age):
        self.name = name   # 姓名
        # 私有的本质, 是 Python 解释器执行代码,发现属性名或者方法名前有两个_, 会将这个名字重命名
        # 会在这个名字的前边加上 _类名前缀,即 self.__age ===> self._Person__age
        self.__age = age  # 年龄, 将其定义为私有属性, 属性名前加上两个 _

    def __str__(self):  # 在类内部可以访问私有属性的
        return f'名字: {self.name}, 年龄: {self.__age}'

    def set_age(self):
        self.__age +=1


xm = Person('小明', 18)
print(xm)
# 在类外部直接访问 age 属性
# print(xm.__age)  # 会报错, 在类外部不能直接使用私有属性
print(xm.__dict__)
# 直接修改 age 属性
xm.__age = 20  # 这个不是修改私有属性, 是添加了一个公有的属性 __age
print(xm.__dict__)
print(xm)  # 名字: 小明, 年龄: 18
print(xm._Person__age)  # 能用但是不要用  18
xm._Person__age = 19
print(xm)  # 名字: 小明, 年龄: 19

# 补充:
# 对象.__dict__   魔法属性, 可以将对象具有的属性组成字典返回

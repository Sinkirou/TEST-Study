"""
猫类, 属性 name, age , show_info(输出属性信息)
"""


class Cat:
    # 定义添加属性的方法
    def __init__(self, n, age):  # 这个方法是创建对象之后调用
        self.name = n  # 给对象添加 name 属性
        self.age = age   # 给对象添加 age 属性

    # 输出属性信息
    def show_info(self):
        print(f'小猫的名字是: {self.name}, 年龄是: {self.age}')


# 创建对象,不要在自己类缩进中创建
# Cat()  # 创建对象 ,会输出
blue_cat = Cat('蓝猫', 2)

blue = blue_cat
blue.show_info()

# 创建黑猫
black_cat = Cat('黑猫', 3)
black_cat.show_info()

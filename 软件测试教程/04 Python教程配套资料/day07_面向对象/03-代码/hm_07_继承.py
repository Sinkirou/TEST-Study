# 1. 定义一个 动物类, 吃
class Animal:
    def eat(self):
        print('要吃东西')


# 2. 定义一个 狗类, 继承动物类, 吃, 叫
class Dog(Animal):
    def bark(self):
        print('汪汪汪叫....')


# 3. 定义一个 哮天犬类, 继承 狗类
class XTQ(Dog):
    pass


# 创建 动物类的对象
# ani = Animal()
# ani.eat()
# 创建狗类对象
# dog = Dog()
# dog.eat()  # 调用父类中的方法
# dog.bark()   # 调用自己类中方法
# 创建哮天犬类对象
xtq = XTQ()
xtq.bark()  # 调用 父类 Dog 类的方法
xtq.eat()   # 可以调用 父类的父类中的方法


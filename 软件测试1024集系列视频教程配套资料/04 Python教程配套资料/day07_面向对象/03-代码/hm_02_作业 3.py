class Student:
    # 添加属性
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"姓名: {self.name}, 年龄: {self.age} 岁"

    def eat(self):
        print(f'{self.name} 要吃饭')

    def sleep(self):
        print(f'{self.name} 要睡觉')

    def year(self):
        self.age += 1


# 创建对象
xm = Student('小明', 18)
xh = Student('小红', 17)
print(xm)
print(xh)
xm.eat()
xm.sleep()
xm.year()
print(xm)


class Person:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return f"姓名: {self.name}, 体重: {self.weight} kg"

    def run(self):
        print(f'{self.name} 跑步 5 km, 体重减少了')
        # 减体重, 即修改属性
        self.weight -= 0.5

    def eat(self):
        print(f'{self.name} 大餐一顿, 体重增加了')
        # 修改体重
        self.weight += 1


xm = Person('小明', 75.0)
print(xm)
xm.run()
print(xm)
xm.eat()
print(xm)

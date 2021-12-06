"""
需求:小猫爱吃鱼，小猫要喝水, 定义不带属性的类
"""


class Cat:
    # 在缩进中书写 方法
    def eat(self):  # self 会自动出现,暂不管
        print(f'{id(self)}, self')
        print('小猫爱吃鱼...')


# 2. 创建对象
blue_cat = Cat()
print(f'{id(blue_cat)}, blue_cat')
# 3. 通过对象调用类中的方法
blue_cat.eat()  # blue_cat 对象调用 eat 方法, 解释器就会将 blue_cat 对象传给 self
print('_*_' * 30)
# 创建对象
black_cat = Cat()
print(f"{id(black_cat)}, black_cat")
black_cat.eat()  # black_cat 对象调用 eat 方法, 解释器就会将 black_cat 对象传给 self

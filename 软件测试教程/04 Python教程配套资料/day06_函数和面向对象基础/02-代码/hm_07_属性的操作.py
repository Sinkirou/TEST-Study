class Cat:
    # 在缩进中书写 方法
    def eat(self):  # self 会自动出现,暂不管
        print(f'{id(self)}, self')
        print(f'小猫{self.name} {self.age}爱吃鱼...')


# 2. 创建对象
blue_cat = Cat()
print(f'{id(blue_cat)}, blue_cat')
# 给 蓝猫添加 name 属性
blue_cat.name = '蓝猫'
blue_cat.age = 2
# 3. 通过对象调用类中的方法
blue_cat.eat()  # blue_cat 对象调用 eat 方法, 解释器就会将 blue_cat 对象传给 self
print('_*_' * 30)
# # 创建对象
black_cat = Cat()
black_cat.name = '黑猫'
black_cat.age = 3
print(f"{id(black_cat)}, black_cat")
black_cat.eat()  # black_cat 对象调用 eat 方法, 解释器就会将 black_cat 对象传给 self

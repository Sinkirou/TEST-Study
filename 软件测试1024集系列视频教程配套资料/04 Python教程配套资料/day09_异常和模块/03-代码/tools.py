# 定义一个函数 add()  对两个数字进行求和计算
def add(a, b):
    return a + b


def func():
    print('我是 tools 模块中的 func 函数')


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def play(self):
        print(f"{self.name} 在快乐的玩耍")



if __name__ == '__main__':
    # 调用函数
    print('在代码中调用函数')
    print(add(1, 2))
    print(add(10, 20))
    print('tools:', __name__)


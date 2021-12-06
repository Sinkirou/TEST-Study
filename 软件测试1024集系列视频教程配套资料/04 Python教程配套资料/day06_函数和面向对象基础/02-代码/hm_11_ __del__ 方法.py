class Demo:
    def __init__(self, name):
        print('我是 __init__, 我被调用了 ')
        self.name = name

    def __del__(self):
        print(f'{self.name} 没了, 给他处理后事...')


# Demo('a')

a = Demo('a')
b = Demo('b')
del a  # 删除销毁 对象,
print('代码运行结束')

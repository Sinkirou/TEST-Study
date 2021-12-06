# 1. 定义 人类 Person, 方法 work, 输出: 人需要工作
class Person:
    def work(self):
        print('人需要工作')


# 2. 定义 开发工程师类 Coder 继承 Person 类, 方法 work, 输出: 开发的工作是写代码
class Coder(Person):
    def work(self):
        print('开发人员 --> 工作是写代码')


# 3. 定义 测试工程师类 Tester 继承 Person 类, 方法 work, 输出: 测试的工作是 测试项目....
class Tester(Person):
    def work(self):
        print('测试人员 --> 工作是 测试项目....')


class UI(Person):
    def work(self):
        print('ui 工作')


# 4. 定义 公司类 Company, 定义方法 show_work(查看不同岗位的工作), 参数人类对象, 在这个方法中调用 work 方法
class Company:
    def show_work(self, worker):  # worker 参数需要传入一个对象,只要这个对象有 work 方法
        """worker 是 Person 类以及其子类的对象"""
        worker.work()


# 创建 Company 类的对象
c = Company()
# 创建 Coder 类的对象
xw = Coder()
# # 创建 Tester 类对象
xh = Tester()

xb = Person()

c.show_work(xw)   # 开发人员 --> 工作是写代码
c.show_work(xh)   # 测试人员 --> 工作是 测试项目....
c.show_work(xb)  # 人需要工作

xl = UI()
c.show_work(xl)
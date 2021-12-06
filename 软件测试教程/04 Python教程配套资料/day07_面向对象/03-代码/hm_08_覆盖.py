class Dog:
    def bark(self):
        print('汪汪汪叫.....')


class XTQ(Dog):
    # XTQ 类bark 方法不再是汪汪汪叫, 改为 嗷嗷嗷叫
    def bark(self):
        print('嗷嗷嗷叫...')


xtq = XTQ()
xtq.bark()



import random


class Game:
    # 类属性, 游戏的最高分
    top_score = 0

    def __init__(self, name):
        # 定义实例属性 name
        self.name = name

    @staticmethod
    def show_help():
        print('这是游戏的帮助信息')

    @classmethod
    def show_top_score(cls):
        print(f'游戏的最高分为 {cls.top_score}')

    def start_game(self):
        print(f'{self.name} 开始一局游戏, 游戏中 ...,', end='')
        score = random.randint(10, 100)  # 本次游戏的得分
        print(f'本次游戏得分为 {score}')
        if score > Game.top_score:
            # 修改最高分
            Game.top_score = score


xw = Game('小王')
xw.start_game()
xw.show_top_score()
xw.start_game()
xw.show_top_score()
xw.show_help()

e = 1000
f = 1000
print(e is f)
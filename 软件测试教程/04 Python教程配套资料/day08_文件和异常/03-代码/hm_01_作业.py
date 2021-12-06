import random


class Game:
    # 类属性, 游戏的最高分
    top_score = 0
    # 获取最高分玩家的名字
    top_score_player = ''

    def __init__(self, name):
        # 定义实例属性 name
        self.name = name

    def show_help(self):
        print('这是游戏的帮助信息')

    def show_top_score(self):
        print(f'游戏的最高分为: 玩家{Game.top_score_player} 分数: {Game.top_score}')

    def start_game(self):
        print(f'{self.name} 开始一局游戏, 游戏中 ...,', end='')
        score = random.randint(10, 100)  # 本次游戏的得分
        print(f'本次游戏得分为 {score}')
        if score > Game.top_score:
            # 修改最高分
            Game.top_score = score
            # 修改最高分玩家的名字
            Game.top_score_player = self.name


xw = Game('小王')
xw.start_game()
xw.show_top_score()
xh = Game('小红')
xh.start_game()
xh.show_top_score()
xl = Game('小李')
xl.start_game()
xl.show_top_score()
xz = Game('小张')
xz.start_game()
xz.show_top_score()

open()
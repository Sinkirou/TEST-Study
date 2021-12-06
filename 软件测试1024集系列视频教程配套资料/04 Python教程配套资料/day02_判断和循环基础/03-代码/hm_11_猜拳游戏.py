import random

# 1. 自己出拳(石头(1)/剪刀(2)/布(3)) input  (player)
player = int(input('请出拳石头(1)/剪刀(2)/布(3):'))   # 不要忘了类型转换
# 2. 电脑随机出拳 (使用随机数模块(工具)完成)  (computer)
computer = random.randint(1, 3)
# 3. 判断输赢
# 3.1 玩家胜利
if (player == 1 and computer == 2) or (player == 2 and computer == 3) or (player == 3 and computer == 1):
    print('恭喜你获得胜利')
# 3.2 平局  player == computer
elif player == computer:
    print('平局')
# 3.3 玩家输了 else
else:
    print('输了, 不要放弃, 再来一局')

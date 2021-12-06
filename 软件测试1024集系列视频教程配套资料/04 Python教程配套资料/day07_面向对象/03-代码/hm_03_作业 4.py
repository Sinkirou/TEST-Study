class Computer:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def play_movie(self, movie):
        print(f'{self.brand} 播放电影 {movie}')


# 创建对象
mi = Computer('小米', 4999)
mac = Computer('Mac', 16999)
mi.play_movie('葫芦娃')
mac.play_movie('变形金刚')
mi.play_movie('西游记')

# 定义家具类
class HouseItem:
    """家具类"""
    def __init__(self, name, area):
        """添加属性的方法"""
        self.name = name
        self.area = area

    def __str__(self):
        return f'家具名字{self.name}, 占地面积 {self.area} 平米'


class House:
    """房子类"""
    def __init__(self, name, area):
        self.name = name  # 户型
        self.total_area = area  # 总面积
        self.free_area = area   # 剩余面积
        self.item_list = []     # 家具名称列表

    def __str__(self):
        return f"户型: {self.name}, 总面积:{self.total_area}平米, 剩余面积: {self.free_area} 平米, " \
               f"家具名称列表: {self.item_list}"

    def add_item(self, item):  # item  表示的家具的对象
        # 判断房子的剩余面积(self.free_area)和家具的占地面积(item.area)之间的关系
        # self 表示的 房子对象, 缺少一个家具对象使用传参解决
        if self.free_area > item.area:
            # 添加家具, ---> 向列表中添加数据
            self.item_list.append(item.name)
            # 修改剩余面积
            self.free_area -= item.area
            print(f'{item.name} 添加成功')
        else:
            print('剩余面积不足, 换个大房子吧')


# 创建家具对象
bed = HouseItem('席梦思', 4)
chest = HouseItem('衣柜', 2)
table = HouseItem('餐桌', 1.5)
print(bed)
print(chest)
print(table)

# 创建房子对象
house = House('三室一厅', 150)
print(house)
# 添加 床
house.add_item(bed)
print(house)

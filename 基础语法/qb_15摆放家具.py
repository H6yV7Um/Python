class Furniture:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "【%s】 占地面积 %.1f平方米" % (self.name, self.area)


class House:
    def __init__(self, house_type, area):
        # 户型
        self.house_type = house_type

        # 总面积
        self.area = area

        # 剩余面积
        self.free_area = area

        # 家具列表
        self.furniture_list = []

    def __str__(self):
        # python会将()内的内容连接在一起,这样输出内容太长时可以换行
        return ("房子是 【%s】,总面积 %.1f 平米(剩余面积 %.1f 平米),家具列表是 %s" % (self.house_type, self.area,
                                                                 self.free_area, self.furniture_list))

    # 添加家具
    def add_furniture(self, furniture):
        print("要添加的家具是 %s" % furniture)

        # 1、先判断家具面积大小
        if furniture.area > self.free_area:
            print("该家具面积太大 %.1f 平米,放不下！" % furniture.area)
            return

        # 2、添加到家具列表
        self.furniture_list.append(furniture.name)

        # 3、计算房子剩余面积
        self.free_area -= furniture.area


bed = Furniture("床", 4.0)
table = Furniture("桌子", 1.5)
print(bed)
print(table)

my_home = House("两室一厅", 84.00)
print(my_home)
my_home.add_furniture(bed)
print(my_home)
my_home.add_furniture(table)
print(my_home)

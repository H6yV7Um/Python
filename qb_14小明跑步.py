class Person:
    def __init__(self, name, weight):
        # self.属性 = 形参
        self.name = name
        self.weight = weight

    def __str__(self):
        return "我叫 %s,体重 %.1f kg" % (self.name, self.weight)

    def eat(self):
        print("我要吃鸡腿！")
        self.weight += 1

    def run(self):
        print("我要锻炼身体！")
        self.weight -= 0.5


grubby = Person("grubby", 75.0)
print(grubby)
grubby.eat()
print(grubby)
grubby.run()
print(grubby)

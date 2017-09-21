"""
在变量和方法的名称前面加上__代表私有化,不能在类的外部访问
"""


class Girl:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def secret(self):
        print("%s 的年龄是 %d" % (self.name, self.__age))

    def __secret(self):
        print("%s 的年龄是 %d" % (self.name, self.__age))


moon = Girl("moon", 18)
moon.secret()
moon.__secret()

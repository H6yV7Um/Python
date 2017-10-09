"""
面向对象:
"""


class Cat:
    # __init__(python内置方法)用来初始化类,创建对象时自动调用
    def __init__(self, name):
        self.name = name
        print("%s 来了" % self.name)

    # __del__(python内置方法)是在对象从内存中销毁前自动执行(如果希望对象销毁前做些什么可以写在__del__方法里面)
    def __del__(self):
        print("%s 走了" % self.name)

    # __str__(python内置方法)可以自定义print函数输出的对象内容,该方法必须返回一个字符串
    def __str__(self):
        return "我是小猫【%s】" % self.name

    # 自定义方法
    def eat(self):
        # 哪个对象调用该方法，self就是哪个对象的引用
        print("%s 爱吃鱼" % self.name)


cat01 = Cat("Tom")
print(cat01)  # 改造__str__方法后,print不再输出地址值而是__str__方法return的值
cat01.eat()

# del cat01  # 手动删除对象,提前从内存中销毁,然后执行下方代码

print("-" * 30)  # cat01是全局变量,所有代码执行完才会从内存中销毁





# print(cat01)  # 打印对象在内存中地址值(16进制)
# addr = id(cat01)
# print("%d" % addr)  # %d以10进制输出
# print("%x" % addr)  # %x以16进制输出

# cat02 = Cat("Jerry")
# cat02.eat()

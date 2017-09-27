"""
多态:
"""


class Dog(object):
    def __init__(self, name):
        self.name = name

    def bark(self):
        print("我是 %s" % self.name)


class Hsq(Dog):
    def __init__(self, name):
        self.name = name

    def bark(self):
        print("我是 %s" % self.name)


class Person(object):
    def __init__(self, name):
        self.name = name

    def play_to_dog(self, dog):
        print("%s 和 %s 一起玩耍" % (self.name, dog.name))
        dog.bark()


# sky = Dog("sky")
infi = Hsq("infi")

moon = Person("moon")
moon.play_to_dog(infi)

class Test(object):
    instance = None
    flag = False

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = object.__new__(cls)
        return cls.instance

    def __init__(self, name):
        if not Test.flag:
            self.name = name
        Test.flag = True


a = Test("xixi")
print(id(a))
print(a.name)
b = Test("haha")
print(id(b))
print(b.name)

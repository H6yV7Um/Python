"""
单例模式: 不管类创建多少对象,在内存中只有一个实例

python创建对象时会默认调用下面2个方法：
1、__new__: 在内存中分配空间并返回对象引用,然后将引用作为参数传递给__init__方法,一定要返回对象引用,不然__init__方法不会执行
2、__init__: 对传递进来的对象进行初始化,定义实例属性

步骤:
1、定义一个类属性,初始值None
2、重写__new__方法
3、判断类属性,调用父类方法分配空间
4、返回对象引用
"""


class Single(object):

    # 1、记录第一个被创建对象的引用
    instance = None

    # 记录初始化标记
    init_flag = False

    # 2、重写__new__方法
    def __new__(cls, *args, **kwargs):

        # 3、判断类属性,为对象分配空间
        if cls.instance is None:
            cls.instance = super().__new__(cls)

        # 4、返回对象引用
        return cls.instance

    def __init__(self):

        # 1、判断标记
        if Single.init_flag:
            return

        # 2、给对象初始化
        print("init...")

        # 3、修改标记
        Single.init_flag = True


s1 = Single()
print(s1)
s2 = Single()
print(s2)

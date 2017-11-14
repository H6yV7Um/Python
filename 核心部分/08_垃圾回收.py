import gc
import sys

"""
垃圾回收(gc): python中的gc以引用计数为主,分代回收为辅
引用计数: 一旦没有引用,内存直接释放;但是如果出现循环引用的情况,内存是无法使释放的
分代回收: 0代(第1条链子)存放刚刚创建的对象,1代(第2条链子)存放0代清理之后存在的对象,2代(第3条链子)存放多次清理1代后还存在的对象
小整数对象池: [-5,257)范围内的整数对象是python提前创建好的,不管你用不用都在那里,不会被垃圾回收
大整数对象池: 每一个大整数都会创建一个新的对象,销毁对象会被垃圾回收
intern机制: 单个字符/单词也是共用对象,引用计数为0则销毁
"""

print(gc.get_count())
print(gc.get_threshold())

a = 100
print(id(a))  # 1963265584
del a
b = 100
print(id(b))  # 1963265584

c = 12340000
print(id(c))
d = 12340000
print(id(d))

e = "hello python"
f = e
print(sys.getrefcount(e))

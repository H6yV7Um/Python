import time
from timeit import Timer

"""
时间复杂度计算规则: 
基本操作: 只有常数项,O(1)
顺序结构: 加法
循环结构: 乘法
分支结构: 取最大值
时间消耗: O(1) < O(logn) < O(n) < O(nlogn) < O(n2) < O(n3) < O(2n) < O(n!) < O(nn)
大O记法: 处理规模为n的数据所用时间T(n)即是算法复杂度,一般只看最高次项,比如3n^2和10n^2是一个级别,
        复杂度默认指最坏复杂度
数据结构: 静态的描述了数据元素之间的关系
程序 = 数据结构 + 算法
算法是一种解决问题的设计思想,数据结构是算法处理问题的载体
"""
# 如果 a+b+c=N且 a^2+b^2=c^2(a,b,c 为自然数)，如何求出所有a、b、c可能的组合?
start_time = time.time()
for a in range(0, 1001):
    for b in range(0, 1001):
        # for c in range(0, 1001):
        c = 1000 - a - b
        if a + b + c == 1000 and a ** 2 + b ** 2 == c ** 2:
            print("a=%d,b=%d,c=%d" % (a, b, c))
# 算法复杂度: T(n) = n*n*(1+max(0,1))
#                = 2n^2
#                = O(n^2)

end_time = time.time()
print("time:%d" % (end_time - start_time))

"""
timeit模块: 可以测试一段Python程序的运行速度
用法: t = Timer(stmt='pass', setup='pass', timer=<timer function>)
     t.timeit(num)   -- 测试num次代码结果取平均值
     Timer: 测量小段代码执行速度的类;
     stmt参数: 要测试的代码语句(statment);
     setup参数: 运行代码时需要的设置;
     timer参数: 一个定时器函数，与平台有关;
"""
def test01():
    l = []
    for i in range(1000):
        l = l + [i]

def test02():
    l = []
    for i in range(1000):
        l.append(i)

def test03():
    l = [i for i in range(1000)]

def test04():
    l = []
    for i in range(1000):
        l.extend([i])

t1 = Timer("test01()", "from __main__ import test01")
print("+:", t1.timeit(10000))
t2 = Timer("test02()", "from __main__ import test02")
print("append", t2.timeit(10000))
t3 = Timer("test03()", "from __main__ import test03")
print("generator", t3.timeit(10000))
t4 = Timer("test04()", "from __main__ import test04")
print("extend", t4.timeit(10000))



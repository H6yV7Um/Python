from threading import Thread, Lock
import time

"""
1、threading模块的Thread类可以创建线程
"""


# 自定义类继承Thread类
class MyThread(Thread):
    # 重写run方法
    def run(self):
        # 功能代码块
        for i in range(3):
            print("---我是线程%s---%d" % (self.name, i))
            time.sleep(1)


# if __name__ == "__main__":
#     for i in range(3):
#         t = MyThread()
#         t.start()


"""
2、threading模块的Lock类可以给线程上锁
同步: 当多个线程同时修改某一共享变量时,需要进行同步控制(加锁),保证线程安全
创建锁: lock = Lock()
上锁: lock.acquire([block]) -- block = True/False 表示阻塞/非阻塞,默认为True
解锁: lock.release()

锁的好处: 保证数据安全
锁的坏处: 阻止了多线程的并发执行,上锁的代码实际上是单线程执行完的,效率低
         由于可以存在多个锁,不同线程持有不同锁并试图获取对方持有的锁时会导致死锁 
"""
num = 0

def test01():
    global num
    for i in range(1000000):
        # 获取锁: True表示阻塞,即如果这个锁已经锁上了,那么这个线程会卡在这里一直等到解锁为止
        #        False表示非阻塞,即不管本次上锁是否成功,线程都不会卡在这里,而是继续往下走
        flag = lock.acquire(True)
        if flag:
            num += 1
            # 操作完共享数据记得释放锁
            lock.release()
    print("test01---the num is %d" % num)

def test02():
    global num
    for i in range(1000000):
        flag = lock.acquire(True)
        if flag:
            num += 1
            lock.release()
    print("test02---the num is %d" % num)

# 创建一个锁对象,此时是未锁上的
lock = Lock()

t1 = Thread(target=test01)
t1.start()

t2 = Thread(target=test02)
t2.start()


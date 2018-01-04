from threading import Thread
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

if __name__ == "__main__":
    for i in range(3):
        t = MyThread()
        t.start()




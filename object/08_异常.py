# coding=utf-8
"""
try:
    # 尝试执行的代码
    num = int(input("输入整数:"))
    result = 1 / num
    print(result)
except ZeroDivisionError:
    # 捕获已知异常
    print("已知错误: division by zero")
except Exception as result:
    # 捕获未知异常
    print("未知错误: %s" % result)
else:
    # 没有异常才会执行的代码
    print("代码ok没有问题！")
finally:
    # 最终一定会执行的代码
    print("=" * 50)
"""

# 异常传递性: 比如一个函数代码块里可能有异常,可以在调用这个函数时再处理异常
class Test(object):
    def __init__(self, switch):
        self.switch = switch

    def cal(self, a, b):
        try:
            return a / b
        except Exception as result:
            if self.switch:
                # 将异常打印在控制台
                print("捕获到的异常：%s" % result)
            else:
                # 抛出异常给方法调用者
                raise

t = Test(True)
t.cal(10, 0)
t.switch = False
t.cal(10, 0)

"""
with语句: 只适用于以下支持上下文管理协议(context management protocol)的对象
file
decimal.Context
thread.LockType
threading.Lock
threading.RLock
threading.Condition
threading.Semaphore
threading.BoundedSemaphore
with语句会执行上下文表达式(context_expr)获得上下文管理器,上下文管理器提供一个上下文对象,处理with语句块中的细节:
一旦获得上下文对象,就会调用它的__enter__()方法,将完成with语句块执行前的所有准备工作,如果with语句后面跟了as语句,则用__enter__()方法的返回值来赋值;
当with语句块结束时,无论正常结束还是异常,都会调用上下文对象的__exit__()方法,__exit__()方法有3个参数,如果with语句正常结束,三个参数都是None
如果发生异常,三个参数的值分别等于调用sys.exc_info()函数返回的三个值:类型(异常类)、值(异常实例)和跟踪记录(traceback),相应的跟踪记录对象;
因为上下文管理器主要作用于共享资源,__enter__()和__exit__()方法干的基本是需要分配和释放资源的低层次工作,
比如: 数据库连接、锁分配、信号量加/减、状态管理、文件打开/关闭、异常处理等;
"""
from contextlib import contextmanager
import sys

class A(object):
    """
    给自定义类添加这两个方法配合with语句使用
    """
    def __enter__(self):
        print("__enter__() is called!")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__exit__() is called!")

with A() as a:
    print("=" * 30)
# 结果:
# __enter__() is called!
# ==============================
# __exit__() is called!

"""
contextlib模块实现上下文自动管理
"""
# 锁机制
@contextmanager
def locked(lock):
    lock.acquired()
    try:
        yield
    finally:
        lock.release()

# 数据库操作
@contextmanager
def transaction(db):
    db.begin()

    try:
        yield db
    except:
        db.rollback()
        raise
    else:
        db.commit()

# 标准输出重定向
@contextmanager
def stdout_redirect(new_stdout):
    old_stdout = sys.stdout
    sys.stdout = new_stdout
    try:
        yield
    finally:
        sys.stdout = old_stdout

with open("file.txt", "w") as f:
    with stdout_redirect(f):
        print("hello world")

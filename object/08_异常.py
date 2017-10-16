# try:
#     # 尝试执行的代码
#     num = int(input("输入整数:"))
#     result = 1 / num
#     print(result)
# except ZeroDivisionError:
#     # 捕获已知异常
#     print("已知错误: division by zero")
# except Exception as result:
#     # 捕获未知异常
#     print("未知错误: %s" % result)
# else:
#     # 没有异常才会执行的代码
#     print("代码ok没有问题！")
# finally:
#     # 最终一定会执行的代码
#     print("=" * 50)

"""
异常传递性: 比如一个函数代码块里可能有异常,可以在调用这个函数时再处理异常
"""


def input_pwd():

    # 1、输入密码
    pwd = input("输入密码:")

    # 2、判断密码长度
    if len(pwd) == 6:
        return pwd

    # 3、创建异常对象,提示错误信息
    ex = Exception("长度有误！")

    # 4、主动抛出异常
    raise ex


# 调用函数的时候再处理异常,而不是写在函数内部
try:
    print(input_pwd())
# 此处的Exception就是函数内部创建的异常对象
except Exception as result:
    print(result)

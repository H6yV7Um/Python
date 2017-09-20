"""
变量: 全局变量和局部变量
函数: 实现特定功能的方法
"""

gl_num = 10  # 全局变量命名时加个前缀以示区分,防止和局部变量重名


def test01():
    # global关键字表示全局变量(此时如果对变量重新赋值的话是修改全局变量)
    # global num

    # 给num变量重新赋值(只在当前函数有效)
    num = 20
    print("数字num的值是%d" % num)


def test02():
    print("数字num的值是%d" % gl_num)


test01()
test02()

# 交换两个变量值
a = 100
b = 200

# 方式一(各语言通用)
# c = b
# b = a
# a = c
# print(a, b)

# 方式二(python特有)
# a, b = (b, a)
a, b = b, a  # 当返回结果是元组时,()可以省略
print(a)
print(b)

"""
函数中的变量在内存中的理解(重点)
"""

# 函数内部赋值操作
gl_num = 55


def test03(num):
    print("函数内部代码:")
    num = 99  # 函数内部的赋值操作不会改变全局变量的值(画内存图)
    print(num)


test03(gl_num)
print(gl_num)

# 函数内部方法操作
gl_list = [1, 2, 3]


def test04(num_list):
    print("函数内部代码:")
    num_list.append(5)  # 函数内部的方法操作会改变全局变量的值(画内存图)
    print(num_list)


test04(gl_list)
print(gl_list)

# 列表的 += 相当于调用extend()方法
gl_num = 10
gl_list = [11, 22, 33]


def test05(num, num_list):
    print("函数内部代码:")
    num += num  # 等同于 num = num + num

    # num_list = num_list + num_list
    num_list += num_list  # 等同于num_list.extend(num_list)

    print(num, num_list)


test05(gl_num, gl_list)
print(gl_num, gl_list)

"""
缺省参数: 当某个参数多数情况下都是固定值时就可以设置成缺省参数,比如列表的sort方法(默认升序,指定reverse=Ture才是降序 )
注意事项: 缺省参数要放在参数列表的末尾
"""


def test06(name, gender=True):  # gender默认值True,调用函数时可以不写;

    gender_value = "男生"

    if not gender:
        gender_value = "女生"

    print("%s 是 %s" % (name, gender_value))


test06("grubby")
test06("moon", gender=False)

"""
多值参数: 函数要接受的参数个数或类型不确定时使用
         *args可以接受元组
         **kwargs可以接受字典
"""


def test07(num, *args, **kwargs):
    print(num)
    print(args)
    print(kwargs)


test07(1, 2, 3, 4, name="grubby", age=18)


# 累加案例
def test08(*args):
    result = 0
    for n in args:
        result += n
    print(result)


test08(1, 2, 3)

# 元组和字典的拆包(简化变量传递)
gl_tuple = (1, 2, 3)
gl_dict = {"name": "grubby", "age": 19}


def test09(*args, **kwargs):
    print(args)
    print(kwargs)


test09(*gl_tuple, **gl_dict)  # 要在元组和字典前面加上*/**标识,不然都会当成第一个参数传入(注意看参数高亮提示)

"""
递归: 函数调用函数本身
"""


# 累加案例
def sum_num(n):
    if n == 1:
        return 1
    else:
        return sum_num(n - 1) + n


result = sum_num(100)
print(result)


# 菲波那切数列
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


result = fibonacci(10)
print(result)

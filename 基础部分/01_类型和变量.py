"""
5大数据类型:
不可变类型: 数字(int float bool)、字符串、元组
可变类型: 列表、字典(key必须是不可变类型,value任意;因为python设置键值对时会先对key做hash处理,而hash()函数只能接受不可变类型)
   注意: 变量的CUD操作改变的是list/dict的内容,而list/dict在内存中引用的地址值并不变,重新赋值才会改变变量在内存中引用的地址值
"""

name = "小明"
age = 119
sex = True
height = 1.80
weight = 65.0
print(name)

print(type(name))

# 运算(True=1;False=0)
print(age + sex)

"""
变量: 全局变量和局部变量
"""

# 全局变量命名时加个前缀以示区分,防止和局部变量重名
gl_num = 10
gl_list = [11, 22, 33]


def test01():
    num = 20
    print("数字num的值是%d" % num)


def test02():
    print("数字num的值是%d" % gl_num)


test01()
test02()

"""
变量在内存中地址值的理解(重点)
"""


# 函数内部赋值操作
def test03(num, num_list):
    print("函数内部代码:")
    num = 99  # 函数内部的赋值操作不会改变全局变量的值,不管数据是不是可变类型(画内存图)
    num_list = [4, 5, 6]
    print(num)
    print(num_list)


test03(gl_num, gl_list)
print(gl_num)
print(gl_list)


# 函数内部方法操作
def test04(num_list):
    print("函数内部代码:")
    num_list.append(5)  # 函数内部的方法操作会改变可变类型的全局变量的值(画内存图)
    print(num_list)


test04(gl_list)
print(gl_list)


# 列表的 += 相当于调用extend()方法
def test05(num, num_list):
    print("函数内部代码:")
    num += num  # 不可变类型:等同于 num = num + num

    # num_list = num_list + num_list
    num_list += num_list  # 可变类型:等同于num_list.extend(num_list)

    print(num, num_list)


test05(gl_num, gl_list)
print(gl_num, gl_list)

"""
is: 比较内存地址(是否引用同一个对象),是身份运算符(is/is not)
==: 比较内容
"""

a = [1, 2, 3]
b = [1, 2, 3]
c = a
print(a is b)  # false
print(a == b)  # true
print(a is c)  # true
print(a == c)  # true

"""
交换两个变量值
"""
a = 100
b = 200

# 方式一
# c = b
# b = a
# a = c
# print(a, b)

# 方式二
a = a + b
b = a - b
a = a - b

# 方式三(python特有)
# a, b = (b, a)
a, b = b, a  # 当返回结果是元组时,()可以省略
print(a)
print(b)

print("=" * 50)

"""
LEGB规则: python使用LEGB的顺序来查找符号对应的对象
locals: 局部变量
enclosing: 外部嵌套函数(闭包中常见)
globals: 全局变量
builtins: python类建的(自带的),与之对应的是像os、random这些要导入的模块
"""
num = 100
def test1():
    # num = 200
    def test2():
        # num = 300
        print(num)
    return test2

ret = test1()
ret()

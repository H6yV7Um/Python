"""
5大数据类型:
不可变类型: 数字(int float bool)、字符串、元组
可变类型: 列表、字典(key必须是不可变类型,value任意;因为python设置键值对时会先对key做hash处理,而hash()函数只能接受不可变类型)
   注意: 变量的CUD操作改变的是list/dict的内容,而list/dict在内存中引用的地址值并不变,重新赋值才会改变变量在内存中引用的地址值

type()函数: 可以查看变量类型
id()函数: 可以查看变量在内存中的地址值
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


# coding=utf-8
"""
程序开发三大流程:
1、顺序: 从上往下按顺序执行
2、分支(if): 根据条件判断,决定执行代码的分支
3、循环(while): 让特定代码重复执行

break: 跳出当前整个循环
continue: 跳出本次循环继续下次循环

print函数默认是换行的,在结尾添加end=""可以不换行接着输出
转义字符: \t制表符 \n换行符
"""

# i = 0
# while i <= 3:
#     print("hello python")
#     i += 1
# print(i)

# 求和
# i = 0
# result = 0
# while i <= 100:
#     if i % 2 != 0:
#         result += i
#     # result += i
#     i += 1
# print(result)

# break演示
# i = 0
# while i < 5:
#     if i == 3:
#         break
#     print(i)
#     i += 1
# print("over")

# continue演示
# i = 0
# while i < 5:
#     if i == 3:
#         # 注意:使用continue关键字之前要先对计数器+1,不然会死循环
#         i += 1
#         continue
#     print(i)
#     i += 1
# print("over")

# print函数默认是换行的,在结尾添加end=""可以不换行
# print("*", end="")
# print("*")

# 演示循环嵌套
# *
# **
# ***
# ****
# *****
# row = 1
# while row <= 5:
#     col = 1
#     while col <= row:
#         print("*", end="")
#         col += 1
#     print("")
#     row += 1

# 打印99乘法表
row = 1
while row <= 9:
    col = 1
    while col <= row:
        print("%d * %d = %d" % (col, row, row * col), end="\t")
        col += 1
    print("")  # 换行
    row += 1

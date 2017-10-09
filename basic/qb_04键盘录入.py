"""
input(""):键盘录入只能输入字符串,数字类型要用int,float等函数转换
"""

# price_str = input("请输入单价:")
# weight_str = input("请输入重量:")
# # 类型转换
# price = float(price_str)
# weight = int(weight_str)
# # 乘法运算(字符串之间是不能做乘法运算的,要转换成数字类型)
# money = price * weight
# # 输出结果
# print(money)


# 改进版
price = float(input("请输入单价:"))
weight = int(input("请输入重量:"))
money = price * weight
print(money)

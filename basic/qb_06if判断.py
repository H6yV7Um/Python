"""
if/else语句: 条件判断分支是一个独立代码块
elif: 有多次条件判断
if嵌套: 有多层条件判断

逻辑运算符: and, or, not

random: 随机数
"""

import random

# if/else演示
# age = int(input("请输入年龄:"))
# if age >= 18:
#     print("来happy吧")
#     print("哈哈")
# else:
#     print("写作业去")
#     print("嘻嘻")
# print("这句代码会执行吗")

# not演示
# is_employee = True
# if not is_employee:
#     print("非本司员工不得入内")

# elif演示
# num = int(input("输入数字:"))
# if num == 1:
#     print("今天是星期一")
# elif num == 2:
#     print("今天是星期二")
# elif num == 3:
#     print("今天是星期三")
# elif num == 4:
#     print("今天是星期四")
# elif num == 5:
#     print("今天是星期五")
# elif num == 6:
#     print("今天是星期六")
# elif num == 7:
#     print("今天是星期日")
# else:
#     print("输入有误")

# if嵌套演示
# has_ticket = True
# knife_length = 25
# if has_ticket:
#     print("您已买票,请过安检")
#     if knife_length > 20:
#         print("刀具长度 %d 公分超出限制不允许上车" % knife_length)
#     else:
#         print("刀具长度ok可以上车")
# else:
#     print("大哥请先去买票")

# 练习1
computer = random.randint(1, 3)
player = int(input("请输入数字,剪刀(1)/石头(2)/布(3):"))
print("电脑出的是 %d 玩家出的是 %d" % (computer, player))
if (computer == 1 and player == 2) \
        or (computer == 2 and player == 3) \
        or (computer == 3 and player == 1):
    print("玩家赢")
elif computer == player:
    print("平局")
else:
    print("电脑赢")

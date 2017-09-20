"""
字符串：
"""

str1 = "hello python hello java"

# 1、遍历循环字符串
print(str1[8])
for c in str1:
    print(c, end="")
print("")

# 2、统计字符串长度
print(len(str1))  # len(): 计算长度

# 3、统计小字符串出现次数
print(str1.count("he"))  # count(): 统计次数

# 4、子字符串出现位置
print(str1.index("py"))  # index(): 求索引
print(str1.find("abc"))  # find(): 与index类似,但是子字符串不存在的话不会报错,而是返回-1

# 5、判断操作
print(str1.isspace())  # isspace(): 判断空白字符(包括空格、\t、\r、\n等)
print(str1.isdecimal())  # isdecimal(): 判断是否是数字
print(str1.startswith("he"))  # startswith(): 开头
print(str1.endswith("va"))  # endswith(): 结尾

# 6、替换操作
print(str1.replace("java", "php"))
print(str1)  # 注意: replace()操作会返回新的字符串结果,而不会改变原来的字符串

# 7、文本对齐
poem = ["\t\n登鹳雀楼",
        "王之涣",
        "白日依山尽",
        "黄河入海流\t\n",
        "欲穷千里目",
        "更上一层楼"]
for p in poem:                                  # strip(): 去除空白字符
    print("|%s|" % p.strip().center(10, " "))   # center(): 居中对齐;ljust(): 靠左对齐;rjust(): 靠右对齐

# 8、切割和合并
poem_str = "登颧雀楼 \t 白日依山尽\n 呵呵呵\t 王之涣\r"
print(poem_str)
poem_list = poem_str.split()  # split(): 将字符串切割成列表,不带参数默认按一切空白字符切割
print(poem_list)
poem_str1 = "".join(poem_list)  # join(): 将列表合并成字符串
print(poem_str1)

# 9.切片(index包左不包右,字符串、元组、列表都可以用)
num_str = "0123456789"
print(num_str[2:6])   # 截取2~5位置
print(num_str[2:])    # 截取2~末尾
print(num_str[0:6])   # 截取0~5位置
print(num_str[:])     # 截取 开头~末尾
print(num_str[::2])   # 从0位置每隔一个取一个(步长=2)
print(num_str[1::2])  # 从1位置每隔一个取一个(步长=2)
print(num_str[2:-1])  # 截取从2~末尾-1
print(num_str[-2:])   # 截取末尾2个字符
print(num_str[::-1])  # 字符串逆序



"""
文件读写: 一个函数(open),三个方法(read、write、close)
open: 默认只读,w只写(有内容就覆盖),a追加
read: 一次读取所有内容,执行完指针会移动到文件末尾
readline: 一次读取一行,执行完指针会移到下一行
"""

# 1、打开文件
file1 = open("E://aaa.txt")
file2 = open("E://bbb.txt", "w")

# 2、读写文件

# text = file1.read()
# file2.write(text)

while True:

    # 按行读取
    text = file1.readline()

    # 判断是否到末尾
    if not text:
        break

    # 写入新文件
    file2.write(text)

# 3、关闭文件
file1.close()
file2.close()

"""
文件读写: 一个函数(open),三个方法(read、write、close)
open(): 默认r只读,w只写(有内容就覆盖),a追加;操作图片、视频等二进制文件: rb,wb,ab
read(size): 不写size一次读取所有行,执行完指针会移动到文件末尾
readline(): 每次读取一行,返回str,执行完指针会移到下一行
readlines(): 一次读取所有行,返回list,每行都是一个元素
tell(): 获取当前文件位置
seek(offset, from): 调整当前文件位置
    offset: 偏移量
    from: 方向 0表示文件开头 1表示当前位置 2表示文件结尾(python3目前只能写0！)
"""

import os

"""
文件读写
"""

# 1、打开文件
file1 = open("E://aaa.txt", encoding='utf-8')
file2 = open("E://bbb.txt", "w")

# 2、读写文件
while True:

    # 按行读取
    # text = file1.readline()
    text = file1.readlines()
    print(type(text))

    # 判断是否到末尾
    if not text:
        break

    # 写入新文件
    # file2.write(text)
    for t in text:
        file2.write(t)

# 3、关闭文件
file1.close()
file2.close()

"""
文件定位
"""

file = open("E://aaa.txt", encoding='utf-8')
str1 = file.read(5)
print("读取的字符串是 %s" % str1)
position = file.tell()
print("当前文件位置是 %s" % position)
file.seek(3, 0)
str2 = file.read()
print("读取的字符串是 %s" % str2)
file.close()

"""
文件相关操作: 需要导入python的os模块
os.rename(path1, path2): 重命名
os.remove(): 刪除文件
os.mkdir(): 创建文件夹
os.getcwd(): 获取当前目录
os.listdir(): 遍历指定目录下所有文件(夹),返回list列表
os.rmdir(): 删除文件夹
os.path.isfile(): 判断是否是文件
os.path.isdir(): 判断是否是文件夹
os.path.getsize(filename): 获取文件大小,求文件夹大小的话需要递归遍历所有文件
"""

# os.rename("E://bbb.txt", "E://hehe.txt")
# os.remove("E://hehe.txt")
# os.mkdir("E://test")
# os.getcwd()
# list = os.listdir("E://")
# print(list)
# os.rmdir("E://test")


# 批量修改文件名
# dir_name = "E://test/"
# file_list = os.listdir(dir_name)
# for file in file_list:
#     os.rename(dir_name + file, dir_name + 'python-' + file)

# 删除空文件
dir_name = "D://"
file_list = os.listdir(dir_name)
print(file_list)
for file in file_list:
    print(file)
    if os.path.getsize(dir_name + file) == 0:
        os.remove(dir_name + file)

print(os.path.getsize("E://aaa.txt"))


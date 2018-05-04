# coding=utf-8
"""
文件读写: 一个函数(open),三个方法(read、write、close)
open(): 默认r只读,w只写(有内容就覆盖),a追加,r+可读可写;操作图片、视频等二进制文件: rb,wb,ab
read(size): 不写size就一次读取所有行,返回str,执行完指针会移动到文件末尾
readline(): 每次读取一行,返回str,执行完指针会移到下一行,包括 "\n" 字符
readlines(): 一次读取所有行,返回list,每行都是一个元素
tell(): 获取当前文件位置
seek(offset, from): 调整当前文件位置
    offset: 偏移量(注意：utf-8格式中文占3个字节，gbk格式中文占2个字节)
    from: 方向 0表示文件开头 1表示当前位置 2表示文件结尾(python3目前只能写0！)

文件操作: 导入os模块
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

import os

# 文件读写
def file01():
    # 1、打开文件
    file1 = open("E://aaa.txt", encoding='utf-8')
    file2 = open("E://bbb.txt", "w")
    # 2、读写文件
    while True:
        text = file1.readlines()
        print(type(text))
        if not text:
            break
        for t in text:
            file2.write(t)
    # 3、关闭文件
    file1.close()
    file2.close()

# 文件定位
def file02():
    file = open("C://Users/chenq/Documents/aaa.txt", encoding='utf-8')
    # str1 = file.read(5)
    # print(str1)
    # position = file.tell()
    # print(position)
    #
    #
    # file.seek(3, 0)
    # str2 = file.read()
    # print(str2)
    # file.close()
    res = file.readline()
    print(res)
    pos = file.tell()
    print(pos)

# 递归文件夹操作指定后缀名的文件
dir_name = "D://学习资料/python数据分析与机器学习实战/python数据分析与机器学习实战/"
def digui(path, suffix):
    list = os.listdir(path)
    for file in list:
        if os.path.isfile(path + file):
            if file.endswith(suffix):
                file_new = file.replace("龙天论坛", "")
                os.rename(path + file, path + file_new)
        else:
            digui(path + file + "/", suffix)

# 递归文件夹删除小于200k的文件
def digui02(path):
    list = os.listdir(path)
    for file in list:
        if os.path.isfile(path+file):
            if os.path.getsize(path+file) < 1024*200:
                os.remove(path+file)
        else:
            digui02(path+file+"/")


if __name__ == "__main__":
    file02()
    # digui(dir_name, ".flv")
    # digui02(dir_name)

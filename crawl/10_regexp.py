"""
pattern = re.compile("")
pattern.match(): 从起始位置往后查找,返回第一个符合的字符串
pattern.search(): 从任意位置往后查找,返回第一个符合的字符串
pattern.findall(): 所有的全部匹配,返回列表
pattern.split(): 分割字符串,返回列表
pattern.sub(): 替换,返回字符串
re.I表示忽略大小写;re.S表示全文匹配而不是只匹配当前这一行
"""

import re

# match()
pattern = re.compile(r"\d+")
m = pattern.match("aaa123bbb456")
print(m)  # None
m = pattern.match("aaa123bbb456", 2, 5)
print(m)  # None
m = pattern.match("aaa123bbb456", 3, 5)
print(m)  # <_sre.SRE_Match object; span=(3, 5), match='12'>
print(m.group())  # 12

pattern = re.compile(r"([a-z]+) ([a-z]+)", re.I)  # re.I表示忽略大小写;re.S表示全文匹配
m = pattern.match("Hello World Hello Python")
# group()方法返回符合规则的组,不写默认0
print(m.group(0))  # Hello World
print(m.group(1))  # Hello
print(m.group(2))  # World
# print(m.group(3))  # IndexError: no such group

# span()方法返回符合规则的第n个串的索引区间
print(m.span())  # (0, 11)
print(m.span(1))  # (0, 5)
print(m.span(2))  # (6, 11)

# search()
pattern = re.compile(r"\d+")
s = pattern.search("aaa123bbb456")
print(s.group())  # 123
s = pattern.search("aaa123bbb456", 2, 5)
print(s.group())  # 12
s = pattern.search("aaa123bbb456", 3, 5)
print(s.group())  # 12

# findall()
pattern = re.compile(r"\d+")
f = pattern.findall("abc 123 def 456")
# findall()返回的是列表,不需要调用group()
print(f)  # ['123', '456']
pattern = re.compile(r"\d*")  # *表示贪婪模式: 尽可能获取多的
f = pattern.findall("abc 123 def 456")
print(f)  # ['', '', '', '', '123', '', '', '', '', '', '456', '']
pattern = re.compile(r"\d?")  # ?表示非贪婪模式: 尽可能获取少的
f = pattern.findall("abc 123 def 456")
print(f)  # ['', '', '', '', '1', '2', '3', '', '', '', '', '', '4', '5', '6', '']

# split()
pattern = re.compile("[\s\d\\\;]+")
s = pattern.split("abc12 de;34\fg")
print(s)  # ['abc', 'de', 'g']

# sub()
pattern = re.compile("\d+")
str = "abc123def"
s = pattern.sub("emmm", str)
print(s)  # abcemmmdef
pattern = re.compile(r"(\w+)(\w+)")
str = "hello python"
f = pattern.findall(str)
print(f)  # [('hell', 'o'), ('pytho', 'n')]
s = pattern.sub("java", str)
print(s)  # java java

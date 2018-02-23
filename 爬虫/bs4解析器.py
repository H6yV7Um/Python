"""
Beautiful Soup: 也是一个HTML/XML的解析器
lxml是局部遍历,而Beautiful Soup基于HTML DOM,会载入整个文档,解析整个DOM树,因此时间和内存开销大很多,所以性能要低于lxml
BeautifulSoup用来解析HTML比较简单,API非常人性化,支持CSS选择器、Python标准库中的HTML解析器,也支持lxml的XML解析器
抓取工具 	  运行速度 	使用难度
regexp 	    最快 	  困难
BS4 	     慢 	     最简单
lxml 	     快 	     简单
"""

from bs4 import BeautifulSoup


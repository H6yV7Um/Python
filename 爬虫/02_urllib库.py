"""
urllib在python3中被改为urllib.parse
urllib2在python3中被改为urllib.request

1、urllib.parse模块
urlencode(): 编码   --将{key:value}字典转换成"key=value"字符串,拼接成能被web服务器接受的url
unquote(): 解码

2、urllib.request模块
request方法:
Request(): 构造请求对象,主要有3个参数: url,data(区分get/post请求): 默认为空;headers(http报头的键值对): 默认为空;
urlopen(): 发送请求                         
add_header(): 添加/修改一个HTTP报头 
get_header(): 获取一个已有的HTTP报头,注意第一个字母大写,后面全小写

response方法:
read(): 读取服务器返回文件的内容
info(): 返回服务器响应的HTTP报头
getcode(): 返回HTTP请求的响应码
geturl(): 返回返回实际数据的url,防止重定向问题
"""

import urllib.request
import urllib.error
import random

# 待爬取url
url = "http://www.baidu.com/"

# 不同浏览器在发送请求的时候，会有不同的User-Agent头
# urllib2默认的User-Agent头为：Python-urllib/x.y,需要伪装成浏览器
# HTTP报头
ua_header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36"
}

# User-Agent列表
ua_list = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/5.0 (Windows NT 6.1; rv2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
    "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11"
]

# 随机选一个(针对反爬虫)
user_agent = random.choice(ua_list)

# 通过request()方法构造一个请求对象
# request = urllib.request.Request(url) -- 此时User-Agent: Python-urllib/3.5
request = urllib.request.Request(url)

# 通过add_header()方法添加/修改一个HTTP报头
request.add_header("User-Agent", user_agent)

# 通过urlopen()方法发送请求,并返回服务器响应内容
response = urllib.request.urlopen(request)

# 输出服务器相应内容
print(response.read().decode("utf-8"))

# 通过get_header()方法获取一个已有的HTTP报头,注意第一个字母大写,后面全小写
print(request.get_header("User-agent"))

# 输出HTTP响应码,成功返回200，4服务器页面出错，5服务器问题
print(response.getcode())

# 输出返回实际数据的url,防止重定向问题
print(response.geturl())

# 输出服务器相应的HTTP报头
print(response.info)

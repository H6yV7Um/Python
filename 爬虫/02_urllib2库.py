import urllib.request

"""
urllib2是Python2.7自带的模块(不需要下载，导入即可使用)
urllib2官方文档：https://docs.python.org/2/library/urllib2.html
urllib2源码：https://hg.python.org/cpython/file/2.7/Lib/urllib2.py
urllib2在python3.x 中被改为urllib.request
"""

# 待爬取url
url = "http://www.baidu.com/"

# 不同浏览器在发送请求的时候，会有不同的User-Agent头
# urllib2默认的User-Agent头为：Python-urllib/x.y,需要伪装成浏览器
# HTTP报头
ua_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36"
}

# 通过request()方法构造一个请求对象
# request()方法主要有3个参数: url,data(get/post请求),headers(http报头的键值对)
request = urllib.request.Request(url, headers=ua_headers)

# 通过urlopen()方法发送请求,并返回服务器响应内容
response = urllib.request.urlopen(request)

# 输出服务器相应内容
#print(response.read())

# 输出HTTP响应码,成功返回200，4服务器页面出错，5服务器问题
print(response.getcode())

# 输出返回实际数据的url,防止重定向问题
print(response.geturl())

# 输出服务器相应的HTTP报头
print(response.info)

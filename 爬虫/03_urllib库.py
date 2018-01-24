import urllib.request
import urllib.parse

"""
urllib.parse模块的urlencode()方法可以将字典键值对按url编码转换,从而能被web服务器接收
urlencode(): 编码   -- 将key:value键值对转换成"key=value"字符串
unquote(): 解码
"""

url = "http://www.baidu.com/s"
keyword = input("请输入要搜索的关键字: ")
wd = {"wd": keyword}
wd1 = urllib.parse.urlencode(wd)
# wd2 = urllib.parse.unquote(wd1)
print(wd1)

ua_header = {
    "User-Agent": "Mozilla..."
}

fullurl = url + "?" + wd1
print(fullurl)

request = urllib.request.Request(fullurl, headers=ua_header)

response = urllib.request.urlopen(request)

print(response.read())
print(response.info())
print(response.getcode())
print(response.geturl())
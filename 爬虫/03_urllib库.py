import urllib.request
import urllib.parse

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
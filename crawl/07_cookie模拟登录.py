"""
cookie: 网站服务器为了辨别用户身份和进行Session跟踪而储存在浏览器上的文本文件,cookie可以保持登录信息到用户下次与服务器的会话
Python处理Cookie,一般是通过http.cookiejar模块和urllib.request模块的HTTPCookieProcessor处理器类一起使用
http.cookiejar模块: 存储cookie对象
HTTPCookieProcessor处理器: 处理cookie对象,并构建handler对象
"""

import http.cookiejar
import urllib.request

"""
1、访问网站获取cookie并输出在控制台
"""
# 创建cookieJar对象用来保存cookie
cookieJar = http.cookiejar.CookieJar()
# 创建cookie处理器对象
cookie_handler = urllib.request.HTTPCookieProcessor(cookieJar)
# 创建opener
opener = urllib.request.build_opener(cookie_handler)
# 以get方式访问页面,会自动将cookie保存到cookieJar
res1 = opener.open("http://www.baidu.com")
# 输出页面
#print(response.read().decode("utf-8"))
# 从cookieJar获取cookie
cookieStr = ""
for item in cookieJar:
    cookieStr = cookieStr + item.name + "=" + item.value + ";"
# 打印cookie
print(cookieStr)

"""
2、访问网站获取cookie并保存到本地
"""
# 本地文件路径
filename = "C://users/qmtv/cookie.txt"
# 创建cookieJar对象(用MozillaCookieJar,有save()实现)
cookieJar = http.cookiejar.MozillaCookieJar(filename)
# 创建cookie处理器对象
cookie_handler = urllib.request.HTTPCookieProcessor(cookieJar)
# 创建opener
opener = urllib.request.build_opener(cookie_handler)
# 访问页面,会自动将cookie保存到cookieJar
res2 = opener.open("http://www.baidu.com")
# 保存cookie到本地
cookieJar.save()

"""
3、从文件获取cookie,作为请求的一部分访问页面
"""
# 创建cookieJar对象(用MozillaCookieJar,有load()实现)
cookieJar = http.cookiejar.MozillaCookieJar()
# 从文件中读取cookie内容
cookieJar.load("C://users/qmtv/cookie.txt")
# 创建cookie处理器对象
cookie_handler = urllib.request.HTTPCookieProcessor(cookieJar)
# 创建opener
opener = urllib.request.build_opener(cookie_handler)
# 访问页面
res3 = opener.open("http://www.baidu.com")
# 输出
print(res3.read().decode("utf-8", "ignore"))





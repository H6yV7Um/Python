"""
http请求主要分为get和post两种:
get是从服务器上获取数据,post是向服务器传送数据
get请求: 参数显示在浏览器的url中,例如: http://www.baidu.com/s?wd=Chinese
post请求: 参数在请求体当中,以隐式的方式发送,请求的参数包含在"Content-Type"消息头里,指明该消息体的媒体类型和编码
注意: 尽量避免get方式提交表单,可能会导致安全问题
"""

"""
http请求包含: 请求行,请求头,空格,请求体(post)
POST http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule HTTP/1.1
Host: fanyi.youdao.com
Connection: keep-alive
Content-Length: 202
Accept: application/json, text/javascript, */*; q=0.01
Origin: http://fanyi.youdao.com
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Referer: http://fanyi.youdao.com/
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: OUTFOX_SEARCH_USER_ID=-388253338@10.169.0.84; JSESSIONID=aaal-CPvBwa9P85-5f7ew; OUTFOX_SEARCH_USER_ID_NCOO=2060469077.47785; fanyi-ad-id=39535; fanyi-ad-closed=1; ___rl__test__cookies=1517115259862

i=rabbit&from=AUTO&to=AUTO&smartresult=dict&client=fanyideskweb&salt=1517115259867&sign=cb455e27816176d6dbdbd09cfa87c8cd&doctype=json&version=2.1&keyfrom=fanyi.web&action=FY_BY_REALTIME&typoResult=false
"""

import urllib.parse
import urllib.request

# 注意: post请求的url要通过抓包获取,不是浏览器上显示的url
# {"errorCode":50}问题: 将url里的translate_o改成translate
url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"

# 完整的请求头
headers = {
    # "host": "fanyi.youdao.com",
    # "accept": "application/json, text/javascript, */*; q=0.01",
    # "X-requested-with": "XmlhTtprequest",
    "User-Agent": "mozilla/5.0 (windoWS NT 10.0; WOW64) apPleWebKit/537.36 (KHTMl, liKe geckO) chrome/62.0.3202.89 safari/537.36"
    # "content-type": "application/x-www-form-urlencoded; charsET=UTF-8"
}

# 用户接口输入
kw = input("输入要翻译的内容:")

# post请求数据(抓包时WebForms里的参数)
formdata = {
"i": kw,
"doctype": "json"
}

# url转码
data = urllib.parse.urlencode(formdata)
# TypeError: POST data should be bytes or an iterable of bytes. It cannot be of type str.
data1 = bytes(data, encoding="utf-8")

# 创建请求对象(有data参数说明是post请求)
request = urllib.request.Request(url, data=data1, headers=headers)
# 向服务器提交请求
response = urllib.request.urlopen(request)
# 服务器响应数据
result = str(response.read(), encoding="utf-8")
print(result)
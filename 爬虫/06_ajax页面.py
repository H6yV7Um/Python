"""
ajax方式加载的页面,数据来源是json;拿到json就拿到了网页数据
"""

import urllib.parse
import urllib.request

# ajax页面的url也是通过抓包获取
url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action="

# 请求头
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv2.0.1) Gecko/20100101 Firefox/4.0.1"}

# post请求数据(抓包时WebForms里的参数)
formdata = {
    "start": "0",
    "limit": "20"
}

# URL转码
data = urllib.parse.urlencode(formdata)
# TypeError: POST data should be bytes or an iterable of bytes. It cannot be of type str.
data = bytes(data, encoding="utf-8")

# 创建请求对象
request = urllib.request.Request(url, data=data, headers=headers)
# 向服务器提交请求
response = urllib.request.urlopen(request)
# 服务器响应数据
result = str(response.read(), encoding="utf-8")

# 保存到本地
f = open("D://movie.json", "w", encoding="utf-8")
f.write(result)
f.close()

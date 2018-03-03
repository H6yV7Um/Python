import requests
import json
import jsonpath

# 任务开发请求链接
url = "https://ide-cn-shanghai.data.aliyun.com/web/folder/listObject?keyword=&objectId=-1&projectId=29820&reRender=true&tenantId=171224272675329&type=1"
# url = "https://ide-cn-shanghai.data.aliyun.com/web/folder/listObject?objectId=22594607&projectId=29820&tenantId=171224272675329&type=1"
# url = "https://ide-cn-shanghai.data.aliyun.com/web/flow/loadProp?objectId=22182283&projectId=29820&tenantId=171224272675329"

# 请求头
headers = {
    "Host": "ide-cn-shanghai.data.aliyun.com",
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
    "Upgrade-Insecure-Requests": "1",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cookie": "cna=0RylEtTpfmYCAbSouGb1YCwH; UM_distinctid=160101e3e7c6e7-0fbf34c447325d-5b452a1d-100200-160101e3e7d8ee; cnz=Fs+3Ep3shAYCAWa4qLRQmfQ2; aliyun_choice=CN; _ga=GA1.2.1339959910.1513152795; aliyun_site=CN; bs_n_lang=zh_CN; aliyun_lang=zh; bd=s0ouCmI%3D; csrf_token=7f2ecb086b1e407291b843fe9f453960; channel=jkDbvGIL2YU%3D; sidebar-type=full; ck2=4620cd2a4ad7314796a4fee9fdec79b5; an=chenqian; lg=true; sg=n21; login_aliyunid='chenqian @ 1065151969971491'; login_aliyunid_ticket=_XNpdGJxz7mWg27D1MT6TgHx8NYmCT2kp983ItcmBeAfq1S1E2ml6JYlY4q9CyLstMknfiSc2GhOwNcWzj5bYLpKzKZ49O80KpzxYXWJ0WPzFXDzr7rhZ_Dua5Qyv2KMv85szYAdhP4$; login_aliyunid_sc=74u48x24xL7xCj1SQ9*cYL0T_GM6j755J0Ue*32gOhpT1BgjJpN52iRpWSCNRD1qGIMsDH2NK_pe423j3IpcTSjXfilT_b*s0jXnTKaoslOXYQhG1shU4g$$; c_token=5fb6a200eb5db1983b64e9fbd9dc703e; login_aliyunid_csrf=648e607223724beaa796732ab18b406a; lvc=sAhuVA2hU3tOiw%3D%3D; isg=BBUVH6NS484xPse2KbK4HkwAJBFjAt1cl9RM7Zeelg1x7qzgdGIb9NbIvPLYaeHc"
}
# 发送get请求
response = requests.get(url, headers=headers)
# 获取json数据
text = response.text
print(text)
# 将json字符串转换成Python对象
dict_data = json.loads(text)
# print(type(dict))  # <class 'dict'>
# 获取data键
data = jsonpath.jsonpath(dict_data, '$..data')[0]

# 判断data键的数据类型
def digui(data):
    # 如果data类型是dict,说明是文件,ok了！
    if type(data) is dict:
        # 取出data里的id
        id = jsonpath.jsonpath(data, '$..id')[0]
        # 根据id拼接url
        url1 = "https://ide-cn-shanghai.data.aliyun.com/web/flow/loadProp?objectId=" + str(id) + "&projectId=29820&tenantId=171224272675329"
        # 发送请求获取数据
        response1 = requests.get(url1, headers=headers)
        # 将json数据转换成Python对象dict
        dict1 = json.loads(response1.text)
        # 给文件命名
        filename = jsonpath.jsonpath(dict1, '$..name')[0]
        print(filename)
        # 获取sql脚本
        content = jsonpath.jsonpath(dict1, '$..content')
        print(content)
        # 判断sql脚本是否有内容(阿里云测试那几个脚本并不可用)
        if content is not False:
            # 有就取出具体sql
            content_new = jsonpath.jsonpath(dict1, '$..content')[0]
            print(content_new)
            # 写入本地文件
            with open("C://Users/Public/Downloads/odps/" + filename + ".sql", "w") as f:
                f.write(content_new)
        else:
            print("hehe")
    # 如果data类型是list,说明是文件夹,继续递归...
    else:
        # 获取id列表
        id_list = jsonpath.jsonpath(dict_data, '$..id')
        print(id_list)
        # 遍历列表
        for id in id_list:
            print(id)
            # url2 = "https://ide-cn-shanghai.data.aliyun.com/web/folder/listObject?objectId=" + str(id) + "&projectId=29820&tenantId=171224272675329&type=1"
            url1 = "https://ide-cn-shanghai.data.aliyun.com/web/flow/loadProp?objectId=" + str(id) + "&projectId=29820&tenantId=171224272675329"
            url2 = "https://ide-cn-shanghai.data.aliyun.com/web/folder/listObject?objectId=" + str(id) + "&projectId=29820&tenantId=171224272675329&type=1"
            # 接收请求数据
            res1 = requests.get(url1, headers=headers)
            # print(res1.text)
            # 转成Python对象
            data1 = json.loads(res1.text)
            print(data1)
            # 获取data字段值
            data11 = jsonpath.jsonpath(data1, '$..data')[0]
            print(data11)
            # 如果是脚本文件
            if data11 is not None:
                # 给文件命名
                filename = jsonpath.jsonpath(data1, '$..name')[0]
                print(filename)
                # 获取sql脚本
                content = jsonpath.jsonpath(data1, '$..content')
                print(content)
                # 判断sql脚本是否有内容(阿里云测试那几个脚本并不可用)
                if content is not False:
                    # 有就取出具体sql
                    content_new = jsonpath.jsonpath(data1, '$..content')[0]
                    print(content_new)
                    # 写入本地文件
                    with open("C://Users/Public/Downloads/odps/" + filename + ".sql", "w") as f:
                        f.write(content_new)
                else:
                    print("hehe")
            # 如果不是脚本文件
            else:
                # 接收请求数据
                res2 = requests.get(url2, headers=headers)
                # 转成Python对象
                dict2 = json.loads(res2.text)
                # 获取data字段
                data2 = jsonpath.jsonpath(dict2, '$..data')[0]
                print(data2)
                digui(data2)

digui(data)


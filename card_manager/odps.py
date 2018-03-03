import requests
import json
import jsonpath

class Odps(object):

    def getUrl(self):
        """
        遍历列表获取所有任务的请求链接
        :return:
        """

        # 任务开发请求链接
        url = "https://ide-cn-shanghai.data.aliyun.com/web/folder/listObject?keyword=&objectId=-1&projectId=29820&reRender=true&tenantId=171224272675329&type=1"

        self.getData(url)

    def getData(self, url):
        """
        获取单个sql脚本相关内容
        :param url:
        :return:
        """

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
        # 调用download方法
        self.download(text)

    def download(self, text):
        """
        下载到本地
        :param text:
        :return:
        """

        # 将json字符串转换成Python对象
        dict = json.loads(text)
        # print(type(dict))  # <class 'dict'>
        # 获取sql脚本
        content = jsonpath.jsonpath(dict, '$..content')[0]
        # 获取文件名(任务名)
        filename = jsonpath.jsonpath(dict, '$..name')[0]
        # print(type(content))  # <class 'str'>
        print(content)
        # 将content序列化成json数组
        # array = json.dumps(content, ensure_ascii=False)
        # 写入本地文件
        with open("C://Users/Public/Downloads/odps/" + filename + ".sql", "w") as f:
            f.write(content)

if __name__ == "__main__":
    o = Odps()
    o.getUrl()
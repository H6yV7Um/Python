import requests
import json
import jsonpath


class Odps(object):

    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
            "cookie": "cna=gBRKEw0StSECAbSpHwYUzPv7; cnz=XxpLE7CGbDgCAVa4qLQRVOOV; _ga=GA1.2.1551129035.1522805856; aliyun_site=CN; bs_n_lang=zh_CN; aliyun_lang=zh; bd=s0ouCmI%3D; csrf_token=a0d0cfd0157b4028a4bb9c83a877da31; aliyun_choice=CN; _gid=GA1.2.533537398.1523267294; login_aliyunid_csrf=9f47a49ccea1477e8630210ba5c3cdc4; login_aliyunid='chenqian @ 1065151969971491'; login_aliyunid_ticket=_XNpdGJxz7mWg27D1MT6TttRsR7Ovw03okpwtHvU8v8fq1S1E2ml6JYlY4q9CyLstMknfiSc2GhOwNcWzj5bYLpKzKZ49O80KpzxYXWJ0WPzFXDzr7rhZ_Dua5Qyv2KMv85szYAdhP4$; login_aliyunid_sc=74u48x24xL7xCj1SQ9*cYL0T_GM6j755J0Ue*32gOhpT1BgjJpN52iRpWSCNRD1qeroUoZyaa5CV2jKJ8BaIYQM8nownX8rR0jXnTKaoslOXYQhG1shU4g$$; c_token=d743bda3b69d577578984ffbe0710fbb; ck2=afe88d378eb6a34a9297bae49560e4dd; an=chenqian; lg=true; sg=n21; UM_distinctid=162b289d2ed73-09abbe397b5a67-b353461-100200-162b289d2eeb74; lvc=sAhuVyJgPFiEjQ%3D%3D; isg=BPr-3hV8dLiRNPgHGrsv34_5SyCwu2r991ggvgTIWwlj93sxaDv5lb5BQ4Mr5_Yd"
        }

    def getpage(self):
        for page in range(1, 233):
            url = "https://dmc-cn-shanghai.data.aliyun.com/web/meta/table/search?pageNum="+str(page)+"&pageSize=10&keyword=&categoryLevel=1&categoryId=&appGuid=&tenantId=171224272675329&projectId=29820"
            self.gettable(url)

    def gettable(self, url):
        res = requests.get(url, headers=self.headers)
        text = json.loads(res.text)
        tables = jsonpath.jsonpath(text, '$..tableGuid')
        self.getsql(tables)

    def getsql(self, datas):
        for data in datas:
            url = "https://dmc-cn-shanghai.data.aliyun.com/web/meta/table/ddl?tableGuid="+data+"&resourceType=odps&tenantId=171224272675329&projectId=29820"
            res = requests.get(url, headers=self.headers)
            text = json.loads(res.text)
            sql = text.get('data')
            with open("C://Users/Public/Downloads/test01.sql", "a") as f:
                f.write(sql + "\n")


if __name__ == "__main__":
    o = Odps()
    o.getpage()
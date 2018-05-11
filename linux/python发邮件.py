# coding=utf-8
import yagmail

def send_mail():

    # 连接邮箱服务器
    yag = yagmail.SMTP(user="chenqian@meihaofenqi.com", password="Cq224500821", host="smtp.exmail.qq.com")

    # 收件人(多个收件人可用list表示)
    to = "chenqian@meihaofenqi.com"
    # 抄送人
    cc = "1573976179@qq.com"
    # 主题
    subject = "日常查询"
    # 正文
    contents = "你好：\r\n今天数据请查收，谢谢！"
    # 附件
    files = "C://Users/chenq/Desktop/aaa.csv"

    # 发送
    yag.send(to=to, subject=subject, contents=contents, attachments=files, cc=cc)


if __name__ == "__main__":
    send_mail()
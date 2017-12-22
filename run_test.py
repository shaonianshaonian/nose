# coding=utf-8
import unittest
from HTMLTestRunner import HTMLTestRunner
# from common import HTMLTestRunner
import time
import os, smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header


# 定义发送邮件
def send_mail(file_new):
    """
    f = open(file_new, 'rb')
    mail_body = f.read()
    print(mail_body)
    f.close()"""   # 作为HTML发送邮件时用
    receiver = "1406840058qq.com"
    """
    msg = MIMEText(mail_body,'html','utf-8')  
    msg['Subject'] = Header('xxx接口自动化测试报告','utf-8') """  # 作为HTML发送邮件时用

    msg = MIMEMultipart()
    msg.attach(MIMEText("测试人：wuyuwei\n时间：" + now, 'plain', 'UTF-8'))
    msg['From'] = Header("wuyuwei" , 'UTF-8')
    msg['Subject'] = Header('供应商接口自动化测试报告', 'utf-8')
    att1 = MIMEText(open(file_new, 'rb').read(), 'plain', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename="test_result.html"'
    msg.attach(att1)

    smtp = smtplib.SMTP()
    smtp.connect('smtp.exmail.qq.com')
    smtp.login('wuyuwei@youmidou.cn', 'Wyw123456')
    smtp.sendmail("wuyuwei@youmidou.cn", receiver, msg.as_string())
    smtp.quit()
    print('邮件已发出！注意查收。')
# 查找最新报告并发送


def new_report(test_report):
    lists = os.listdir(test_report)
    lists.sort(key=lambda fn: os.path.getmtime(test_report + '\\' + fn))
    file_new = os.path.join(test_report, lists[-1])
    print(file_new)
    return file_new


if __name__ == "__main__":
    test_dir = 'D:\\nose\\test_case'
    test_report = 'D:\\nose\\test_result'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')
    # 按照一定的格式获取当前的时间
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    # 定义报告存放路径
    filename = 'D:\\nose\\test_result\\' + now + 'test_result.html'
    # 定义测试报告
    fp = open(filename, "wb")
    runner = HTMLTestRunner(stream=fp,
                            title="登陆接口测试报告",
                            description="测试用例执行情况：")
    # 运行测试
    runner.run(discover)
    fp.close()

    new_report = new_report(test_report)
    send_mail(new_report)

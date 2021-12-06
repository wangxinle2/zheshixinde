
'''
    入口程序：
        用于扫描加法，减法用例
        并执行得到测试报告
    1.HTMLTestRunner

'''
import HTMLTestRunner
import unittest

# 加载8条用例
tests = unittest.defaultTestLoader.discover(r"D:\pycharmProject\day12【单元测试】\day12",pattern="Test*.py")

# 创建运行器，来运行8条用例
runner = HTMLTestRunner.HTMLTestRunner(
    title = "计算器的测试报告",
    description="加法和减法的测试报告",
    verbosity=1,
    stream = open(file="计算器.html",mode="wb+")
)


# 生成测试报告

runner.run(tests)

from HTMLTestRunner import HTMLTestRunner
import unittest
import time
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
import smtplib
import os


# 定义发送邮件
def send_mail(file):
    f = open(file, 'rb',).read()
    # f.close()
    att = MIMEText(f, 'base64', 'utf-8')
    att['content-type'] = 'application/octet-stream'
    att.add_header('Content-Disposition', 'attachment', filename='计算器.html')
    msg = MIMEText('各位好，附件是本次的测试报告，请查阅!谢谢', 'HTML', 'utf-8')

    msg_all = MIMEMultipart('related')
    msg_all['Subject'] = Header('自动化测试报告', "utf-8")

    print('添加附件')
    msg_all.attach(att)
    print('添加成功')
    msg_all.attach(msg)

    smtp = smtplib.SMTP()
    smtp.connect('smtp.qq.com', 25)
    smtp.login('645536018@qq.com', 'cfkxpvdlahofbebb')
    smtp.sendmail('645536018@qq.com', '645536018@qq.com', msg_all.as_string())
    smtp.quit()
    print('email has send out!')


# 查找测试报告
def find_report(address):
    lists = os.listdir(address)
    lists.sort(key=lambda fn: os.path.getmtime(address + '\\' + fn))
    file_new = os.path.join(address, lists[-1])
    print(file_new)
    return file_new


if __name__ == '__main__':
# 测试案例目录
    test_dir = 'D:\pycharmProject\day12【单元测试】\day12'
    # 测试报告保存目录
    address_report = 'D:\pycharmProject\day12【单元测试】\day12'
# 在测试案例目录加载以test开头的案例集
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='Test*.py')
    now = time.strftime("%Y-%m-%d_%H_%M_%S")
    # 每次生成的报告绝对路径和时间戳报告名称
    filename = address_report + '\\' + now + '计算器.HTML'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title='测试报告', description='用例执行情况' )
    # 执行已保存的案例集
    runner.run(discover)
    fp.close()

    new_report = find_report(address_report)
    print(new_report)
    send_mail(new_report)


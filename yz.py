#coding:utf-8

import requests
from bs4 import BeautifulSoup
import time
import os
import smtplib
from email.mime.text import MIMEText

def main():
    cookie = input("填入Cookie:\r\n")
    url = r'https://yz.chsi.com.cn/tm/student/zhiy/list.action'
    headers = {
        'cookie': cookie,
        'Host': 'yz.chsi.com.cn',
        'Referer': 'https://yz.chsi.com.cn/tm/student/zhiy/list.action',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
    }
    html = requests.get(url, headers=headers)
    if(html.status_code != 200):
        print("登陆失败、")
        os._exit(0)
    soup = BeautifulSoup(html.text, 'lxml')
    content = soup.find('table', class_='ui-table').find('tbody').find_all('td')[-2].string.strip()
    return content

def youxiang(receive='1061700625@qq.com'):
    msg_from = '2580833660@qq.com'  # 发送方邮箱
    passwd = 'wpbevfnmpfdsdiad'  # 填入发送方邮箱的授权码
    receiver = receive  # 收件人邮箱

    subject = "已更新"  # 主题
    content = "已更新"  # 正文

    msg = MIMEText(content)
    msg['Subject'] = subject
    msg['From'] = msg_from
    msg['To'] =  ";".join(receiver)# 收件人为多个收件人,通过join将列表转换为以;为间隔的字符串
    try:
        s = smtplib.SMTP_SSL("smtp.qq.com", 465)# 邮件服务器及端口号
        s.login(msg_from, passwd)
        s.sendmail(msg_from, receiver, msg.as_string())
        print("邮件已发送成功！")
        time.sleep(5)
    except smtplib.SMTPException:
        print("Error")
    finally:
        s.quit()

if __name__ == '__main__':
    rec = input("输入接收邮箱：\r\n")
    while 1:
        content = main()
        print('**', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), '**')
        if('等待复试通知' in content):
            print("未更新。- ", end='')
            print(content)
            print("5分钟后重试")
            time.sleep(60*5)
        else:
            print("已更新！- ", end='')
            print(content)
            youxiang(rec)
            break




















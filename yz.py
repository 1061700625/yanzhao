#coding:utf-8

import requests
from bs4 import BeautifulSoup
import time
import os

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

if __name__ == '__main__':
    while 1:
        content = main()
        print('**', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), '**')
        if('等待复试通知' in content):
            print("未更新。- ", end='')
            print(content, '\r\n')
            print("5分钟后重试")
            time.sleep(60*5)
        else:
            print("已更新！- ", end='')
            print(content, '\r\n')
            break




















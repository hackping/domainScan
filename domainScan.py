#!/usr/bin/python
#coding:utf-8
import requests
import re



'''结果保存到文件内'''
def writurl(url):
    print(url)
    file = open('result.txt','a')
    with file as f:
        f.write(url+'\n')

    file.close()


def urlopen(url1 , url2):


    header = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'DNT': '1',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'
        }

    try:


        reponse1 = requests.get(url1, timeout=3, headers=header)
        code1 = reponse1.status_code


        if (code1 == 200):
            u1 = re.findall('//.*', url1)

            writurl(u1[0][2:])

        else:
            reponse2 = requests.get(url2, timeout=3, headers=header)
            code2 = reponse2.status_code
            if (code2 == 200):
                u2 = re.findall('//.*', url2)

                writurl(u2[0][2:])


    except:
        pass


'''读取文件域名前缀'''
def scan(url):

    f = open('domain.txt','r')
    for line in f:
        u1 = 'http://'+ line.strip() + '.'+url
        u2 = 'https://'+ line.strip() + '.'+url

        urlopen(u1, u2)

        #print(line.strip() + '.'+url)
    f.close()

    #reponse = requests.get(url)
    #print(reponse.text)


if __name__ == "__main__":
    '''使用前清空结果文件内容'''
    file = open('result.txt','w+')
    file.truncate()
    file.close()


    print('请输入域名(如：baidu.com)：')
    url = raw_input()

    scan(url)
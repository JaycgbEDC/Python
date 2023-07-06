import requests
import re


pat_li = re.compile(r"2023必看热片.*?<ul>(?P<u1>.*?)</ul>", re.S)
pat_link = re.compile(r"<a href='(?P<link>.*?)'", re.S)
pat_data = re.compile(r'◎片　　名　(?P<name>.*?)<br />.*?<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<download>.*?)"', re.S)



def ask_url(url):
    """ 根据url返回html网页 """
    requests.packages.urllib3.disable_warnings()  # 忽略警告
    response = requests.get(url, verify=False)  # verify=False 去掉安全验证
    response.encoding = 'gb2312'  # 指定字符集（head中有）
    return response.text


def get_link(base_url):
    """ 获取电影天堂89的2023必看电影的链接列表 """
    html = ask_url(base_url)
    link_list = []
    it1 = pat_li.finditer(html)
    for item1 in it1:
        temp = item1.group('u1')
        it2 = pat_link.finditer(temp)
        for item2 in it2:
            link_list.append(base_url + item2.group('link'))
    return link_list


def get_data(link_list):
    """ 根据列表中的每一个链接提取名字及下载链接 """
    for link in link_list:
        html = ask_url(link)
        match = pat_data.search(html)
        print(match.group('name'))
        print(match.group('download'))


def main():
    base_url = 'https://www.dytt89.com/'
    link_list = get_link(base_url)
    get_data(link_list)


if __name__ == '__main__':
    main()
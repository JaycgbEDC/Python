import urllib.request, urllib.error


def ask_url(url):
    """ 根据url获取html 
    :param: url
    :returns: html
    """
    html = ''
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.34'
    }
    req = urllib.request.Request(url, headers=headers)
    try:
        response = urllib.request.urlopen(req)
        html = response.read().decode('utf-8')
    except urllib.error.URLError as e:
        print(e)
    return html


def get_html(base_url):
    """ 获取10页html信息
    :param: base_url
    :returns: html_list
    """
    html_list = []
    for i in range(1, 2):
        html_list.append(ask_url(base_url + str(i)))
    print(html_list)



def main():
    base_url = 'https://www.zhipin.com/web/geek/job?query=python&city=100010000&page='
    html_list = get_html(base_url)


if __name__ == '__main__':
    main()
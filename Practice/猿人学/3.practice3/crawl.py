import requests


Base_api = "https://match.yuanrenxue.cn/api/match/3"


def every_page(i: int, d: dict):
    params = {
        "page": i
    }
    headers = {
        "content-length": '0',
        "sec-ch-ua": '"Not/A)Brand";v="99", "Microsoft Edge";v="115", "Chromium";v="115"',
        "sec-ch-ua-mobile": '?0',
        "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.200',
        "sec-ch-ua-platform": "Windows",
        "accept": '*/*',
        "origin": 'https://match.yuanrenxue.cn',
        "sec-fetch-site": 'same-origin',
        "sec-fetch-mode": 'cors',
        "sec-fetch-dest": 'empty',
        "referer": 'https://match.yuanrenxue.cn/match/3',
        "accept-encoding": 'gzip, deflate, br',
        "accept-language": 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        "cookie": 'Hm_lvt_c99546cf032aaa5a679230de9a95c7db=1689688507,1689688622,1689820559,1691545682; Hm_lvt_9bcbda9cbf86757998a2339a0437208e=1689688622,1689820921,1689820945,1691546075; qpfccr=true; no-alert3=true; tk=-1675320745105519819; sessionid=o2etctcldth2yepqpyxwwxw41rmcuw77'
    }
    session = requests.session()
    session.headers = headers
    session.post(url = "https://match.yuanrenxue.cn/jssm")
    if i == 4 or i == 5:
        headers['user-agent'] = 'yuanrenxue.project'
    response = session.get(url = Base_api, params = params)
    for i in response.json()["data"]:
        d[i["value"]] = d.get(i["value"], 0) + 1


def crawl():
    d = {}
    for i in range(5):
        every_page(i + 1, d)
    print(max(d, key = lambda x: d[x]))


if __name__ == '__main__':
    crawl()
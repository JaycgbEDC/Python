import requests
import socket
import sys
import json


s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
try:
    s.connect(("localhost", 8080))
except Exception as e:
    print('Server not found or not open', e)
    sys.exit()


Base_api = f"https://match.yuanrenxue.cn/api/match/5"
proxy = "127.0.0.1:7890"
proxies = {
    "http": "http://" + proxy,
    "https": "http://" + proxy
}


def get_data():
    msg = "get_data"
    s.sendall(msg.encode())
    data = s.recv(1024)
    print('Received tcp_data: ', data.decode())
    return data.decode()


def every_page(page, m, f, session, l):
    params = {
        'page': page,
        'm': m,
        'f': f
    }
    response = session.get(url = Base_api, params=params, proxies = proxies)
    print(response.json())
    data = response.json()["data"]
    for d in data:
        l.append(d["value"])


def crawl():
    l = []
    tcpData = json.loads(get_data())
    cookie, m, f = tcpData["cookie"], tcpData["params_m"], tcpData["params_f"]
    headers = {
        'sec-ch-ua': '"Not/A)Brand";v="99", "Microsoft Edge";v="115", "Chromium";v="115"',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'x-requested-with': 'XMLHttpRequest',
        'sec-ch-ua-mobile': '?0',
        'user-agent': "yuanrenxue.project",
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://match.yuanrenxue.cn/match/5',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'cookie': cookie
    }
    session = requests.session()
    session.headers = headers
    for i in range(5):
        every_page(i + 1, m, f, session, l)
    print(sum(sorted(l, reverse = True)[:5]))
    s.close()


if __name__ == '__main__':
    crawl()
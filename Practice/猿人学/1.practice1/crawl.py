import requests

import subprocess
from functools import partial
subprocess.Popen = partial(subprocess.Popen, encoding="utf-8")

import execjs


Base_api = f"https://match.yuanrenxue.cn/api/match/1?"


def get_m():
    with open("env.js", encoding = 'utf-8') as f:
        node = execjs.get()
        js_code = node.compile(f.read())
        result = js_code.eval(f'get_m()')
        return result


def every_page(page, m):
    page_price = 0
    req_api = Base_api + f"page={page}&m={m}"
    response = requests.get(req_api)
    for d in response.json()["data"]:
        page_price += int(d["value"])
    print("success!")
    return page_price, len(response.json()["data"])


def crawl():
    price = 0
    count = 0
    for i in range(5):
        page_price, page_count = every_page(i+1, get_m())
        price += page_price
        count += page_count
    print(price / count)


if __name__ == '__main__':
    crawl()
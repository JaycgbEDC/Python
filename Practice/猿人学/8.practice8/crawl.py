import requests
import base64
import os
from lxml import etree
from processing import run


Base_api = "https://match.yuanrenxue.cn/api/match/"
proxy = "127.0.0.1:7890"
proxies = {
    "http": "http://" + proxy,
    "https": "http://" + proxy
}
session = requests.session()


def get_params(page):
    answer = ""
    verify_url = Base_api + "8_verify"
    path = f"./img/{page}/origin.jpeg"
    os.makedirs(f"./img/{page}", exist_ok=True)
    html = (session.get(url=verify_url, proxies = proxies)).json()["html"]
    initial = etree.HTML(html)
    img = initial.xpath("/html/body/img/@src")[0].split(',', 1)[1]
    text_list = initial.xpath("//p/text()")
    with open(path, "wb") as fp:
        fp.write(base64.b64decode(img))
    res = run(path)
    print(f"识别结果：{res}")
    print(f"点击文字：{text_list}")
    for s in text_list:
        num = res.get(s, -1)
        if num == -1:
            raise Exception("识别不全或有误！")
        answer += str(num) + '|'
    params = {
        "page": page,
        "answer": answer
    }
    return params


def every_page(page, d):
    num_api = Base_api + "8"
    params = get_params(page)
    response = session.get(url=num_api, params=params, proxies=proxies).json()
    print(response)


def deal_d(d):
    pass


def crawl():
    d = {}
    every_page(1, d)
    # for i in range(5):
    #     every_page(i + 1, d)
    # res = deal_d(d)
    # print(res)


if __name__ == '__main__':
    crawl()
import requests
import base64
import os
from lxml import etree
from processing import run


Base_api = "https://match.yuanrenxue.cn/api/match/"
session = requests.session()


def get_params(page):
    answer = ""
    verify_url = Base_api + "8_verify"
    path = f"./img/{page}/origin.jpeg"
    os.makedirs(f"./img/{page}", exist_ok=True)
    html = (session.get(url=verify_url)).json()["html"]
    initial = etree.HTML(html)
    img = initial.xpath("/html/body/img/@src")[0].split(',', 1)[1]
    text_list = initial.xpath("//p/text()")
    with open(path, "wb") as fp:
        fp.write(base64.b64decode(img))
    # res = run(path)
    # print(f"识别结果：{res}")
    # print(f"点击文字：{text_list}")
    run(path)
    answer = input(f"请输入四个汉字{text_list}的坐标，每个数字用空格隔开：").replace(' ', '|')
    print(f"answer: {answer}")
    params = {
        "page": page,
        "answer": answer
    }
    return params


def every_page(page, d: dict):
    num_api = Base_api + "8"
    params = get_params(page)
    response = session.get(url=num_api, params=params).json()
    print(response)
    if response["status"] != '1':
        raise Exception("发生错误！！！")
    for num_d in response["data"]:
        num = num_d["value"]
        d[num] = d.get(num, 0) + 1


def crawl():
    d = {}
    every_page(1, d)
    for i in range(5):
        every_page(i + 1, d)
    print(d)


if __name__ == '__main__':
    crawl()
import requests
import execjs


Base_api = f"https://match.yuanrenxue.cn/api/match/2?"


def get_m():
    with open("env.js", encoding = 'utf-8') as f:
        node = execjs.get()
        js_code = node.compile(f.read())
        result = js_code.call("get_m")
        return result


def every_page(page):
    count_page = 0
    api = Base_api + f"page={page}"
    headers = {
        "cookie": get_m()
    }
    print(headers)
    response = requests.get(url = api, headers=headers)
    data = response.json()["data"]
    for d in data:
        count_page += d["value"]
    return count_page


def crawl():
    count = 0
    for i in range(5):
        count += every_page(i + 1)
    print(count)


if __name__ == '__main__':
    crawl()
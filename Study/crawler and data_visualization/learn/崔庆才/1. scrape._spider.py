#  爬取Scrape的书籍信息，503页共9040书籍
#  网站url：https://spa16.scrape.center/
import multiprocessing
import httpx
import logging
import json
import os


total_page = 503
base_url = "https://spa16.scrape.center/api/book/"
result_dir = "./data"
os.path.exists(result_dir) or os.makedirs(result_dir)
logging.basicConfig(level = logging.INFO, format = '%(asctime)s - %(levelname)s: %(message)s')


def scrape_page(url, parameters):
    """ 爬取指定url的json信息 """
    logging.info('scraping %s...', url)
    try:
        client = httpx.Client(http2 = True)
        response = client.get(url, params = parameters)
        if response.status_code == 200:
            return response.json()
        logging.error("get invalid status code %s while scraping %s", response.status_code, url)
    except httpx.RequestError:
        logging.error("error occured while scraping %s", url, exc_info = True)


def scrape_index(page):
    """ 爬取指定offset的json信息 """
    offset = str(page * 18)
    index_url = f"{base_url}?limit=18&offset={offset}"
    parameters = {
            "limit": '18',
            "offset": offset
    }
    return scrape_page(index_url, parameters)


def scrape_parse(index_json: dict):
    """ 对json解析，提取出url号 """
    for item in index_json.get("results"):
        id = item.get("id")
        detail_url = base_url + id + '/'
        logging.info("get detail url %s", detail_url)
        yield detail_url


def scrape_detail(url):
    return scrape_page(url, None)


def parse_detail(detail_json: dict):
    """ 提取出详情页的书籍名字、评分、简介、出版时间、封面图片地址 """
    name = detail_json.get("name")
    score = detail_json.get("score")
    introduction = detail_json.get("introduction")
    publish_time = detail_json.get("published_at")
    cover = detail_json.get("cover")
    return {
        "name": name,
        "score": score,
        "introduction": introduction,
        "publish_time": publish_time,
        "cover": cover
    }


def save_data(data: dict):
    """ 保存数据为json格式 """
    name = data.get("name")
    data_path = f"{result_dir}/{name}.json"
    json.dump(data, open(data_path, 'w', encoding = "utf-8"), ensure_ascii = False, indent = 2)


def main(page):
    index_json = scrape_index(page)
    detail_urls = scrape_parse(index_json)
    for detail_url in detail_urls:
        detail_json = scrape_detail(detail_url)
        data = parse_detail(detail_json)
        logging.info("get detail data %s", data)
        logging.info("saving data to json file")
        save_data(data)
        logging.info("data saved successfully")


if __name__ == "__main__":
    pool = multiprocessing.Pool()
    pages = range(total_page)
    pool.map(main, pages)
    pool.close()
    pool.join()
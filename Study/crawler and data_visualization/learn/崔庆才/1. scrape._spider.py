#  爬取Scrape的书籍信息，503页共9040书籍
#  网站url：https://spa5.scrape.center/（spa16爬取999个就不行了）
import asyncio
import httpx
import logging
import json
import time
from motor.motor_asyncio import AsyncIOMotorClient


TOTAL_PAGE = 503
BASE_URL = "https://spa5.scrape.center/api/book/"
# RESULT_DIR = "./data"
# os.path.exists(RESULT_DIR) or os.makedirs(RESULT_DIR)
logging.basicConfig(level = logging.INFO, format = '%(asctime)s - %(levelname)s: %(message)s')

MONGO_CONNECTION_STRING = "mongodb://localhost:27017"
MONGO_DB_NAME = "books"
MONGO_COLLECTION_NAME = "scrape"
clt = AsyncIOMotorClient(MONGO_CONNECTION_STRING)
db = clt[MONGO_DB_NAME]
collection = db[MONGO_COLLECTION_NAME]

CONCURRENCY = 5  # 协程并发数量限制
semaphore = asyncio.Semaphore(CONCURRENCY)
client = None

proxy = "127.0.0.1:7890"
proxies = {
    "http://": "http://" + proxy,
    "https://": "http://" + proxy
}


async def scrape_api(url):
    """ 爬取指定url的json信息 """
    async with semaphore:
        try:
            logging.info('scraping %s...', url)
            response = await client.get(url)
            if response.status_code == 200:
                return response.json()
            logging.error("get invalid status code %s while scraping %s", response.status_code, url)
        except:
            logging.error("error occured while scraping %s", url, exc_info = True)


async def scrape_index(page):
    """ 爬取列表页 """
    offset = str(page * 18)
    index_url = f"{BASE_URL}?limit=18&offset={offset}"
    return await scrape_api(index_url)


async def save_data(data: dict):
    """ 保存数据到mongodb """
    logging.info(f'saving data {data.get("id")}')
    if data:
        condition = {"id": data.get("id")}
        return await collection.update_one(condition, {"$set": data}, upsert = True)
    

async def scrape_detail(id):
    url = BASE_URL + id + '/'
    data = await scrape_api(url)
    await save_data(data)


async def main():
    global client
    client = httpx.AsyncClient(verify = False, http2 = True, proxies = proxies)
    scrape_index_tasks = [asyncio.ensure_future(scrape_index(page)) for page in range(TOTAL_PAGE)]  # 爬取列表页tasks
    results = await asyncio.gather(*scrape_index_tasks)
    # logging.info("results %s", json.dumps(results, ensure_ascii = False, indent = 2))
    ids = []
    for index_data in results:  # 获取书的id
        if not index_data:
            continue
        for item in index_data.get("results"):
            ids.append(item.get("id"))
    scrape_detail_tasks = [asyncio.ensure_future(scrape_detail(id)) for id in ids]  # 爬取详情页tasks
    await asyncio.wait(scrape_detail_tasks)  # 这里用wait方法和gather方法效果是一样的，只是返回值不一样
    await client.aclose()


if __name__ == "__main__":
    t_s = time.time()
    asyncio.get_event_loop().run_until_complete(main())
    t_e = time.time()
    print(f"crawl done! cost time(minutes): {(t_e - t_s) // 60}")
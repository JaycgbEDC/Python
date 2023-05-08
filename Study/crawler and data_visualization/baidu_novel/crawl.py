# 小说网址：https://dushu.baidu.com/pc/detail?gid=4356351013
# https://dushu.baidu.com/api/pc/getCatalog?data={%22book_id%22:%224306311367%22} (其中%22是")  此url是所有章节的内容(名称, cid)
# https://dushu.baidu.com/api/pc/getChapterContent?data={%22book_id%22:%224306311367%22,%22cid%22:%224306311367|11722243%22,%22need_bookinfo%22:1}  此url是章节的全部内容
import asyncio
import aiohttp
import aiofiles
import requests
import json
import time


async def aio_download(book_id, cid, title):
    data = {
        "book_id":book_id,
        "cid":f"{book_id}|{cid}",
        "need_bookinfo":1
    }
    data = json.dumps(data)
    url = f'https://dushu.baidu.com/api/pc/getChapterContent?data={data}'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            dic = await response.json()
            async with aiofiles.open("./content/" + title, 'w', encoding = "utf-8") as fp:
                await fp.write(dic["data"]["novel"]["content"])


async def main(url):
    response = requests.get(url)
    dic = response.json()
    tasks = []
    for item in dic["data"]["novel"]["items"]:
        title = item["title"]
        cid = item["cid"]
        tasks.append(aio_download(book_id, cid, title))
    await asyncio.wait(tasks)


if __name__ == "__main__":
    book_id = "4306311367"  # 每本书都有自己的book_id
    catlog_url = f'https://dushu.baidu.com/api/pc/getCatalog?data={{"book_id":"{book_id}"}}'  # 用两个连续的{{表示左大括号
    t1 = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(catlog_url))
    t2 = time.time()
    print(f"爬取完毕！用时{t2 - t1}")
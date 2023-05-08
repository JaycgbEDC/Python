import time
import aiohttp
import asyncio
import requests


def download(url):
    """ 同步方式下载url内容 """
    name = url.split('/')[-1]
    response = requests.get(url)
    content = response.content
    with open("./synchronic/" + name, "wb") as fp:
        fp.write(content)


async def aio_download(url):
    name = url.split('/')[-1]
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            with open("./asynchronic/" + name, "wb") as fp:
                fp.write(await response.content.read())


async def main(urls):
    tasks = [asyncio.create_task(aio_download(url)) for url in urls]
    await asyncio.wait(tasks)


if __name__ == "__main__":
    urls = [
        "https://www.umei.cc/d/file/20221104/5bdfd2065d8baf28ed43662c1ef6d980.jpeg", 
        "https://www.umei.cc/d/file/20221104/smallec53911442cb74041aa21e47cf475e551667542255.jpg", 
        "https://www.umei.cc/d/file/20221104/smalldcc52b0db28b0ed32c9fb4f6e6a9034f1667542233.jpg", 
        "https://www.umei.cc/d/file/20221104/smallff3a00d2fa67b046c08c683ae1b79b2c1667542214.jpg", 
        "https://www.umei.cc/d/file/20221104/smallbf84da90bf3de3c8e4f9c47493974f251667542166.jpg"
    ]
    t1 = time.time()
    for url in urls:
        download(url)
    t2 = time.time()
    print(f"传统同步方式下载图片耗时：{t2 - t1}")

    t3 = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(urls))
    t4 = time.time()
    print(f"协程+aiohttp下载图片耗时：{t4 - t3}")
""" url: https://cokemv.me/
流程:
    1. 拿到https://cokemv.me/vodplay/3736-1-1.html的页面源代码
    2. 从源代码中提取到m3u8的url
    3. 下载m3u8
    4. 读取m3u8文件, 下载视频
    5. 合并视频
"""
import requests
import re
import asyncio
import aiohttp
import aiofiles
import os


def get_url_m3u8(url):
    """  
    params:
    url: url present html
    return:
    url_m3u8: the url of m3u8 file
    """
    response = requests.get(url)
    html = response.text
    pat = re.compile(r'},"url":"(?P<url_m3u8>.*?)","url_next"', re.S)
    url_m3u8 = "https://m3u.cokemv.org/m3u8.php?url=" + pat.search(html).group("url_m3u8").replace('\\', '')
    response.close()
    print("get_url_m3u8 succeed! --return url")
    return url_m3u8


def download_m3u8(url):
    """  
    params:
    url: the url of m3u8 file
    """
    response = requests.get(url)
    with open("./video.m3u8", "w") as fp:
        fp.write(response.text)
    response.close()
    print("download_m3u8 file succeed!")


async def download_video(url, name, session):
    """  
    params:
    url: the url of ts
    name: ts name
    session: avoid frequent request
    """
    async with session.get(url) as response:
        async with aiofiles.open("./video/" + name, "wb") as fp:
            content = await response.content.read()
            await fp.write(content)
        print(f"{name}下载完毕！")


async def main_download_video():
    tasks = []
    async with aiohttp.ClientSession() as session:  # 提前准备好session
        async with aiofiles.open("./video.m3u8", "r") as fp:
            async for line in fp:
                if line.startswith('#'):
                    continue
                line = line.strip()  # 注意去掉空白换行符，否则url无效
                tasks.append(asyncio.create_task(download_video(line, line.split('/')[-1], session)))  
            await asyncio.wait(tasks)


def ts2mp4():
    os.system("copy /b .\\video\\*.ts .\\movie.mp4")
    print("convert done!")


def main():
    # url = "https://cokemv.me/vodplay/3736-1-1.html"
    # url_m3u8 = get_url_m3u8(url)
    # download_m3u8(url_m3u8)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main_download_video())
    ts2mp4()


if __name__ == "__main__":
    main()
    print("done!")
import asyncio
from pyppeteer import launch
from pyquery import PyQuery as pq


width, height = 1366, 768


async def main():
    brower = await launch(userDataDir = "./userdata", ignoreHTTPSErrors = True, devtools = True, args = ["--disable-infobars", f"--window-size={width},{height}"])  # 设置cookie存放位置便于下次自动登录，忽略不安全连接错误，默认打开调试工具，去除弹出“自动化测试”信息，设置浏览器的宽高
    page = await brower.newPage()
    await page.evaluateOnNewDocument('Object.defineProperty(navigator, "webdriver", {get: () => undefined})')  # 防止检测出是自动化测试
    await page.setViewport({"width": width, "height": height})  # 设置页面窗口大小以便截图
    await page.goto("https://antispider1.scrape.center/")
    await page.waitForSelector(".item .name")  # 一直等待直到匹配成功
    doc = pq(await page.content())  
    names = [item.text() for item in doc(".item .name").items()]
    print(f"Names: {names}")
    await asyncio.sleep(2)
    await page.screenshot(path = "example.png")
    dimensons = await page.evaluate('''() => {
        return {
            width: document.documentElement.clientWidth,
            height: document.documentElement.clientHeight,
            deviceScaleFactor: window.devicePixelRatio,
        }
    }''')  # 执行js代码返回页面的宽、高、像素大小比率，return的格式为json
    print(dimensons)
    await asyncio.sleep(100)
    await brower.close()


asyncio.get_event_loop().run_until_complete(main())
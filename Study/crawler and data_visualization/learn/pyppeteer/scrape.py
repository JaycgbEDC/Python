from pyppeteer import launch
from pyppeteer.errors import TimeoutError
import logging
import asyncio


logging.basicConfig(level = logging.INFO, format = "%(asctime)s - %(levelname)s: %(message)s")

INDEX_URL = "https://spa2.scrape.center/page/"
TIMEOUT = 10
TOTAL_PAGE = 11
WINDOW_WIDTH, WINDOW_HEIGHT = 1366, 768

browser, tab = None, None


async def init():
    global browser, tab
    browser = await launch(userDataDir = "./userdata", ignoreHTTPSErrors = True, headless = True, args = ["--disable-infobars", f"--window-size={WINDOW_WIDTH},{WINDOW_HEIGHT}"])
    tab = await browser.newPage()
    await tab.setViewport({"width": WINDOW_WIDTH, "height": WINDOW_HEIGHT})


async def scrape_page(url, selector):
    logging.info(f"scraping {url}")
    try:
        await tab.goto(url)
        await tab.waitForSelector(selector, options = {
            "timeout": TIMEOUT * 1000
        })
    except TimeoutError:
        logging.info("error occured while scraping %s", url, exc_info = True)


async def scrape_index(page):
    url = f"{INDEX_URL}{page}"
    await scrape_page(url, ".item .name")


async def scrape_detail(url):
    await scrape_page(url, "h2")


async def parse_index():
    return await tab.querySelectorAllEval(".item .name", "nodes => nodes.map(node => node.href)")

async def parse_detail():
    url = tab.url
    name = await tab.querySelectorEval("h2", "node => node.innerText")
    categories = await tab.querySelectorAllEval(".categories button span", "nodes => nodes.map(node => node.innerText)")
    cover = await tab.querySelectorEval(".cover", "node => node.src")
    score = await tab.querySelectorEval(".score", "node => node.innerText")
    drama = await tab.querySelectorEval(".drama p", "node => node.innerText")
    return {
        "url": url,
        "name": name,
        "categories": categories,
        "cover": cover,
        "score": score,
        "drama": drama
    }


async def main():
    await init()
    try:
        for page in range(1, TOTAL_PAGE + 1):
            await scrape_index(page)
            detail_urls = await parse_index()
            for detail_url in list(detail_urls):
                logging.info("get detail url %s", detail_url)
                await scrape_detail(detail_url)
                detail_data = await parse_detail()
                logging.info("detail data %s", detail_data)
    finally:
        await browser.close()


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
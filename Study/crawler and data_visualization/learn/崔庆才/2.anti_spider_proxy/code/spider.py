import requests
from requests import Session
from pyquery import PyQuery as pq
from loguru import logger
from code.db import RedisQueue
from code.request import MovieRequest
from code.config import *


BASE_URL = "https://antispider5.scrape.center/"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.50"
}


class Spider():
    session = Session()
    queue = RedisQueue()

    @logger.catch
    def get_proxy(self):
        """
        get proxy from proxypool
        :return: proxy
        """
        response = requests.get(PROXY_POOL_URL)
        if response.status_code == 200:
            logger.debug(f"get proxy in function-get_proxy {response.text}")
            return response.text

    def start(self):
        """
        start request
        """
        self.session.headers.update(HEADERS)
        start_url = BASE_URL
        request = MovieRequest(url = start_url, callback = self.parse_index)
        self.queue.add(request)

    def parse_index(self, response):
        """
        parse index page
        :param response: response
        :return: new request
        """
        doc = pq(response.text)

        # request for detail
        items = doc(".item .name").items()
        for item in items():
            detail_url = BASE_URL + item.attr("href")
            request = MovieRequest(url = detail_url, callback = self.parse_detail)
            yield request
        
        # request for next page
        next_href = doc(".next").attr("href")
        if next_href:
            next_url = BASE_URL + next_href
            request = MovieRequest(url = next_url, callback = self.parse_index)
            yield request

    def parse_detail(self, response):
        """
        parse detail
        :param response: response of detail
        :return: data
        """
        doc = pq(response.text)
        cover = doc("img.cover").attr("src")
        name = doc("a > h2").text()
        categories = [item.text() for item in doc(".categories button span").items()]
        yield {
            "cover": cover,
            "name": name,
            "categories": categories
        }

    def request(self, request):
        """
        execute request
        :param request: MovieRequest
        :return: response
        """
        proxy = self.get_proxy()
        logger.debug(f"get proxy in function-request {proxy}")
        proxies = {
            "http": "http://" + proxy,
            "https": "http://" + proxy
        } if proxy else None
        return self.session.send(request.prepare(), timeout = request.timeout, proxies = proxies)
    
    def error(self, request):
        """
        error handling
        :param request: request
        :return:
        """
        request.fail_time = request.fail_time + 1
        logger.debug(f"request of {request.url} failed {request.fail_time} times")
        if request.fail_time < MAX_FAILED_TIME:
            self.queue.add(request)

    def schedule(self):
        """
        schedule request
        :return:
        """
        while not self.queue.empty():
            request = self.queue.pop()
            callback = request.callback
            logger.debug(f"executing request {request.url}")
            response = self.request(request)
            logger.debug(f"response status {response.status_code} of {request.url}")
            if not response or not response.status_code in VALID_STATUSES:
                self.error(request)
                continue
            results = list(callback(response))
            if not results:
                self.error(request)
                continue
            for result in results:
                if isinstance(result, MovieRequest):
                    logger.debug(f"generated new request {result.url}")
                    self.queue.add(result)
                if isinstance(result, dict):
                    logger.debug(f"scraped new data {result}")
    
    def run(self):
        """
        run
        :return:
        """
        self.start()
        self.schedule()


if __name__ == '__main__':
    spider = Spider()
    spider.run()
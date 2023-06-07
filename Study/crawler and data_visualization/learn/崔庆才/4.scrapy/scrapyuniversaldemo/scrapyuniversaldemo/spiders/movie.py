from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapyuniversaldemo.items import MovieItem
from scrapyuniversaldemo.loaders import MovieItemLoader


class MovieSpider(CrawlSpider):
    name = "movie"
    allowed_domains = ["ssr1.scrape.center"]
    start_urls = ["https://ssr1.scrape.center"]

    rules = (
        Rule(LinkExtractor(restrict_css = ".item .name"), callback="parse_detail", follow=True),
        Rule(LinkExtractor(restrict_css = ".next"), follow = True)
    )

    def parse_detail(self, response):
        loader = MovieItemLoader(item = MovieItem(), response = response)
        loader.add_css("name", ".item h2::text")
        loader.add_css("categories", ".categories button span::text")
        loader.add_css("cover", ".cover::attr(src)")
        loader.add_css("published_at", ".info span::text", re = "(\d{4}-\d{2}-\d{2})\s?上映")
        loader.add_xpath("score", '//p[contains(@class, "score")]/text()')
        loader.add_xpath("drama", "//div[contains(@class, 'drama')]/p/text()")
        yield loader.load_item()
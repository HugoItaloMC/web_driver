from scrapy.item import Field, Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from bs4 import BeautifulSoup

from typing import Dict, List, Any, Sequence, Generator


class ElementArticle(Item):
    it_by: Field = Field()
    take_more: Field = Field()


class ElementVideo(Item):
    it_by: Field = Field()
    take_more: Field = Field()


class ElementNews(Item):
    it_by: Field = Field()
    take_more: Field = Field()


class LatamIGNCrawler(CrawlSpider):

    name: str = "scrapy_latam_ign"

    custom_settings: Dict = {'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36',
                             'CLOSESPIDER_PAGECOUNT': 100}  # Quantinity from pages it rollening

    allowed_domains: List[str] = ["latam.ign.com"]  # Main URL allowed the Crawler

    start_urls: List[str] = ["https://latam.ign.com/se/?q=ps4&order_by=&model=article"]

    download_delay: int = 1  # Await before new request

    # Context URL parser while rollening pages
    rules: Sequence[Rule] = (
        #  To parser the URL get pattern and liken over the `regex`
        Rule(
            LinkExtractor(allow=r'type='),  # Apply regex to get elements
            follow=True),
        Rule(
            LinkExtractor(allow=r'/video/'),
            follow=True,
            callback='parse_element_video'),  # Get method parser element

        Rule(
            LinkExtractor(allow='/news/'),
            follow=True, callback='parse_element_news')
    )

    def parse_element_video(self, response) -> Generator:
        # Search element in DOM
        element: Any[ItemLoader | Item] = ItemLoader(ElementVideo(), response)
        element.add_xpath("it_by", '//h1/text()')

        element.add_xpath("take_more",
                          '//span[@class="publish-date"]/text()')
        yield element.load_item()

    def parse_element_news(self, response) -> Generator:
        # Search element in DOM
        element: Any[ItemLoader | Item] = ItemLoader(ElementNews(), response)
        element.add_xpath("it_by", '//h1/text()')

        element.add_xpath("take_more",
                          '//div[@id="id_text"]//*/text()')
        yield element.load_item()

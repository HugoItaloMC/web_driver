from scrapy.item import Field, Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader


from typing import Dict, List, Any, Sequence, Generator

from ..items import *


class TestMercadoLivreCrawler(CrawlSpider):

    name: str = "test_scrapy"

    custom_settings: Dict = {'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36',
                             'CLOSESPIDER_PAGECOUNT': 40}  # Quantinity from pages it rollening

    allowed_domains: List[str] = ["mercadolivre.com.br", "lista.mercadolivre.com.br"]  # Main URL allowed the Crawler

    start_urls: List[str] = ["https://lista.mercadolivre.com.br/celulares-smartphones"]

    download_delay: int = 1  # Await before new request

    # Context URL parser while rollening pages
    rules: Sequence[Rule] = (
        #  To parser the URL get pattern and liken over the `regex`
        Rule(
            LinkExtractor(allow=r'/_Desde_\d*'),  # Apply regex to get elements
            follow=True
        ),
        Rule(
            LinkExtractor(allow=r'.*MLB(\d+||\D)'),
            follow=True,
            callback='parse_items')  # Get method parser element

    )

    def parse_items(self, response) -> Generator:
        # Search element in DOM
        element: Any[ItemLoader | Item] = ItemLoader(ItemFromFinder(), response)
        element.add_xpath("it_by", '//h1/text()')
        element.add_xpath("take_more", '//p[@class="ui-pdp-description__content"]/text()')
        yield element.load_item()

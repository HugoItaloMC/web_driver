from scrapy.item import Item, Field  # Field: to attr in object for elements HTML | Item: For object inheritance that will contain HTML elements
from scrapy.spiders import Spider  # Object to Main Inheritance in getting by web-site
from scrapy.selector import Selector  # Get xpath
from scrapy.loader import ItemLoader  # Joined Main element with child elements in Python objects
from scrapy.loader.processors import MapCompose
from bs4 import BeautifulSoup

from typing import Dict, List, Generator, Any


class Elements(Item):
    text_from_title = Field()
    text_from_content = Field()


class StackOverFlowSpider(Spider):
    name: str = "my_first_spider"
    # This agent in header from request
    custom_settings: Dict = {"user-agent": "Mozilla/5.0 (X11, Linux X86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chormium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36"}
    start_urls: List[str] = ['https://stackoverflow.com/questions']  # Is URL to get scraping

    def parse(self, response) -> Generator:
        # This parser scraping
        selector: Selector = Selector(response)
        main_div: Selector = selector.xpath('//div[@id="questions"]//div[@class="s-post-summary--content"]')
        for child_div in main_div:
            #  Gets Elements in `main_div`
            element: Any[ItemLoader | Item] = ItemLoader(Elements(), child_div)
            element.add_xpath("text_from_title", './/h3/a/text()')
            element.add_xpath("text_from_content", './/div[@class="s-post-summary--content-excerpt"]/text()')
            yield element.load_item()
            # Write in console: "scrapy runspider `ModulePy.py` -O `NameFileOutPut.json` ", to upload file how json

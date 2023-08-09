# Web Scraping in web-site by groups to app `WhatsApp`
# Listening mains groups feed homepage

from scrapy.item import Item, Field  # Field: to attr in object for elements HTML | Item: For object inheritance that will contain HTML elements
from scrapy.spiders import Spider  # Object to Main Inheritance in getting by web-site
from scrapy.selector import Selector  # Get xpath
from scrapy.loader import ItemLoader  # Joined Main element with child elements in Python objects


from typing import Dict, List, Generator, Any


class Elements(Item):
    #  elements the context from web-site
    text_from_title = Field()
    text_from_content = Field()


class IGruposSpider(Spider):
    name: str = "spider_igrupos_from"
    # This agent in header from request
    custom_settings: Dict = {"user-agent": "Mozilla/5.0 (X11, Linux X86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chormium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36"}
    start_urls: List[str] = ['https://www.igrupos.com/whatsapp']  # Is URL to begin scraping

    def parse(self, response) -> Generator:
        # This parser is method from `scrapy.Spider` object, builtin parameter `response`
        selector: Selector = Selector(response)  # To response builtin also we can iterate over the `response` util `for`
        main_div: Selector = selector.xpath('//div[@class="media-body"]')  # Get div main in container from more div's
        for child_div in main_div:
            #  Get child's div in main div
            element: Any[ItemLoader | Item] = ItemLoader(Elements(), child_div)

            element.add_xpath(field_name="text_from_title",  # Name Key to json
                              xpath='.//a/span/text()')   # XPath from DOM to insert value it key above

            element.add_xpath(field_name='text_from_content',
                              xpath='.//a/text()')
            yield element.load_item()
            # Write in console: "scrapy runspider `ModulePy.py` -O `NameFileOutPut.json` ", to upload file how json

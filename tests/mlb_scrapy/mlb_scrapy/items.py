# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class ItemFromFinder(Item):
    it_by: Field = Field()
    take_more: Field = Field()


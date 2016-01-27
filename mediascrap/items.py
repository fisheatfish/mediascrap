# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class NewsItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    site = Field()
    date_article=Field()
    body = Field()
    url = Field()
    timeOfScrap = Field()
    pass



class NettutsItem(Item):
    # define the fields for your item here like:
    # name = Field()

    title = Field()
    pass
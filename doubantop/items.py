# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class doubantopItem(scrapy.Item):
    name = scrapy.Field()
    douban = scrapy.Field()
    pass

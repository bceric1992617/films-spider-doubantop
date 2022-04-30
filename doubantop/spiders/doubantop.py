# -*- coding: utf-8 -*-
import scrapy
import json
import os
import time
import datetime
import sys
import re
import pymysql
from urllib.parse import quote
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from doubantop.items import doubantopItem




class doubantop(CrawlSpider):
    name = 'doubantop'
    allowed_domains = [
        'douban.com'
    ]

    start_urls = []
    filmUrls = ['https://movie.douban.com/top250?start=$&filter=']
    pageNum = 225 #225
    i = 0
    while i <= pageNum:
        start_urls.append(filmUrls[0].replace('$', str(i), 1))
        i += 25
 

    def parse(self, response):
        item = doubantopItem()
        item['name'] = response.xpath("//span[@class='title'][1]/text()").extract()
        item['douban'] = response.xpath("//span[@class='rating_num']/text()").extract()
  
        return item





      
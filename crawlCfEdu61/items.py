# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Crawlcfedu61Item(scrapy.Item):
    # define the fields for your item here like:
    rank = scrapy.Field()
    name = scrapy.Field()
    number_solved = scrapy.Field()
    penalty = scrapy.Field()
    success_hacks = scrapy.Field()
    fail_hacks = scrapy.Field()
    time_detail = scrapy.Field()
    problems_detail = scrapy.Field()


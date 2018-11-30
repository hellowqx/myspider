# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Myspider3Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class PictureprojectItem(scrapy.Item):
    pass
    # define the fields for your item here like:
    # name = scrapy.Field()
    image_urls = scrapy.Field()
    # images = scrapy.Field()

class JobItem(scrapy.Item):
    name=scrapy.Field()
    addr=scrapy.Field()
    company=scrapy.Field()
    salary=scrapy.Field()
    times=scrapy.Field()
    phone=scrapy.Field()
    intro=scrapy.Field()
    com_info=scrapy.Field()

class HotItem(scrapy.Item):
    nickname=scrapy.Field()
    addr=scrapy.Field()
    sex=scrapy.Field()
    birth=scrapy.Field()



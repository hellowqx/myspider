# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MyscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    images = scrapy.Field()  # 文件名称
    image_urls = scrapy.Field()  # 文件url路径
    image_paths = scrapy.Field()  # 文件本地路径






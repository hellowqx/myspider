# -*- coding: utf-8 -*-
from scrapy import Spider

class Sina_Spider(Spider):
    name = 'sina'
    allowed_domains='sina.com.cn'
    start_urls=['https://www.sina.com.cn']

    def parse(self, response):
        print(response.text)
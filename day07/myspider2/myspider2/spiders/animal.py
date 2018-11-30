# -*- coding: utf-8 -*-
import scrapy
from ..items import MyItem
import time

class AnimalSpider(scrapy.Spider):
    name = 'animal'
    allowed_domains = ['iltaw.com']
    start_urls = ['http://www.iltaw.com/animal/all']

    def parse(self, response):
        alls=response.xpath("//ul[@class='info-list']/li[@class='clearfix']")
        for i in alls:
            name=i.xpath(".//div[@class='text-wrap']/h3/a/text()").extract_first()
            intro=i.xpath(".//div[@class='text-wrap']/p/text()").extract_first()
            img=i.xpath(".//div[@class='image-wrap']/a/img[@class='loading-v1']/@data-url").extract_first()
            print(img,1111111111111)
            my_item=MyItem()
            my_item['name']=name.strip()
            my_item['intro']=intro.strip()
            my_item['link']=img.strip()
            print(name,intro,img)

            #抛出数据
            yield my_item


        #下一页
        next_page=response.xpath("//div[@class='pager-v1 right']/a[text()='>']/@href").extract_first()
        if next_page is not None:
            time.sleep(2)
            print(next_page,111111111111111111111111)
            yield response.follow(next_page,self.parse)





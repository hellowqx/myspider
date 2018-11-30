""" 
    -*- coding: utf-8 -*-
    @Time    : 2018/11/28 20:53
    @Author  : WQX
    @title   :
    
"""

# -*- coding: utf-8 -*-
import scrapy
from ..items import HotItem,PictureprojectItem
import time
base_url='https://www.9000.com'
class AnimalSpider(scrapy.Spider):
    name = 'hot_person'
    allowed_domains = ['9000.com']
    start_urls = ['https://www.9000.com/Photos/index.html']

    def parse(self, response):
        alls=response.xpath("//div[@class='index-hot-con']/ul/li/div[@class='index-hot-img']/a")
        for i in alls:
            url=base_url+i.xpath('.//@href').extract_first()
            time.sleep(2)
            # yield response.follow(url,self.parse1)
            yield response.follow(url,self.pic)

    #下一页
        next_page=response.xpath("//a[text()='下一页']/@href").extract_first()
        next_url=base_url+next_page
        print(next_url)
        yield response.follow(next_url,self.parse)

    def parse1(self,response):
        nickname=response.xpath("//div[@class='homepage-notice mt10'][2]/p[2]/text()").extract_first()
        birth=response.xpath("//div[@class='homepage-notice mt10'][2]/p[3]/text()").extract_first()
        sex=response.xpath("//div[@class='homepage-notice mt10'][2]/p[4]/text()").extract_first()
        addr=response.xpath("//div[@class='homepage-notice mt10'][2]/p[5]/text()").extract_first()



        hot_item=HotItem()
        hot_item['nickname']=nickname
        hot_item['birth']=birth
        hot_item['sex']=sex
        hot_item['addr']=addr

        # yield hot_item

    def pic(self,response):
        linkss=list()
        links = response.xpath("//div[@class='baguetteBoxOne gallery']/a/img")
        for i in links:
            link = base_url + i.xpath(".//@src").extract_first()
            linkss.append(link)

        items = PictureprojectItem()
        items['image_urls'] = linkss
        print(items,11111111111111111111)
        yield items


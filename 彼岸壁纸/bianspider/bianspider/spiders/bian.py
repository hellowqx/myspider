# -*- coding: utf-8 -*-
import scrapy

from ..items import BianspiderItem

# class BianSpider(CrawlSpider):
#     name = 'bian'
#     allowed_domains = ['netbian.com']
#     start_urls = ['http://www.netbian.com/meinv/']
#
#     rules = (
#         Rule(LinkExtractor(allow=r"/desk/"), callback='parse_item', follow=True),
#         Rule(LinkExtractor(restrict_xpaths="//a[text()='下一页']"),follow=True),
#     )
#
#     def parse_item(self, response):
#
#         image_urls=response.xpath("//table[@id='endimg']//tr/td/a/img/@src")
#         print(image_urls,1111111111111)
#         img_item =BianspiderItem(image_urls=image_urls)
#         print('已存入一张')
#         return img_item

import time
base='http://www.netbian.com'
class BianSpider(scrapy.Spider):
    name = 'bian'
    allowed_domains = ['netbian.com']
    start_urls = ['http://www.netbian.com/meinv/']

    def parse(self, response):
        #首页链接
        index_links=response.xpath("//div[@class='list']/ul/li/a/@href").extract()
        for link in index_links:
            link=base+link
            yield response.follow(link,self.img1)

        #下一页
        next_page=response.xpath("//div[@class='page']/a[text()='下一页>']/@href").extract_first()
        next_url=base+next_page
        print(next_url,'跳转%s页———————————————————————'%(next_page))
        if next_page:
            time.sleep(2)
            yield response.follow(next_url,self.parse)

    #相册外部900x600小图
    def img1(self,response):
        img_url=response.xpath("//div[@class='pic']/div[@class='pic-down']/a/@href").extract_first()
        img_urls=base+img_url
        if img_url:
            yield response.follow(img_urls,self.img2)

    #高清大图1920
    def img2(sel,response):
        image_urls=response.xpath("//table[@id='endimg']//tr/td/a/img/@src").extract_first()
        print(image_urls)
        img_item =BianspiderItem(image_urls=[image_urls])
        print('已下载此照片')
        return img_item

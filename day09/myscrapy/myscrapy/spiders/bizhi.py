""" 
    -*- coding: utf-8 -*-
    @Time    : 2018/11/29 9:29
    @Author  : WQX
    @title   :
    
"""

import time
import scrapy

from ..items import MyscrapyItem
base_url='http://desk.zol.com.cn'

class BizhiSpider(scrapy.Spider):
    name = 'bizhi'
    allowed_domains=['zol.com.cn']
    start_urls=['http://desk.zol.com.cn/meinv/1920x1080/']

    def parse(self, response):
        alls=response.xpath("//ul[@class='pic-list2  clearfix']/li/a[@class='pic']")
        for link in alls:
            url = base_url + link.xpath('.//@href').extract_first()
            # time.sleep(2)
            print(url, 11111111)
            yield response.follow(url,self.download_pic)

        #下一页

        next_page=response.xpath("//a[@id='pageNext']/@href").extract_first()
        if next_page:
            next_url=base_url+next_page
            print(next_url,'下一页连接')
            yield response.follow(next_url,self.parse)

    def download_pic(self,response):
        pic=response.xpath("//div[@id='mouscroll']//img[@id='bigImg']/@src").extract()
        myitem=MyscrapyItem()
        myitem['image_urls']=list(pic)
        yield myitem


        #下一张
        next_pic=response.xpath("//div[@id='photo-next']/a[@id='pageNext']/@href").extract_first()
        if next_pic:
            next_pic=base_url+next_pic
            yield response.follow(next_pic,self.download_pic)

        else:
            print("本相册采集完毕")
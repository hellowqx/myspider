""" 
    -*- coding: utf-8 -*-
    @Time    : 2018/11/27 17:26
    @Author  : WQX
    @title   :
    
"""
# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
import time
from ..items import MidItem

class BaiduSpider(scrapy.Spider):
    name = 'yaopin'
    allowed_domains = ['111.com.cn']
    start_urls = ['https://www.111.com.cn/categories/']


    def parse(self, response):
        alls=response.xpath("//dd/em/a")
        for all in alls:
            i=all.xpath('.//@href').extract_first()
            #药品分类的一级连接
            i='https:'+i
            yield response.follow(i,self.parse1)


    # 药品2级页面
    def parse1(self, response):
        infos = response.xpath("//ul[@id='itemSearchList']/li")
        for info in infos:
            time.sleep(2)
            try:
                price = info.xpath(".//p[@class='price']/span/text()").extract_first()
                name = info.xpath(".//a[@class='product_pic pro_img']/img/@alt").extract_first()
            except:
                pass


            my_item = MidItem()
            my_item['name'] = name.strip()
            my_item['price'] = price.strip()

            yield my_item
        # 下一页
        next_page = response.xpath("//div[@class='turnPageBottom']/a[@class='page_next']/@href").extract_first()
        if next_page is not None:
            time.sleep(3)
            yield response.follow(next_page, self.parse1)

        else:
            print('此类药品采集完毕')

# scrapy crawl yaopin
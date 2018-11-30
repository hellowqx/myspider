""" 
    -*- coding: utf-8 -*-
    @Time    : 2018/11/27 11:25
    @Author  : WQX
    @title   :
    
"""


import scrapy
import pyttsx3
engine=pyttsx3.init()
class My_spider(scrapy.Spider):
    name='spider_1'
    start_urls=[
        "http://quotes.toscrape.com/page/1/",
    ]
    #解析
    def parse(self,response):
        quotes=response.css('div.quote')
        print(quotes)
        for i in quotes:
            # 产生
            yield{
                'text':response.css('span.text::text').extract_first(),
                'author':response.xpath("//div[@class='quote']/span[2]/small[@class='author']/text()").extract_first()

            }
        engine.say('本页采集完毕')
        engine.runAndWait()
        #获取下一页数据
        next_page=response.xpath("//li[@class='next']/a/@href").extract_first()
        print(next_page,1111111111)


        if next_page:
            yield response.follow(next_page,self.parse)
            engine.say('开始采集下一页'+next_page)
            engine.runAndWait()
        else:
            print('采集完毕')
            engine.say('数据采集完毕')
            engine.runAndWait()



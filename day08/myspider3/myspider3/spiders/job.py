""" 
    -*- coding: utf-8 -*-
    @Time    : 2018/11/28 11:36
    @Author  : WQX
    @title   :
    
"""
# -*- coding: utf-8 -*-
import scrapy
import time
from ..items import JobItem
out_base='https://docs.scrapy.org/en/latest/'

class ScrapySpider(scrapy.Spider):
    name = 'job'
    allowed_domains = ['51job.com']
    start_urls = ['https://search.51job.com/list/000000%252C00,000000,0000,00,9,99,python%2B%25E7%2588%25AC%25E8%2599%25AB,2,1.html']

    def parse(self, response):
        jobs=response.xpath("//div[@id='resultList']/div[@class='el']")
        for job in jobs:

            name=job.xpath(".//p[@class='t1 ']/span/a/@title").extract_first()

            company=job.xpath(".//span[@class='t2']/a/text()").extract_first()
            addr=job.xpath(".//span[@class='t3']/text()").extract_first()
            salary=job.xpath(".//span[@class='t4']/text()").extract_first()
            times=job.xpath(".//span[@class='t5']/text()").extract_first()
            link=job.xpath(".//p[@class='t1 ']/span[1]/a/@href").extract_first()


            # print(name,company,addr,salary,times,link)
            job_item=JobItem()
            job_item['name']=name
            job_item['company']=company
            job_item['addr']=addr
            job_item['salary']=salary
            job_item['times']=times

            yield response.follow(link,self.job_info,meta={'item':job_item})

        next_page=response.xpath("//a[text()='下一页']/@href").extract_first()
        if next_page :
            print(next_page,2222222222222222222222222222222222222222)
            time.sleep(2)
            yield response.follow(next_page,self.parse)
        else:
            print('数据采集完毕——————————————————————————————————————————————————————————')


    #
    def job_info(self,response):

        job_item=response.meta['item']
        intro=response.xpath("//div[@class='tCompany_main']//div[@class='bmsg job_msg inbox']/p")
        b=(str(i.xpath('string(.)').extract_first()) for i in intro)
        intro=''.join(b)
        com_info=response.xpath("//div[@class='tCompany_main']/div[@class='tBorderTop_box'][3]/div[@class='tmsg inbox']").xpath('string(.)').extract_first()
        phone=response.xpath("//div[@class='tBorderTop_box'][2]/div[@class='bmsg inbox']/p[@class='fp']").xpath('string(.)').extract_first()
        job_item['intro'] = intro.replace('\t,\n,\r','')
        job_item['com_info'] = com_info.strip()
        job_item['phone'] = phone.strip()
        print(job_item)


        yield job_item




# <p\s+class="fp">.*?</span>(.*?)</p>




















'scrapy crawl job'


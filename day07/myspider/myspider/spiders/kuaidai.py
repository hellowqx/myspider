# """
#     -*- coding: utf-8 -*-
#     @Time    : 2018/11/27 16:22
#     @Author  : WQX
#     @title   :快代
#
#
# """
#
#
# from scrapy import Spider
# import pyttsx3
# import time
# # from ..items import WebItem
# import requests
# engine=pyttsx3.init()
#
#
# class ChuaiDai(Spider):
#     name = 'kuaidai'
#     allowed_domains='www.kuaidaili.com'
#     start_urls=['https://www.kuaidaili.com/free/']
#
#
#     def parse(self, response):
#         alls=response.xpath("//div[@class='con-body']/div/div[@id='list']")
#         for all in alls:
#             #采集对应信息
#             ip=all.xpath(".//table[@class='table table-bordered table-striped']//tr[5]/td[1]/text()").extract_first()
#             print(ip)
#             port=all.xpath(".//table[@class='table table-bordered table-striped']/tbody/tr[1]/td[2]/text()").extract_first()
#             print(port)
#             type=all.xpath(".//table[@class='table table-bordered table-striped']/tbody/tr[1]/td[4]/text()").extract_first()
#
#             #创建ITEM对象
#             # web_item=WebItem()
#             web_item['ip']=ip
#             web_item['type']=type
#             web_item['port']=port
#             # print(web_item,1111111111111)
#
#             yield web_item
#
#         #下一页
#         for i in range(1,2000):
#             engine.say('开始采集第%s页'%i)
#             engine.runAndWait()
#             next_page='https://www.kuaidaili.com/free/inha/'+str(i)+'/'
#             print(next_page)
#
#             yield response.follow(next_page,self.parse)
#             time.sleep(2)
#
#         print('数据采集完毕')